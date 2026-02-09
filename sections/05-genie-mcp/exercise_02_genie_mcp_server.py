"""
Exercise 02: Genie MCP 서버
Databricks Genie를 MCP 서버로 래핑하여 Claude Code에서 사용할 수 있게 합니다.

실행: python exercise_02_genie_mcp_server.py
"""
import os
import time

import httpx
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()

DATABRICKS_HOST = os.getenv("DATABRICKS_HOST", "")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN", "")
GENIE_SPACE_ID = os.getenv("GENIE_SPACE_ID", "")

if not all([DATABRICKS_HOST, DATABRICKS_TOKEN, GENIE_SPACE_ID]):
    print("⚠️  .env 파일에 필요한 환경변수를 설정해주세요.")
    exit(1)

mcp = FastMCP("Genie MCP")

headers = {
    "Authorization": f"Bearer {DATABRICKS_TOKEN}",
    "Content-Type": "application/json",
}
base_url = f"{DATABRICKS_HOST}/api/2.0/genie/spaces/{GENIE_SPACE_ID}"


def _create_conversation() -> str:
    resp = httpx.post(f"{base_url}/conversations", headers=headers)
    resp.raise_for_status()
    return resp.json()["conversation_id"]


def _send_and_poll(conversation_id: str, question: str, max_wait: int = 60) -> dict:
    resp = httpx.post(
        f"{base_url}/conversations/{conversation_id}/messages",
        headers=headers,
        json={"content": question},
    )
    resp.raise_for_status()
    message_id = resp.json()["message_id"]

    url = f"{base_url}/conversations/{conversation_id}/messages/{message_id}"
    for _ in range(max_wait // 2):
        resp = httpx.get(url, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        status = data.get("status", "")
        if status == "COMPLETED":
            return data
        if status in ("FAILED", "CANCELLED"):
            return {"error": f"질의 실패: {status}"}
        time.sleep(2)
    return {"error": "응답 시간 초과"}


# 💡 학습 포인트: MCP tool로 Genie API를 래핑
@mcp.tool()
def ask_genie(question: str) -> str:
    """Databricks Genie에 자연어로 데이터를 질의합니다.

    Args:
        question: 데이터에 대한 자연어 질문 (예: '이번 달 매출은?')

    Returns:
        Genie의 응답 결과
    """
    conversation_id = _create_conversation()
    result = _send_and_poll(conversation_id, question)

    if "error" in result:
        return f"❌ {result['error']}"

    # 결과에서 텍스트 응답 추출
    attachments = result.get("attachments", [])
    text_parts = []

    for attachment in attachments:
        if "text" in attachment:
            text_parts.append(attachment["text"].get("content", ""))
        if "query" in attachment:
            text_parts.append(f"SQL: {attachment['query'].get('query', '')}")

    return "\n".join(text_parts) if text_parts else str(result)


@mcp.tool()
def get_genie_space_info() -> str:
    """현재 설정된 Genie Space 정보를 반환합니다."""
    return f"Host: {DATABRICKS_HOST}\nSpace ID: {GENIE_SPACE_ID}"


if __name__ == "__main__":
    mcp.run()
