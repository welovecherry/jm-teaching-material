# 강의1 · 클라우드·SaaS 환경과 망 구성도 (오전, 총 120분)

> **이 교시 한 문장:** 남의 컴퓨터(클라우드)를 빌려 쓰는 세 가지 방식(IaaS·PaaS·SaaS)을 구분하고, 그 접속 흐름을 **망 구성도**로 그립니다.

| 시간 | 소주제 | 핵심 한 줄 |
|------|--------|-----------|
| 00-20분 | IaaS/PaaS/SaaS 비교 | 어디까지 빌리느냐의 차이 |
| 20-45분 | SaaS 접속 흐름 | 재택 확대 → 보안팀의 '가시성' 문제 |
| 45-70분 | 망 구성도 표기법·DMZ | 표준 기호로 구조를 그린다 |
| 70-95분 | 실제 망 구성도 읽기 | 구간(내부망/DMZ/클라우드/VPN) 식별 |
| 95-120분 | draw.io 작성 준비 | 도구로 직접 그려보기 |

## 이 교시에 나오는 어려운 용어
| 용어 (한글발음) | 한 줄 뜻 (아주 쉽게) | 비유 |
|----------------|----------------------|------|
| **IaaS(아이아스)** | 서버(인프라)만 빌려 쓰기 | 빈 땅을 빌림 |
| **PaaS(파스)** | 개발 환경까지 갖춰진 걸 빌리기 | 골조까지 지어진 집 |
| **SaaS(사스)** | 완성된 서비스를 그냥 쓰기 | 완제품 아파트 임대 |
| **DMZ(디엠지)** | 외부 공개 서버를 두는 완충 구역 | 현관 응접실 |
| **Latency(레이턴시)** | 데이터가 목적지까지 걸리는 시간 | 편지 도착까지 걸린 날 |
| **Jitter(지터)** | 그 지연이 들쭉날쭉한 정도 | 배송일이 매번 다름 |
| **Packet Loss(패킷 로스)** | 가다가 사라진 패킷 비율 | 도중 분실된 택배 |
| **RTT(왕복시간)** | 갔다가 돌아오는 데 걸린 시간 | 편지+답장까지 걸린 시간 |

---

## ⏱️ 00-20분 · IaaS / PaaS / SaaS 비교

!!! abstract "이 블록을 마치면"
    ✔ 세 유형을 '내가 어디까지 책임지느냐'로 구분한다

'클라우드를 쓴다'는 건 결국 **남의 컴퓨터를 빌려 쓰는 것**입니다. 어디까지 빌리느냐에 따라 세 가지로 나뉩니다.

!!! example "쉬운 비유 — 집으로 이해하기"

    - **IaaS(아이아스)** = **빈 땅**을 빌림. 건물(OS·프로그램)은 내가 다 올림. (예: AWS EC2)
    - **PaaS(파스)** = **골조까지 지어진 집**을 빌림. 나는 인테리어(내 코드)만. (예: Heroku)
    - **SaaS(사스)** = **완제품 아파트**에 그냥 입주. 관리는 집주인이. (예: 그룹웨어·CRM)

### 🔬 깊이 보기 — '책임 범위'로 세 유형 완전정복

핵심은 =="무엇을 내가 관리하고, 무엇을 공급자가 관리하느냐"==입니다. 위로 갈수록 내가 편하지만 통제권은 줄어듭니다.

| 관리 항목 | IaaS | PaaS | SaaS |
|-----------|:---:|:---:|:---:|
| 애플리케이션(서비스) | 🙋 나 | 🙋 나 | 🏢 공급자 |
| 런타임·미들웨어 | 🙋 나 | 🏢 공급자 | 🏢 공급자 |
| 운영체제(OS) | 🙋 나 | 🏢 공급자 | 🏢 공급자 |
| 서버·네트워크·전원 | 🏢 공급자 | 🏢 공급자 | 🏢 공급자 |

