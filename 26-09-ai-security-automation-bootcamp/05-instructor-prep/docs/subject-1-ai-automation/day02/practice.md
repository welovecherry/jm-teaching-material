# 실습 · 보안 로그 파일 파서 작성 (총 120분)

> **실습 목표:** CSV 형식의 샘플 보안 로그를 안전하게 읽고, 오류 상황에서도 죽지 않는 파서를 완성한다.

!!! note "강사 예습본 안내"
    학생 배포용 베이스라인·문제지는 강사가 직접 작성합니다. 여기서는 강사가 먼저 풀어보는 **참고 정답 스케치**와 예습 포인트를 담습니다.

## 진행 단계 (상세교안 기준)

1. `agent_core/sample_logs.csv`를 20~30줄로 작성한다 (컬럼: `timestamp,user,event,ip`)
2. `agent_core/log_parser.py`를 만들고 `parse_logs(filepath)` 함수를 작성한다
3. `csv.DictReader`로 읽고, 각 행의 이벤트 유형을 분류해 리스트에 저장한다
4. 파일이 없거나 컬럼이 누락된 경우를 대비해 `try/except`로 방어한다
5. `RotatingFileHandler`로 `agent.log`에 처리 현황(시작-완료-실패건수)을 기록한다
6. 일부러 잘못된 경로를 입력해 예외처리가 정상 동작하는지 테스트한다

**산출물:** `agent_core/log_parser.py`, `agent_core/sample_logs.csv`, `agent.log`

## 🧑‍🏫 강사 참고 정답 스케치 (예습용)

```python
# log_parser.py — 안전한 보안 로그 파서
import csv
import logging
from logging.handlers import RotatingFileHandler
from collections import Counter

# ① 로깅 설정 (파일 회전 포함)
handler = RotatingFileHandler('agent.log', maxBytes=1_000_000,
                              backupCount=5, encoding='utf-8')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    handlers=[handler])

def parse_logs(filepath):
    logging.info(f'{filepath} 파싱 시작')
    try:
        with open(filepath, encoding='utf-8') as f:
            rows = list(csv.DictReader(f))          # ② CSV → 딕셔너리 리스트
        # ③ 실패 이벤트 집계
        fails = [r['user'] for r in rows if r.get('event') == 'login_failed']
        logging.info(f'읽기 완료 - 전체 {len(rows)}건, 실패 {len(fails)}건')
        return rows, Counter(fails)
    except FileNotFoundError:                        # ④ 파일 없음 방어
        logging.error(f'{filepath} 파일 없음 - 빈 결과 반환')
        return [], Counter()

if __name__ == '__main__':                           # ⑤ 이 파일을 직접 실행할 때만
    rows, counter = parse_logs('sample_logs.csv')
    print(f'실패 상위: {counter.most_common(3)}')
    parse_logs('없는파일.csv')                        # 일부러 오류 유발 테스트
```

!!! tip "🐍 이 스크립트에 오늘 배운 문법이 다 있다"
    - **함수·기본 반환**: `parse_logs`(리팩토링·재사용)
    - **with open + DictReader**: 안전한 파일·CSV 읽기(②)
    - **`.get()` + 컴프리헨션 + Counter**: 집계(③, Day1 복습)
    - **try/except 구체적 예외**: FileNotFoundError 방어(④)
    - **logging + RotatingFileHandler**: 처리 현황 기록(①)
    - **`if __name__ == '__main__':`**: "이 파일을 직접 실행할 때만" 도는 관용구(⑤) — 모듈로 import될 땐 안 돎

!!! warning "🐍 문법 상자 — `if __name__ == '__main__':`"
    이 관용구는 "이 파일을 **직접** 실행했을 때만" 아래 코드를 돌립니다. 다른 파일에서 `import log_parser`로 **가져올 땐 실행 안 됩니다.** 그래서 함수는 재사용하되, 테스트 실행 코드는 이 안에 둡니다. 실무 파이썬 파일의 표준 패턴이라 꼭 짚어 주세요.

## 강사 예습 포인트

- **먼저** 정상 파일 → 없는 파일 순서로 실행해, 없는 파일에서도 **안 죽고 로그만 남기는지** 확인
- `agent.log`를 열어 시간·레벨이 붙은 기록을 눈으로 확인
- 학생이 자주 막히는 지점:
  - `encoding='utf-8'` 빠뜨려 한글 깨짐
  - except를 try보다 넓게(Exception 먼저) 놓아 구체적 except 무력화
  - `.get()` 대신 `[]`로 컬럼 접근 → 누락 컬럼에서 KeyError
  - `if __name__` 없이 테스트 코드를 두어 import 시 원치 않게 실행됨

## 평가 기준 (상세교안)

- 파일이 없을 때 프로그램이 죽지 않고 안내 메시지를 출력하는가
- logging으로 처리 현황이 기록되는가
- 함수화가 되어 다른 파일 경로에도 재사용 가능한가
