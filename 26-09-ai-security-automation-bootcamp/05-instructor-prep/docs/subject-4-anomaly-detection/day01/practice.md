# 실습 · 샘플 로그 데이터셋 탐색 및 전처리 (총 120분)

!!! note "자리표시 — 뼈대만 (강사가 직접 채웁니다)"
    실습 베이스라인 코드·상세 문제는 강사가 직접 작성합니다. 상세교안의 진행 단계만 잡아 두었습니다.

> **실습 목표:** 3개 로그 소스(로그인/방화벽/SaaS)를 pandas로 탐색하고 공통 스키마로 정규화한다.

## 진행 단계 (상세교안 기준)

1. `anomaly_detection/explore_logs.py`를 생성해 3개 CSV를 pandas로 읽고 탐색한다(`head`·`info`·`value_counts`)
2. 각 로그의 결측치·이상 타임스탬프 비율을 확인하고 정제한다(`to_datetime(coerce)`·`dropna`)
3. `anomaly_detection/normalize.py`에 `normalize_login()`, `normalize_firewall()`, `normalize_saas()`를 구현한다
4. 3개 로그를 공통 스키마(timestamp·user·source·event_type·detail)로 변환해 하나의 리스트로 통합한다
5. 통합 결과를 `normalized_events.json`으로 저장한다(`ensure_ascii=False`)
6. 정규화 전후 건수를 비교해 `anomaly_detection/day01_summary.md`에 기록한다

**산출물:** `anomaly_detection/normalize.py`, `normalized_events.json`

## (작성 예정) 강사 예습 포인트

- 강사가 **먼저** 3개 CSV를 만들어(성공/실패·차단 섞어) `value_counts()`로 분포를 확인
- 일부러 **깨진 타임스탬프·빈 user**를 몇 건 심어, `coerce`+`dropna`로 걸러지는지 눈으로 확인
- **건수 대조**: 원본/전처리후/정규화후 건수를 각각 찍어 손실 지점을 추적하는 시범
- 학생이 자주 막히는 지점 기록:
  - `read_csv` 경로·인코딩 문제
  - `to_datetime`에서 `coerce` 빠뜨려 깨진 값에 멈춤
  - 방화벽 로그엔 `user`가 없어 정규화 시 처리 고민(src_ip를 user 대체로 둘지 등)
  - `detail`에 무엇을 담을지 로그별로 다름

## 평가 기준 (상세교안)

- 3개 로그 소스 모두 정상적으로 정규화되는가
- 결측치·이상 데이터가 적절히 처리되는가
- 정규화 전후 건수 비교로 데이터 손실을 검증했는가
