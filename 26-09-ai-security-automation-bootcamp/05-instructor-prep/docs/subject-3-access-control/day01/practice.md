# 실습 · 조직 RBAC 설계 및 최소권한 정책 구현 (총 120분)

!!! note "자리표시 — 뼈대만 (강사가 직접 채웁니다)"
    실습 베이스라인 코드·상세 문제는 강사가 직접 작성합니다. 상세교안의 진행 단계만 잡아 두었습니다.

> **실습 목표:** 가상 A사 조직 구조를 반영한 RBAC과 권한 매트릭스를 설계하고, 통합 판단 함수를 구현한다.

## 진행 단계 (상세교안 기준)

1. 가상 A사 조직 시나리오(4개 부서, 부서별 3~5개 권한) 확인
2. `config/roles.json`, `user_roles.json`, `policy_matrix.json` 설계·작성
3. `rbac.py`에 `has_permission()`, `assign_role()`, `revoke_role()` 구현
4. `policy.py`에 `check_policy()`, `is_exception_valid()`, `evaluate_access()` 구현
5. 예외 샘플 3건(만료 전/후 포함)을 `config/exceptions.json`에 작성해 테스트
6. 4가지 테스트 케이스(정상/위반/예외허용/예외만료거부)를 `day01_test_result.md`에 정리

**산출물:** `access_control/rbac.py`, `policy.py`, `config/*.json`

## (작성 예정) 강사 예습 포인트

- 강사가 **먼저 4개 함수를 직접 구현**해보고, 학생이 자주 막히는 지점 기록
  (`.get` 안 써서 KeyError / `levels.index` 비교 방향 헷갈림 / 만료일 비교 실수)
- "예외 만료" 테스트를 위해 **어제 날짜/내일 날짜** 예외를 각각 넣어 보는 팁
- 강의 중 ✍️ 손코딩과 연결: 강의에서 친 함수를 실습에서 파일로 완성

## 평가 기준 (상세교안)

- RBAC과 권한 매트릭스가 최소권한 원칙에 맞게 설계되었는가
- 예외 만료 여부가 정확히 판단되는가
- 4가지 테스트 케이스가 모두 예상대로 동작하는가
