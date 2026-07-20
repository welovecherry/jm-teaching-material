/* 상단 진행률 바(체크박스 기반) + 섹션별 '읽음' 체크박스(localStorage 저장) */
(function () {
  function articleEl() {
    return (
      document.querySelector(".md-content__inner") ||
      document.querySelector("article")
    );
  }

  function ensureBar() {
    if (!document.querySelector(".reading-progress-track")) {
      var track = document.createElement("div");
      track.className = "reading-progress-track";
      document.body.appendChild(track);
    }
    if (!document.querySelector(".reading-progress")) {
      var bar = document.createElement("div");
      bar.className = "reading-progress";
      document.body.appendChild(bar);
    }
  }

  function updateBar() {
    var bar = document.querySelector(".reading-progress");
    if (!bar) return;
    var boxes = document.querySelectorAll(".readcheck input");
    if (!boxes.length) {
      bar.style.width = "0%";
      return;
    }
    var done = 0;
    boxes.forEach(function (b) {
      if (b.checked) done++;
    });
    bar.style.width = Math.round((done / boxes.length) * 100) + "%";
  }

  function injectChecks() {
    var article = articleEl();
    if (!article || article.dataset.rcInjected) return;
    article.dataset.rcInjected = "1";

    var headings = Array.prototype.slice.call(article.querySelectorAll("h2"));
    headings.forEach(function (h2, i) {
      var key = "sec:" + location.pathname + "#" + i;
      var label = document.createElement("label");
      label.className = "readcheck";

      var box = document.createElement("input");
      box.type = "checkbox";
      box.checked = localStorage.getItem(key) === "1";

      var span = document.createElement("span");
      span.textContent = "여기까지 읽음";

      label.appendChild(box);
      label.appendChild(span);
      if (box.checked) label.classList.add("checked");

      box.addEventListener("change", function () {
        if (box.checked) localStorage.setItem(key, "1");
        else localStorage.removeItem(key);
        label.classList.toggle("checked", box.checked);
        updateBar();
      });

      var next = headings[i + 1];
      if (next && next.parentNode) next.parentNode.insertBefore(label, next);
      else article.appendChild(label);
    });
  }

  function init() {
    ensureBar();
    injectChecks();
    updateBar();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else if (document.readyState !== "loading") {
    init();
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
