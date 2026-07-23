# 실습 · 권한 회수 자동화 및 조건기반 정책 엔진 구현 (총 120분)

!!! note "자리표시 — 뼈대만 (강사가 직접 채웁니다)"
    실습 베이스라인 코드·상세 문제는 강사가 직접 작성합니다. 상세교안의 진행 단계만 잡아 두었습니다.

> **실습 목표:** 과다권한 회수봇과 조건기반 정책·임시권한을 통합한 최종 정책 엔진을 완성한다.

## 진행 단계 (상세교안 기준)

1. `access_control/revoke.py`에 `classify_revocation()`, `revoke_permission()`, `log_revocation()`을 구현한다
2. `config/sensitive_permissions.json`으로 민감 권한 목록을 분리 관리한다
3. Day2 `request_flow.py`의 `create_request()`를 import해 `create_revocation_approval()`을 구현하고 `run_revocation_bot()`으로 통합한다
4. `access_control/conditional.py`에 `check_time_condition()`, `evaluate_conditional_access()`, `grant_temporary_access()`를 구현한다
5. `evaluate_full_access()`로 1일차 정책 매트릭스 + 조건부 접근 + 임시권한을 통합한다
6. 4가지 테스트(일반권한 자동회수 / 민감권한 승인요청 / 조건 미충족 거부 / 임시권한 허용)를 `day04_test_result.md`에 정리한다

**산출물:** `access_control/revoke.py`, `conditional.py`, `revocation_log.json`

## (작성 예정) 강사 예습 포인트

- 강사가 **먼저** 회수 3유형을 각각 테스트하며, 민감/일반 권한이 서로 다른 경로로 처리되는지 확인
- **경계값**: `check_time_condition`의 9시·18시 딱 걸치는 시각으로 연쇄 비교(`start <= h < end`)를 검증(강의2 ✍️ 블록과 연결)
- JIT: `duration_hours=2`로 준 뒤, `expires_at`을 과거로 조작해 `is_temp_access_valid`가 False가 되는지 확인
- 학생이 자주 막히는 지점 기록:
  - `revoke_permission`에서 `if role in ...` 없이 `remove` 호출 → 에러
  - 조건을 OR로 묶어 구멍 생김(AND여야 함)
  - `evaluate_full_access`에서 임시권한 경로(`any(...)`)를 빠뜨림

## 평가 기준 (상세교안)

- 민감 권한과 일반 권한이 올바르게 분류·처리되는가
- 조건기반 정책과 임시권한이 정확히 동작하는가
- 2일차 모듈(request_flow.py)이 정상적으로 재사용되는가
