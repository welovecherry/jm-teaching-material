# 【샘플】 1.5과목 · 파이썬 브릿지 — **1층. 딕셔너리 1개**

!!! warning "이건 '파이썬 문법 브릿지' 형식 샘플입니다"
    1과목은 정해진 커리큘럼이라 손대기 어렵고, 파이썬 시간이 짧습니다.
    그래서 **3·4·5과목 코드를 읽기 위한 최소 문법**만 따로 모아 8층 계단으로 쌓는 별도 트랙을 만듭니다.
    이 문서는 그중 **1층(딕셔너리 1개)** 하나를 끝까지 완성한 시험판입니다.

    새로 들어간 장치: 🔹 **백준식 문제** · ▶ **접기 정답** · 🧱 **3과목 연결고리** · 🧪 **정리 퀴즈**

> **이 층 한 문장:** 3·4·5과목의 모든 데이터는 **딕셔너리**로 되어 있습니다. 딕셔너리 **한 개**를 완벽하게 다루는 것이 전부의 시작입니다.

## 8층 계단 중 지금 위치

| 층 | 내용 | 상태 |
|----|------|------|
| **1층** | **딕셔너리 1개 + `.get()`** | 👈 **지금 여기** |
| 2층 | 리스트 1개 + `.append()` | 예정 |
| 3층 | 딕셔너리가 들어있는 리스트 ⭐ | 예정 |
| 4층 | for + if + append | 예정 |
| 5층 | def + return + 기본값 인자 | 예정 |
| 6층 | 딕셔너리 두 개 겹치기 | 예정 |
| 7층 | 날짜(datetime) | 예정 |
| 8층 | json 저장 + f-string | 예정 |

## 이 층에 나오는 용어

| 용어 (한글발음) | 한 줄 뜻 (아주 쉽게) | 비유 |
|----------------|---------------------|------|
| **딕셔너리(dictionary, 딕셔너리)** | 이름표를 붙여 값을 넣어두는 상자 | 사물함 |
| **키(key, 키)** | 이름표 | 사물함 번호 |
| **값(value, 밸류)** | 이름표에 붙어 있는 내용물 | 사물함 안 물건 |
| **키-값 쌍(key-value pair)** | 이름표 + 내용물 한 세트 | 사물함 1칸 |
| **`KeyError`(키에러)** | 없는 이름표를 찾을 때 나는 에러 | 없는 사물함을 열려다 실패 |
| **`.get()`(겟)** | 없어도 에러 안 내고 꺼내는 방법 | 비어 있으면 그냥 빈손으로 |
| **`in`(인)** | 그 이름표가 있는지 확인 | 사물함이 있나 확인 |
| **`.items()`(아이템즈)** | 이름표와 내용물을 한 쌍씩 꺼내기 | 사물함을 하나씩 열어보기 |

---

## 1-A · 왜 딕셔너리가 필요한가

직원 한 명의 정보를 저장한다고 해봅시다. 변수만 쓰면 이렇게 됩니다.

```python
user_name = "kim01"
user_dept = "finance"
user_level = "read"
```

한 명은 괜찮습니다. 그런데 **사람이 100명**이 되면? `user_name_1`, `user_name_2`... 감당이 안 됩니다.

그래서 **한 사람의 정보를 한 상자에** 담습니다. 이게 딕셔너리입니다.

```python
user = {"name": "kim01", "dept": "finance", "level": "read"}
```

읽는 법: **중괄호 `{ }`** 안에, **`"이름표": 값`**을 **쉼표**로 나열합니다.

!!! tip "🧱 3과목 연결고리"
    3과목 교안에 나오는 접근 요청 데이터가 정확히 이 모양입니다.

    ```python
    request = {'id': 'req-1001', 'user': 'kim01', 'system': '재무시스템',
               'level': '수정', 'status': 'requested'}
    ```

    **지금 배우는 이 상자 하나**가 3과목 Day2 코드의 주인공입니다.

---

## 1-B · 값 꺼내기 — 대괄호 `[ ]`

이름표를 대괄호에 넣으면 내용물이 나옵니다.

```python
user = {"name": "kim01", "dept": "finance", "level": "read"}

print(user["name"])    # kim01
print(user["dept"])    # finance
```

