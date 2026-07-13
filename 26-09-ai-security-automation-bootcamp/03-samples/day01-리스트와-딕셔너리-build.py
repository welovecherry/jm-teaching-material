# -*- coding: utf-8 -*-
# Day 1 · 리스트와 딕셔너리 교안 v6 — 개념→예제→'즉시' 손코딩(촘촘히), 손코딩 문제 다수
import json, os
cells=[]
def md(t): cells.append({"cell_type":"markdown","metadata":{},"source":t})
def code(t): cells.append({"cell_type":"code","metadata":{},"execution_count":None,"outputs":[],"source":t})

# ═══ 표지 ═══
md("""# Day 1 — 리스트와 딕셔너리

## 여러 값을 한 번에 다루기 · 80–105분

> **만든 날짜:** 2026-07-13 · **버전:** v6

앞에서 변수 하나에 값 하나를 담았습니다. 이제 **여러 값**을 한 번에 담는 두 그릇,
**리스트**와 **딕셔너리**를 배웁니다. 예제를 본 직후 바로 **직접 쳐보는 문제**가 이어집니다.
많이 쳐볼수록 빨리 익숙해집니다.""")

# ═══ 학습목표 ═══
md("""## 학습목표

이 시간이 끝나면 다음을 할 수 있습니다.

1. 리스트로 여러 값을 담고, 번호(인덱스)로 꺼내기
2. `len()`으로 개수 세기, `append()`로 값 추가하기
3. 딕셔너리로 이름표-값을 담고, 이름으로 꺼내기
4. `.get()`으로 없는 키도 안전하게 다루기""")

# ═══ 사용법 ═══
md("""## 이 노트북 쓰는 법

- 회색 코드 칸을 클릭하고 **`Shift + Enter`** 로 한 칸씩 실행합니다.
- **예제(💻)를 실행해 결과를 확인한 뒤, 바로 아래 문제(✍️)를 직접 풀어 보세요.**

| 표시 | 뜻 |
|------|-----|
| 📖 | 개념(읽기) |
| 💻 | 예제(실행해 결과 확인) |
| ✍️ | 문제(직접 작성) |
| ✅ | 결과("이렇게 나오면 성공") |
| ❓ | 핵심 질문(답은 본문에) |

> 뒤쪽 **`[심화·자습]`** 은 시간이 남거나 자습·리추얼 때 풀면 됩니다.""")

# ══════════════════════════════════════════════════
# 1. 리스트
# ══════════════════════════════════════════════════
md("""---
## 1. 리스트 (list) — 여러 값을 '순서대로'

- 사용자가 여러 명, 로그가 여러 줄일 때 값마다 변수를 만들면 번거롭습니다.
- **리스트**는 여러 값을 **순서대로** 한 그릇에 담습니다. 대괄호 `[ ]` 안에 쉼표로 나열합니다.

> **왜 리스트를 쓸까?** "값이 여러 개"일 때 하나로 묶어 관리하기 위해서입니다.""")

code('''# 💻 예제 — 리스트 만들고, 전체 출력하기
users = ["kim01", "lee02", "park03"]   # 값 3개를 순서대로 담음
print(users)''')
md("""**✅ 성공 출력**
```
['kim01', 'lee02', 'park03']
```""")

code('''# ✍️ 문제 (빈칸 채우기) — 서버 이름 2개를 담은 리스트를 만드세요.  기대 출력: ['web01', 'web02']
servers = [____, ____]      # "web01", "web02" 를 넣으세요
print(servers)''')

md("""### 📖 번호(인덱스)로 꺼내기

- 리스트의 값은 **번호(인덱스)** 로 꺼냅니다: `리스트[번호]`
- 번호는 **0부터** 셉니다. 첫 번째 = `[0]`, 두 번째 = `[1]`.""")

code('''# 💻 예제 — 번호로 값 꺼내기
users = ["kim01", "lee02", "park03"]
print(users[0])   # 첫 번째
print(users[1])   # 두 번째''')
md("""**✅ 성공 출력**
```
kim01
lee02
```""")

code('''# ✍️ 문제 (출력 예측) — 무엇이 나올지 먼저 예측한 뒤 실행하세요.
users = ["kim01", "lee02", "park03"]
print(users[2])   # 예측: ?''')

md("""### 📖 개수 세기(len)와 값 추가(append)

- `len(리스트)` → 값의 **개수**
- `리스트.append(값)` → 맨 **뒤에 값 하나 추가** (로그가 하나씩 들어올 때 자주 씀)""")

code('''# 💻 예제 — 개수와 추가
users = ["kim01", "lee02"]
print(len(users))       # 2
users.append("park03")  # 뒤에 추가
print(users)            # 3개가 됨
print(len(users))       # 3''')
md("""**✅ 성공 출력**
```
2
['kim01', 'lee02', 'park03']
3
```""")

