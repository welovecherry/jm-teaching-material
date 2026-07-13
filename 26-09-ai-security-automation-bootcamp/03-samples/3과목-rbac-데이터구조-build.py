# -*- coding: utf-8 -*-
# 3과목(접근통제) Day1 · 45-70분 RBAC 데이터 구조 설계와 구현 — v7 스타일 적용, v1
import json, os
cells=[]
def md(t): cells.append({"cell_type":"markdown","metadata":{},"source":t})
def code(t): cells.append({"cell_type":"code","metadata":{},"execution_count":None,"outputs":[],"source":t})
def blank(): code("# ✍️ 여기에 직접 작성해 보세요\n")
def prob(title, steps, expected, hints):
    md(f"""### ✍️ 문제 — {title}

{steps}

**기대 출력**
```
{expected}
```
<details><summary>힌트 보기 (막힐 때만 펼치세요)</summary>

{hints}
</details>""")
    blank()

# ═══ 표지 ═══
md("""# 3과목 접근통제 · Day 1 — RBAC 데이터 구조 설계와 구현

## 역할 기반 접근통제를 파이썬으로 표현하기 · 45–70분

> **만든 날짜:** 2026-07-13 · **버전:** v1

누가 무엇을 할 수 있는지를 코드로 관리하는 **RBAC**을, 이미 배운 **딕셔너리와 리스트**로
표현해 봅니다. 그리고 "이 사람이 이 권한이 있나?"를 확인하는 함수를 직접 만듭니다.

> 예제를 실행해 확인한 뒤, 바로 아래 문제(✍️)를 직접 작성해 보세요. 막히면 힌트를 펼칩니다.""")

# ═══ 학습목표 ═══
md("""## 학습목표

1. RBAC(역할 기반 접근통제)의 구조(계정 → 역할 → 권한)를 이해하기
2. `roles`, `user_roles` 를 **딕셔너리 + 리스트**로 설계하기
3. 권한 확인 함수 `has_permission()` 을 만들고 사용하기""")

# ═══ 사용법 ═══
md("""## 이 노트북 쓰는 법

| 표시 | 뜻 |
|------|-----|
| 📖 | 개념(읽기) |
| 💻 | 예제(실행해 결과 확인) |
| ✍️ | 문제(직접 작성) |
| ✅ | 결과("이렇게 나오면 성공") |
| ❓ | 핵심 질문(답은 본문에) |

> 코드 칸은 **`Shift + Enter`** 로 실행합니다. 뒤쪽 `[심화·자습]`은 시간이 남을 때 풀면 됩니다.""")

# ══════════════════════════════════════════════════
# 1. RBAC이란
# ══════════════════════════════════════════════════
md("""---
## 1. RBAC이 뭔가요?

접근통제란 **"누가(계정) 무엇을(권한) 할 수 있는지"** 를 정하는 일입니다.

- 계정에 권한을 **직접** 붙이면? 사람이 수백 명이면 한 명 한 명 권한을 관리해야 해서 관리가 지옥이 됩니다.
- 그래서 중간에 **역할(Role)** 을 둡니다. 이것이 **RBAC(Role-Based Access Control, 역할 기반 접근통제)** 입니다.

```
계정(kim01)  →  역할(sales)  →  권한(customer_read, quote_write)
```

- **장점:** 역할의 권한만 바꾸면, 그 역할을 가진 **모든 사람의 권한이 한 번에** 바뀝니다.

> **왜 역할을 중간에 둘까?** 직원이 부서를 옮겨도 **역할 하나만 바꾸면** 권한 전체가 갱신되기 때문입니다.""")

# ══════════════════════════════════════════════════
# 2. RBAC을 딕셔너리로 표현
# ══════════════════════════════════════════════════
md("""---
## 2. RBAC을 딕셔너리로 표현하기

RBAC에는 두 가지 관계가 있고, 둘 다 **딕셔너리 + 리스트**(이미 배운 조합!)로 표현합니다.

1. **`roles`** : 역할 → 그 역할이 가진 **권한 목록**
2. **`user_roles`** : 사용자 → 그 사용자가 가진 **역할 목록**

> 값은 영어로 씁니다. (예: 역할 `sales`=영업담당자, 권한 `customer_read`=고객정보 조회)""")

code('''# 💻 예제 — RBAC 데이터를 딕셔너리로
roles = {"sales": ["customer_read", "quote_write"]}   # 역할 → 권한 목록
user_roles = {"kim01": ["sales"]}                     # 사용자 → 역할 목록

print(roles["sales"])         # sales 역할이 가진 권한들
print(user_roles["kim01"])    # kim01 이 가진 역할들''')
md("""**✅ 성공 출력**
```
['customer_read', 'quote_write']
['sales']
```""")

prob("역할과 사용자 추가하기",
"""아래 두 딕셔너리를 만든 뒤, 값을 하나씩 추가하세요.
1. `roles` 에 `"manager"` 역할을 만들고 권한 목록 `["user_manage", "log_read"]` 를 담으세요.
2. `user_roles` 에 `"lee02"` 사용자를 만들고 역할 목록 `["manager"]` 를 담으세요.
3. `lee02` 의 역할 목록을 출력하세요.""",
"['manager']",
"""- 딕셔너리에 새 항목: `roles["manager"] = [...]` 또는 처음부터 `{"manager": [...]}`.
- 권한/역할은 **리스트**로 담습니다(대괄호).
- 출력: `print(user_roles["lee02"])`.""")

