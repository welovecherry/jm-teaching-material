# 실습 · 공개 API 연동 데이터 수집기 (총 120분)

> **실습 목표:** 실제 공개 API를 호출해 데이터를 받아오고, 가공한 뒤 JSON으로 저장하는 미니 파이프라인을 완성한다.

!!! note "강사 예습본 안내"
    학생 배포용 베이스라인·문제지는 강사가 직접 작성합니다. 여기서는 강사가 먼저 풀어보는 **참고 정답 스케치**와 예습 포인트를 담습니다.

## 진행 단계 (상세교안 기준)

1. `agent_core/api_client.py`를 생성한다
2. 무료 공개 API의 키를 발급받아 `.env`에 저장한다
3. `call_with_retry()`를 활용한 `fetch_data()` 함수를 작성한다
4. 받아온 JSON에서 필요한 필드만 추출해 리스트로 가공한다
5. 가공 결과를 `api_result.json`으로 저장한다
6. 키 하드코딩 여부·`.env`의 `.gitignore` 포함 여부를 서로 코드 리뷰한다

**산출물:** `agent_core/api_client.py`, `.env.example`, `api_result.json`

## 🧑‍🏫 강사 참고 정답 스케치 (예습용)

```python
# api_client.py — 공개 API 수집기
import os
import time
import json
import logging
import requests
from dotenv import load_dotenv

load_dotenv()                                        # ① .env 로드
API_TOKEN = os.environ.get('API_TOKEN', '')          # ② 환경변수에서 키
BASE_URL = 'https://api.example.com/v1'

def call_with_retry(url, params=None, max_retry=3):   # ③ 재시도 래퍼
    headers = {'Authorization': f'Bearer {API_TOKEN}'}
    for attempt in range(max_retry):
        try:
            r = requests.get(url, params=params, headers=headers, timeout=5)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            logging.warning(f'실패({attempt+1}/{max_retry}): {e}')
            time.sleep(2)
    raise RuntimeError('API 호출 최종 실패')

def fetch_data():
    raw = call_with_retry(f'{BASE_URL}/events', params={'status': 'open'})
    # ④ 필요한 필드만 추출·가공
    return [{'id': e['id'], 'title': e.get('title', '')} for e in raw['results']]

if __name__ == '__main__':
    data = fetch_data()
    with open('api_result.json', 'w', encoding='utf-8') as f:   # ⑤ JSON 저장
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f'{len(data)}건 수집 완료')
```

```text
# 📄 .env  (절대 깃에 올리지 않음)
API_TOKEN=sk-실제키

# 📄 .env.example  (이건 깃에 올림 — 값은 비움)
API_TOKEN=

# 📄 .gitignore
.env
```

!!! tip "🐍 이 스크립트에 오늘+지금까지 배운 게 다 있다"
    - **환경변수(.env + os.environ)**: 키 분리(①②)
    - **재시도(range·timeout·raise_for_status)**: 견고한 호출(③)
    - **params·headers**: 안전한 요청 구성
    - **컴프리헨션 + `.get`**: 필드 추출·가공(④, Day1·3 복습)
    - **json.dump(ensure_ascii=False)**: 저장(⑤, Day3)
    - **`if __name__`**: 테스트 실행(Day2)

## 강사 예습 포인트

- **먼저** `.env` 없이 실행 → 키 없음 상황 확인, 그다음 `.env` 채워 성공까지
- 일부러 timeout을 아주 짧게(예: 0.001) 줘서 재시도·최종 실패가 도는지 확인
- 공개 API 추천: 인증 없는 것(예: JSONPlaceholder)으로 먼저 흐름 익히고, 인증 있는 것으로 확장
- 학생이 자주 막히는 지점:
  - `requests` 미설치(`pip install requests`, `python-dotenv`)
  - 키를 코드에 하드코딩(가장 중요한 리뷰 포인트)
  - `.env`를 `.gitignore`에 안 넣음
  - `raise_for_status` 없이 4xx/5xx를 성공으로 오인
  - `raw['results']` 구조 가정 오류 → 먼저 `print(raw)`로 구조 확인

## 평가 기준 (상세교안)

- API 키가 코드에 노출되지 않고 환경변수로 분리되었는가
- 요청 실패 시 프로그램이 죽지 않고 재시도 후 명확히 에러를 알리는가
- 결과가 구조화된 JSON으로 저장되는가
