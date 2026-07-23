# 실습 · 이벤트 분류 및 로그인·트래픽 탐지 룰 구현 (총 120분)

!!! note "자리표시 — 뼈대만 (강사가 직접 채웁니다)"
    실습 베이스라인 코드·상세 문제는 강사가 직접 작성합니다. 상세교안의 진행 단계만 잡아 두었습니다.

> **실습 목표:** 이벤트를 유형별로 분류하고, 비정상 로그인·트래픽 급증 탐지 룰을 구현해 검증한다.

## 진행 단계 (상세교안 기준)

1. `anomaly_detection/classify.py`에 `classifier_registry`와 `classify_event()`를 구현한다
2. 1일차 `normalized_events.json`으로 베이스라인(평균·표준편차)을 계산한다(`groupby`·`describe`)
3. `anomaly_detection/login_detection.py`에 `detect_bruteforce()`(시간창 포함), `detect_offhour_login()`을 구현한다
4. 테스트용 login 샘플에 **5분 내 6회 실패**를 심어 탐지가 되는지 확인한다
5. `anomaly_detection/traffic_detection.py`에 `detect_traffic_spike()`(rolling)을 구현하고 의도적 급증 구간으로 검증한다
6. 임계값을 `config/detection_thresholds.json`으로 분리하고 결과를 `day02_result.md`에 정리한다

**산출물:** `anomaly_detection/classify.py`, `login_detection.py`, `traffic_detection.py`

## (작성 예정) 강사 예습 포인트

- 강사가 **먼저** `detect_bruteforce()`의 '시간창 없는 1차 버전'과 '보완 버전'을 둘 다 돌려, 오탐 차이를 눈으로 확인(강의2 ✍️ 블록과 연결)
- `rolling(window).mean()`을 window=5/60으로 바꿔 탐지 건수가 달라지는지 실험
- **콜드 스타트**: 데이터 적은 신규 사용자의 베이스라인 처리 방법 시연
- 학생이 자주 막히는 지점 기록:
  - `detect_bruteforce`에서 시간창 조건 누락(이름엔 있는데 코드엔 없음)
  - `rolling`의 앞부분 NaN(window 미만 구간) 처리
  - 임계값을 코드에 하드코딩(config로 빼야 함)
  - registry에 함수를 `()` 붙여 등록(호출 결과가 아니라 함수 자체를 넣어야 함)

## 평가 기준 (상세교안)

- 규칙 기반과 베이스라인 기반 분류가 모두 구현되었는가
- 의도적으로 삽입한 이상 케이스가 정확히 탐지되는가
- 임계값이 하드코딩되지 않고 config로 분리되었는가
