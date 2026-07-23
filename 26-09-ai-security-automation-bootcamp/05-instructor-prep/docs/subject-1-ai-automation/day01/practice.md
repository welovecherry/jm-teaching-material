# 실습 · 제어문 기반 로그 필터링 스크립트 (총 120분)

> **실습 목표:** 오늘 배운 변수·자료형·조건문·반복문·집계만으로 실전형 로그 필터링 스크립트(`day01_basic.py`)를 완성한다.

!!! note "강사 예습본 안내"
    학생 배포용 베이스라인·문제지는 강사가 직접 작성합니다. 여기서는 **강사가 먼저 풀어보는 참고 정답 스케치**와 예습 포인트를 담습니다.

## 진행 단계 (상세교안 기준)

1. `agent_core/day01_basic.py` 파일을 생성한다
2. 예제의 `logs` 리스트를 20개로 확장한 샘플 데이터를 만든다
3. `event`가 `login_failed`인 것만 추출해 사용자별 실패 횟수를 `Counter`로 집계한다
4. 2회 이상인 사용자를 '확인 필요' 목록으로 출력한다
5. 임계값(`THRESHOLD`)은 하드코딩하지 않고 파일 상단 변수로 분리한다 — config 분리 습관의 첫걸음
6. 완성 스크립트를 조원과 교차 실행하며 입력값을 바꿔도 오류가 없는지 확인한다

**산출물:** `agent_core/day01_basic.py`

## 🧑‍🏫 강사 참고 정답 스케치 (예습용)

```python
# day01_basic.py — 로그 필터링·카운팅 스크립트
from collections import Counter

# ① 설정값은 코드 맨 위에 분리 (하드코딩 금지 습관)
THRESHOLD = 2   # 이 횟수 이상 실패하면 '확인 필요'

# ② 샘플 로그 (실제 실습에선 20개로 확장)
logs = [
    {'user': 'kim01', 'event': 'login_failed'},
    {'user': 'lee02', 'event': 'login_success'},
    {'user': 'kim01', 'event': 'login_failed'},
    {'user': 'park03', 'event': 'login_failed'},
    # ... 20개까지 확장
]

# ③ 실패 로그의 user만 골라 집계 (컴프리헨션 + Counter)
failed_users = [log['user'] for log in logs if log['event'] == 'login_failed']
counter = Counter(failed_users)

# ④ 임계값 이상 반복 실패한 사용자 출력
print(f'=== 실패 {THRESHOLD}회 이상 사용자 ===')
for user, cnt in counter.items():
    if cnt >= THRESHOLD:
        print(f'{user}: {cnt}회 실패 — 확인 필요')
```

!!! tip "🐍 이 스크립트에 오늘 배운 문법이 다 들어있다"
    - **변수·상수 분리**: `THRESHOLD`(①)
    - **리스트·딕셔너리**: `logs`(②)
    - **컴프리헨션 + 조건**: `failed_users`(③)
    - **Counter 집계 + for + if + f-string**: 출력(④)
    - 즉 오늘 배운 조각들이 한 파일로 조립됩니다. "작은 문법들이 모여 도구가 된다"를 체감시키세요.

## 강사 예습 포인트

- **먼저** THRESHOLD를 2→3으로 바꿔 출력이 달라지는 걸 확인(설정 분리의 이점 체감)
- 학생이 자주 막히는 지점:
  - 리스트 인덱스 0/1 헷갈림
  - `=`와 `==` 혼동
  - f-string 안에서 딕셔너리 키 따옴표 충돌(`{log["user"]}`)
  - `int()` 없이 문자열 숫자 계산 시도
  - 들여쓰기 오류(IndentationError)
- **확장 아이디어**: `event` 종류를 `set`으로 뽑아 "어떤 이벤트 유형들이 있나" 보여주기

## 평가 기준 (상세교안)

- 조건문·반복문을 활용해 정상 동작하는가
- 임계값(THRESHOLD)이 하드코딩되지 않고 변수로 분리되었는가
- 출력 메시지가 f-string으로 읽기 쉽게 작성되었는가
