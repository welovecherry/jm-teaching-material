# 🧪 어려운 객관식 3종 (임시 · 주제: IP·서브네팅)

기존 문제가 "단답 암기형"이라 아쉽다 하셔서, **생각·계산·판단이 필요한** 3가지 스타일을 같은 주제로 만들었습니다. 보기를 눌러 난이도를 느껴보시고, 마음에 드는 스타일(또는 조합)을 골라주세요.

---

## 형식 A · 계산·적용형 (직접 따져야 답이 나옴)

> 공식을 외웠는지가 아니라 **적용**할 수 있는지 묻습니다.

<div class="quiz">
<p class="quiz-q"><span class="tag">형식 A</span><b>한 부서에 PC가 <b>100대</b> 있습니다. 이 부서를 하나의 서브넷에 모두 담으려면 <u>최소</u> 어떤 CIDR이 필요할까요? (사용 가능 호스트 = 2ⁿ − 2)</b></p>
<button class="quiz-opt">/24 (254대)</button>
<button class="quiz-opt" data-correct>/25 (126대)</button>
<button class="quiz-opt">/26 (62대)</button>
<button class="quiz-opt">/27 (30대)</button>
<div class="quiz-explain"><b>정답: /25.</b> 100대를 담으려면 2ⁿ−2 ≥ 100 → n=7 → 126대(/25)면 충분합니다. /26(62대)은 부족하고, /24(254대)도 담기지만 <b>"최소"</b> 조건에 맞는 가장 작은 대역은 /25입니다. (함정: /24도 되지만 낭비)</div>
<button class="quiz-retry">다시 풀기</button>
</div>

---

## 형식 B · 시나리오 오류 진단형 (상황을 주고 "무엇이 잘못됐나")

> 실제 설계 표를 주고 **겹침·모순을 찾아내는** 실무형 문제입니다.

<div class="quiz">
<p class="quiz-q"><span class="tag">형식 B</span><b>영업팀에 <code>192.168.1.0/26</code>(.0~.63)을 배정했습니다. 아래 다른 팀 배정 중 <u>영업팀 대역과 겹쳐서 잘못된</u> 것은?</b></p>
<button class="quiz-opt">개발팀 192.168.1.64/27 (.64~.95)</button>
<button class="quiz-opt" data-correct>게스트 192.168.1.32/27 (.32~.63)</button>
<button class="quiz-opt">서버 192.168.1.96/28 (.96~.111)</button>
<button class="quiz-opt">관리 192.168.1.112/28 (.112~.127)</button>
<div class="quiz-explain"><b>정답: 게스트 192.168.1.32/27.</b> 이 대역(.32~.63)은 영업팀(.0~.63) 안에 완전히 포함되어 <b>겹칩니다</b>. 나머지는 .64 이후라 겹치지 않습니다. → 대역 배정 시 "이전 대역의 끝+1"에서 시작하는지 항상 확인.</div>
<button class="quiz-retry">다시 풀기</button>
</div>

---

## 형식 C · 복합 진술 평가형 (4개 설명 중 옳은/틀린 것 고르기)

> 각 보기가 "문장"이라, 여러 개념을 동시에 판단해야 합니다. 오개념 교정에 강합니다.

<div class="quiz">
<p class="quiz-q"><span class="tag">형식 C</span><b>IP·서브네팅에 대한 다음 설명 중 <u>옳은</u> 것은?</b></p>
<button class="quiz-opt">CIDR 숫자가 커질수록(/24→/28) 수용 가능한 호스트가 늘어난다</button>
<button class="quiz-opt" data-correct>/30 서브넷의 사용 가능 호스트는 2개다</button>
<button class="quiz-opt">사설 IP(192.168.x.x)는 인터넷 전체에서 유일하다</button>
<button class="quiz-opt">NAT는 공인 IP를 사설 IP로 바꿔 내부에 나눠주는 기술이다</button>
<div class="quiz-explain"><b>정답: /30은 사용 가능 호스트 2개.</b> (2²−2=2, 점대점 링크에 자주 씀) &nbsp;/&nbsp; 나머지 오답 이유: ① CIDR 숫자가 커지면 호스트는 <b>줄어든다</b> ③ 사설 IP는 내부 전용이라 <b>유일하지 않다</b> ④ NAT는 반대로 <b>사설→공인</b>으로 바꿔 인터넷으로 내보낸다.</div>
<button class="quiz-retry">다시 풀기</button>
</div>

---

## 어떤 스타일이 좋으세요?
| 형식 | 요구 능력 | 강점 |
|------|-----------|------|
| **A · 계산·적용형** | 공식을 실제로 적용 | 진짜 이해했는지 검증 |
| **B · 시나리오 진단형** | 상황 분석·오류 탐지 | 실무 감각 |
| **C · 복합 진술 평가형** | 여러 개념 동시 판단 | 오개념 교정 |

> "A+C 섞기", "블록마다 A, 정리에서 C"처럼 **조합**도 됩니다. 고르시면 Day1 강의1 문제를 이 난이도로 **다시 만들고**, 앞으로 전 강의에 적용합니다.
