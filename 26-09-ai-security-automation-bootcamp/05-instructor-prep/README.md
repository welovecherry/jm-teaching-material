# 05-instructor-prep · 강사 예습 튜토리얼 (MkDocs)

강사(정민홍) 본인이 **강의 전에 먼저 공부**하기 위한 예습 사이트입니다.
학생용 산출물(`03-samples`, `04-build`)과는 목적이 다른 별도 카테고리입니다.

- 기준(진실의 원천): 각 과목 `02-source/.../*_상세교안.md`
- 작성 순서: **2과목 → 3과목 → 4과목 → 1과목**
- 작성 규칙: [`docs/prep-style-guide.md`](docs/prep-style-guide.md)

## 폴더 구조
```
05-instructor-prep/
├── mkdocs.yml                      # 사이트 설정 + 네비게이션(과목·Day 순서)
├── docs/
│   ├── index.md                    # 홈 + 진도 체크박스
│   ├── prep-style-guide.md         # 예습 문서 작성 규칙
│   ├── subject-2-network-zt/       # 2과목 day01~day08
│   ├── subject-3-access-control/   # 3과목 day01~day05
│   ├── subject-4-anomaly-detection/# 4과목 day01~day05
│   └── subject-1-ai-automation/    # 1과목 day01~day08
```
> 폴더 경로는 ASCII(깨끗한 URL), 사이드바에 보이는 이름은 한글입니다.

## 처음 한 번: 설치
```bash
pip install mkdocs-material
```

## 로컬에서 미리보기 (작성하면서 실시간 확인)
```bash
cd 26-09-ai-security-automation-bootcamp/05-instructor-prep
mkdocs serve
# 브라우저에서 http://127.0.0.1:8000 열기 (저장하면 자동 새로고침)
```

## GitHub Pages로 배포 (나만 보기 → 나중에)
```bash
mkdocs gh-deploy
```
> 이 리포는 private이므로 Pages도 비공개 유지 가능합니다. 배포는 스타일 확정 후 진행합니다.
