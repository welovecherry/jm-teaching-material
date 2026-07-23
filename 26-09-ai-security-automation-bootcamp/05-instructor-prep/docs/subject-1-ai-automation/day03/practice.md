# 실습 · 비정형 로그 정규화 스크립트 (총 120분)

> **실습 목표:** raw 텍스트 로그를 정규표현식으로 파싱해 구조화된 JSON으로 저장하는 파이프라인을 완성한다.

!!! note "강사 예습본 안내"
    학생 배포용 베이스라인·문제지는 강사가 직접 작성합니다. 여기서는 강사가 먼저 풀어보는 **참고 정답 스케치**와 예습 포인트를 담습니다.

## 진행 단계 (상세교안 기준)

1. `agent_core/raw_logs.txt`에 방화벽/웹서버 스타일 raw 로그 15~20줄을 준비한다
2. `agent_core/normalize_logs.py`를 만들고 정규표현식 패턴을 정의한다
3. `parse_raw_logs()`로 각 줄을 파싱해 딕셔너리 리스트를 만든다
4. 필수 필드(time, level, user, ip) 존재 여부를 체크한다
5. 결과를 `normalized_logs.json`으로 저장한다(`ensure_ascii=False`, `indent=2`)
6. 매칭 실패 줄은 `unmatched_logs.txt`로 기록해 데이터 누락을 방지한다

**산출물:** `agent_core/normalize_logs.py`, `normalized_logs.json`

## 🧑‍🏫 강사 참고 정답 스케치 (예습용)

```python
# normalize_logs.py — raw 로그를 정형 JSON으로
import re
import json

# ① named group 패턴 (시간·레벨·사용자·IP)
PATTERN = (r'(?P<time>[\d-]+ [\d:]+) (?P<level>\w+) '
           r'failed login for (?P<user>\w+) from (?P<ip>[\d.]+)')

REQUIRED = ['time', 'level', 'user', 'ip']

def parse_raw_logs(lines):
    results, unmatched = [], []
    for line in lines:
        m = re.search(PATTERN, line)
        if m:
            record = m.groupdict()                    # ② 딕셔너리로
            missing = [k for k in REQUIRED if not record.get(k)]  # ③ 필수 체크
            if missing:
                unmatched.append(line)                # 필드 누락도 실패 취급
            else:
                results.append(record)
        else:
            unmatched.append(line)                    # ④ 매칭 실패 별도 보관
    return results, unmatched

if __name__ == '__main__':
    with open('raw_logs.txt', encoding='utf-8') as f:
        lines = [l.strip() for l in f if l.strip()]   # 빈 줄 제거

    parsed, unmatched = parse_raw_logs(lines)

    # ⑤ 정형 결과 JSON 저장
    with open('normalized_logs.json', 'w', encoding='utf-8') as f:
        json.dump(parsed, f, indent=2, ensure_ascii=False)

    # ⑥ 매칭 실패 줄 별도 저장 (조용한 손실 방지)
    with open('unmatched_logs.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(unmatched))

    print(f'정형 {len(parsed)}건, 미매칭 {len(unmatched)}건')
```

!!! tip "🐍 이 스크립트에 오늘 배운 문법이 다 있다"
    - **named group 패턴 + groupdict**: raw → 딕셔너리(①②)
    - **필수 필드 체크(컴프리헨션 + `.get`)**: 누락 방어(③)
    - **매칭 실패 별도 보관**: 조용한 손실 방지(④)
    - **json.dump(ensure_ascii=False, indent=2)**: 정형 저장(⑤)
    - **건수 출력**: Day1의 전후 대조 습관
    - Day1~3이 한 파일로 합쳐집니다: 자료구조 → 파일IO → 정규식 → JSON.

## 강사 예습 포인트

- **먼저** raw 로그에 일부러 형식이 다른 줄(예: IP 없는 줄)을 섞어, `unmatched_logs.txt`에 잡히는지 확인
- 정규식 패턴을 [regex101.com](https://regex101.com) 같은 도구로 시각적으로 테스트하는 팁 (온라인)
- 학생이 자주 막히는 지점:
  - `r'...'` 안 써서 백슬래시 문제
  - `\.`(진짜 점) 대신 `.`(아무 문자) 사용
  - named group 문법 `(?P<name>...)`의 `?P` 빠뜨림
  - 매칭 실패 줄을 그냥 버림(별도 기록 누락)

## 평가 기준 (상세교안)

- 정규표현식이 최소 4개 필드(시간/레벨/사용자/IP)를 정확히 추출하는가
- 매칭 실패 로그가 조용히 사라지지 않고 별도로 기록되는가
- 결과 JSON 파일의 한글이 깨지지 않는가
