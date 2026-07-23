# 실습 · 접근 요청-승인-부여 워크플로우 완성 (총 120분)

!!! note "자리표시 — 뼈대만 (강사가 직접 채웁니다)"
    실습 베이스라인 코드·상세 문제는 강사가 직접 작성합니다. 상세교안의 진행 단계만 잡아 두었습니다.

> **실습 목표:** 요청 생성 → 검토 → 승인/반려 → 부여로 이어지는 접근 요청-승인 워크플로우를 코드로 완성하고, 정상·정책위반·SLA초과 3가지 시나리오를 돌린다.

## 진행 단계 (상세교안 기준)

1. `access_control/request_flow.py`에 `create_request()`를 구현한다(id·user·system·level·status·requested_at·approver·sla_hours 필드)
2. `approve_request()`에 **상태 전이 검증**(`reviewing`이 아니면 `ValueError`)을 넣어 구현한다
3. `check_sla_breach()`로 기한 초과 요청을 색출하는 함수를 구현한다
4. `approve_request_with_policy_check()`로 Day1의 `evaluate_access()`를 연동한다
5. 요청 3건을 만들어 `config/requests.json`에 저장한다(정상 / 정책 위반 / SLA 초과)
6. 4가지 테스트(정상 승인 / 잘못된 상태 승인 시도→에러 / 정책 위반 자동 반려 / SLA 초과 탐지)를 `day02_test_result.md`에 정리한다

**산출물:** `access_control/request_flow.py`, `config/requests.json`

## (작성 예정) 강사 예습 포인트

- 강사가 **먼저** `approve_request()`를 구현하며 "이미 approved된 요청을 또 승인하면?"을 직접 실행해 `ValueError`를 눈으로 확인
- **경계값 SLA**: `requested_at`을 25시간 전으로 넣어 24h 기한 초과를 재현하는 팁(강의2 ✍️ 블록과 연결)
- 학생이 자주 막히는 지점 기록:
  - `datetime.fromisoformat()`을 안 쓰고 문자열끼리 비교하려다 실패
  - `!=` 대신 `==`로 조건을 반대로 씀
  - `json.dump`에서 `ensure_ascii=False`를 빼 한글이 깨짐
- 강의 중 ✍️ 손코딩과 연결: 강의에서 친 `approve_request()`를 실습에서 파일로 완성

## 평가 기준 (상세교안)

- 상태 전이 검증이 잘못된 승인을 정확히 막는가(에러 발생 확인)
- SLA 초과 요청이 정확히 색출되는가
- Day1 정책 함수(`evaluate_access`)가 승인 로직에 정상 연동되는가
