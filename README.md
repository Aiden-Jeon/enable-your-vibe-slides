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

## 실습 코드

실습 코드는 별도 레포에서 관리됩니다:

**[enable-your-vibe-code](https://github.com/aiden-jeon/enable-your-vibe-code)** — 클론 후 `uv sync`로 환경을 설정하세요.

## 커리큘럼 (총 240분)

### Part 1: 기초 다지기 (70분)

| # | 섹션 | 시간 | 유형 | 설명 |
|---|------|------|------|------|
| 01 | [AI Foundation](sections/01-ai-foundation/) | 15분 | 강의 | Vibe Coding 개념, Claude AI 차별점, 에이전틱 코딩 |
| 02 | [Claude Code Features](sections/02-claude-code-features/) | 20분 | 강의+데모 | CLI 사용법, CLAUDE.md, 핵심 기능 4가지 |
| 03 | [MCP Architecture](sections/03-mcp-architecture/) | 25분 | 강의+실습 | MCP 프로토콜, FastMCP로 첫 MCP 서버 만들기 |

### Part 2: 실전 구현 (170분)

| # | 섹션 | 시간 | 유형 | 설명 |
|---|------|------|------|------|
| 04 | [Genie MCP](sections/04-genie-mcp/) | 30분 | 실습 | Databricks Genie API → MCP 서버 구현 |
| 05 | [Skills](sections/05-skills/) | 30분 | 강의+실습 | Skills/Agents 개념, Custom Skill 작성, 레퍼런스 활용 |
| 06 | [Custom Agents](sections/06-agents/) | 25분 | 강의+실습 | agent.md 구조, Skills vs Agents, 에이전트 만들기 |
| 07 | [Hooks](sections/07-hooks/) | 25분 | 강의+실습 | 이벤트 기반 자동화, 안전 가드레일, Auto-format |
| 08 | [AI Dev Kit](sections/08-ai-dev-kit/) | 15분 | 강의+데모 | ChatAgent, MLflow Tracing, 배포 파이프라인 |
| 09 | [Build UI](sections/09-build-ui/) | 30분 | 실습 | FastAPI + 채팅 UI 구현 |
| 10 | [Deploy to Databricks](sections/10-deploy-to-databricks/) | 15분 | 실습 | Databricks Apps 배포 |

### 학습 경로

```
Part 1: 기초                               Part 2: 실전
┌──────────────┐                          ┌──────────────────┐
│ 01 AI 기초    │──→ 02 Claude Code ──→ 03 MCP 아키텍처 ──→ 04 Genie MCP
└──────────────┘                          └──────────────────┘
                                                   │
                                          05 Skills ──→ 06 Agents ──→ 07 Hooks
                                                   │
                                          08 AI Dev Kit ──→ 09 UI 만들기 ──→ 10 배포
```

## 슬라이드 보기

```bash
# 방법 1: 로컬 서버로 전체 슬라이드 서빙
uv run --with pyyaml shared/scripts/serve-slides.py
# → http://localhost:8000 에서 확인

# 방법 2: 마스터 인덱스 페이지 열기
open index.html
# → 전체 섹션 네비게이션

# 방법 3: 개별 섹션 슬라이드 직접 열기
open sections/01-ai-foundation/index.html
```

## 검증

```bash
# 전체 섹션 구조 검증
uv run --with pyyaml shared/scripts/validate-section.py

# 특정 섹션만 검증
uv run --with pyyaml shared/scripts/validate-section.py sections/04-genie-mcp
```

## 프로젝트 구조

```
enable-your-vibe/
├── index.html                 # 마스터 인덱스 (전체 섹션 네비게이션)
├── sections/
│   ├── 01-ai-foundation/      # 강의: Claude AI 기초
│   ├── 02-claude-code-features/ # 강의+데모: Claude Code 사용법
│   ├── 03-mcp-architecture/   # 강의+실습: MCP 아키텍처
│   ├── 04-genie-mcp/          # 실습: Genie MCP 서버
│   ├── 05-skills/             # 강의+실습: Skills 개념에서 실전까지
│   ├── 06-agents/             # 강의+실습: Custom Agents
│   ├── 07-hooks/              # 강의+실습: Hooks 이벤트 기반 자동화
│   ├── 08-ai-dev-kit/         # 강의+데모: AI Dev Kit
│   ├── 09-build-ui/           # 실습: UI 만들기
│   └── 10-deploy-to-databricks/ # 실습: Databricks 배포
├── shared/
│   ├── assets/theme.css       # 커스텀 reveal.js 테마
│   └── scripts/
│       ├── serve-slides.py    # 슬라이드 프리뷰 서버
│       └── validate-section.py # 섹션 구조 검증
└── .claude/
    ├── CLAUDE.md              # 프로젝트 컨벤션 가이드
    ├── skills/                # Claude Code Skills (3개)
    └── agents/                # Claude Code Agents (2개)
```

## 기술 스택

| 영역 | 기술 |
|------|------|
| 슬라이드 | reveal.js 5.x (CDN, 빌드 불필요) |
| 배포 | Databricks Apps |
| AI 에이전트 | databricks-agents, MLflow |

## 라이선스

Internal Use Only
