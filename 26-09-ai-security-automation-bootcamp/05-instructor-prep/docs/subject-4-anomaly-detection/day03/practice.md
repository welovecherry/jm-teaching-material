# 실습 · 고급 탐지 로직 및 상관분석 구현 (총 120분)

!!! note "자리표시 — 뼈대만 (강사가 직접 채웁니다)"
    실습 베이스라인 코드·상세 문제는 강사가 직접 작성합니다. 상세교안의 진행 단계만 잡아 두었습니다.

> **실습 목표:** 비인가접근·SaaS이상·IOC 탐지를 구현하고, 시간 윈도우 기반 상관분석으로 위험점수를 종합한다.

## 진행 단계 (상세교안 기준)

1. `anomaly_detection/advanced_detection.py`에 `detect_unauthorized_access()`, `detect_saas_anomaly()`, `match_ioc()`를 구현한다
2. 3과목 `access_control`의 config(`roles.json`, `policy_matrix.json`)를 import해 실제로 연동한다
3. `config/threat_intel.json`에 샘플 악성 IP 5개를 작성하고 매칭 테스트를 진행한다
4. `anomaly_detection/correlation.py`에 `group_by_user()`, `check_chain()`을 구현하고 3단계 체이닝 패턴을 테스트 데이터에 삽입해 검증한다
5. `calculate_risk_score()`에 상관분석 매칭 결과를 가산하는 로직을 연동한다
6. 테스트 이벤트 10건(정상 5·이상 5)의 위험점수를 `anomaly_detection/day03_risk_scores.json`으로 저장한다

**산출물:** `anomaly_detection/advanced_detection.py`, `correlation.py`, `day03_risk_scores.json`

## (작성 예정) 강사 예습 포인트

- 강사가 **먼저** "실패5→성공→비인가→다운로드" 킬체인을 테스트 데이터로 만들어 `check_chain()`이 잡는지 확인
- `window_minutes`를 10/30/60으로 바꿔 탐지 건수 변화와 오탐 여부를 눈으로 확인(강의2 튜닝 실험과 연결)
- 3과목 config를 실제로 import해 비인가 접근 판단이 연동되는지 시연
- 학생이 자주 막히는 지점 기록:
  - `group_by_user`에서 정렬 누락 → 체이닝 실패
  - `check_chain`의 window 시간 비교에서 `timedelta` 안 쓰고 문자열 비교
  - 위험점수 가중치를 코드에 하드코딩(config로)
  - IOC 목록 하드코딩(threat_intel.json으로)

## 평가 기준 (상세교안)

- 3과목 access_control 모듈과 실제로 연동되는가
- 체이닝 규칙이 의도한 시나리오를 정확히 탐지하는가
- 위험점수 계산이 가중치·상관분석 기반으로 합리적으로 동작하는가
