# 실습 · Webhook 수신·정기 실행 자동화 스크립트 (총 120분)

> **실습 목표:** Webhook으로 이벤트를 수신·처리하고, 스케줄러로 정기 점검까지 이어지는 자동화 스크립트를 완성한다.

!!! note "강사 예습본 안내"
    학생 배포용 베이스라인·문제지는 강사가 직접 작성합니다. 여기서는 강사가 먼저 풀어보는 **참고 정답 스케치**와 예습 포인트를 담습니다.

## 진행 단계 (상세교안 기준)

1. `agent_core/webhook_server.py`를 만들어 강의1 예제를 확장한다(argparse `--port` 옵션)
2. 수신 이벤트 중 `login_failed`만 WARNING 레벨로 로깅한다
3. `agent_core/scheduler_job.py`에 Day2 `log_parser.py`를 import해 '매 1분마다' 로그 점검을 실행한다
4. `processed_ids.json`으로 멱등성을 구현해 중복 처리를 막는다
5. curl 3~5개를 담은 `test_webhook.sh`로 다양한 이벤트를 전송한다
6. 5분 이상 실행해 로그 누적을 확인하고, 운영 시 cron 시각을 `docs/`에 메모한다

**산출물:** `agent_core/webhook_server.py`, `scheduler_job.py`, `test_webhook.sh`

## 🧑‍🏫 강사 참고 정답 스케치 (예습용)

```python
# webhook_server.py — argparse 옵션 붙인 Webhook 서버
import argparse
import logging
from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.get_json()
    event = data.get('event')
    if event == 'login_failed':                     # ① 조건: 실패만 경고
        logging.warning(f'login_failed 수신: {data.get("user")}')
    else:
        logging.info(f'수신: {event}')
    return {'status': 'received'}, 200              # ② 200 응답

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)   # ③ CLI 옵션
    args = parser.parse_args()
    app.run(port=args.port)
```

```python
# scheduler_job.py — 멱등성 + 정기 실행
import json, os, time, schedule
from log_parser import parse_logs               # ④ Day2 모듈 재사용

PROCESSED_FILE = 'processed_ids.json'

def load_processed():                            # ⑤ 처리 ID 파일에서 로드
    if os.path.exists(PROCESSED_FILE):
        with open(PROCESSED_FILE, encoding='utf-8') as f:
            return set(json.load(f))
    return set()

def job():
    processed = load_processed()
    rows, _ = parse_logs('sample_logs.csv')
    new_count = 0
    for row in rows:
        rid = row.get('id') or f"{row['timestamp']}-{row['user']}"
        if rid not in processed:                 # ⑥ 멱등성: 안 한 것만
            # ... handle_event(row) ...
            processed.add(rid)
            new_count += 1
    with open(PROCESSED_FILE, 'w', encoding='utf-8') as f:
        json.dump(list(processed), f)            # ⑦ 처리 ID 저장(껐다 켜도 유지)
    print(f'신규 {new_count}건 처리')

schedule.every(1).minutes.do(job)                # ⑧ 매 1분
if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
```

```bash
# test_webhook.sh — curl로 이벤트 여러 개 전송
curl -X POST http://localhost:5000/webhook -H 'Content-Type: application/json' -d '{"event":"login_failed","user":"kim01"}'
curl -X POST http://localhost:5000/webhook -H 'Content-Type: application/json' -d '{"event":"login_success","user":"lee02"}'
```

!!! tip "🐍 이 실습에 오늘+지금까지 배운 게 다 있다"
    - **Flask + route + 상태코드**: Webhook 서버(①②)
    - **argparse**: --port 유연화(③)
    - **모듈 import**: Day2 log_parser 재사용(④)
    - **멱등성(set + JSON 저장)**: 중복 방지(⑤⑥⑦)
    - **schedule + while True**: 정기 실행(⑧)
    - **curl**: 서버 테스트(test_webhook.sh)

## 강사 예습 포인트

- **먼저** 같은 curl을 두 번 보내거나 job을 두 번 돌려, `processed_ids.json` 덕분에 **중복 처리가 안 되는지** 확인
- `--port 5001`로 실행해 argparse 옵션이 먹는지 확인
- 학생이 자주 막히는 지점:
  - Flask·schedule 미설치
  - 서버를 안 켜고 curl 보내 연결 거부(강의1 확인질문과 연결)
  - `processed_ids`를 파일로 저장 안 해서 재시작하면 초기화됨
  - `while True`에 `time.sleep` 없어 CPU 과사용
- 운영 메모 예시: "실무라면 scheduler_job을 cron `*/1 * * * *`로 등록"

## 평가 기준 (상세교안)

- Webhook 서버가 POST 요청을 정상 수신하고 200을 반환하는가
- 스케줄러가 반복 실행되며 이미 처리한 이벤트를 중복 처리하지 않는가
- CLI 인자로 설정이 유연하게 바뀌는가