code('''# ✍️ 문제 (빈칸 채우기) — logs 에 "e3" 을 추가하고 개수를 출력하세요.  기대 출력: 3
logs = ["e1", "e2"]
logs.____("e3")     # 추가 메서드 이름을 넣으세요
print(len(logs))''')

code('''# ✍️ 문제 (백지 코딩테스트) — 아래를 직접 작성하세요.
#   1) ports 라는 리스트에 정수 22, 80, 443 을 담기
#   2) 첫 번째 값과 개수를 출력하기
#   기대 출력:
#   22
#   3
# (여기에 코드를 작성하세요)
pass  # 완성한 뒤 실행하세요''')

# ══════════════════════════════════════════════════
# 2. 딕셔너리
# ══════════════════════════════════════════════════
md("""---
## 2. 딕셔너리 (dict) — '이름표'로 꺼내기

- 리스트는 "몇 번째"로 꺼냅니다. 그런데 로그 한 줄은 *user·event·ip* 처럼 **이름 있는 정보**입니다.
- **딕셔너리**는 **이름표(키)-값** 쌍으로 담고, **이름으로** 꺼냅니다. 중괄호 `{ }` 를 씁니다.

> **왜 딕셔너리를 쓸까?** `log["user"]` 가 `log[0]` 보다 "무엇을 꺼내는지" 훨씬 분명하기 때문입니다.""")

code('''# 💻 예제 — 딕셔너리 만들고, 이름으로 꺼내기
log = {"user": "kim01", "event": "login_failed"}
print(log["user"])    # "user" 라는 이름표의 값
print(log["event"])   # "event" 라는 이름표의 값''')
md("""**✅ 성공 출력**
```
kim01
login_failed
```""")

code('''# ✍️ 문제 (빈칸 채우기) — log 에서 event 값을 꺼내 출력하세요.  기대 출력: logout
log = {"user": "lee02", "event": "logout"}
print(log[____])      # "event" 를 넣으세요''')

md("""### 📖 키가 여러 개일 때

- 딕셔너리에는 이름표-값 쌍을 여러 개 담을 수 있습니다.
- 보안 로그 한 줄을 통째로 딕셔너리로 표현하면 다루기 편합니다.""")

code('''# 💻 예제 — 로그 한 줄을 통째로
log = {
    "customer": "hanbit",
    "user": "kim01",
    "event": "login_failed",
    "ip": "203.0.113.5",
}
print(log["customer"])
print(log["ip"])''')
md("""**✅ 성공 출력**
```
hanbit
203.0.113.5
```""")

code('''# ✍️ 문제 (출력 예측) — 무엇이 나올지 예측한 뒤 실행하세요.
log = {"customer": "hanbit", "user": "kim01", "event": "login_failed"}
print(log["user"])     # 예측: ?
print(log["event"])    # 예측: ?''')

md("""### 📖 없는 키도 안전하게 — `.get()`

- 대괄호 `log["없는키"]` 로 **없는 이름표**를 꺼내면 **에러가 나서 프로그램이 멈춥니다.**
- `log.get("없는키")` 는 없으면 조용히 `None`("값 없음")을 돌려주어 멈추지 않습니다.""")

code('''# 💻 예제 — 대괄호 vs .get()
log = {"user": "kim01"}
print(log.get("user"))     # 있으면 값 → kim01
print(log.get("country"))  # 없으면 None (에러 없음)''')
md("""**✅ 성공 출력**
```
kim01
None
```""")

code('''# ✍️ 문제 (버그 수정) — 아래는 없는 키 "ip" 를 대괄호로 꺼내 에러가 납니다.
#   .get() 을 쓰도록 한 줄만 고쳐 None 이 나오게 하세요.  기대 출력: None
log = {"user": "kim01"}
print(log["ip"])   # ← 여기가 문제''')

code('''# ✍️ 문제 (백지 코딩테스트) — 아래를 직접 작성하세요.
#   1) server 라는 딕셔너리에 name="web01", port=8080 을 담기
#   2) name 값과 port 값을 각각 출력하기
#   기대 출력:
#   web01
#   8080
# (여기에 코드를 작성하세요)
pass  # 완성한 뒤 실행하세요''')

md("""### ❓ 핵심 질문

`log["event"]` 대신 `log.get("event")` 를 쓰면 **어떤 상황에서 더 안전**할까요?
> 답은 위 `.get()` 설명 안에 있습니다. "없는 키를 꺼낼 때"를 떠올려 보세요.""")