!!! danger "가장 흔한 실수"
    ```python
    print(user[name])     # ❌ 따옴표 빠짐 → NameError
    print(user["Name"])   # ❌ 대소문자 다름 → KeyError
    ```
    이름표는 **글자 그대로** 똑같아야 합니다. `"name"`과 `"Name"`은 다른 이름표입니다.

### 🔹 문제 1-1. 부서 꺼내기

**설명**
접근 요청 하나가 딕셔너리로 주어집니다. 요청한 사람이 속한 시스템 이름을 화면에 출력하세요.

**주어지는 것**
```python
request = {"id": "req-1001", "user": "kim01", "system": "finance_system", "status": "requested"}
```

**만들 것**
`system` 값을 출력하는 한 줄

**나와야 하는 결과**
```
finance_system
```

??? success "▶ 정답 보기"
    ```python
    print(request["system"])
    ```

    **왜 이렇게 되나:** `request["system"]`이 `"finance_system"`이라는 값을 꺼내오고, `print()`가 그걸 화면에 찍습니다.

---

## 1-C · 값 바꾸기 · 새로 넣기

대괄호는 **꺼낼 때**도 쓰고 **넣을 때**도 씁니다. 왼쪽에 놓으면 넣기입니다.

```python
request = {"id": "req-1001", "user": "kim01", "status": "requested"}

request["status"] = "reviewing"      # 있는 이름표 → 값이 바뀜
request["approver"] = "fin_manager"  # 없는 이름표 → 새로 생김

print(request)
# {'id': 'req-1001', 'user': 'kim01', 'status': 'reviewing', 'approver': 'fin_manager'}
```

==있으면 덮어쓰기, 없으면 새로 만들기.== 규칙은 이 하나뿐입니다.

### 🔹 문제 1-2. 요청 승인 처리하기

**설명**
검토 중이던 요청이 승인되었습니다. 상태를 바꾸고, 승인한 사람을 새로 기록하세요.

**주어지는 것**
```python
request = {"id": "req-1002", "user": "lee02", "status": "reviewing"}
```

**만들 것**
1. `status`를 `"approved"`로 바꾸기
2. `approver` 이름표에 `"hr_manager"`를 새로 넣기

**나와야 하는 결과**
```
{'id': 'req-1002', 'user': 'lee02', 'status': 'approved', 'approver': 'hr_manager'}
```

??? success "▶ 정답 보기"
    ```python
    request["status"] = "approved"
    request["approver"] = "hr_manager"
    print(request)
    ```

    **왜 이렇게 되나:** `status`는 이미 있던 이름표라 값만 바뀌고, `approver`는 없던 이름표라 **맨 뒤에 새로 붙습니다.** 그래서 출력 순서가 저렇게 나옵니다.

!!! tip "🧱 3과목 연결고리"
    Day2 `approve_request()` 함수의 핵심이 딱 이 두 줄입니다.

    ```python
    request['status'] = 'approved'
    request['approved_at'] = datetime.now().isoformat()
    ```

---

## 1-D · 없는 이름표를 찾으면? — `KeyError`

여기가 **1층에서 제일 중요한 부분**입니다.

```python
user = {"name": "kim01", "dept": "finance"}

print(user["phone"])
```

결과:

```
KeyError: 'phone'
```

프로그램이 **거기서 멈춥니다.** 뒤에 코드가 100줄 있어도 한 줄도 실행되지 않습니다.

!!! danger "왜 이게 보안 자동화에서 치명적인가"
    로그 데이터는 **필드가 자주 빠져 있습니다.** 로그 10,000건을 훑는 코드가 9,999번째에서 `KeyError`로 멈추면, 앞의 결과까지 전부 날아갑니다.

    실습 시간에 나오는 에러 1위가 이겁니다.

### 🔹 문제 1-3. 어떤 에러가 날까

**설명**
아래 코드를 실행하면 어떻게 될지 예상해보세요. (직접 쳐서 확인해보시는 걸 권합니다)

**주어지는 것**
```python
log = {"user": "kim01", "result": "fail"}
print(log["ip"])
print("검사 완료")
```

**만들 것**
① 화면에 무엇이 나올지 ② `"검사 완료"`는 출력될지 답하기

**나와야 하는 결과**
```
KeyError: 'ip'
```

