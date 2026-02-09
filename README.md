# Enable Your Vibe - Vibe Coding 핸즈온 세션

> Vibe Coding으로 Vibe Coding을 가르치는 핸즈온 교육 자료

## 개요

사내 데이터 엔지니어/사이언티스트를 대상으로 한 **Vibe Coding 핸즈온 세션**(반나절, 3-4시간)입니다. 이 교육 자료 자체도 Vibe Coding으로 제작되어, "Vibe Coding으로 Vibe Coding을 가르치는" 경험을 제공합니다.

### 학습 목표

- Claude AI와 Claude Code의 핵심 기능 이해
- MCP(Model Context Protocol)로 AI 도구 확장하기
- Databricks Genie MCP 서버를 직접 구현하기
- Skills/Agents를 활용한 워크플로우 자동화
- FastAPI로 채팅 UI를 만들고 Databricks Apps로 배포하기

### 대상

- Python과 Databricks에 익숙한 데이터 엔지니어 / 데이터 사이언티스트
- AI 코딩 도구에 관심 있는 개발자

## 사전 준비

| 항목 | 설명 |
|------|------|
| Python 3.11+ | `python --version`으로 확인 |
| [uv](https://docs.astral.sh/uv/) | Python 패키지 매니저 (`curl -LsSf https://astral.sh/uv/install.sh \| sh`) |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Anthropic CLI (`npm install -g @anthropic-ai/claude-code`) |
| Databricks CLI | `pip install databricks-cli` 또는 `brew install databricks` |
| Databricks 워크스페이스 | 접근 권한 + Personal Access Token |
| Genie Space | 사전 생성된 Genie Space ID 필요 (섹션 05~09) |

## 환경 설정

```bash
# 1. 프로젝트 클론
git clone <repo-url>
cd enable-your-vibe

# 2. 의존성 설치
uv sync

# 3. 환경변수 설정 (실습 섹션용)
cp sections/05-genie-mcp/code/.env.example sections/05-genie-mcp/code/.env
# .env 파일에 DATABRICKS_HOST, DATABRICKS_TOKEN, GENIE_SPACE_ID 입력
```

## 커리큘럼 (총 190분)

### Part 1: 기초 다지기 (75분)

| # | 섹션 | 시간 | 유형 | 설명 |
|---|------|------|------|------|
| 01 | [AI Foundation](sections/01-ai-foundation/) | 15분 | 강의 | Vibe Coding 개념, Claude AI 차별점, 에이전틱 코딩 |
| 02 | [Claude Code Features](sections/02-claude-code-features/) | 20분 | 강의+데모 | CLI 사용법, CLAUDE.md, 핵심 기능 4가지 |
| 03 | [MCP Architecture](sections/03-mcp-architecture/) | 25분 | 강의+실습 | MCP 프로토콜, FastMCP로 첫 MCP 서버 만들기 |
| 04 | [Skills Ecosystem](sections/04-skills-ecosystem/) | 15분 | 강의 | Skills, Agents, Hooks 생태계 이해 |

### Part 2: 실전 구현 (115분)

| # | 섹션 | 시간 | 유형 | 설명 |
|---|------|------|------|------|
| 05 | [Genie MCP](sections/05-genie-mcp/) | 30분 | 실습 | Databricks Genie API → MCP 서버 구현 |
| 06 | [Skills Workflow](sections/06-skills-workflow/) | 25분 | 실습 | Custom Skill 작성, 레퍼런스 활용 |
| 07 | [AI Dev Kit](sections/07-ai-dev-kit/) | 15분 | 강의+데모 | ChatAgent, MLflow Tracing, 배포 파이프라인 |
| 08 | [Build UI](sections/08-build-ui/) | 30분 | 실습 | FastAPI + 채팅 UI 구현 |
| 09 | [Deploy to Databricks](sections/09-deploy-to-databricks/) | 15분 | 실습 | Databricks Apps 배포 |

### 학습 경로

```
Part 1: 기초                          Part 2: 실전
┌──────────────┐                     ┌──────────────────┐
│ 01 AI 기초    │──→ 02 Claude Code ──→ 03 MCP 아키텍처 ──→ 05 Genie MCP ──→ 08 UI 만들기 ──→ 09 배포
└──────────────┘                     └────────┬─────────┘
                                              │
                                              └──→ 04 Skills ──→ 06 Skills 실습
                                              │
                                              └──→ 07 AI Dev Kit
```

## 슬라이드 보기

```bash
# 방법 1: 로컬 서버로 전체 슬라이드 서빙
python shared/scripts/serve-slides.py
# → http://localhost:8000 에서 확인

# 방법 2: 마스터 인덱스 페이지 열기
open index.html
# → 전체 섹션 네비게이션

# 방법 3: 개별 섹션 슬라이드 직접 열기
open sections/01-ai-foundation/slides/index.html
```

## 검증

```bash
# 전체 섹션 구조 검증
python shared/scripts/validate-section.py

# 특정 섹션만 검증
python shared/scripts/validate-section.py sections/05-genie-mcp
```

## 프로젝트 구조

```
enable-your-vibe/
├── index.html                 # 마스터 인덱스 (전체 섹션 네비게이션)
├── sections/
│   ├── 01-ai-foundation/      # 강의: Claude AI 기초
│   ├── 02-claude-code-features/ # 강의+데모: Claude Code 사용법
│   ├── 03-mcp-architecture/   # 강의+실습: MCP 아키텍처
│   ├── 04-skills-ecosystem/   # 강의: Skills 생태계
│   ├── 05-genie-mcp/          # 실습: Genie MCP 서버
│   ├── 06-skills-workflow/    # 실습: Skills 워크플로우
│   ├── 07-ai-dev-kit/         # 강의+데모: AI Dev Kit
│   ├── 08-build-ui/           # 실습: UI 만들기
│   └── 09-deploy-to-databricks/ # 실습: Databricks 배포
├── shared/
│   ├── assets/theme.css       # 커스텀 reveal.js 테마
│   └── scripts/
│       ├── serve-slides.py    # 슬라이드 프리뷰 서버
│       └── validate-section.py # 섹션 구조 검증
├── .claude/
│   ├── CLAUDE.md              # 프로젝트 컨벤션 가이드
│   ├── skills/                # Claude Code Skills (3개)
│   └── agents/                # Claude Code Agents (2개)
└── pyproject.toml             # 프로젝트 설정 & 의존성
```

## 기술 스택

| 영역 | 기술 |
|------|------|
| 슬라이드 | reveal.js 5.x (CDN, 빌드 불필요) |
| 코드 | Python 3.11+, uv |
| MCP 서버 | FastMCP |
| 웹 UI | FastAPI + HTML/CSS/JS |
| 배포 | Databricks Apps |
| AI 에이전트 | databricks-agents, MLflow |

## 라이선스

Internal Use Only
