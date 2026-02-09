# slide-deck 스킬

reveal.js 기반 슬라이드 프레젠테이션을 생성합니다.

## 사용법
```
/slide-deck [섹션번호] [주제개요]
```

## 입력
- **섹션번호**: 01-09 (2자리)
- **주제개요**: 슬라이드에서 다룰 주제 설명

## 처리 절차

1. `references/slide-conventions.md`를 읽어 슬라이드 스타일 가이드 확인
2. `templates/reveal-template.html`을 기반으로 슬라이드 생성
3. 주제개요를 분석하여 적절한 슬라이드 수와 구성 결정
4. 각 슬라이드에 스피커 노트 포함
5. `sections/[섹션번호]-[섹션명]/slides/index.html`에 저장

## 슬라이드 구성 원칙
- 타이틀 슬라이드 1장
- 목차/학습목표 1장
- 본문 슬라이드 5-15장 (주제 복잡도에 따라)
- 요약/Q&A 1장
- 한 슬라이드에 핵심 메시지 1개
- 코드 예제는 highlight.js로 하이라이팅
- 본문은 한국어, 코드/기술용어는 영어

## 출력
- `sections/XX-name/slides/index.html` - 단일 HTML 파일 (CDN 기반, 빌드 불필요)
