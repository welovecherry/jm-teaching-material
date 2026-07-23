# 실습 · 접근통제 결과 리포트 자동화 완성 및 발표 (총 120분)

!!! note "자리표시 — 뼈대만 (강사가 직접 채웁니다)"
    실습 베이스라인 코드·상세 문제는 강사가 직접 작성합니다. 상세교안의 진행 단계만 잡아 두었습니다.

> **실습 목표:** 1~4일차 모듈을 통합해 접근통제 결과를 자동으로 리포트화하는 스크립트를 완성하고 시연한다.

## 진행 단계 (상세교안 기준)

1. `access_control/weekly_report.py`에 `generate_weekly_report()`를 완성한다(6개 모듈 import + 집계 + details 근거)
2. `access_control_weekly_report_YYYYMMDD.md`로 결과를 저장한다(1과목 템플릿+데이터 결합 재사용)
3. `agent_core/tool_router.py`에 핵심 함수(`evaluate_full_access`, `run_revocation_bot`)를 등록하는 코드를 실제로 작성해 연동을 확인한다
4. 코드 리뷰 체크리스트(config 하드코딩·예외처리·로깅·재사용)로 `access_control/` 전체를 점검하고 발견된 문제를 수정한다
5. 5분 내외 발표 자료(access_control 모듈 구조도 + 데모 화면)를 준비한다
6. 조별로 실제 리포트 생성을 시연하고 피드백을 `day05_retrospective.md`에 정리한다

**산출물:** `access_control/weekly_report.py`, `access_control_weekly_report_*.md`, `day05_retrospective.md`

## (작성 예정) 강사 예습 포인트

- 강사가 **먼저** 6개 모듈을 import해 `generate_weekly_report()`를 돌려, 5일치 함수가 한 번에 소환되는 흐름을 체감
- **임계치 알림**: `threshold`를 낮춰 알림이 뜨는 경우/안 뜨는 경우를 각각 재현(강의2 깊이보기와 연결)
- `tool_router` 등록 두 줄로 1과목 Agent가 접근통제를 '도구'로 호출하는 데모를 미리 구성
- 학생이 자주 막히는 지점 기록:
  - `import *`로 이름 충돌 → 명시적 import로 해결
  - 리포트에 건수만 넣고 `details` 근거를 빠뜨림
  - 코드 리뷰에서 하드코딩·로그 누락을 스스로 못 찾음
- 발표 팁: 모듈 구조도(Day5 강의1 재사용 지도 활용) + 실제 리포트 1장 시연

## 평가 기준 (상세교안)

- 1~4일차 모든 모듈이 오류 없이 통합되는가
- 주간 리포트가 실제 운영에 쓸 수 있는 수준(요약+근거)으로 구성되었는가
- agent_core와의 연동 지점(tool_router 등록)을 명확히 설명할 수 있는가
