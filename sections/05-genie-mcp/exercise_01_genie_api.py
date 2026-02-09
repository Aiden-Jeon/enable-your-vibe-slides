"""
Exercise 01: Genie API 직접 호출
Databricks Genie API를 직접 호출하여 자연어 질의를 수행합니다.

실행: python exercise_01_genie_api.py
"""
import os
import time

import httpx
from dotenv import load_dotenv

load_dotenv()

DATABRICKS_HOST = os.getenv("DATABRICKS_HOST", "")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN", "")
GENIE_SPACE_ID = os.getenv("GENIE_SPACE_ID", "")

if not all([DATABRICKS_HOST, DATABRICKS_TOKEN, GENIE_SPACE_ID]):
    print("⚠️  .env 파일에 필요한 환경변수를 설정해주세요.")
    print("   cp .env.example .env 후 값을 입력하세요.")
    exit(1)

# 💡 학습 포인트: Databricks API 인증은 Bearer 토큰 방식
headers = {
    "Authorization": f"Bearer {DATABRICKS_TOKEN}",
    "Content-Type": "application/json",
}
base_url = f"{DATABRICKS_HOST}/api/2.0/genie/spaces/{GENIE_SPACE_ID}"


def create_conversation() -> str:
    """새 Genie 대화를 생성합니다."""
    resp = httpx.post(f"{base_url}/conversations", headers=headers)
    resp.raise_for_status()
    return resp.json()["conversation_id"]


def send_message(conversation_id: str, question: str) -> dict:
    """Genie에 자연어 질문을 보냅니다."""
    resp = httpx.post(
        f"{base_url}/conversations/{conversation_id}/messages",
        headers=headers,
        json={"content": question},
    )
    resp.raise_for_status()
    return resp.json()


def poll_result(conversation_id: str, message_id: str, max_wait: int = 60) -> dict:
    """결과가 준비될 때까지 폴링합니다."""
    url = f"{base_url}/conversations/{conversation_id}/messages/{message_id}"
    for _ in range(max_wait // 2):
        resp = httpx.get(url, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        status = data.get("status", "")
        if status == "COMPLETED":
            return data
        if status in ("FAILED", "CANCELLED"):
            raise RuntimeError(f"Genie 질의 실패: {status}")
        print(f"  ⏳ 상태: {status}, 대기 중...")
        time.sleep(2)
    raise TimeoutError("Genie 응답 시간 초과")


def main():
    print("🧞 Genie API 직접 호출 예제")
    print("=" * 50)

    # Step 1: 대화 생성
    print("\n1️⃣ 대화 생성 중...")
    conversation_id = create_conversation()
    print(f"   대화 ID: {conversation_id}")

    # Step 2: 질문 전송
    question = "총 매출액을 알려주세요"
    print(f"\n2️⃣ 질문 전송: '{question}'")
    result = send_message(conversation_id, question)
    message_id = result["message_id"]
    print(f"   메시지 ID: {message_id}")

    # Step 3: 결과 폴링
    print("\n3️⃣ 결과 대기 중...")
    final = poll_result(conversation_id, message_id)
    print(f"\n✅ 결과:")
    print(f"   {final}")


if __name__ == "__main__":
    main()
