# Section 05: Genie MCP 서버 만들기

## 학습 목표

- Databricks Genie API의 구조와 호출 방법을 이해한다
- FastMCP로 Genie MCP 서버를 직접 구현한다
- Claude Code에서 Genie MCP를 연결하여 자연어 데이터 질의를 수행한다

## 사전 준비

### 필수 요구사항

1. **Databricks 워크스페이스** 접근 권한
2. **Genie Space** 생성 완료 (Databricks UI에서 생성)
3. **Personal Access Token** 발급 (Databricks Settings > Developer > Access Tokens)

### Python 패키지 설치

```bash
pip install httpx python-dotenv fastmcp
```

## 환경 설정

### 1. `.env` 파일 생성

```bash
cp .env.example .env
```

### 2. `.env` 파일 편집

```env
DATABRICKS_HOST=https://your-workspace.cloud.databricks.com
DATABRICKS_TOKEN=dapi_xxxxxxxxxxxxxxxx
GENIE_SPACE_ID=your-genie-space-id
```

- **DATABRICKS_HOST**: Databricks 워크스페이스 URL (끝에 `/` 없이)
- **DATABRICKS_TOKEN**: Personal Access Token
- **GENIE_SPACE_ID**: Genie Space의 ID (URL에서 확인 가능)

## 실습 파일

### Exercise 01: Genie API 직접 호출

Genie API의 3단계 호출(대화 생성 -> 메시지 전송 -> 결과 폴링)을 직접 체험합니다.

```bash
python exercise_01_genie_api.py
```

**학습 포인트:**
- Databricks API 인증 방식 (Bearer 토큰)
- Genie API의 비동기 처리 구조
- 폴링 패턴으로 결과 대기

### Exercise 02: Genie MCP 서버

Genie API를 FastMCP로 래핑한 MCP 서버입니다. Claude Code에서 직접 사용할 수 있습니다.

```bash
python exercise_02_genie_mcp_server.py
```

**학습 포인트:**
- FastMCP의 `@mcp.tool()` 데코레이터 활용
- REST API를 MCP tool로 래핑하는 패턴
- docstring이 Claude Code에 tool 설명으로 제공되는 구조

## Claude Code에서 MCP 서버 연결

### `.claude/settings.local.json` 설정

프로젝트 루트에 아래 파일을 생성하거나 수정합니다:

```json
{
  "mcpServers": {
    "genie": {
      "command": "python",
      "args": ["sections/05-genie-mcp/exercise_02_genie_mcp_server.py"],
      "cwd": "."
    }
  }
}
```

### 사용 방법

1. Claude Code를 재시작하거나 `/mcp` 명령으로 MCP 서버 상태를 확인합니다
2. `genie` 서버가 연결되었는지 확인합니다
3. 자연어로 데이터를 질의합니다:

```
사용자: "이번 달 매출 합계를 알려줘"
Claude: ask_genie tool을 호출하여 결과를 조회합니다...
```

## 학습 포인트 요약

| 개념 | 설명 |
|------|------|
| **Genie API 구조** | 대화 생성 -> 메시지 전송 -> 결과 폴링의 3단계 |
| **Bearer 인증** | Databricks Personal Access Token 사용 |
| **폴링 패턴** | 비동기 API 결과를 주기적으로 확인하여 동기적으로 처리 |
| **래핑 패턴** | 복잡한 REST API 호출을 단순한 MCP tool로 추상화 |
| **FastMCP** | Python 데코레이터 기반의 간편한 MCP 서버 구현 |
| **환경변수 관리** | dotenv로 민감한 인증 정보를 코드와 분리 |
