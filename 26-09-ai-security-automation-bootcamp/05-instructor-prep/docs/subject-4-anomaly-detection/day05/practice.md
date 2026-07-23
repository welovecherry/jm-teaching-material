# 실습 · AI 기반 이벤트 요약·우선순위 분류 자동화 구현 및 발표 (총 120분)

!!! note "자리표시 — 뼈대만 (강사가 직접 채웁니다)"
    실습 베이스라인 코드·상세 문제는 강사가 직접 작성합니다. 상세교안의 진행 단계만 잡아 두었습니다.

> **실습 목표:** 1~4일차 모든 탐지 모듈을 통합하고 AI 요약·우선순위 분류까지 이어지는 최종 파이프라인을 완성해 시연한다.

## 진행 단계 (상세교안 기준)

1. `anomaly_detection/pipeline.py`를 생성해 1~4일차 모든 모듈을 import한다
2. `run_anomaly_pipeline()`으로 원본 로그 입력부터 위험점수·우선순위 산출까지 전체 흐름을 통합한다
3. high 우선순위로 분류된 이벤트를 자연어 요약한다(1과목 `event_summarizer` 재사용)
4. 결과를 `anomaly_detection_report_YYYYMMDD.json/md`로 저장한다
5. `agent_core/tool_router.py`에 이상탐지 모듈의 핵심 함수를 등록하는 코드를 작성해 연동을 확인한다
6. 5분 내외 발표 자료를 준비해 팀별로 전체 파이프라인을 시연하고, 피드백을 `anomaly_detection/day05_retrospective.md`에 정리한다

**산출물:** `anomaly_detection/pipeline.py`, `anomaly_detection_report_*.json`, `day05_retrospective.md`

## (작성 예정) 강사 예습 포인트

- 강사가 **먼저** 1~4일차 모듈을 import해 `run_anomaly_pipeline()`을 끝까지 돌려, 로그→요약 리포트 전 과정을 체감
- **high만 요약**: 전체 요약 vs high만 요약의 비용·가독성 차이를 시연(강의2와 연결)
- `tool_router` 등록으로 1과목 Agent가 이상탐지를 도구로 호출하는 데모, 그리고 5과목 SOAR 입력으로 넘어가는 흐름 설명
- **디버깅**: 고장난 pipeline 샘플을 준비해 traceback 아래→위 읽기를 시범
- 학생이 자주 막히는 지점 기록:
  - `import *` 이름 충돌
  - 우선순위 계산에 자산 중요도 반영 누락
  - high 필터링 없이 전부 요약(비용 폭증)
  - 발표 시 4→5과목(탐지→대응) 연결 설명 부족

## 평가 기준 (상세교안)

- 1~4일차 모든 모듈이 하나의 파이프라인으로 오류 없이 통합되는가
- high 우선순위 이벤트에 대한 자연어 요약이 정상 생성되는가
- agent_core 연동 지점을 발표에서 명확히 설명하는가
