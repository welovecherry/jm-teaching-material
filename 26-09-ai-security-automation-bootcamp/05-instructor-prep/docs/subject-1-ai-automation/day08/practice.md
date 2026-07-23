# 실습 · 미니 프로젝트 최종 완성 및 시연 (총 120분)

> **실습 목표:** 리뷰에서 발견한 문제를 반영해 파이프라인을 완성하고, 팀/개인별로 실제 동작을 시연·발표한다.

!!! note "강사 예습본 안내"
    학생 배포용 베이스라인·문제지는 강사가 직접 작성합니다. 여기서는 강사가 먼저 풀어보는 **참고 정답 스케치**와 예습 포인트를 담습니다.

## 진행 단계 (상세교안 기준)

1. 코드 리뷰 지적 항목(config 분리·예외처리·로깅)을 `pipeline.py`에 반영·수정한다
2. 정상 케이스(입력→요약→알림→리포트)를 처음부터 끝까지 한 번에 실행해 확인한다
3. 예외 케이스(잘못된 입력 파일 등)도 실행해 안전하게 처리되는지 재확인한다
4. 5분 내외 발표 자료(아키텍처 1장, 데모 화면)를 준비한다
5. 조별로 파이프라인 실행을 시연하고 피드백을 받는다
6. 피드백·개선 아이디어를 `docs/day08_retrospective.md`에 정리한다(캡스톤 시작 시 참고)

**산출물:** `agent_core/` 전체 완성본, `docs/day08_retrospective.md`

## 🧑‍🏫 강사 참고 정답 스케치 (예습용)

```python
# pipeline.py — 1~7일차 통합 오케스트레이션
import logging
import yaml
from log_parser import parse_logs             # Day2
from normalize_logs import normalize          # Day3
from event_summarizer import summarize_events # Day7
from report_generator import generate_report  # Day7
from notifier import notify                    # Day8(신규)

def load_config(path):                         # ① config 분리
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)

def has_high_risk(summaries, threshold=3):
    return sum(1 for s in summaries if s.get('risk_level') == 'high') >= threshold

def run_pipeline(config_path):
    config = load_config(config_path)
    # ② 각 단계 try/except — 부분 실패 견딤
    try:
        logs = parse_logs(config['log_input_path'])
    except Exception as e:
        logging.error(f'입력 실패: {e}')
        return None

    try:
        summaries = summarize_events(normalize(logs))
    except Exception as e:
        logging.error(f'요약 실패, 원본만 보고: {e}')
        summaries = [{'summary': f'원본 {len(logs)}건', 'risk_level': 'unknown'}]

    if has_high_risk(summaries):               # ③ 고위험이면 알림
        notify(f"[{config['customer_name']}] 고위험 이벤트 발견")

    return generate_report(summaries, today='2026-07-07')  # ④ 리포트

if __name__ == '__main__':
    print(run_pipeline('config/example_customer.yaml'))
```

```yaml
# config/example_customer.yaml
customer_name: '가상 A사'
threshold: 5
log_input_path: 'sample_logs.csv'
alert_channel: 'email'
```

!!! tip "🐍 이 파일에 8일 전체가 응축된다"
    - **config 분리(yaml)**: 고객사만 바꿔 재사용(①, Day8)
    - **모듈 import**: Day2·3·7 재사용
    - **단계별 try/except**: 부분 실패 견딤(②, Day2·8)
    - **logging**: 실패 기록(Day2)
    - **조건부 알림**: 고위험만(③, Day5·7)
    - `run_pipeline`이 3·4과목 `weekly_report`·`pipeline`과 똑같은 오케스트레이션입니다.

## 강사 예습 포인트

- **먼저** 정상 파일 → 잘못된 경로 → 요약 단계 강제 실패(네트워크 끊기) 순으로 실행해, **부분 실패에도 죽지 않고** 로그·리포트가 나오는지 확인
- config를 B사용으로 복제해 값만 바꿔 실행 → 코드 수정 없이 재사용되는지 확인
- 리뷰 4항목으로 자기 코드를 점검하고, 발견된 하드코딩·예외 누락을 수정
- 학생이 자주 막히는 지점:
  - config 키 오타 → KeyError(traceback 아래줄 읽기 연습)
  - 요약 실패 시 전체 중단(부분 실패 처리 누락)
  - 알림 실패 fallback 누락
  - 모듈 import 경로 문제
- 회고 문서에 "캡스톤에서 이 agent_core에 3·4과목 도구를 어떻게 등록할지" 한 줄 메모 남기기

## 평가 기준 (상세교안)

- 전체 파이프라인이 오류 없이 시연되는가
- 코드 리뷰 지적사항이 실제로 반영되었는가
- 발표에서 아키텍처와 캡스톤 연결점을 명확히 설명하는가