**보안 관점(중요):** 위 표가 곧 **"보안 책임을 누가 지느냐"**입니다(책임 공유 모델). SaaS라도 **내 계정·접근권한 관리는 여전히 내 책임**입니다 — 그래서 6일차 Zero Trust가 필요해집니다.

!!! question "확인질문 · 나의 답"
    **Q. 회사가 자체 서버 없이 이메일·문서작업 서비스를 그대로 쓴다면 어떤 유형일까요?**
    A. **SaaS**입니다. 완성된 서비스를 그대로 이용하고, 서버·OS·앱 관리는 모두 공급자가 합니다. (회사는 계정·권한만 관리)

<div class="quiz">
<p class="quiz-q"><span class="tag">퀴즈</span><b>같은 클라우드인데 SaaS가 IaaS보다 '내가 관리할 것이 적은' 이유로 가장 적절한 것은?</b></p>
<button class="quiz-opt">SaaS가 IaaS보다 항상 저렴하기 때문</button>
<button class="quiz-opt" data-correct>SaaS는 앱·OS·서버까지 공급자가 관리하는 완성 서비스라, 이용자는 계정·권한 정도만 책임지기 때문</button>
<button class="quiz-opt">SaaS는 인터넷 없이도 동작하기 때문</button>
<button class="quiz-opt">IaaS는 보안을 신경 쓸 필요가 없기 때문</button>
<div class="quiz-explain"><b>정답: 2번.</b> 위로 갈수록(IaaS→SaaS) 공급자 책임이 커집니다. 대신 통제권은 줄어듭니다. 가격(1번)이나 오프라인 동작(3번)과는 무관합니다.</div>
<button class="quiz-retry">다시 풀기</button>
</div>

---

## ⏱️ 20-45분 · SaaS 접속 흐름과 재택근무 확대의 영향

!!! abstract "이 블록을 마치면"
    ✔ SaaS 접속 경로를 그린다 ✔ ==재택 직결 접속이 왜 '가시성' 문제를 낳는지== 안다

**사내에서 SaaS에 접속하는 경로:**

```mermaid
flowchart LR
    PC[사내 PC] --> N[사내망] --> FW[방화벽/프록시] --> I[인터넷] --> S[SaaS 서버]
    classDef dev fill:#3b5bdb,stroke:#2f4bc0,color:#fff
    classDef gate fill:#f59f00,stroke:#c67c00,color:#111
    classDef net fill:#2f9e44,stroke:#237a35,color:#fff
    class PC dev
    class N,FW gate
    class I,S net
```

사내에서는 **방화벽/프록시를 거치므로 보안팀이 트래픽을 볼 수 있습니다.** 그런데 **재택근무가 늘면서** 직원이 집에서 회사 VPN을 거치지 않고 **SaaS에 곧장 접속**하는 경우가 많아졌습니다.

!!! warning "여기서 6일차(Zero Trust)가 시작됩니다 — 가시성 문제"
    집 PC → 바로 SaaS로 가면, 그 트래픽은 **회사 방화벽을 안 거칩니다.** 즉 보안팀은 ==누가 언제 무엇에 접속했는지 파악하기 어렵습니다(가시성 상실).== '경계 안=안전'이라는 전제가 무너진 것이죠. 그래서 "경계 대신 매 접근을 검증하자"는 Zero Trust가 나옵니다.

!!! question "확인질문 · 나의 답"
    **Q. 직원이 회사 VPN을 거치지 않고 집에서 바로 SaaS에 접속하면, 보안팀은 그 접속을 얼마나 파악할 수 있을까요?**
    A. 거의 파악하기 어렵습니다. 회사 방화벽·프록시를 거치지 않아 **로그가 회사에 남지 않기 때문**입니다. 이 '가시성 상실'이 Zero Trust·SASE 같은 새 접근이 필요한 이유입니다.

