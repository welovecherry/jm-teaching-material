/* ⭐ 내 단어장
   - 용어표 각 줄 앞에 체크박스를 자동 삽입 (markdown은 건드리지 않음)
   - 체크한 용어는 localStorage에 저장(새로고침·재방문해도 유지)
   - '내 단어장' 페이지에서 전 과목 누적 표시 + 복습 모드 + 메모 저장 */
(function () {
  var KEY = "wordbook.v1";

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; }
    catch (e) { return {}; }
  }
  function save(d) { localStorage.setItem(KEY, JSON.stringify(d)); }
  function norm(s) { return (s || "").replace(/\s+/g, " ").trim(); }
  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }
  function count() { return Object.keys(load()).length; }

  /* 현재 페이지의 출처 이름 (예: "강의1 · OSI 7계층 모델 (오전, 총 120분)") */
  function currentSource() {
    var h1 = document.querySelector(".md-content__inner h1");
    var t = h1 ? norm(h1.textContent).replace(/¶/g, "") : norm(document.title);
    return t;
  }

  /* 사이드바의 '내 단어장' 링크에 개수 표시 */
  function updateNavCount() {
    var n = count();
    document.querySelectorAll('.md-nav__link[href]').forEach(function (a) {
      if (!/wordbook\/?$/.test(a.getAttribute("href") || "")) return;
      var base = a.dataset.wbBase || norm(a.textContent);
      a.dataset.wbBase = base;
      a.textContent = n ? base + " (" + n + ")" : base;
    });
  }

  /* 1) 용어표에 체크박스 주입
     — 제목 위치가 아니라 '표 헤더에 용어가 있는지'로 찾아, Material의 표 감싸기에도 안전 */
  function injectTermTables() {
    var article = document.querySelector(".md-content__inner");
    if (!article) return;
    var src = currentSource();
    var url = location.pathname;
    var data = load();

    article.querySelectorAll("table").forEach(function (table) {
      if (table.dataset.wbInit) return;
      var firstTh = table.querySelector("thead th");
      if (!firstTh || !/용어/.test(firstTh.textContent)) return; // 용어표만
      table.dataset.wbInit = "1";

      var hr = table.querySelector("thead tr");
      if (hr) {
        var th = document.createElement("th");
        th.className = "wb-col";
        th.textContent = "⭐";
        hr.insertBefore(th, hr.firstChild);
      }

      table.querySelectorAll("tbody tr").forEach(function (tr) {
        var cells = tr.querySelectorAll("td");
        if (!cells.length) return;
        var term = norm(cells[0].textContent);
        if (!term) return;
        var meaning = cells[1] ? norm(cells[1].textContent) : "";
        var analogy = cells[2] ? norm(cells[2].textContent) : "";

        var td = document.createElement("td");
        td.className = "wb-col";
        var box = document.createElement("input");
        box.type = "checkbox";
        box.className = "wb-check";
        box.title = "단어장에 담기";
        box.checked = !!data[term];
        if (box.checked) tr.classList.add("wb-on");

        box.addEventListener("change", function () {
          var d = load();
          if (box.checked) {
            var prev = d[term] || {};
            d[term] = {
              term: term, meaning: meaning, analogy: analogy,
              source: src, url: url, memo: prev.memo || ""
            };
            tr.classList.add("wb-on");
          } else {
            delete d[term];
            tr.classList.remove("wb-on");
          }
          save(d);
          updateNavCount();
        });

        td.appendChild(box);
        tr.insertBefore(td, tr.firstChild);
      });
    });
  }

  /* 2) 단어장 페이지 렌더 */
  function renderWordbook() {
    var root = document.getElementById("wordbook-root");
    if (!root) return;
    var d = load();
    var items = Object.keys(d).map(function (k) { return d[k]; });

    if (!items.length) {
      root.innerHTML =
        '<p class="wb-empty">아직 담은 용어가 없습니다. 각 강의 상단 <b>“이 교시에 나오는 어려운 용어”</b> 표에서 ⭐를 눌러 담아보세요.</p>';
      return;
    }
    items.sort(function (a, b) { return (a.source || "").localeCompare(b.source || ""); });

    var html =
      '<div class="wb-toolbar">' +
      '<button class="wb-btn" id="wb-review">🔁 복습 모드</button>' +
      '<button class="wb-btn" id="wb-clear">🗑 전체 비우기</button>' +
      '<span class="wb-count">총 ' + items.length + '개</span></div>' +
      '<p class="wb-hint" id="wb-hint"></p>' +
      '<table class="wb-table"><thead><tr>' +
      '<th>용어</th><th>뜻</th><th>비유</th><th>메모</th><th>어디서</th><th></th>' +
      '</tr></thead><tbody>';

    items.forEach(function (it) {
      html +=
        '<tr data-term="' + esc(it.term) + '">' +
        '<td class="wb-term">' + esc(it.term) + "</td>" +
        '<td class="wb-hide">' + esc(it.meaning) + "</td>" +
        '<td class="wb-hide">' + esc(it.analogy) + "</td>" +
        '<td><textarea class="wb-memo" rows="1" placeholder="메모…">' + esc(it.memo || "") + "</textarea></td>" +
        '<td class="wb-src"><a href="' + esc(it.url) + '">' + esc(it.source) + "</a></td>" +
        '<td><button class="wb-del" title="단어장에서 빼기">✕</button></td>' +
        "</tr>";
    });
    html += "</tbody></table>";
    root.innerHTML = html;
    bind(root);
  }

  function bind(root) {
    var reviewBtn = root.querySelector("#wb-review");
    var hint = root.querySelector("#wb-hint");

    reviewBtn.addEventListener("click", function () {
      var on = root.classList.toggle("wb-review");
      reviewBtn.classList.toggle("on", on);
      hint.textContent = on
        ? "뜻·비유가 가려졌습니다. 먼저 스스로 떠올린 뒤, 줄을 클릭하면 공개됩니다."
        : "";
      root.querySelectorAll("tr.revealed").forEach(function (tr) {
        tr.classList.remove("revealed");
      });
    });

    root.querySelector("#wb-clear").addEventListener("click", function () {
      if (!confirm("단어장을 전부 비울까요? (메모도 함께 지워집니다)")) return;
      save({});
      renderWordbook();
      updateNavCount();
    });

    root.querySelectorAll("tbody tr").forEach(function (tr) {
      /* 복습 모드에서 줄 클릭 → 공개 */
      tr.addEventListener("click", function (e) {
        if (!root.classList.contains("wb-review")) return;
        if (e.target.closest(".wb-memo, .wb-del, a")) return;
        tr.classList.toggle("revealed");
      });

      /* 메모: 타이핑하면 바로 저장 */
      var memo = tr.querySelector(".wb-memo");
      var timer = null;
      memo.addEventListener("input", function () {
        clearTimeout(timer);
        timer = setTimeout(function () {
          var d = load();
          var t = tr.dataset.term;
          if (d[t]) { d[t].memo = memo.value; save(d); }
        }, 250);
      });

      /* 빼기 */
      tr.querySelector(".wb-del").addEventListener("click", function () {
        var d = load();
        delete d[tr.dataset.term];
        save(d);
        renderWordbook();
        updateNavCount();
      });
    });
  }

  function init() {
    injectTermTables();
    renderWordbook();
    updateNavCount();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else if (document.readyState !== "loading") {
    init();
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
