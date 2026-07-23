/* 인터랙티브 객관식 퀴즈: 보기 클릭 → 정답/오답 표시 + 해설
   + 틀린 문제는 '복습하기'용으로 localStorage에 기록(맞히면 자동 제거) */
(function () {
  var WRONGKEY = "reviewWrong.v1";
  function loadWrong() { try { return JSON.parse(localStorage.getItem(WRONGKEY)) || {}; } catch (e) { return {}; } }
  function saveWrong(d) { localStorage.setItem(WRONGKEY, JSON.stringify(d)); }
  function pageSource() {
    var h = document.querySelector(".md-content__inner h1");
    return (h ? h.textContent : document.title).replace(/¶/g, "").replace(/\s*\([^)]*\)\s*$/, "").replace(/\s+/g, " ").trim();
  }
  function recordResult(quiz, opts, explain, correctPicked) {
    if (quiz.classList.contains("wb-wrongq")) return; // 복습 페이지의 재출제는 여기서 기록 안 함
    var b = quiz.querySelector(".quiz-q b");
    var qtext = b ? b.textContent.trim() : "";
    if (!qtext) return;
    var d = loadWrong();
    if (correctPicked) {
      if (d[qtext]) { delete d[qtext]; saveWrong(d); }
    } else {
      d[qtext] = {
        q: qtext,
        opts: opts.map(function (o) { return { t: o.textContent, c: o.hasAttribute("data-correct") }; }),
        explain: explain ? explain.innerHTML : "",
        source: pageSource(), url: location.pathname
      };
      saveWrong(d);
    }
  }

  function initQuiz(quiz) {
    if (quiz.dataset.qinit) return;
    quiz.dataset.qinit = "1";
    var opts = Array.prototype.slice.call(quiz.querySelectorAll(".quiz-opt"));
    var explain = quiz.querySelector(".quiz-explain");
    var retry = quiz.querySelector(".quiz-retry");

    function reveal(picked) {
      quiz.classList.add("answered");
      opts.forEach(function (b) {
        b.disabled = true;
        if (b.hasAttribute("data-correct")) b.classList.add("quiz-correct");
      });
      if (picked && !picked.hasAttribute("data-correct")) picked.classList.add("quiz-wrong");
      if (explain) explain.classList.add("show");
      recordResult(quiz, opts, explain, picked && picked.hasAttribute("data-correct"));
    }
    function reset() {
      quiz.classList.remove("answered");
      opts.forEach(function (b) {
        b.disabled = false;
        b.classList.remove("quiz-correct", "quiz-wrong");
      });
      if (explain) explain.classList.remove("show");
    }
    opts.forEach(function (btn) {
      btn.addEventListener("click", function () {
        if (quiz.classList.contains("answered")) return;
        reveal(btn);
      });
    });
    if (retry) retry.addEventListener("click", reset);
  }

  function initAll() {
    document.querySelectorAll(".quiz").forEach(initQuiz);
  }

  // Material for MkDocs 인스턴트 내비 대응 + 일반 로드 대응
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(initAll);
  } else if (document.readyState !== "loading") {
    initAll();
  } else {
    document.addEventListener("DOMContentLoaded", initAll);
  }
})();