<div class="quiz">
<p class="quiz-q"><span class="tag">퀴즈</span><b>재택 직원이 집에서 SaaS에 곧장 접속할 때 보안팀의 '가시성'이 떨어지는 이유로 가장 적절한 것은?</b></p>
<button class="quiz-opt">집 인터넷이 회사보다 느리기 때문</button>
<button class="quiz-opt">SaaS는 로그를 아예 남기지 않기 때문</button>
<button class="quiz-opt" data-correct>그 트래픽이 회사 방화벽·프록시를 거치지 않아, 접속 기록이 회사에 남지 않기 때문</button>
<button class="quiz-opt">재택 PC는 IP 주소가 없기 때문</button>
<div class="quiz-explain"><b>정답: 3번.</b> 경계(방화벽)를 안 지나므로 회사가 볼 로그가 없습니다. 이 '경계의 붕괴'가 Zero Trust의 등장 배경입니다.</div>
<button class="quiz-retry">다시 풀기</button>
</div>

---

## ⏱️ 45-70분 · 망 구성도의 표준 표기법과 DMZ

!!! abstract "이 블록을 마치면"
    ✔ 표준 기호로 구조를 읽고 ==DMZ 2중 방화벽 구조의 이유==를 설명한다

망 구성도는 **약속된 기호**로 그립니다: 라우터(원형/원통), 스위치(사각), 방화벽(벽돌 무늬), 서버(상자). 선은 연결을, 점선은 논리적/VPN 연결을 뜻합니다.

**전형적인 구조 — DMZ 2중 방화벽:**

```mermaid
flowchart LR
    NET[인터넷] --> FW1[외부 방화벽]
    FW1 --> DMZ[DMZ<br/>웹서버]
    DMZ --> FW2[내부 방화벽]
    FW2 --> INT[내부망<br/>DB·사무망]
    classDef ext fill:#e8590c,stroke:#c24906,color:#fff
    classDef fw fill:#f59f00,stroke:#c67c00,color:#111
    classDef dmz fill:#7048e8,stroke:#5a37c0,color:#fff
    classDef intz fill:#2f9e44,stroke:#237a35,color:#fff
    class NET ext
    class FW1,FW2 fw
    class DMZ dmz
    class INT intz
```

외부 공개 서버(웹)는 DMZ에, 진짜 중요한 DB·사무망은 내부 방화벽 뒤에 둡니다. **방화벽을 두 번 거쳐야** 내부에 닿습니다.

!!! question "확인질문 · 나의 답"
    **Q. 웹서버가 해킹당했을 때, DMZ 구조가 없다면 내부망까지 바로 위험해지는 이유는?**
    A. DMZ가 없으면 웹서버가 내부망과 **같은 구역**에 있어, 웹서버를 장악한 공격자가 **추가 벽 없이** 곧장 DB·사무망으로 이동할 수 있기 때문입니다. DMZ는 그 사이에 방화벽 벽을 하나 더 두어 침해 확산을 막습니다.

<div class="quiz">
<p class="quiz-q"><span class="tag">퀴즈</span><b>외부 공개 웹서버를 DMZ에 두고 내부망과 방화벽으로 한 번 더 분리하는 이유로 가장 적절한 것은?</b></p>
<button class="quiz-opt">DMZ가 웹서버 속도를 높여 주기 때문</button>
<button class="quiz-opt">웹서버는 방화벽을 통과할 수 없기 때문</button>
<button class="quiz-opt">DMZ에 두면 IP 주소가 필요 없기 때문</button>
<button class="quiz-opt" data-correct>공격에 노출되기 쉬운 웹서버가 뚫리더라도, 내부망까지 곧장 넘어가지 못하게 벽을 하나 더 두려는 것이기 때문</button>
<div class="quiz-explain"><b>정답: 4번.</b> DMZ는 '완충 구역'입니다. 노출 서버의 침해가 핵심 내부망으로 번지는 것을 이중 방화벽으로 차단합니다.</div>
<button class="quiz-retry">다시 풀기</button>
</div>

---

## ⏱️ 70-95분 · 실제 망 구성도 읽기 실습

!!! abstract "이 블록을 마치면"
    ✔ 구성도에서 내부망/DMZ/클라우드/VPN 터널 구간을 짚는다