# ══════════════════════════════════════════════════
# 3. has_permission 함수
# ══════════════════════════════════════════════════
md("""---
## 3. 권한 확인 함수 `has_permission()`

"이 사용자가 이 권한을 가지고 있나?"를 확인하려면 두 딕셔너리를 이어서 봐야 합니다.

1. 그 사용자의 **역할들**을 찾고 (`user_roles`)
2. 각 역할의 **권한 목록**을 보고 (`roles`)
3. 원하는 권한이 그 안에 **있으면** `True`, 끝까지 없으면 `False`.

- `.get(user, [])` — 없는 사용자면 `None` 대신 **빈 리스트 `[]`** 를 돌려줍니다(기본값 지정). 그래서 에러 없이 안전합니다.
- `"권한" in 리스트` — 값이 리스트 안에 있으면 `True`.""")

code('''# 💻 예제 — 권한 확인 함수
roles = {"sales": ["customer_read", "quote_write"]}
user_roles = {"kim01": ["sales"]}

def has_permission(user, permission, roles, user_roles):
    for role in user_roles.get(user, []):        # ① 사용자의 역할들
        if permission in roles.get(role, []):     # ② 그 역할의 권한에 있나?
            return True                           # ③ 있으면 True
    return False                                  # 끝까지 없으면 False

print(has_permission("kim01", "customer_read", roles, user_roles))  # True
print(has_permission("kim01", "user_delete", roles, user_roles))    # False''')
md("""**✅ 성공 출력**
```
True
False
```""")

code('''# ✍️ 문제 (출력 예측) — 무엇이 나올지 예측한 뒤 실행하세요.
#   (roles, user_roles, has_permission 은 위에서 이미 정의됨)
print(has_permission("kim01", "quote_write", roles, user_roles))   # 예측: ?''')

md("""### ❓ 핵심 질문

`user_roles` 에 **없는 사용자**(예: `"ghost"`)로 `has_permission()` 을 호출하면 어떤 값이 나올까요?
> 답은 위 `.get(user, [])` 설명 안에 있습니다. "없으면 빈 리스트"를 떠올려 보세요.""")

# ══════════════════════════════════════════════════
# [심화·자습]
# ══════════════════════════════════════════════════
md("""---
## [심화·자습] — 더 해보기
> 시간이 남거나 자습·리추얼 때 풀어 보세요.

### 📖 없는 사용자도 안전한 이유
- `user_roles.get("ghost", [])` 는 `[]`(빈 리스트)를 돌려줍니다.
- 그러면 `for` 반복이 한 번도 돌지 않고 곧바로 `return False` 가 됩니다. **에러 없이** 처리됩니다.""")

code('''# 💻 (심화) 없는 사용자로 확인해도 에러가 아니라 False
print(has_permission("ghost", "customer_read", roles, user_roles))   # False''')
md("""**✅ 성공 출력**
```
False
```""")

prob("새 사용자에게 역할을 주고 권한 확인하기 (백지)",
"""1. `user_roles` 에 `"park03"` 사용자를 추가하고 역할 `"sales"` 를 주세요.
2. `park03` 이 `"quote_write"` 권한을 가졌는지 `has_permission()` 으로 확인해 출력하세요.""",
"True",
"""- 역할 주기: `user_roles["park03"] = ["sales"]`.
- 확인: `has_permission("park03", "quote_write", roles, user_roles)`.
- `sales` 역할에 `quote_write` 가 있으므로 결과는 `True`.""")

md("""### ❓ 면접 질문

**"계정에 권한을 직접 붙이는 방식보다, 중간에 역할을 두는 RBAC이 나은 점은 무엇인가요?"**
> 힌트: "역할 하나만 바꾸면…". 위 `1번` 개념 설명에서 답을 찾아보세요.""")

# ═══ 마무리 ═══
md("""---
## 오늘 요약

1. **RBAC** = 계정 → **역할** → 권한. 역할을 중간에 두어 권한 관리를 쉽게 함.
2. **데이터 구조** — `roles`(역할→권한 목록), `user_roles`(사용자→역할 목록). 둘 다 딕셔너리 + 리스트.
3. **`has_permission()`** — 사용자의 역할들을 훑어, 그 역할의 권한에 원하는 권한이 있으면 `True`.
4. **`.get(user, [])`** — 없는 사용자는 빈 리스트 → 에러 없이 `False`.""")

md("""## 종합 퀴즈 (객관식)

**Q1.** RBAC에서 계정과 권한 사이에 두는 중간 단계는? ① 그룹 ② 역할(Role) ③ 부서
<details><summary>정답 보기</summary>② 역할(Role)</details>

**Q2.** `roles = {"sales": ["customer_read"]}` 에서 sales 의 권한 목록을 꺼내려면? ① `roles["sales"]` ② `roles[0]` ③ `roles.sales`
<details><summary>정답 보기</summary>① `roles["sales"]` — 딕셔너리는 이름(키)으로 꺼냄</details>

**Q3.** `user_roles.get("ghost", [])` 의 결과는? ① 에러 ② `None` ③ `[]`
<details><summary>정답 보기</summary>③ `[]` — 없는 키면 기본값으로 지정한 빈 리스트를 돌려줌</details>""")

md("""## 다음 시간 예고

이어서 **역할 부여/회수 함수(`assign_role` 등)** 를 만들고, `roles`·`user_roles` 데이터를
코드에 하드코딩하지 않고 **JSON 파일로 분리**해 관리하는 법을 배웁니다.""")

# ═══ 저장 ═══
nb={"cells":cells,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":"3.11"}},"nbformat":4,"nbformat_minor":5}
out="/Users/hong/jm-teaching-material/26-09-ai-security-automation-bootcamp/03-samples/3과목-rbac-데이터구조-v1.ipynb"
os.makedirs(os.path.dirname(out),exist_ok=True)
with open(out,"w",encoding="utf-8") as f: json.dump(nb,f,ensure_ascii=False,indent=1)
print("cells:",len(cells)); print("saved:",out)
