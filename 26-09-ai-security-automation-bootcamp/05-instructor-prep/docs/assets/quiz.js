/* 인터랙티브 객관식 퀴즈: 보기 클릭 → 정답/오답 표시 + 해설 */
(function () {
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
