# 실습 · 이벤트 요약·보고서 자동 생성 파이프라인 (총 120분)

> **실습 목표:** 다건의 보안 이벤트를 배치 처리로 요약하고, 사람이 읽기 좋은 보고서를 자동 생성한다.

!!! note "강사 예습본 안내"
    학생 배포용 베이스라인·문제지는 강사가 직접 작성합니다. 여기서는 강사가 먼저 풀어보는 **참고 정답 스케치**와 예습 포인트를 담습니다.

## 진행 단계 (상세교안 기준)

1. `agent_core/event_summarizer.py`를 생성한다
2. Day3 `normalized_logs.json`(30~50건)을 `chunk_list()`로 20건씩 나눈다
3. 각 청크에 `build_prompt()`→`call_llm()`→`parse_llm_json()`으로 요약을 수집하고 `risk_order`로 정렬한다
4. `agent_core/report_generator.py`에서 템플릿+LLM으로 `daily_report_YYYYMMDD.md`를 생성한다
5. high 등급이 3건 이상이면 경고 문구가 자동 삽입되는지 테스트한다
6. 결과를 `event_summary_report.json`, `daily_report_*.md`로 저장한다

**산출물:** `agent_core/event_summarizer.py`, `report_generator.py`, `daily_report_*.md`

## 🧑‍🏫 강사 참고 정답 스케치 (예습용)

```python
# event_summarizer.py — 배치 요약 + 정렬
from llm_client import call_llm, parse_llm_json     # Day6 재사용

RISK_ORDER = {'high': 0, 'medium': 1, 'low': 2}

def chunk_list(items, size=20):                      # ① 제너레이터
    for i in range(0, len(items), size):
        yield items[i:i+size]

def summarize_events(events):
    summaries = []
    for batch in chunk_list(events, 20):             # ② 20건씩
        prompt = f'다음 로그를 건별로 요약. JSON 배열로만: {batch}'
        parsed = parse_llm_json(call_llm('당신은 보안 애널리스트.', prompt))
        summaries.extend(parsed or [])               # ③ 실패해도 계속
    # ④ 위험도순 정렬 (대소문자 방어)
    summaries.sort(key=lambda s: RISK_ORDER.get(str(s.get('risk_level','')).lower(), 3))
    return summaries
```

```python
# report_generator.py — 템플릿 + LLM + 조건부 경고
from llm_client import call_llm

TEMPLATE = '''# 보안 이벤트 일일 요약 보고서
작성일: {date}

## 요약
총 {total}건 중 위험도 high {high_count}건

## 상세 내역
{details}
'''

def generate_report(summaries, today):
    high_count = sum(1 for s in summaries if s.get('risk_level') == 'high')  # ⑤ 코드가 정확히 셈
    # ⑥ 상세 문단만 LLM 위임
    details = call_llm('보고서 문단 작성기.',
                       f'다음을 문장 문단으로(글머리표 없이): {summaries}')
    report = TEMPLATE.format(date=today, total=len(summaries),
                             high_count=high_count, details=details)
    if high_count >= 3:                              # ⑦ 조건부 경고
        report = '[긴급 확인 필요]\n' + report
    return report
```

!!! tip "🐍 이 실습에 오늘+지금까지 배운 게 다 모인다"
    - **제너레이터(yield) + 배치**: chunk_list(①②)
    - **Day6 LLM 재사용 + 방어적 파싱**: call_llm·parse_llm_json(③)
    - **정렬(sort key lambda) + 대소문자 방어**: risk_order(④)
    - **건수는 코드가 정확히**: high_count(⑤)
    - **부분 위임**: 상세 문단만 LLM(⑥)
    - **조건부 경고**: if high_count(⑦)
    - 이 `event_summarizer.py`가 4과목 Day5에서 재사용한 바로 그 모듈입니다.

## 강사 예습 포인트

- **먼저** high가 3건 이상인 데이터와 미만인 데이터로 각각 실행해, 경고 문구 삽입/미삽입을 확인
- LLM이 `'High'`(대문자)로 답해도 `.lower()` 덕분에 정렬이 맞는지 확인(강의1 확인질문 연결)
- 학생이 자주 막히는 지점:
  - `high_count`를 LLM에게 세게 함(코드가 세야 정확)
  - details에 리스트를 그대로 넣어 보고서가 지저분함
  - 배치 없이 전부 한 번에 넣어 길이 초과
  - `parse_llm_json`이 None일 때 `.extend(None)`로 에러 → `or []`로 방어

## 평가 기준 (상세교안)

- 청크 단위 배치 처리와 정렬이 정상 동작하는가
- 보고서 형식이 매번 일관되게 유지되는가
- high 등급 이벤트 수에 따라 경고 문구가 조건부로 삽입되는가
