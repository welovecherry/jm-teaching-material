# Day별 교육 내용 — AI·보안 자동화 부트캠프

> 하루 6시간 = 강의1(120분) + 강의2(120분) + 실습(120분). 앞뒤 리추얼 2h는 교안 바깥 운영 요소.
> 출처: `02-source/시냅스_SKT K-뉴딜 과정/*/N과목_*_상세교안.md` (원본이 진실의 원천).
> 과목 매핑: 1과목=P1-1, 2과목=P1-2, 3과목=P2-1, 4과목=P2-2, 5과목=P2-3.

| 과목 | 일수 | 링크 |
|---|---|---|
| 1과목 P1-1 AI·자동화 기초 | 8일 | [바로가기](#1과목-p1-1--ai자동화-기초-8일) |
| 2과목 P1-2 네트워크·ZT 운영 기초 | 8일 | [바로가기](#2과목-p1-2--네트워크zt-운영-기초-8일) |
| 3과목 P2-1 접근통제 자동화 | 5일 | [바로가기](#3과목-p2-1--접근통제-자동화-5일) |
| 4과목 P2-2 이상탐지 자동화 | 5일 | [바로가기](#4과목-p2-2--이상탐지-자동화-5일) |
| 5과목 P2-3 자동 대응 SOAR | 5일 | [바로가기](#5과목-p2-3--자동-대응-soar-5일) |
| P3 캡스톤 운영 | 10일 | [바로가기](#p3--캡스톤-운영-10일) |

> ⚠️ 운영 카드에는 2과목이 **7.5일**로 적혀 있으나 상세교안에는 Day 1~8이 있습니다. 확인 필요.

---

# 1과목 P1-1 — AI·자동화 기초 (8일)

## Day 1 — 오리엔테이션·개발환경 구축 & Python 기초(변수·자료형·제어문)

**산출물** `agent_core/day01_basic.py`

**강의1** 과정 로드맵 / Python·VS Code 설치 / venv와 폴더 구조 / 변수·자료형과 f-string / list·dict / 연산자·형변환

**강의2** if·elif·else / for·while과 enumerate / 리스트 컴프리헨션과 break·continue / set·Counter로 집계 / 실습 과제 안내

**실습** 로그 20건에서 `login_failed`만 뽑아 사용자별 집계 → 2회 이상 '확인 필요' 출력. `THRESHOLD`는 상단 변수로 분리

---

## Day 2 — 함수·모듈화 & 파일 입출력·예외처리·로깅

**산출물** `agent_core/log_parser.py`, `sample_logs.csv`, `agent.log`

**강의1** 함수 정의와 어제 코드 리팩토링 / 모듈 분리와 import / datetime으로 타임스탬프 다루기 / open·with문 파일 읽기쓰기 / csv.DictReader / PEP8 네이밍

**강의2** try·except·finally 예외처리 / logging 모듈 기초 / RotatingFileHandler로 로그 회전 / 예외처리+로깅 결합 파서 / 실습 안내

**실습** CSV 보안 로그를 읽는 `parse_logs()`를 만들고, 파일이 없어도 죽지 않도록 방어. 처리 현황은 `agent.log`에 기록

---

## Day 3 — 자료구조 심화 & JSON·정규표현식

**산출물** `agent_core/normalize_logs.py`, `normalized_logs.json`

**강의1** 중첩 자료구조 접근 / JSON이 표준 교환 포맷인 이유 / json 모듈 loads·dumps·load·dump / 어제 파서에 JSON 저장 기능 추가 / 필수 필드 체크

**강의2** 정규표현식이 필요한 이유 / 기본 패턴 문법과 search·findall / 그룹핑과 named group / 여러 줄 로그 일괄 처리 / 실습 안내

**실습** raw 텍스트 로그 15~20줄을 정규표현식으로 파싱해 `normalized_logs.json`으로 저장. 매칭 실패한 줄은 따로 기록

---

## Day 4 — API·HTTP·requests 실전 & 인증정보 관리

**산출물** `agent_core/api_client.py`, `.env.example`, `api_result.json`

**강의1** API란 무엇인가 / HTTP 메서드와 URL 구조 / 상태코드와 응답 구조 / API Key·OAuth 인증 방식 / python-dotenv로 민감정보 관리

**강의2** requests.get으로 공개 API 호출 / 쿼리 파라미터와 헤더 / POST 요청과 요청 본문 / 에러 처리와 재시도 패턴 / 실습 안내

**실습** 공개 API를 호출해 필요한 필드만 뽑아 `api_result.json`으로 저장. API 키는 `.env`로 분리하고 서로 코드 리뷰

---

## Day 5 — Webhook·CLI 자동화 & 워크플로우 설계·스케줄링

**산출물** `agent_core/webhook_server.py`, `scheduler_job.py`, `test_webhook.sh`

**강의1** Polling과 Webhook 비교 / Flask로 Webhook 수신 서버 만들기 / 터미널 기본 명령어와 curl 테스트 / argparse로 CLI 인자 받기

**강의2** 트리거-조건-액션 모델 / 멱등성과 중복 실행 방지 / schedule 라이브러리로 반복 실행 / cron 문법 / 실습 안내

**실습** Webhook 서버로 이벤트를 받아 `login_failed`만 경고 로깅하고, 스케줄러가 매 1분 로그를 점검. 처리한 이벤트는 중복 처리하지 않음

---

## Day 6 — LLM 개념·프롬프트 엔지니어링 & AI Agent Tool-use 구조

**산출물** `agent_core/llm_client.py`, `tool_router.py`, `agent_result.json`

**강의1** LLM 동작 원리와 환각 / 프롬프트 4원칙(역할·지시·형식·예시) / LLM API 호출 실습 / 구조화된 출력 파싱 / AI Agent 예고

**강의2** 챗봇과 AI Agent의 차이 / Tool-use(함수 호출) 구조 / 도구 호출 라우터 구현 / 승인 게이트 개념 예고 / 실습 안내

**실습** LLM으로 로그를 요약하고, `tool_registry` 기반 라우터로 LLM이 고른 도구를 실제 실행. 결과를 `agent_result.json`으로 저장

---

## Day 7 — LLM 활용(이벤트요약·고객리서치) & 보고서 자동생성

**산출물** `agent_core/event_summarizer.py`, `report_generator.py`, `daily_report_*.md`

**강의1** 이벤트 요약의 실무 맥락과 Human-in-the-loop / 요약 프롬프트 설계와 청크 배치 처리 / risk_level 우선순위 정렬 / 프롬프트 체이닝 / 중간 결과 검증과 로깅

**강의2** 왜 템플릿+LLM 결합인가 / f-string 보고서 템플릿 / 상세 문단만 LLM에 위임 / 조건부 경고 문구 삽입 / 실습 안내

**실습** 이벤트 30~50건을 20건씩 나눠 요약·정렬하고, 템플릿에 채워 `daily_report_YYYYMMDD.md`를 자동 생성. high 3건 이상이면 경고 문구 삽입

---

## Day 8 — 보안데이터 파이프라인 통합·알림연동 & 전체 리뷰·발표

**산출물** `agent_core/` 전체 완성본, `docs/day08_retrospective.md`

**강의1** 전체 파이프라인 개관(입력→분류→요약→알림→리포팅) / smtplib 이메일 발송 / 메신저 Webhook 알림과 실패 fallback / config.yaml로 설정값 분리 / `run_pipeline()` 오케스트레이션

**강의2** 전체 코드 리뷰 체크리스트 / 의도적 오류를 넣은 디버깅 실습 / 발표 자료 준비 / 캡스톤 연계 안내

**실습** 리뷰 지적사항을 반영해 파이프라인을 완성하고 정상·예외 케이스를 처음부터 끝까지 실행. 조별 시연·피드백 후 회고를 `docs/`에 정리

---

# 2과목 P1-2 — 네트워크·ZT 운영 기초 (8일)

> 코딩 없는 개념·설명력 과목. 산출물은 문서·다이어그램.

## Day 1 — 네트워크 기초 I: OSI 7계층과 TCP/IP

**산출물** `network_zt/day01_packet_analysis.md`

**강의1** 네트워크를 배우는 이유(보안관제·기술영업 관점) / 1~3계층과 MAC vs IP / 4~7계층과 포트번호 / 계층으로 장애를 좁히는 bottom-up 진단 / OSI 한 장 정리

**강의2** TCP vs UDP 차이 / 3-way Handshake와 SYN Flood 예고 / IP 헤더와 패킷 구조(출발지·목적지·TTL) / Wireshark 설치와 필터 사용법

**실습** Wireshark로 웹 접속 패킷을 캡처해 SYN·SYN-ACK·ACK 3단계를 찾고, IP 헤더의 출발지·목적지·TTL을 기록해 분석 문서로 정리

---

## Day 2 — IP 주소 체계·서브네팅 & 라우팅·VLAN

**산출물** `network_zt/day02_subnet_design.md`

**강의1** IPv4 32비트 주소 구조와 공인·사설IP / 서브넷 마스크와 CIDR 표기법 / 부서별 서브네팅 계산(/26·/27·/28) / NAT 개념과 첫 번째 방어선

**강의2** 라우팅 테이블과 다음 홉·기본 게이트웨이 / 정적 vs 동적 라우팅 / 스위치와 VLAN 논리적 분리 / 망 구성도에서 라우팅 구간·VLAN 경계 읽기

**실습** 가상 A사(본사 3개 부서·지사·서버실)에 겹치지 않는 서브넷을 설계하고, 본사→지사 패킷 경로를 순서대로 적어 조원과 교차 검증

---

## Day 3 — DNS 개념과 동작원리

**산출물** `network_zt/day03_dns_analysis.md`

**강의1** DNS가 필요한 이유(인터넷의 전화번호부) / Root·TLD·Authoritative 계층 구조 / 재귀 질의 vs 반복 질의 / 레코드 타입 A·AAAA·CNAME·MX·TXT

**강의2** `nslookup`·`dig`로 레코드 조회 / DNS 캐싱과 TTL·전파 지연 / DNS Spoofing·Cache Poisoning 원리 / DNS 로그에서 DGA 등 이상징후 찾기

**실습** 도메인 5개 이상의 A·MX 레코드를 조회하고 `dig +trace`로 전체 경로를 확인. DNS 로그 30줄에서 의심 도메인을 근거와 함께 선정

---

## Day 4 — VPN 개념·종류 & 방화벽 기본

**산출물** `network_zt/day04_firewall_ruleset.md`

**강의1** VPN이 필요한 이유(재택근무·지사 연결) / Site-to-Site VPN 구조 / Remote Access VPN 구조와 인증 절차 / VPN의 경계 기반 한계와 Zero Trust 등장 배경

**강의2** 방화벽의 정의와 Allow/Deny / 룰 구성 요소와 룰 순서의 중요성 / 화이트리스트 vs 블랙리스트 / 가상 시나리오 룰셋 설계 시연

**실습** 가상 A사(웹서버·DB서버·내부 사무망·관리자 PC)에 화이트리스트 원칙으로 방화벽 룰셋을 설계하고 룰 순서를 배치해 표로 작성

---

## Day 5 — 클라우드·SaaS 환경·망 구성도 & 네트워크 품질지표

**산출물** `network_zt/day05_diagram.png`, `day05_quality_report.md`

**강의1** IaaS·PaaS·SaaS 비교 / SaaS 접속 흐름과 재택근무 확대에 따른 가시성 이슈 / 망 구성도 표준 표기법과 DMZ / 실제 망 구성도 읽기 / draw.io 기본 사용법

**강의2** Latency와 Jitter의 정의 / `ping`으로 RTT·Jitter 측정 / Packet Loss와 `traceroute` 구간별 지연 확인 / SaaS 접속 지연 종합 진단 흐름

**실습** draw.io로 인터넷-외부방화벽-DMZ-내부방화벽-내부망 구성도를 그리고, 3개 이상 목적지에 ping 10회·traceroute를 실측해 지연 진단 리포트 작성

---

## Day 6 — Zero Trust 원칙 & PDP/PEP·최소권한·지속검증

**산출물** `network_zt/day06_zt_scenario.md`

**강의1** 경계 기반 보안의 한계와 Zero Trust 등장 / ZT 5대 원칙 중 ID·Device·Network / Application·Policy 축과 위험기반 인증 / ZT vs 경계보안 비교표 작성

**강의2** PDP와 PEP의 역할과 분리 이유 / PDP/PEP 흐름 다이어그램 / 최소권한 원칙과 default deny / 지속적 검증과 위험 기반 인증 / ZT 성숙도 스코어링 예고

**실습** 5일차 A사 구성도에 ZT 5대 원칙별 적용 방안을 표로 정리하고, PDP/PEP 판단·집행 순서도와 부서별 최소권한 기준표, 가상 ZT 성숙도 점수를 문서화

---

## Day 7 — 정책 로그 이해 & 고객 환경 설명 문서화

**산출물** `network_zt/day07_customer_report.md`

**강의1** 정책 로그의 정의와 감사·이상탐지에서의 가치 / 주요 필드(timestamp·user·resource·action·reason·risk_score) 해석 / 여러 로그를 모아 보는 패턴 분석 / 1과목 JSON 파싱 스킬과의 연결

**강의2** 기술 용어를 비전문가에게 설명하는 원칙(비유·두괄식) / 결론-근거-권고 3단 구조 템플릿 / 표·그래프·다이어그램 활용 / 설명자료 예시 초안 검토

**실습** 정책 로그 30~50줄에서 핵심 이슈 1~2가지를 선정해, 결론-근거-권고 구조와 시각화를 갖춘 비전문가용 고객 설명자료를 작성하고 상호 검토

---

## Day 8 — 장애·위협·접근통제 이슈 도식화 & 종합 발표

**산출물** `network_zt/day08_issue_diagram.png`, `day08_retrospective.md`

**강의** 1~7일차 종합 지도 / 장애·위협·접근통제 이슈 유형 분류 / 플로우차트·타임라인으로 이슈 도식화 / 팀별 시나리오 도식화 작업 / 캡스톤 연계 안내와 발표 준비

**실습** 팀별로 이슈 하나를 골라 발생부터 대응까지를 플로우차트 또는 타임라인으로 도식화하고, 5분 발표 후 피드백을 회고 문서로 정리

---

# 3과목 P2-1 — 접근통제 자동화 (5일)

## Day 1 — RBAC 원리 & 최소권한 정책 설계 기준

**산출물** `access_control/rbac.py`, `policy.py`, `config/*.json`

**강의1** 1~2과목 복습과 접근통제가 필요한 이유 / 계정·권한·역할·그룹의 관계와 RBAC 원리 / RBAC 데이터 구조와 `has_permission()` 라이브 코딩 / 역할 부여·회수 함수와 JSON 분리 / argparse 조회 CLI

**강의2** 최소권한 원칙 심화 / 부서×시스템 권한 매트릭스 설계 / 예외 관리 원칙(승인자·만료일) / 매트릭스 JSON 구조화와 `check_policy()`·`is_exception_valid()` / 통합 `evaluate_access()`와 PDP 대응

**실습** 가상 A사 4개 부서 시나리오로 roles·user_roles·policy_matrix JSON을 설계하고, 정상/위반/예외허용/예외만료거부 4가지 테스트 케이스를 정리

---

## Day 2 — 접근 요청-승인-부여 프로세스 자동화

**산출물** `access_control/request_flow.py`, `requests.json`

**강의1** 비공식 요청 방식의 문제점 / 요청→검토→승인·반려→부여→회수 단계 정의 / SLA와 승인자 지정 규칙(관리자 권한 이중승인) / 요청 데이터 구조 설계

**강의2** `create_request()`·`approve_request()`·`reject_request()`와 상태 전이 검증 / `check_sla_breach()` / 요청 이력 JSON 저장·필터 조회 / 1일차 `evaluate_access()`와 연동한 승인 이중 검증

**실습** 요청 5건(승인 2·반려 1·SLA 초과 2)을 만들어 `requests.json`에 누적하고, SLA 초과 강조 출력과 정책 이중 검증을 붙여 결과 정리

---

## Day 3 — 접근 점검·회수 프로세스 & 과다권한 탐지

**산출물** `access_control/overprivilege.py`, `overprivilege_report_*.json`

**강의1** 정기 점검(access review)이 필요한 이유 / 점검 주기와 항목 체크리스트 / 과다권한의 정의와 위험 / 권한-사용이력 비교, 부서 불일치 탐지 접근법

**강의2** `detect_unused_permissions()` 90일 미사용 탐지 / `detect_dept_mismatch()` 부서 불일치 탐지 / 미사용·부서불일치·만료예외 종합 리포트 / 테스트 데이터와 경계값 검증

**실습** 탐지 함수 두 개와 종합 리포트 생성 함수를 구현해 날짜가 자동 반영되는 JSON 리포트를 만들고, 과다권한 후보 3건 이상 탐지 확인

---

## Day 4 — 권한 회수 자동화 & 조건기반 정책·예외승인

**산출물** `access_control/revoke.py`, `conditional.py`, `revocation_log.json`

**강의1** 회수 시나리오 3유형(즉시·유예 후·승인 후) / `classify_revocation()` / 유예 알림과 자동 회수·회수 로그 / 2일차 요청-승인 모듈 재사용한 회수 승인 요청 / `run_revocation_bot()` 통합

**강의2** 정적 정책의 한계와 시간·위치·디바이스 조건 / `check_time_condition()`·`evaluate_conditional_access()` / 임시권한(JIT Access)과 만료 자동 무효화 / `evaluate_full_access()`로 정책 엔진 통합

**실습** 회수 자동화와 조건기반 정책·임시권한을 구현하고 민감 권한 목록을 config로 분리. 자동회수·승인요청·조건 미충족 거부·임시권한 허용 4가지 케이스 실행

---

## Day 5 — 권한 점검 체크리스트 & 접근통제 결과 리포트 자동화·통합

**산출물** `access_control/weekly_report.py`, `access_control_weekly_report_*.md`, `day05_retrospective.md`

**강의1** 1~4일차 종합 지도 / 권한 점검 최종 체크리스트(자동 항목과 수동 항목 구분) / 전 모듈 종합 주간 리포트 구조 설계 / `agent_core/tool_router.py` 연동 지점 확인

**강의2** 전 모듈을 import하는 `weekly_report.py` 오케스트레이션 / `generate_weekly_report()` / 리포트 저장과 임계치 초과 알림 연동 / config·예외처리·로깅·재사용성 코드 리뷰 체크리스트

**실습** 주간 리포트 생성 스크립트를 완성해 날짜별 마크다운 리포트를 저장하고, tool_router에 핵심 함수를 등록해 연동 확인 후 조별 시연·회고

---

# 4과목 P2-2 — 이상탐지 자동화 (5일)

## Day 1 — 로그·이벤트·알림 개념 & SIEM/XDR 구조·데이터 전처리

**산출물** `anomaly_detection/normalize.py`, `normalized_events.json`

**강의1** 이상탐지가 필요한 이유(1~3과목 복습) / 로그·이벤트·알림의 계층 구조 / SIEM과 XDR 개념 비교 / 실습 데이터셋 소개(로그인·방화벽·SaaS 로그)

**강의2** pandas로 로그 탐색(`head()`·`value_counts()`) / 결측치·이상 타임스탬프 정제 / 3개 로그 소스 공통 스키마 설계 / 정규화 결과 JSON 저장과 건수 검증

**실습** 3개 로그 소스를 pandas로 탐색·정제하고 `normalize_login()`·`normalize_firewall()`·`normalize_saas()`로 공통 스키마 변환해 `normalized_events.json` 생성

---

## Day 2 — 이벤트 유형 분류(베이스라인) & 로그인·트래픽 급증 탐지 룰

**산출물** `anomaly_detection/classify.py`, `login_detection.py`, `traffic_detection.py`

**강의1** 베이스라인이란 무엇인가 / 통계 기반 vs 규칙 기반 베이스라인 / 관제 이벤트 5대 유형과 로그 소스 짝짓기 / `classifier_registry` 등록 구조 설계

**강의2** 비정상 로그인 탐지 룰(실패횟수·업무시간외) / `detect_bruteforce()`·`detect_offhour_login()` / 트래픽 급증과 이동평균 / `rolling()` 기반 `detect_traffic_spike()`

**실습** 이벤트 분류기와 로그인·트래픽 탐지 룰을 구현하고 의도적 이상 케이스로 검증. 임계값은 `config/detection_thresholds.json`으로 분리

---

## Day 3 — 비인가접근·SaaS이상·악성행위 탐지 & 상관분석

**산출물** `anomaly_detection/advanced_detection.py`, `correlation.py`, `day03_risk_scores.json`

**강의1** 3과목 RBAC 연계 비인가 접근 정의 / SaaS 이상 사용 탐지 / IOC 매칭 개념과 구현 / 가중치 기반 위험점수 스코어링

**강의2** 단일 이벤트의 한계와 킬체인·상관분석 / 사용자별 이벤트 시퀀스 구성 / 시간 윈도우 기반 `check_chain()` / 윈도우 임계값 튜닝 실험

**실습** 고급 탐지 함수와 상관분석을 구현하고 3과목 `roles.json`·`policy_matrix.json`을 연동해, 테스트 이벤트 10건의 위험점수를 JSON으로 저장

---

## Day 4 — 오탐·미탐 검토 & 탐지룰 튜닝

**산출물** `anomaly_detection/evaluation.py`, `day04_fp_analysis.md`, `day04_tuning_result.md`

**강의1** 오탐(FP)과 미탐(FN) 개념 / 정밀도와 재현율 계산식과 트레이드오프 / 보안관제에서 우선할 지표 / 탐지-검토-수정-재적용 튜닝 사이클

**강의2** 라벨링 테스트셋으로 `evaluate_detector()` 구현 / 오탐 사례 원인 분석 / 예외 조건 추가로 룰 개선 / 튜닝 전후 성능 비교

**실습** 라벨링 테스트셋으로 2~3일차 탐지 함수의 정밀도·재현율을 측정하고, 오탐 원인을 분석해 룰을 개선한 뒤 전후 성능을 비교 기록

---

## Day 5 — AI 기반 이벤트 요약·우선순위 분류 & 전체 통합·발표

**산출물** `anomaly_detection/pipeline.py`, `anomaly_detection_report_*.json`, `day05_retrospective.md`

**강의1** 1~4일차 파이프라인 종합 지도 / 1과목 LLM 요약 모듈 연결 / 위험점수·상관분석·자산중요도 기반 우선순위 기준 설계 / `agent_core` tool_router 연동 지점 확인

**강의2** `run_anomaly_pipeline()` 오케스트레이션 / high 우선순위 이벤트 자연어 요약 연동 / 코드 리뷰 체크리스트 / 의도적 오류 주입 디버깅 실습

**실습** 1~4일차 모든 모듈을 통합한 최종 파이프라인을 완성해 리포트를 생성하고, tool_router 연동을 확인한 뒤 팀별 시연 발표

---

# 5과목 P2-3 — 자동 대응 SOAR (5일)

## Day 1 — SOAR 개념·플레이북 구조 & 탐지-분류-조치-보고 흐름

**산출물** `soar_response/playbooks/*.md`, `incident.py`, `config/playbook_registry.json`

**강의1** 탐지에서 대응으로(1~4과목 복습) / SOAR 3요소(오케스트레이션·자동화·대응) / 플레이북 4대 구성요소(트리거·조건·액션·승인) / 플레이북 예시와 문서화 템플릿

**강의2** 탐지-분류-조치-보고 4단계 파이프라인 개관 / 이벤트 수집과 심각도 분류 인터페이스 / 3가지 조치 유형과 보고 단계 설계 / incident 상태 관리와 플레이북 자동 매칭

**실습** 4과목 탐지 시나리오 3가지에 대한 플레이북 초안을 작성하고, incident 상태 구조와 `match_playbook()` 구현

---

## Day 2 — 계정 잠금·접근 차단 자동화 시나리오

**산출물** `soar_response/containment.py`, `config/vip_accounts.json`, `containment_log.json`

**강의1** 계정 잠금이 필요한 상황과 오탐 부작용 / 트리거-조건-액션-해제 시나리오 설계 / 3과목 권한 회수와 계정 잠금의 차이 / `lock_account()`·`unlock_account()`와 조치 로깅

**강의2** IP 차단과 세션 종료의 차이 / 2과목 방화벽 룰 재사용한 `block_ip()` / `terminate_session()` / VIP 계정 예외 처리와 차단 해제 절차

**실습** 계정잠금·IP차단·세션종료 함수를 구현하고 조치 이력을 통일 로깅. VIP 계정 승인 우회 등 테스트 시나리오 3건 실행

---

## Day 3 — 티켓 생성·알림 전파·에스컬레이션 워크플로우

**산출물** `soar_response/ticketing.py`, `escalation.py`, `config/escalation_rules.json`

**강의1** 티켓 시스템 연동과 추적 가능성 / 1과목 API POST 지식 기반 ITSM 연동 개념 / 플레이북·조치이력을 결합한 `create_ticket()` / 티켓 상태와 incident 상태 동기화

**강의2** 이메일 vs 메신저 알림 채널 선택과 1과목 알림 함수 재사용 / SLA 기반 에스컬레이션 규칙 설계 / `escalate()` 구현 / 알림 피로도 관리와 4과목 튜닝의 영향

**실습** 티켓 생성부터 알림 전파, 에스컬레이션까지 이어지는 워크플로우를 구현하고, 1차 무응답 시 2차 에스컬레이션이 발생하는 시나리오를 시뮬레이션

---

## Day 4 — 초동대응 리포트 & 승인게이트·오탐대응·리스크평가

**산출물** `soar_response/report.py`, `approval_gate.py`, `incident_report_*.md`, `risk_assessment.md`

**강의1** 초동 대응 리포트의 5대 구성요소 / 타임라인 형식 사고 경위 정리 / `collect_incident_data()`로 1~3일차 데이터 취합과 템플릿 뼈대 / LLM으로 사고개요·후속조치 생성, 기술팀용·경영진용 버전 관리

**강의2** 가역성·영향범위·확실성 기준의 자동조치 vs 승인필요 구분 / 공통 승인 게이트 `execute_action()` / 오탐 복구 절차와 4과목으로 이어지는 피드백 루프 / 운영 리스크 종합 평가표

**실습** 1~3일차 데이터를 취합한 초동 대응 리포트를 두 버전으로 생성하고, 공통 승인 게이트와 `handle_false_positive()` 오탐 복구 절차를 구현·검증

---

## Day 5 — 전체 대응 플레이북 통합 & 최종 발표

**산출물** `soar_response/soar_engine.py`, `day05_final_retrospective.md`

**강의1** 1~4일차 SOAR 모듈 종합 지도 / `security-agent-toolkit` 5개 모듈 전체 구조 확인 / 캡스톤 4대 주제와 모듈 매핑 / 캡스톤 착수 가이드

**강의2** `run_soar_pipeline()` 오케스트레이션 / 4과목 파이프라인과의 종단간 연결 / 전체 코드 리뷰 체크리스트 / `agent_core/tool_router.py` 최종 연동

**실습** 1~4일차 모듈을 하나의 플레이북 엔진으로 통합하고 4과목 출력과 종단간 테스트를 수행한 뒤, 탐지-대응 전체 파이프라인을 팀별로 최종 시연 발표

---

# P3 — 캡스톤 운영 (10일)

> ⚠️ 이 과목은 `02-source/`에 상세교안 원본이 없습니다. 아래는 `course-info.md` 요약 기준이며, 원본 확보 후 위와 같은 형식으로 Day별로 채웁니다.

팀별 보안 봇 제작 코칭, 코드 리뷰, 발표 지도. 1~5과목에서 `security-agent-toolkit/`에 누적한 모듈(`agent_core`, `network_zt`, `access_control`, `anomaly_detection`, `soar_response`)을 팀 프로젝트로 통합.