??? success "▶ 정답 보기"
    ① `KeyError: 'ip'` ② **출력되지 않습니다.**

    **왜 이렇게 되나:** `log`에는 `"ip"` 이름표가 없습니다. 두 번째 줄에서 에러가 나면서 프로그램이 **즉시 멈추기** 때문에, 세 번째 줄인 `print("검사 완료")`는 아예 실행 기회를 못 얻습니다.

---

## 1-E · 에러 없이 꺼내기 — `.get()`

`KeyError`를 피하는 방법이 있습니다. 대괄호 대신 `.get()`을 씁니다.

```python
user = {"name": "kim01", "dept": "finance"}

print(user.get("name"))    # kim01   ← 있으면 똑같이 나옴
print(user.get("phone"))   # None    ← 없어도 에러 안 남
print("검사 완료")          # 검사 완료 ← 프로그램이 안 멈춤!
```

`None`(논)은 **"아무것도 없음"**을 뜻하는 파이썬 값입니다. 빈 문자열 `""`이나 숫자 `0`과는 다릅니다.

| | 있을 때 | 없을 때 |
|---|---|---|
| `user["phone"]` | 값이 나옴 | 💥 **KeyError, 프로그램 멈춤** |
| `user.get("phone")` | 값이 나옴 | `None`, **계속 진행** |

### 🔹 문제 1-4. 멈추지 않게 고치기

**설명**
문제 1-3의 코드가 멈추지 않도록 고치세요.

**주어지는 것**
```python
log = {"user": "kim01", "result": "fail"}
print(log["ip"])
print("검사 완료")
```

**만들 것**
가운데 줄을 `.get()`을 쓰도록 바꾸기

**나와야 하는 결과**
```
None
검사 완료
```

??? success "▶ 정답 보기"
    ```python
    log = {"user": "kim01", "result": "fail"}
    print(log.get("ip"))
    print("검사 완료")
    ```

    **왜 이렇게 되나:** `.get()`은 이름표가 없으면 에러를 내는 대신 `None`을 돌려줍니다. 에러가 안 나니 프로그램이 계속 흘러가고, `"검사 완료"`까지 출력됩니다.

---

## 1-F · 없을 때 대신 쓸 값 정하기 — `.get(키, 기본값)`

`None`이 화면에 찍히는 건 보기 안 좋죠. **없을 때 대신 보여줄 값**을 두 번째 자리에 적어줄 수 있습니다.

```python
user = {"name": "kim01", "dept": "finance"}

print(user.get("phone"))            # None
print(user.get("phone", "미등록"))   # 미등록
print(user.get("dept", "미등록"))    # finance  ← 있으면 기본값은 무시됨
```

읽는 법: **`.get(찾을 이름표, 없으면 이걸로)`**

기본값으로는 아무거나 넣을 수 있습니다. 상황에 맞게 고릅니다.

```python
user.get("phone", "미등록")   # 글자로 보여줄 때
user.get("fail_count", 0)    # 숫자를 셀 때
user.get("roles", [])        # 목록을 훑을 때 (2층에서 진짜 위력이 나옵니다)
```

### 🔹 문제 1-5. 로그인 실패 횟수 세기

**설명**
어떤 계정은 실패 기록이 아예 없어서 `fail_count` 이름표가 없습니다.
기록이 없으면 **0회**로 보고, 실패 횟수에 1을 더해 출력하세요.

**주어지는 것**
```python
account = {"user": "park03", "dept": "sales"}
```

**만들 것**
`fail_count`를 꺼내되 없으면 `0`으로 치고, 거기에 `1`을 더해 출력하는 코드

**나와야 하는 결과**
```
1
```

??? success "▶ 정답 보기"
    ```python
    count = account.get("fail_count", 0)
    print(count + 1)
    ```

    한 줄로도 됩니다.
    ```python
    print(account.get("fail_count", 0) + 1)
    ```

    **왜 이렇게 되나:** 기본값을 `0`(숫자)으로 줬기 때문에 `+ 1`이 가능합니다. 만약 기본값을 `"없음"`(글자)으로 줬다면 `"없음" + 1`이 되어 `TypeError`가 납니다. **기본값의 종류는 뒤에서 할 계산에 맞춰 고릅니다.**

