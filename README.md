# AI 코드 생성 시대의 GitHub 오픈소스 진화 분석

> **"ChatGPT와 Vibe Coding 이후, 개발자 생태계는 어떻게 변했는가?"**

---

## 프로젝트 개요

2022년 11월 ChatGPT 출시 이후 소프트웨어 개발 패러다임이 급격히 변화했습니다.  
본 연구는 AI 코드 생성 도구가 GitHub 오픈소스 생태계에 미친 영향을 정량적으로 분석합니다.

---

## 연구 질문

**RQ1.** ChatGPT 출시 전후(2021-2022 vs 2023-2025) GitHub AI 프로젝트는 어떻게 변화했는가?  
**RQ2.** "AI agent", "autonomous coding" 키워드 레포지토리가 2023년 이후 실제로 증가했는가?  
**RQ3.** AI 분야별(LLM, 강화학습, 컴퓨터비전, NLP) 프로젝트 증가 양상이 다른가?  
**RQ4.** Stack Overflow 질문 수와 GitHub 프로젝트 수 간 상관관계가 있는가?

---

## 가설

**H1.** ChatGPT 출시 이후(2023-2025) AI 레포지토리는 이전(2021-2022) 대비 500% 이상 증가했을 것이다  
**H2.** "AI agent", "autonomous" 키워드 프로젝트는 2023년 이후 급증했을 것이다  
**H3.** LLM 분야가 2023년 이후 가장 높은 성장률을 보일 것이다  
**H4.** GitHub 프로젝트 증가율과 Stack Overflow 질문 증가율 간 강한 양의 상관관계(r > 0.7)가 존재할 것이다

---

## 팀 구성 및 역할

### 윤태웅
- 프로젝트 총괄 및 일정 관리

---

### 송민찬 - GitHub 데이터 수집

**산출물**
- `github_2021.csv`
- `github_2022.csv`
- `github_2023.csv`
- `github_2024.csv`
- `github_2025.csv`

---

### 이라온 - Stack Overflow 데이터 수집 및 전처리

**수집 산출물:**
- `stackoverflow_2021.csv`
- `stackoverflow_2022.csv`
- `stackoverflow_2023.csv`
- `stackoverflow_2024.csv`
- `stackoverflow_2025.csv`

**전처리:**
- 10개 CSV 파일 통합 (GitHub 5개 + Stack Overflow 5개)
- 중복 제거 (레포지토리 ID, 질문 ID 기준)
- 결측치 처리
- 파생 변수 생성:
  - `period`: Before/After ChatGPT (기준: 2022-11-30)
  - `ai_field`: AI 분야 분류 (LLM, 강화학습, 컴퓨터비전, NLP, General ML)
  - 키워드 분류 (AI agent, autonomous, vibe coding 등)

**최종 산출물:**
- `github_all_years_cleaned.csv`
- `stackoverflow_all_years_cleaned.csv`
- `github_so_monthly_merged.csv`

---

### 원준서 - 데이터 분석 & 시각화

**분석:**
- 기술 통계 (ChatGPT 전후 비교, 언어별/분야별 분포)
- 시계열 분석 (월별 트렌드, 증가율)
- 상관관계 분석 (R): GitHub ↔ Stack Overflow 피어슨 상관계수, 회귀 분석
- 가설 검증 (H1~H4)

**시각화**

**생성할 그래프 (6개):**
1. 월별 트렌드 (Line Plot) - ChatGPT 출시일 표시
2. AI 분야별 분포 (Bar Chart) - Before/After 비교
3. 키워드 빈도 순위 (Horizontal Bar)
4. 인기도 비교 (Box Plot) - Before/After Stars 분포
5. Stars vs Forks 관계 (Scatter Plot)
6. GitHub ↔ Stack Overflow 상관관계 (Heatmap)

---

## 분석 방법론

### 데이터 수집
- **GitHub API**: 일별 레포지토리 메타데이터 수집 (2021-2025)
- **Stack Exchange API**: 월별 질문 데이터 수집 (2021-2025)

### 데이터 전처리
- 중복 제거 (ID 기준)
- 결측치 처리 (description, language 등)
- ChatGPT 기준 시점 분할 (2022-11-30)
- AI 분야 자동 분류 (키워드 기반)

### 분석
- **기술통계**: ChatGPT 전후 비교, 분야별 통계
- **시계열 분석**: 월별 트렌드, 증가율 계산
- **상관분석** (R): 피어슨 상관계수, 회귀분석, 시차 분석

### 시각화
- **Python**: matplotlib, seaborn
- **R**: ggplot2, corrplot

---

## 작업 흐름
```
송민찬 (GitHub 수집)     이라온 (Stack Overflow 수집)
         ↓                           ↓
    5개 CSV 파일                5개 CSV 파일
         └───────────┬───────────┘
                     ↓
            이라온 (전처리)
                     ↓
          원준서 (분석 & 시각화)
                     ↓
            윤태웅 (보고서 & PPT)
                     ↓
              최종 결과물
```
