# 강의 사이트 템플릿 (MkDocs Material) — 재사용 자산

`26-09-ai-security-automation-bootcamp/05-instructor-prep`에서 완성한 강의/예습 사이트의
**UI·계층 구조·사이드바·독(dock)·커스텀 위젯**을 다른 강의에서도 그대로 쓰도록 뽑아 둔 폴더입니다.
이 폴더만 복사하면 새 사이트가 바로 섭니다.

## 이 폴더에 든 것
```
_shared/mkdocs-course-site/
├── README.md            ← 지금 이 파일 (설명서)
├── mkdocs.yml.template  ← 주석 단 설정 원본 (복사 후 <...>만 교체)
└── assets/              ← 커스텀 위젯 4종 (그대로 복사해 쓰기)
    ├── custom.css       ← 사이드바/본문 글자크기·형광펜색 등 미세 조정
    ├── quiz.css / quiz.js         ← 인터랙티브 객관식 퀴즈
    ├── progress.css / progress.js ← 진행률 바 + 읽기% 배지 + 읽음 체크
    └── wordbook.css / wordbook.js ← 나만의 단어장(용어 체크 누적)
```

---

## 1. 기술 스택
- **MkDocs + Material 테마** 한 가지로 끝. 정적 사이트 → GitHub Pages 무료 호스팅.
- 설치: `pip install mkdocs-material` (플러그인은 built-in `search`만 씀, 추가 설치 불필요)
- 위젯(퀴즈·진행률·단어장)은 **순수 바닐라 JS + localStorage**. 서버·빌드도구 없음.

## 2. 계층 구조 (사이드바 3단 중첩)
이 사이트의 정체성. `nav`를 이 3단으로 짜는 게 핵심입니다.
```
과목 (예: 1과목 · AI 자동화 기초)
└─ Day (하루 = 6시간)
   ├─ ① 개요·시간표   index.md
   ├─ ② 강의1 (오전)  lecture1.md
   ├─ ③ 강의2 (오후)  lecture2.md
   └─ ④ 실습          practice.md
```
- **폴더 = Day, 파일 = 교시.** 하루를 한 파일에 넣으면 스크롤 지옥이라 교시별로 쪼갭니다.
- **폴더/파일명은 ASCII**(`subject-1-ai-automation/day01/lecture1.md`) → URL이 깨끗함.
- **사이드바에 보이는 이름은 한글** → `nav:`에서 `"한글 제목": ascii/경로.md`로 매핑.
- 짧은 과목(강의 1개뿐인 날 등)은 교시 수를 줄여도 됨 — 4개 묶음은 기본형일 뿐.

## 3. UI 요소 (테마 기본 기능)
`mkdocs.yml`의 `theme.features` / `palette` / `markdown_extensions`로 켭니다.
- **라이트/다크 토글** — 우상단 버튼, OS 설정 자동 감지. `primary` 색만 바꾸면 브랜드색 교체.
- **상단 탭 + 좌 사이드바 + 우 목차(TOC)** 3분할 레이아웃.
- **콜아웃 상자** `!!! note/tip/warning/question/example` — 의미별로 색·아이콘 다름.
- **접기 블록** `??? note "더 깊이"` — 긴 심화 내용 숨기기.
- **코드 복사 버튼 / 검색 하이라이트·자동완성 / mermaid 다이어그램 / 탭 콘텐츠**.
- **텍스트 강조** `==형광펜==` `^^밑줄^^` `~~취소선~~`, 약어 툴팁(`abbr`).

## 4. 커스텀 위젯 & 독(dock) — 이 사이트만의 차별점
Material 기본엔 없는, `assets/`가 주입하는 4가지. **강의 몰입·복습 장치**입니다.

