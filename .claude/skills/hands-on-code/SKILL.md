# hands-on-code 스킬

각 섹션의 실행 가능한 핸즈온 코드 예제와 README를 생성합니다.

## 사용법
```
/hands-on-code [섹션번호] [코드설명]
```

## 입력
- **섹션번호**: 01-09 (2자리)
- **코드설명**: 만들 코드의 목적과 기능 설명

## 처리 절차

1. `references/code-conventions.md`를 읽어 코드 컨벤션 확인
2. 섹션 유형(강의/데모/실습)에 맞는 코드 구성 결정
3. 실행 가능한 Python 파일 생성
4. `.env.example` 파일 생성 (환경변수 필요 시)
5. `README.md` 작성 (실행 방법, 학습 포인트)
6. `sections/[섹션번호]-[섹션명]/code/`에 저장

## 코드 구성 원칙
- 각 파일은 독립 실행 가능
- 단계별로 난이도 증가
- 주석으로 학습 포인트 표시
- 에러 처리 포함
- `.env.example` 패턴으로 시크릿 관리

## 출력
- `sections/XX-name/code/exercise_XX_description.py` - 실습 코드
- `sections/XX-name/code/.env.example` - 환경변수 템플릿 (필요 시)
- `sections/XX-name/code/README.md` - 실행 가이드
