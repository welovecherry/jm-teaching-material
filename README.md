# jm-teaching-material

강사 **정민홍**의 강의 교안 모노레포. 강의별 폴더로 교안을 관리한다.
제작 규칙·워크플로우는 [`CLAUDE.md`](./CLAUDE.md) 참고.

## 폴더명 규칙
`YY-MM-토픽-형태` — 시작 년(2자리)-월 프리픽스 + 영문 kebab-case (하이픈 통일)
(예: `26-08-ai-agent-oneday`). 강의 폴더 내부는 `01-docs / 02-source / 03-samples / 04-build` 순.

## 강의 인덱스

| 시작월 | 강의명 | 형태 | 포맷 | 상태 | 폴더 |
|--------|--------|------|------|------|------|
| 26-09 | AI·보안 자동화 부트캠프 | multi-month | jupyter | sample | [`26-09-ai-security-automation-bootcamp`](./26-09-ai-security-automation-bootcamp) |

> 상태: `planning` → `sample` → `building` → `done`

## 구조
- `_template/` — 새 강의 뼈대 (복사해서 사용)
- `_shared/` — 여러 강의 공통 자산
- `YY-MM-*/` — 각 강의 폴더