| 위젯 | 파일 | 하는 일 | 화면 위치 |
|---|---|---|---|
| 인터랙티브 퀴즈 | `quiz.*` | 4지선다 보기 클릭 → 즉시 채점 + 해설. 틀리면 자동으로 복습 목록에 저장 | 본문 안 |
| 진행률 독 | `progress.*` | 상단 진행 바 + **하단 '📖 읽기 %' 배지(dock)** + 섹션별 '읽음' 체크박스 | 상단/하단 고정 |
| 나만의 단어장 | `wordbook.*` | 용어표 각 줄 앞 체크박스 자동 삽입 → 체크한 용어를 전 과목 누적, 메모 저장 | 본문 표 + 전용 페이지 |
| 미세 스타일 | `custom.css` | 사이드바 최상위(과목) 굵게+구분선, 본문/박스 글자크기 키움, 형광펜색 | 전역 |

- **상태 저장은 전부 브라우저 localStorage.** 서버 없이 새로고침·재방문해도 유지.
  키: `wordbook.v1`(단어장), `reviewWrong.v1`(오답), 진행률은 페이지별 키.
- **퀴즈 HTML 패턴**(본문에 그대로 삽입, 블록 내부 빈 줄 없이):
  ```html
  <div class="quiz">
  <p class="quiz-q"><span class="tag">퀴즈</span><b>질문?</b></p>
  <button class="quiz-opt">오답 보기</button>
  <button class="quiz-opt" data-correct>정답 보기</button>
  <button class="quiz-opt">오답 보기</button>
  <div class="quiz-explain"><b>정답: …</b> 왜 맞고 다른 보기는 왜 틀렸는지.</div>
  <button class="quiz-retry">다시 풀기</button>
  </div>
  ```
- **단어장은 마크다운 표를 그대로 인식** — 문서엔 평범한 용어 표만 쓰면 JS가 체크박스를 붙입니다.
- `wordbook.md` 페이지(누적·복습 표시용)와 `nav`의 `"🔁 복습하기"` 항목이 한 쌍입니다.

## 5. 새 강의에 적용하는 법
```bash
# 1) 새 강의의 사이트 폴더 만들기 (05-instructor-prep 등)
mkdir -p <새강의>/05-instructor-prep/docs
cd <새강의>/05-instructor-prep

# 2) 위젯 자산 통째로 복사
cp -R ../../_shared/mkdocs-course-site/assets docs/assets

# 3) 설정 복사 후 <...> 부분(site_name·nav)만 교체
cp ../../_shared/mkdocs-course-site/mkdocs.yml.template mkdocs.yml
#   → site_name / nav 를 이 강의의 과목·Day 구조로 수정

# 4) 필수 페이지 3개 준비: docs/index.md, docs/wordbook.md, docs/prep-style-guide.md
#    (기존 프로젝트 것을 복사해 내용만 교체하는 게 빠름)

# 5) 로컬 미리보기 (저장하면 자동 새로고침)
pip install mkdocs-material   # 처음 한 번
mkdocs serve                  # http://127.0.0.1:8000

# 6) 배포 (선택) — GitHub Pages
mkdocs gh-deploy
```

## 6. 재사용 시 유의점
- **여러 강의 사이트를 같은 도메인(GitHub Pages)에 올리면** localStorage 키(`wordbook.v1` 등)가
  겹쳐 단어장/진행률이 섞일 수 있음. 강의별로 서브도메인·별도 repo를 쓰거나, JS 상단의 키
  문자열에 강의 식별자를 붙여(`wordbook.v1` → `wordbook.<강의>.v1`) 분리하세요.
- `abbr`·`attr_list`·`md_in_html`은 위젯 동작의 전제라 **빼지 마세요**.
- 문서 작성 규칙(말투·콜아웃 용법·퀴즈 형식·분량)은 원본
  `05-instructor-prep/docs/prep-style-guide.md`가 완성형입니다 — 같이 복사해 쓰면 됩니다.

## 7. 원본 위치 (살아있는 예시)
`26-09-ai-security-automation-bootcamp/05-instructor-prep/` — 실제로 굴러가는 완성본.
막히면 거기의 `mkdocs.yml`·`docs/index.md`·`docs/*/day01/`을 참고하세요.
