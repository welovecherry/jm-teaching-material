/* 상단 스크롤 진행률 바 + 페이지 완독 체크박스(localStorage 저장) */
(function () {
  // 1) 스크롤 진행률 바
  function setupProgressBar() {
    var bar = document.querySelector(".reading-progress");
    if (!bar) {
      bar = document.createElement("div");
      bar.className = "reading-progress";
      document.body.appendChild(bar);
    }
    function update() {
      var el = document.documentElement;
      var scrollable = el.scrollHeight - el.clientHeight;
      var pct = scrollable > 0 ? (el.scrollTop / scrollable) * 100 : 0;
      bar.style.width = pct + "%";
    }
    if (!window.__rpBound) {
      window.addEventListener("scroll", update, { passive: true });
      window.addEventListener("resize", update);
      window.__rpBound = true;
    }
    update();
  }

  // 2) 페이지 완독 체크박스 (URL별로 상태 저장)
  function setupReadCheck() {
    var article =
      document.querySelector(".md-content__inner") ||
      document.querySelector("article");
    if (!article || article.querySelector(".readcheck-done")) return;

    var key = "read:" + location.pathname;
    var wrap = document.createElement("label");
    wrap.className = "readcheck-done";

    var box = document.createElement("input");
    box.type = "checkbox";
    box.checked = localStorage.getItem(key) === "1";

    var span = document.createElement("span");
    span.className = "rc-label";
    span.textContent = "이 페이지 공부 완료";

    wrap.appendChild(box);
    wrap.appendChild(span);
    if (box.checked) wrap.classList.add("checked");

    box.addEventListener("change", function () {
      if (box.checked) localStorage.setItem(key, "1");
      else localStorage.removeItem(key);
      wrap.classList.toggle("checked", box.checked);
    });

    article.appendChild(wrap);
  }

  function init() {
    setupProgressBar();
    setupReadCheck();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else if (document.readyState !== "loading") {
    init();
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