!!! tip "🧱 4과목 연결고리"
    4과목 위험점수 계산 코드가 이 패턴 그대로입니다.

    ```python
    score += weight_table.get(name, 10)   # 가중치가 정해져 있으면 그걸, 없으면 10점
    ```

---

## 1-G · 이름표가 있는지만 확인하기 — `in`

값이 필요한 게 아니라 **"있냐 없냐"만** 알고 싶을 때가 있습니다.

```python
user = {"name": "kim01", "dept": "finance"}

print("dept" in user)     # True
print("phone" in user)    # False
```

`if`와 붙여 쓰면 이렇게 됩니다.

```python
if "phone" in user:
    print("연락처:", user["phone"])
else:
    print("연락처 미등록")
```

!!! note "`in`은 이름표(키)만 봅니다"
    ```python
    print("kim01" in user)    # False !!
    ```
    `"kim01"`은 **값**이지 이름표가 아닙니다. `in`은 왼쪽 이름표들만 훑기 때문에 `False`가 나옵니다. 헷갈리기 쉬운 지점입니다.

### 🔹 문제 1-6. 승인자 배정 여부 확인

**설명**
접근 요청에 승인자가 배정되었는지 확인하는 코드를 만드세요.

**주어지는 것**
```python
request = {"id": "req-1003", "user": "choi04", "status": "requested"}
```

**만들 것**
`approver` 이름표가 있으면 `승인자: (이름)`을, 없으면 `승인자 미배정`을 출력

**나와야 하는 결과**
```
승인자 미배정
```

??? success "▶ 정답 보기"
    ```python
    if "approver" in request:
        print("승인자:", request["approver"])
    else:
        print("승인자 미배정")
    ```

    `.get()`으로도 같은 일을 할 수 있습니다.
    ```python
    print("승인자:", request.get("approver", "미배정"))
    ```

    **어느 쪽을 쓰나:** 출력만 다르게 하려면 `.get()`이 짧아서 좋고, **없을 때 아예 다른 동작**(예: 승인자 자동 배정 함수 호출)을 해야 하면 `in` + `if`가 맞습니다.

---

## 1-H · 통째로 훑기 — `.items()`

이름표와 내용물을 **한 쌍씩** 꺼내며 도는 방법입니다.

```python
user = {"name": "kim01", "dept": "finance", "level": "read"}

for key, value in user.items():
    print(key, "→", value)
```

결과:

```
name → kim01
dept → finance
level → read
```

`for` 뒤에 **변수 두 개**를 쓰는 게 포인트입니다. 앞쪽에 이름표가, 뒤쪽에 내용물이 담깁니다.
이름은 `key`, `value`가 아니어도 됩니다 — 뜻이 통하는 이름이 더 좋습니다.

```python
for field, content in user.items():   # 이래도 똑같이 동작합니다
    print(field, "→", content)
```

### 🔹 문제 1-7. 요청 내역 보기 좋게 출력

**설명**
접근 요청의 모든 항목을 한 줄씩 출력하세요.

**주어지는 것**
```python
request = {"id": "req-1004", "user": "jung05", "system": "hr_system"}
```

**만들 것**
`이름표: 값` 형태로 한 줄씩 출력하는 반복문

**나와야 하는 결과**
```
id: req-1004
user: jung05
system: hr_system
```

??? success "▶ 정답 보기"
    ```python
    for field, value in request.items():
        print(field + ": " + value)
    ```

    `print`에 쉼표를 쓰면 사이에 **공백이 자동으로 하나** 들어갑니다. 위 결과처럼 콜론 바로 뒤에 붙이려면 `+`로 이어붙이거나, 8층에서 배울 f-string을 씁니다.
    ```python
    print(f"{field}: {value}")   # 8층에서 다룹니다 — 이게 제일 편합니다
    ```

!!! tip "🧱 3과목 연결고리"
    Day3 부서 불일치 탐지 코드가 `.items()`로 시작합니다.

    ```python
    for user, granted_dept in user_dept_history.items():
    ```

    변수 이름을 `key, value` 대신 **`user, granted_dept`**로 지어서, 읽자마자 "사람과 그 사람의 부여 당시 부서"임을 알 수 있게 했습니다. 좋은 습관입니다.

---

## 1-I · 상자 안에 상자 — 중첩 딕셔너리 (맛보기)

