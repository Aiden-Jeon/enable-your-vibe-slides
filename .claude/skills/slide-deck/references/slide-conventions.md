# 슬라이드 스타일 가이드

## 테마
- **배경색**: `#1a1a2e` (다크 네이비)
- **텍스트**: `#eee` (밝은 회색)
- **강조색**: `#e94560` (코랄 레드)
- **보조색**: `#0f3460` (딥 블루), `#16213e` (다크 블루)
- **코드 테마**: monokai

## 폰트
- 제목: 시스템 산세리프 (한글 우선)
- 본문: 시스템 산세리프
- 코드: monospace

## 레이아웃 원칙
1. **1슬라이드 1메시지**: 각 슬라이드는 하나의 핵심 메시지만 전달
2. **텍스트 최소화**: 불릿 포인트 3-5개 이하
3. **코드는 핵심만**: 전체 코드가 아닌 핵심 부분만 표시
4. **시각적 계층**: 제목(h2) → 부제(h3) → 본문(p/ul)
5. **여백 충분히**: 슬라이드가 빽빽하지 않게

## 슬라이드 유형별 패턴

### 타이틀 슬라이드
```html
<section>
    <h1>섹션 제목</h1>
    <p>부제 또는 한줄 설명</p>
</section>
```

### 개념 설명 슬라이드
```html
<section>
    <h2>개념 이름</h2>
    <ul>
        <li>핵심 포인트 1</li>
        <li>핵심 포인트 2</li>
        <li>핵심 포인트 3</li>
    </ul>
    <aside class="notes">스피커 노트: 부연 설명</aside>
</section>
```

### 코드 슬라이드
```html
<section>
    <h2>코드 제목</h2>
    <pre><code class="language-python" data-trim>
def example():
    return "hello"
    </code></pre>
    <aside class="notes">코드 설명</aside>
</section>
```

### 비교 슬라이드 (2컬럼)
```html
<section>
    <h2>비교 제목</h2>
    <div style="display: flex; gap: 2rem;">
        <div style="flex: 1;">
            <h3>Before</h3>
            <p>설명</p>
        </div>
        <div style="flex: 1;">
            <h3>After</h3>
            <p>설명</p>
        </div>
    </div>
</section>
```

### 아키텍처 다이어그램 슬라이드
```html
<section>
    <h2>아키텍처</h2>
    <div style="font-family: monospace; text-align: center; font-size: 0.8em;">
        <!-- ASCII 또는 박스 기반 다이어그램 -->
    </div>
    <aside class="notes">다이어그램 설명</aside>
</section>
```

## 스피커 노트 가이드
- 모든 슬라이드에 `<aside class="notes">` 포함
- 슬라이드 내용을 보충하는 설명
- 데모 시 수행할 단계 기록
- 예상 질문과 답변 메모

## 코드 하이라이팅
- `data-trim` 속성으로 불필요한 공백 제거
- `data-line-numbers` 속성으로 라인 번호 표시 (선택)
- `data-line-numbers="3-5"` 형태로 특정 라인 강조 가능
- 지원 언어: python, bash, yaml, json, html, javascript
