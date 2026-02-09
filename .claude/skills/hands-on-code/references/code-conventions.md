# 코드 컨벤션

## 파일 구조
```
sections/XX-name/code/
├── exercise_01_description.py    # 실습 파일 (순서대로)
├── exercise_02_description.py
├── .env.example                  # 환경변수 템플릿
└── README.md                     # 실행 가이드
```

## 파일 명명 규칙
- `exercise_XX_description.py` (XX: 2자리 순번)
- 설명은 snake_case, 영어
- 예: `exercise_01_basic_prompt.py`, `exercise_02_mcp_server.py`

## Python 코드 스타일

### 파일 헤더
```python
"""
Exercise XX: 제목 (한국어)
설명 (한국어)

실행: python exercise_XX_description.py
"""
```

### 임포트 순서
1. 표준 라이브러리
2. 서드파티 라이브러리
3. 로컬 모듈

### 환경변수 패턴
```python
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "")
if not API_KEY:
    print("⚠️  .env 파일에 API_KEY를 설정해주세요.")
    print("   cp .env.example .env 후 값을 입력하세요.")
    exit(1)
```

### 학습 포인트 주석
```python
# 💡 학습 포인트: 여기서 핵심 개념을 설명합니다
result = important_function()

# ✅ 실습: 아래 코드를 수정해보세요
# TODO: 여기에 코드를 작성하세요
```

### main 함수 패턴
```python
def main():
    """메인 실행 함수"""
    # 실습 코드

if __name__ == "__main__":
    main()
```

## .env.example 형식
```
# Section XX: 섹션 제목
# 아래 값들을 실제 값으로 변경해주세요

API_KEY=your-api-key-here
DATABRICKS_HOST=https://your-workspace.cloud.databricks.com
DATABRICKS_TOKEN=your-token-here
```

## README.md 구조
```markdown
# Section XX: 섹션 제목

## 학습 목표
- 목표 1
- 목표 2

## 사전 준비
- 필요한 것들

## 실습 파일

### exercise_01_xxx.py - 제목
설명

### exercise_02_xxx.py - 제목
설명

## 실행 방법
\```bash
# 환경 설정
cp .env.example .env
# .env 파일을 열어 실제 값을 입력

# 실행
python exercise_01_xxx.py
\```
```

## 코드 난이도 단계
1. **기본**: 실행만 하면 되는 완성된 코드
2. **가이드**: TODO 주석이 있는 부분만 채우면 되는 코드
3. **도전**: 힌트만 있고 직접 구현해야 하는 코드