값 자리에 **또 딕셔너리**가 들어갈 수 있습니다. 실제 보안 로그가 이렇게 생겼습니다.

```python
event = {
    "user": "kim01",
    "event_type": "login_failed",
    "detail": {"ip": "10.0.0.5", "device": "laptop"}
}
```

안쪽 값을 꺼내려면 대괄호를 **두 번** 씁니다.

```python
print(event["detail"])         # {'ip': '10.0.0.5', 'device': 'laptop'}
print(event["detail"]["ip"])   # 10.0.0.5
```

**한 단계씩** 읽으면 쉽습니다. `event["detail"]`이 먼저 안쪽 상자를 꺼내고, 거기에 `["ip"]`를 또 붙이는 겁니다.

### 🔹 문제 1-8. 로그에서 IP 꺼내기

**설명**
이상탐지 이벤트에서 접속 IP를 출력하세요.

**주어지는 것**
```python
event = {"user": "lee02", "event_type": "login_failed",
         "detail": {"ip": "192.168.0.77", "device": "mobile"}}
```

**만들 것**
IP만 출력하는 한 줄

**나와야 하는 결과**
```
192.168.0.77
```

??? success "▶ 정답 보기"
    ```python
    print(event["detail"]["ip"])
    ```

    **왜 이렇게 되나:** `event["detail"]`이 `{"ip": ..., "device": ...}`라는 상자를 꺼내주고, 그 상자에서 다시 `["ip"]`로 값을 꺼냅니다. **왼쪽부터 차례대로** 읽으면 됩니다.

### 🔹 문제 1-9. `detail`이 통째로 없는 로그 (⭐ 이 층의 마지막 관문)

**설명**
어떤 로그는 `detail` 자체가 아예 없습니다. 이때도 프로그램이 멈추지 않고 `"알수없음"`이 나오게 만드세요.

**주어지는 것**
```python
event = {"user": "park03", "event_type": "logout"}
```

**만들 것**
IP를 꺼내되, `detail`이 없어도 `event["detail"]["ip"]`가 아니라 안전하게 동작하는 코드

**나와야 하는 결과**
```
알수없음
```

??? success "▶ 정답 보기"
    ```python
    print(event.get("detail", {}).get("ip", "알수없음"))
    ```

    **한 조각씩 뜯어보면:**

    | 조각 | 하는 일 |
    |------|---------|
    | `event.get("detail", {})` | `detail`이 있으면 그 상자를, **없으면 빈 상자 `{}`**를 돌려줌 |
    | `.get("ip", "알수없음")` | 그 상자에서 `ip`를 꺼내되, 없으면 `"알수없음"` |

    **핵심은 기본값이 빈 딕셔너리 `{}`라는 점입니다.** 만약 기본값을 `None`으로 두면 `None.get(...)`이 되어 `AttributeError`로 멈춥니다. **빈 상자를 돌려줘야 뒤에 `.get()`을 또 붙일 수 있습니다.**

    이게 1층에서 가장 어려운 한 줄입니다. 여기까지 이해하셨으면 1층은 끝입니다.

!!! tip "🧱 4과목 연결고리"
    4과목 IOC 매칭 코드에 이 줄이 그대로 나옵니다.

    ```python
    ip = event.get('detail', {}).get('ip')
    ```

    처음 보면 암호 같지만, **`.get()` 두 번**일 뿐입니다.

---

## 🧪 1층 정리 퀴즈

<div class="quiz">
<p class="quiz-q"><span class="tag">1층</span><b><code>user = {"name": "kim01"}</code> 일 때, <code>user["dept"]</code>를 실행하면?</b></p>
<button class="quiz-opt">None이 나온다</button>
<button class="quiz-opt">빈 문자열 ""이 나온다</button>
<button class="quiz-opt" data-correct>KeyError가 나면서 프로그램이 멈춘다</button>
<button class="quiz-opt">아무 일도 안 일어난다</button>
<div class="quiz-explain"><b>정답: KeyError.</b> 대괄호 <code>[ ]</code>는 없는 이름표를 만나면 <b>에러를 내고 프로그램을 멈춥니다.</b> <code>None</code>이 나오는 건 <code>.get()</code>을 썼을 때입니다. (헷갈리기 쉬운 짝이라 꼭 구분해두세요)</div>
<button class="quiz-retry">다시 풀기</button>
</div>

