# jm-teaching-material

강사 **정민홍**의 강의 교안 모노레포. 강의별 폴더로 교안을 관리한다.
제작 규칙·워크플로우는 [`CLAUDE.md`](./CLAUDE.md) 참고.

## 폴더명 규칙
`YYYY-MM_토픽-형태` — 시작 년-월 프리픽스 + 영문 kebab-case 토픽/형태
(예: `2026-08_ai-agent-oneday`).

## 강의 인덱스

| 시작월 | 강의명 | 형태 | 포맷 | 상태 | 폴더 |
|--------|--------|------|------|------|------|
| 2026-09 | AI·보안 자동화 부트캠프 | multi-month | jupyter | planning | [`2026-09_ai-security-automation-bootcamp`](./2026-09_ai-security-automation-bootcamp) |

> 상태: `planning` → `sample` → `building` → `done`

## 구조
- `_template/` — 새 강의 뼈대 (복사해서 사용)
- `_shared/` — 여러 강의 공통 자산
- `YYYY-MM_*/` — 각 강의 폴더
