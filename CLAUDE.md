# 교안 제작 워크플로우 (jm-teaching-material)

이 리포는 강사 **정민홍**의 강의 교안 모노레포다. AI / Agent / Python 등
여러 강의의 교안을 강의별 폴더로 관리한다. 이 문서는 새 강의를 만들 때
따라야 할 규칙과 절차를 정의한다. **새 세션에서 이 파일을 먼저 읽고 그대로 따른다.**

## 폴더명 규칙
형식: `YY-MM_토픽-형태`  (예: `26-08_ai-agent-oneday`)
- `YY-MM` = 강의 **시작** 년(2자리)-월 (알파벳순 정렬 = 시간순 정렬)
- `_` 로 '언제(날짜)'와 '무엇(토픽)'을 구분
- 토픽·형태는 **영문 kebab-case** (한글·공백 금지)
- 형태에는 기간/유형을 인코딩: `oneday`, `2h`, `4wk`, `8wk`, `3mo` 등
- 같은 강의를 다시 열면 새 시작월로 새 폴더 (예: `26-11_python-basics-8wk`)
- 한글 정식 강의명·상세 정보는 폴더명이 아니라 `course-info.md`와 README에 둔다
- 단, `course-info.md` frontmatter의 날짜(`start_date`)는 전체 `YYYY-MM-DD`로 적는다

## 강의 폴더 구조 (`_template/` 복사본)
```
YY-MM_topic-form/
├── docs/
│   ├── course-info.md   (필수) 강의 기본 정보 + frontmatter
│   ├── syllabus.md      (선택) 상세 커리큘럼 = 교안 원본(source of truth)
│   └── output-spec.md   출력 포맷 확정서
├── samples/  ← 가장 작은 모듈 샘플 (승인 전 검토용)
└── build/    ← 최종 산출물 (.ipynb / .html / .pdf)
                장기 강의는 build/week-01/, week-02/ … 로 분할
```

## 제작 워크플로우 (매 강의 반복)
1. **폴더 생성**: `_template/`을 복사해 `YYYY-MM_토픽-형태/` 로 이름 지음
2. **course-info.md 작성 (필수)**: 아래 "새 강의 시작 질문"으로 정보를 받아 채움
3. **output-spec.md 확정**: 어떤 포맷의 교안이 필요한지(Jupyter/HTML 슬라이드/PDF 등)
   대화로 확정하고 기록. **여기서 합의 전에는 전체 교안을 만들지 않는다.**
4. **가장 작은 모듈 1개를 `samples/`에 제작** → 강사 검토·승인
5. **승인되면 `build/`에 전체를 단계적으로 확장** (한 번에 다 만들지 않음)
6. 의미 있는 단위마다 커밋 & 푸시

> 핵심 원칙: **"작게 샘플 → 확인 → 단계적 확장"**. 긴 강의도 절대 한 번에 만들지 않는다.

## 새 강의 시작 시 물어볼 질문
- 강의명(한글) / 토픽 slug(영문)
- 강의 시작일 (YYYY-MM-DD)
- 기간/형태 (원데이 2h? 8주? 3개월?)
- 대상 수강생 (수준·배경)
- 학습 목표 (수강 후 할 수 있게 되는 것)
- 선수 지식 / 사용 도구·환경
- 원하는 산출물 포맷 (Jupyter / HTML 슬라이드 / PDF …)
- 실습 vs 이론 비율

## 강의 정보 저장 규칙 (원본 보존 + 상단 요약)
강사가 두서 없이 강의 정보를 복붙하면:
1. **원본을 절대 손대지 않고** 그대로 보존한다 (진실의 원천 = audit trail).
2. 파일 **맨 위에 정제된 요약**을 붙인다 (빠른 참조용).
3. 요약과 원본이 어긋나면 **원본을 따른다**.
원본이 길거나 상위 맥락이면 `docs/program-context.md` 같은 별도 파일에 보존한다.

## course-info.md frontmatter (README 자동 인덱스용)
```yaml
---
title_ko: "..."          # 한글 정식 강의명
slug: topic-form         # 폴더명의 토픽-형태 부분
start_date: YYYY-MM-DD
duration: oneday|2h|4wk|8wk|3mo
audience: "..."
format: jupyter|html|pdf # output-spec에서 확정
status: planning|sample|building|done
---
```

## 상태(status) 생애주기
`planning`(정보만) → `sample`(작은 모듈 제작·검토중) →
`building`(승인 후 전체 확장중) → `done`(완료)

## 공통 자산
여러 강의가 공유하는 것(환경설정 안내, 로고, 반복 코드 스니펫)은 강의 폴더에
복사하지 말고 `_shared/`에 두고 참조한다.

## 리포 규칙
- 공개 범위: **private** (GitHub: `welovecherry/jm-teaching-material`)
- 새 강의를 추가하면 `README.md`의 인덱스 표에 한 줄 추가한다