<div class="quiz">
<p class="quiz-q"><span class="tag">1층</span><b><code>account = {"user": "park03"}</code> 일 때, <code>account.get("fail_count", 0) + 1</code>의 결과는?</b></p>
<button class="quiz-opt" data-correct>1</button>
<button class="quiz-opt">0</button>
<button class="quiz-opt">None + 1 이라서 TypeError</button>
<button class="quiz-opt">KeyError</button>
<div class="quiz-explain"><b>정답: 1.</b> <code>fail_count</code> 이름표가 없으므로 기본값 <code>0</code>이 나오고, 거기에 1을 더해 <b>1</b>이 됩니다. 만약 기본값을 안 적었다면(<code>.get("fail_count")</code>) <code>None + 1</code>이 되어 TypeError가 났을 겁니다 — <b>기본값을 적는 이유</b>가 여기 있습니다.</div>
<button class="quiz-retry">다시 풀기</button>
</div>

<div class="quiz">
<p class="quiz-q"><span class="tag">1층</span><b><code>user = {"name": "kim01", "dept": "finance"}</code> 일 때, <code>"kim01" in user</code>의 결과는?</b></p>
<button class="quiz-opt">True</button>
<button class="quiz-opt" data-correct>False</button>
<button class="quiz-opt">KeyError</button>
<button class="quiz-opt">None</button>
<div class="quiz-explain"><b>정답: False.</b> <code>in</code>은 <b>이름표(키)</b>만 훑습니다. <code>"kim01"</code>은 값이지 이름표가 아니라서 <code>False</code>입니다. 이름표를 확인하려면 <code>"name" in user</code>라고 써야 <code>True</code>가 나옵니다.</div>
<button class="quiz-retry">다시 풀기</button>
</div>

<div class="quiz">
<p class="quiz-q"><span class="tag">1층</span><b><code>event = {"user": "park03"}</code> 일 때, <code>event.get("detail", {}).get("ip", "알수없음")</code>에서 <u>기본값을 <code>{}</code> 대신 <code>None</code></u>으로 바꾸면 어떻게 될까요?</b></p>
<button class="quiz-opt">똑같이 "알수없음"이 나온다</button>
<button class="quiz-opt">None이 나온다</button>
<button class="quiz-opt" data-correct>AttributeError가 나면서 멈춘다</button>
<button class="quiz-opt">빈 딕셔너리가 나온다</button>
<div class="quiz-explain"><b>정답: AttributeError.</b> 첫 <code>.get()</code>이 <code>None</code>을 돌려주면 그 뒤가 <code>None.get("ip", ...)</code>이 되는데, <code>None</code>에는 <code>.get()</code>이라는 기능이 없어서 멈춥니다. <b>뒤에 <code>.get()</code>을 또 붙일 거면 기본값은 반드시 빈 딕셔너리 <code>{}</code></b>여야 합니다.</div>
<button class="quiz-retry">다시 풀기</button>
</div>

<!-- TODO(human): 5번째 퀴즈 문항 -->

---

## ✅ 1층 통과 체크리스트

아래를 **안 보고** 말할 수 있으면 2층으로 갑니다.

- [ ] 딕셔너리를 만들고 `[ ]`로 값을 꺼낼 수 있다
- [ ] `[ ]`로 값을 바꾸고 새 이름표를 추가할 수 있다
- [ ] **`[ ]`와 `.get()`의 차이를 설명할 수 있다** ⭐ 이게 1층의 핵심입니다
- [ ] `.get(키, 기본값)`에서 기본값을 상황에 맞게 고를 수 있다 (`0` / `""` / `{}`)
- [ ] `in`으로 이름표 존재를 확인할 수 있다
- [ ] `.items()`로 전체를 훑을 수 있다
- [ ] `event.get("detail", {}).get("ip")` 를 보고 무슨 뜻인지 말할 수 있다

## ➡️ 다음 층 예고

**2층 — 리스트 1개 + `.append()`**

1층에서 만든 상자를 **여러 개 모아두는 법**을 배웁니다. 그리고 2층이 끝나면 바로 3층에서 둘이 합쳐집니다.

```python
requests = []                # 빈 바구니
requests.append(request)     # 1층에서 만든 상자를 담기
```
