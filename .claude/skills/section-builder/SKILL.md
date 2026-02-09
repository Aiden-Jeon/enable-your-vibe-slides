# section-builder 스킬

slide-deck + hands-on-code를 연결하여 완전한 섹션을 빌드합니다.

## 사용법
```
/section-builder [섹션번호] [섹션제목]
```

## 입력
- **섹션번호**: 01-09 (2자리)
- **섹션제목**: 섹션의 한국어 제목

## 처리 절차

1. `references/section-spec.md`에서 해당 섹션의 상세 스펙 확인
2. 슬라이드 생성 (slide-deck 스킬의 컨벤션 따름)
3. 핸즈온 코드 생성 (hands-on-code 스킬의 컨벤션 따름)
4. `section.yaml` 메타데이터 생성
5. 슬라이드와 코드 간 교차 참조 확인
   - 슬라이드에서 언급하는 코드가 실제로 존재하는지
   - 코드 파일이 슬라이드에서 참조되는지

## 출력 구조
```
sections/XX-name/
├── index.html              # reveal.js 슬라이드
├── exercise_XX_xxx.py      # 실습 코드
├── .env.example            # 환경변수 (필요 시)
├── README.md               # 코드 실행 가이드
└── section.yaml            # 섹션 메타데이터
```

## section.yaml 형식
```yaml
number: "XX"
title: "섹션 한국어 제목"
duration_minutes: 15
type: "lecture" | "lecture+demo" | "hands-on"
objectives:
  - "학습 목표 1"
  - "학습 목표 2"
  - "학습 목표 3"
slides: "index.html"
code_files:
  - "exercise_XX_xxx.py"
prerequisites:
  - "이전 섹션 또는 사전 지식"
```

## 교차 검증 체크리스트
- [ ] index.html 존재 여부
- [ ] 섹션 루트 내 실습 파일 존재 여부
- [ ] section.yaml의 code_files가 실제 파일과 일치
- [ ] 슬라이드 내 코드 예제가 실습 파일과 일관성 유지
- [ ] .env.example 필요 시 존재 여부
- [ ] README.md 존재 여부
