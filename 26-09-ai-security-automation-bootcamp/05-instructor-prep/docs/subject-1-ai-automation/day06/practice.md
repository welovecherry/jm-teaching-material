# 실습 · LLM 연동 텍스트 요약 및 도구 라우터 구현 (총 120분)

> **실습 목표:** LLM API를 연동해 로그 요약 기능을 만들고, 도구 호출 라우터의 뼈대를 완성한다.

!!! note "강사 예습본 안내"
    학생 배포용 베이스라인·문제지는 강사가 직접 작성합니다. 여기서는 강사가 먼저 풀어보는 **참고 정답 스케치**와 예습 포인트를 담습니다.

## 진행 단계 (상세교안 기준)

1. `agent_core/llm_client.py`를 만들어 LLM API 호출 함수(`call_llm`)를 작성한다
2. Day3 `normalized_logs.json`을 입력으로 받아 로그 요약 프롬프트를 설계한다
3. `parse_llm_json()`으로 응답을 안전하게 파싱한다
4. `agent_core/tool_router.py`에 `tool_registry`·`route_tool_call()` 뼈대를 작성한다(도구 1~2개)
5. LLM에게 'count_failed_logins를 호출해야 하는지' 판단시키는 프롬프트를 설계해 라우터로 실행한다
6. 결과(요약문 + 실행된 도구 이름)를 `agent_result.json`으로 저장한다

**산출물:** `agent_core/llm_client.py`, `agent_core/tool_router.py`, `agent_result.json`

## 🧑‍🏫 강사 참고 정답 스케치 (예습용)

```python
# llm_client.py — LLM 호출 + 방어적 파싱
import os, json, logging, requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('LLM_API_KEY', '')
LLM_URL = 'https://api.example.com/v1/chat/completions'

def call_llm(system, user, temperature=0.2):            # ① Day4 requests 재사용
    headers = {'Authorization': f'Bearer {API_KEY}'}
    payload = {
        'model': 'gpt-4o-mini',
        'messages': [{'role': 'system', 'content': system},
                     {'role': 'user', 'content': user}],
        'temperature': temperature,
    }
    r = requests.post(LLM_URL, json=payload, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()['choices'][0]['message']['content']

def parse_llm_json(text):                                # ② 방어적 파싱
    try:
        start, end = text.index('{'), text.rindex('}') + 1
        return json.loads(text[start:end])
    except (ValueError, json.JSONDecodeError) as e:
        logging.warning(f'파싱 실패: {e}')
        return None
```

```python
# tool_router.py — 도구 라우터 (agent_core 핵심 엔진)
def count_failed_logins(threshold=2):
    return {'result': f'{threshold}회 이상 실패 집계(예시)'}

def send_alert(message):
    return {'sent': message}

tool_registry = {                                        # ③ 이름 → 함수
    'count_failed_logins': count_failed_logins,
    'send_alert': send_alert,
}

def route_tool_call(decision):                           # ④ 라우팅
    name, args = decision['tool'], decision.get('args', {})
    func = tool_registry.get(name)
    if func is None:                                     # ⑤ 없는 도구 → 에러
        raise ValueError(f'알 수 없는 도구: {name}')
    return func(**args)                                  # ⑥ 실행
```

!!! tip "🐍 이 실습에 지금까지 배운 게 다 모인다"
    - **환경변수(.env)**: 키 관리 (Day4)
    - **requests.post + timeout + raise_for_status**: LLM 호출 (Day4)
    - **방어적 JSON 파싱**: 안전 처리 (Day2·3·6)
    - **tool_registry + route_tool_call + `**args`**: 도구 라우팅 (오늘)
    - **없는 도구 → ValueError**: 조용한 실패 방지 (Day2)
    - 이 `tool_router.py`가 3·4과목에서 재등장하는 agent_core의 심장입니다.

## 강사 예습 포인트

- **먼저** LLM에게 정상 JSON을 유도하는 프롬프트(4원칙)를 짜보고, 일부러 군더더기를 붙인 응답도 `parse_llm_json`이 견디는지 확인
- `route_tool_call`에 없는 도구 이름(`{'tool': 'delete_all'}`)을 넣어 ValueError가 나는지 확인
- 실제 LLM 키가 없으면, `call_llm`을 가짜 응답 반환으로 대체해 라우터 흐름만 먼저 테스트
- 학생이 자주 막히는 지점:
  - LLM 응답 구조(`['choices'][0]['message']['content']`) 가정 오류 → `print`로 먼저 확인
  - 프롬프트에 출력 형식(JSON) 지정 누락 → 파싱 실패
  - `**args`를 안 써서 인자 전달 실패
  - 승인 게이트 없이 위험 도구를 자동 실행(개념만이라도 주석으로 표시)

## 평가 기준 (상세교안)

- LLM 응답 파싱 실패 시에도 프로그램이 안전하게 처리되는가
- tool_registry 기반 라우팅이 정상 동작하는가
- 결과가 이해하기 쉬운 형태로 저장되는가
