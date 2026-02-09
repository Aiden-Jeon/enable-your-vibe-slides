# Enable Your Vibe - 프로젝트 가이드

## 프로젝트 개요
Vibe Coding 핸즈온 세션(반나절, 3-4시간) 교육 자료. 대상: 데이터 엔지니어/사이언티스트.

## 프로젝트 구조

```
enable-your-vibe/
├── sections/                    # 9개 교육 섹션
│   └── XX-section-name/
│       ├── index.html           # reveal.js 슬라이드
│       ├── exercise_XX_xxx.py   # 실습 코드 (해당 시)
│       ├── README.md            # 코드 가이드 (해당 시)
│       └── section.yaml         # 섹션 메타데이터
├── shared/
│   ├── assets/theme.css         # 커스텀 reveal.js 테마
│   └── scripts/                 # 유틸리티 스크립트 (sidebar.js 포함)
└── .claude/
    ├── skills/                  # 3개 스킬 (slide-deck, hands-on-code, section-builder)
    └── agents/                  # 2개 에이전트 (researcher, validator)
```

## 섹션 목록

| # | 디렉토리명 | 제목 | 유형 |
|---|-----------|------|------|
| 01 | ai-foundation | Claude AI 기초 | 강의 |
| 02 | claude-code-features | Claude Code 사용법 | 강의+데모 |
| 03 | mcp-architecture | MCP 아키텍처 | 강의+실습 |
| 04 | skills-ecosystem | Skills 생태계 | 강의 |
| 05 | genie-mcp | Genie MCP 서버 만들기 | 실습 |
| 06 | skills-workflow | Skills로 워크플로우 구조화 | 실습 |
| 07 | ai-dev-kit | Databricks AI Dev Kit | 강의+데모 |
| 08 | build-ui | UI 만들기 | 실습 |
| 09 | deploy-to-databricks | Databricks 배포 | 실습 |

## 컨벤션

### 언어
- 슬라이드/문서 본문: **한국어**
- 코드/기술용어/변수명: **영어**

### 슬라이드
- reveal.js 5.x CDN 기반 단일 HTML
- 다크 테마: 배경 `#1a1a2e`, 강조 `#e94560`, 코드 monokai
- 한 슬라이드에 1개 핵심 메시지
- 코드 블록은 highlight.js로 하이라이팅
- 스피커 노트 필수 포함

### 코드
- Python 3.11+, uv로 의존성 관리
- `.env.example` 패턴으로 환경변수 관리
- 각 실습 파일은 독립 실행 가능해야 함
- 파일명: `exercise_XX_description.py`

### 섹션 메타데이터 (section.yaml)
```yaml
number: "01"
title: "섹션 제목"
duration_minutes: 15
type: "lecture" | "lecture+demo" | "hands-on"
objectives:
  - "학습 목표 1"
  - "학습 목표 2"
slides: "index.html"
code_files:
  - "exercise_01_xxx.py"
```

## 기술 스택
- **슬라이드**: reveal.js 5.x (CDN)
- **코드**: Python 3.11+, uv
- **MCP**: FastMCP 프레임워크
- **UI**: FastAPI + 정적 HTML/CSS/JS
- **배포**: Databricks Apps (app.yaml + databricks CLI)