# ══════════════════════════════════════════════════
# [심화·자습]
# ══════════════════════════════════════════════════
md("""---
## [심화·자습] — 더 배우기
> 시간이 남거나 자습·리추얼 때 풀어 보세요.

### 📖 딕셔너리 훑어보기 — keys / values / items
- `keys()` 이름표만 / `values()` 값만 / `items()` 이름표+값 쌍""")

code('''# 💻 (심화) keys / values / items
log = {"user": "kim01", "event": "login_failed"}
print(list(log.keys()))     # 이름표들
print(list(log.values()))   # 값들''')
md("""**✅ 성공 출력**
```
['user', 'event']
['kim01', 'login_failed']
```""")

code('''# ✍️ (심화·출력 예측) items() 로 반복하면 무엇이 나올지 예측한 뒤 실행하세요.
log = {"user": "kim01", "event": "login_failed"}
for key, value in log.items():
    print(key, value)     # 예측: ?''')

md("""### 📖 리스트 + 딕셔너리 조합 (실무에서 가장 많이 씀)
- 로그 **여러 줄** = "딕셔너리(로그 한 줄)를 리스트에 담기".
- 이 구조가 앞으로 로그를 훑고 거르는 실습의 핵심 재료가 됩니다.""")

code('''# 💻 (심화) 딕셔너리들의 리스트
logs = [
    {"user": "kim01", "event": "login_failed"},
    {"user": "lee02", "event": "login_success"},
]
print(logs[0]["user"])    # 첫 번째 로그의 user
print(logs[1]["event"])   # 두 번째 로그의 event''')
md("""**✅ 성공 출력**
```
kim01
login_success
```""")

code('''# ✍️ (심화·백지) 위 logs 에서 '첫 번째 로그의 event' 를 꺼내 출력하세요.
#   기대 출력:  login_failed
logs = [
    {"user": "kim01", "event": "login_failed"},
    {"user": "lee02", "event": "login_success"},
]
# (여기에 코드를 작성하세요)
pass  # 완성한 뒤 실행하세요''')

md("""> **집합(set)·튜플(tuple)** 은 뒤 차시에서 배웁니다(집합은 오늘 강의2의 '중복 제거·집계'에서).

### ❓ 면접 질문
**"리스트와 딕셔너리의 차이는 무엇이며, 보안 로그 한 줄엔 어느 것이 더 적합한가요?"**
> 힌트: "번호로 꺼낸다 vs 이름으로 꺼낸다". 위 개념 설명에서 답을 찾아보세요.""")

# ═══ 마무리 ═══
md("""---
## 오늘 요약

1. **리스트 `[ ]`** — 여러 값을 순서대로. 번호(0부터)로 꺼내고, `len()` 개수, `append()` 추가.
2. **딕셔너리 `{ }`** — 이름표(키)-값. 이름으로 꺼냄. 보안 로그 한 줄에 적합.
3. **`.get()`** — 없는 키도 에러 없이 `None` 을 돌려줘 안전.
4. (심화) **딕셔너리들의 리스트** — 로그 여러 줄을 다루는 실무 핵심 구조.""")

md("""## 종합 퀴즈 (객관식)

**Q1.** `users = ["kim01", "lee02", "park03"]` 에서 두 번째 값을 꺼내려면? ① `users[1]` ② `users[2]` ③ `users["1"]`
<details><summary>정답 보기</summary>① `users[1]` — 0부터 세므로 두 번째는 1번</details>

**Q2.** 리스트 맨 뒤에 값을 추가하는 메서드는? ① `add()` ② `append()` ③ `push()`
<details><summary>정답 보기</summary>② `append()`</details>

**Q3.** 딕셔너리에서 없을 수도 있는 키를 **에러 없이** 꺼내려면? ① `log["key"]` ② `log.get("key")` ③ `log(key)`
<details><summary>정답 보기</summary>② `log.get("key")` — 없으면 None 을 돌려줌</details>""")

md("""## 다음 시간 예고

이어서 **연산자와 형변환**을 배우고, 3교시(강의2)에서 **조건문·반복문**으로
오늘 만든 로그(딕셔너리들의 리스트)를 훑어 "실패한 로그만" 골라내는 실제 필터링을 합니다.""")

# ═══ 저장 ═══
nb={"cells":cells,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":"3.11"}},"nbformat":4,"nbformat_minor":5}
out="/Users/hong/jm-teaching-material/26-09-ai-security-automation-bootcamp/03-samples/day01-리스트와-딕셔너리-v6.ipynb"
os.makedirs(os.path.dirname(out),exist_ok=True)
with open(out,"w",encoding="utf-8") as f: json.dump(nb,f,ensure_ascii=False,indent=1)
print("cells:",len(cells)); print("saved:",out)