본사–지사–클라우드가 섞인 구성도를 보며 각 구간을 식별합니다. 요령: **"이 선을 타고 데이터가 어디서 어디로 가는가"**를 손가락으로 따라갑니다.

- **본사↔지사**: 두 네트워크 사이 → 라우터 + (있다면) VPN 터널(점선)
- **DMZ**: 인터넷과 내부망 사이의 완충 서버 구역
- **클라우드/SaaS로 나가는 트래픽**: 내부망 → 방화벽/프록시 → 인터넷 → 클라우드

!!! question "확인질문 · 나의 답"
    **Q. 이 구성도에서 SaaS로 나가는 트래픽은 어느 구간을 거치나요?**
    A. 사내 PC → 사내망 → **방화벽/프록시** → 인터넷 → SaaS 서버. 핵심은 나갈 때 **방화벽/프록시를 거친다**는 점(여기서 통제·로깅이 이뤄짐)입니다.

<div class="quiz">
<p class="quiz-q"><span class="tag">퀴즈</span><b>망 구성도에서 본사와 지사를 잇는 선이 '점선'으로 그려져 있다면, 가장 적절한 해석은?</b></p>
<button class="quiz-opt">두 지점이 물리적으로 같은 건물에 있다는 뜻</button>
<button class="quiz-opt" data-correct>공용 인터넷 위에 만든 논리적 연결(VPN 터널)이라는 뜻일 가능성이 높음</button>
<button class="quiz-opt">그 선은 실제로는 연결되어 있지 않다는 뜻</button>
<button class="quiz-opt">전원이 연결되어 있다는 뜻</button>
<div class="quiz-explain"><b>정답: 2번.</b> 실선은 물리 연결, 점선은 보통 VPN 같은 논리적 연결을 나타내는 관례입니다. 안 이어진 것(3번)이 아니라 '터널로 이어진' 것입니다.</div>
<button class="quiz-retry">다시 풀기</button>
</div>

---

## ⏱️ 95-120분 · draw.io로 망 구성도 작성 준비

!!! abstract "이 블록을 마치면"
    ✔ draw.io로 도형·연결선·텍스트를 다뤄 구성도를 그릴 수 있다

**draw.io**(무료, diagrams.net)는 브라우저에서 바로 쓰는 다이어그램 도구입니다. 기본 3가지면 구성도를 그립니다.

1. **도형 추가**: 왼쪽 도형 패널에서 끌어다 놓기 (네트워크 아이콘 세트 있음)
2. **선 연결**: 도형 가장자리에서 다른 도형으로 드래그
3. **텍스트**: 도형 더블클릭

!!! tip "실무 팁"
    구성도는 '예쁘게'보다 **'구간 경계가 분명하게'** 그리는 게 중요합니다. DMZ·내부망을 **박스(그룹)로 감싸** 경계를 눈에 보이게 하세요. 실습(오후)에서 직접 그립니다.

---

## ✅ 가르칠 준비 체크리스트 (강의1)

- [ ] IaaS/PaaS/SaaS를 '책임 범위' 표로 설명한다
- [ ] SaaS 접속 경로를 그리고 재택 '가시성' 문제를 설명한다(ZT 예고)
- [ ] DMZ 2중 방화벽 구조와 이유를 설명한다
- [ ] 구성도에서 실선/점선(VPN)·구간을 식별한다
- [ ] 확인질문 4개 + 퀴즈에 답한다

*[IaaS]: Infrastructure as a Service — 인프라(서버)만 빌려 쓰는 클라우드
*[PaaS]: Platform as a Service — 개발 플랫폼까지 제공되는 클라우드
*[SaaS]: Software as a Service — 완성된 소프트웨어를 그대로 쓰는 클라우드
*[DMZ]: DeMilitarized Zone — 외부 공개 서버를 두는 내부망과 분리된 완충 구역
*[VPN]: Virtual Private Network — 공용망 위 암호화된 사설 통로
