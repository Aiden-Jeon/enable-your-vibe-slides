# 9개 섹션 마스터 스펙

## Section 01: AI Foundation - Claude AI 기초
- **시간**: 15분 | **유형**: 강의
- **목표**: AI 코딩 어시스턴트의 개념과 Claude의 특징 이해
- **내용**:
  - Vibe Coding이란? (Andrej Karpathy 인용)
  - AI 코딩 도구의 발전: Copilot → Cursor → Claude Code
  - Claude의 차별점: 긴 컨텍스트, 에이전틱 코딩
  - 핸즈온 세션 전체 로드맵 소개
- **코드**: 없음 (강의 전용)

## Section 02: Claude Code Features - Claude Code 사용법
- **시간**: 20분 | **유형**: 강의+데모
- **목표**: Claude Code CLI의 핵심 기능 숙지
- **내용**:
  - 설치 및 초기 설정
  - 기본 대화: 질문, 코드 생성, 리팩토링
  - CLAUDE.md의 역할과 작성법
  - 컨텍스트 관리: 파일 참조, @mentions
  - 실용 팁: /help, /clear, /compact
- **코드**: 데모용 간단한 예제 (선택)

## Section 03: MCP Architecture - MCP 아키텍처
- **시간**: 25분 | **유형**: 강의+실습
- **목표**: MCP(Model Context Protocol)의 개념과 구조 이해, 간단한 MCP 서버 작성
- **내용**:
  - MCP란? 왜 필요한가?
  - MCP 아키텍처: Host → Client → Server
  - Tool, Resource, Prompt의 세 가지 프리미티브
  - FastMCP로 간단한 서버 만들기
  - Claude Code에서 MCP 서버 연결하기
- **코드**:
  - `exercise_01_hello_mcp.py`: 기본 MCP 서버 (echo tool)
  - `exercise_02_calculator_mcp.py`: 계산기 MCP 서버

## Section 04: Skills Ecosystem - Skills 생태계
- **시간**: 15분 | **유형**: 강의
- **목표**: Claude Code Skills, Agents의 개념과 활용법 이해
- **내용**:
  - Skills란? (SKILL.md 구조)
  - Custom Slash Commands
  - Agents 설정 (agents/ 디렉토리)
  - 이 프로젝트에서 사용하는 Skills/Agents 소개
  - Skills 생태계의 가능성
- **코드**: 없음 (강의 전용)

## Section 05: Genie MCP - Genie MCP 서버 만들기
- **시간**: 30분 | **유형**: 실습
- **목표**: Databricks Genie API를 활용한 MCP 서버 직접 구현
- **내용**:
  - Databricks Genie Space 소개
  - Genie API 구조 이해
  - FastMCP로 Genie MCP 서버 구현
  - 자연어 → SQL → 결과 파이프라인
  - Claude Code에서 Genie MCP 활용
- **코드**:
  - `exercise_01_genie_api.py`: Genie API 직접 호출
  - `exercise_02_genie_mcp_server.py`: Genie MCP 서버 구현
  - `.env.example`: DATABRICKS_HOST, DATABRICKS_TOKEN, GENIE_SPACE_ID

## Section 06: Custom Agents - 나만의 에이전트 만들기
- **시간**: 25분 | **유형**: 강의+실습
- **목표**: Custom Agent 개념과 agent.md 구조 이해, 직접 Agent 만들기
- **내용**:
  - Custom Agents란? (@호출, agent.md)
  - agent.md 구조 (역할/제약 조건/출력 형식)
  - 실제 예시: researcher, validator 에이전트
  - Skills vs Agents 비교
  - Agent 설계 원칙
- **코드**:
  - `exercise_01_simple_agent/`: 간단한 Agent 예제
  - `exercise_02_project_agent/`: 프로젝트용 Agent 예제

## Section 07: Hooks - 이벤트 기반 자동화
- **시간**: 25분 | **유형**: 강의+실습
- **목표**: Hooks 개념과 이벤트 트리거 방식 이해, Hook 설정 실습
- **내용**:
  - Hooks란? (이벤트 기반 자동 실행)
  - Hook 이벤트 타입 (PreToolUse/PostToolUse/Notification/Stop)
  - Hook 설정 구조 (settings.json)
  - 설정 파일 위치와 우선순위
  - 실전 예시: Auto-format, 안전 가드레일
  - Skills + Agents + Hooks 통합
- **코드**:
  - `.claude/settings.json` 예제

## Section 08: Skills Workflow - Skills로 워크플로우 구조화
- **시간**: 25분 | **유형**: 실습
- **목표**: Custom Skills를 만들어 반복 작업을 자동화하는 방법 학습
- **내용**:
  - Skill 설계 원칙
  - SKILL.md 작성법 (입력/처리/출력)
  - 레퍼런스 파일 활용
  - 실제 Skill 만들기 실습
  - Skill 체이닝 패턴
- **코드**:
  - `exercise_01_simple_skill/`: 간단한 Skill 예제 (디렉토리)
  - `exercise_02_skill_with_refs/`: 레퍼런스 활용 Skill 예제

## Section 09: AI Dev Kit - Databricks AI Dev Kit
- **시간**: 30분 | **유형**: 강의+데모
- **목표**: Databricks AI Dev Kit의 5대 구성 요소, MCP 서버, Skills, ChatAgent 인터페이스 이해
- **내용**:
  - AI Dev Kit 전체 그림 (5대 구성 요소)
  - 5대 구성 요소 상세: tools-core, mcp-server, skills, builder-app, ai-dev-project
  - databricks-mcp 서버 아키텍처 (Claude Code → FastMCP → tools-core → SDK)
  - 50+ 도구 카테고리 (SQL, Compute, Jobs, Files, Serving, Pipelines, Genie 등)
  - databricks-skills: 6개 카테고리, 25+ 스킬
  - Skills + MCP Tools 통합: 지식(Skills) + 실행(MCP Tools)
  - 설치 방법: 원라인 설치, 스타터 킷, Skills만 설치
  - databricks-agents 프레임워크의 ChatAgent 인터페이스
  - MLflow Tracing 연동 (데코레이터, autolog, 트레이스 UI)
  - 로컬 개발 → Databricks 배포 워크플로우
  - 워크숍 학습 내용과 AI Dev Kit 매핑
- **코드**: 데모용 ChatAgent 예제 (선택)
