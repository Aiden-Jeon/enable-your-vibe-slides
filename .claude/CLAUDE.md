# Enable Your Vibe - 프로젝트 가이드

## 프로젝트 개요
Vibe Coding 핸즈온 세션(반나절, 3-4시간) 교육 자료 — 슬라이드 전용 레포. 대상: 데이터 엔지니어/사이언티스트.

실습 코드는 별도 레포([enable-your-vibe-code](https://github.com/aiden-jeon/enable-your-vibe-code))에서 관리.

## 프로젝트 구조

```
enable-your-vibe/
├── sections/                    # 8개 교육 섹션 (00-home + 01-08)
│   └── XX-section-name/
│       ├── index.html           # reveal.js 슬라이드
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
| 04 | genie-mcp | Genie MCP 서버 만들기 | 실습 |
| 05 | skills | Skills: 개념에서 실전까지 | 강의+실습 |
| 06 | agents | Custom Agents: 나만의 에이전트 만들기 | 강의+실습 |
| 07 | hooks | Hooks: 이벤트 기반 자동화 | 강의+실습 |
| 08 | ai-dev-kit | Databricks AI Dev Kit | 강의+데모 |

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
```

## 기술 스택
- **슬라이드**: reveal.js 5.x (CDN)
- **배포**: Databricks Apps (app.yaml + databricks CLI)
