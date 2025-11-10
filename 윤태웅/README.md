# AI 코드 생성 시대의 GitHub 오픈소스 진화 분석

> **"ChatGPT와 Vibe Coding 이후, 개발자 생태계는 어떻게 변했는가?"**

---

## 프로젝트 개요

2022년 11월 ChatGPT 출시 이후 소프트웨어 개발 패러다임이 급격히 변화했습니다.  
본 연구는 AI 코드 생성 도구가 GitHub 오픈소스 생태계에 미친 영향을 정량적으로 분석합니다.

---

## 연구 질문

**RQ1.** ChatGPT 출시 전후 GitHub AI 프로젝트는 어떻게 변화했는가?  
**RQ2.** "Vibe coding", "AI agent" 키워드 레포지토리가 실제로 증가했는가?  
**RQ3.** 프로그래밍 언어별 AI 프로젝트 증가 양상이 다른가?  
**RQ4.** Stack Overflow 질문 수와 GitHub 프로젝트 수 간 상관관계가 있는가?

---

## 가설

**H1.** ChatGPT 이후 AI 레포지토리 500% 이상 증가  
**H2.** "Vibe coding" 프로젝트 2023년 이후 급증  
**H3.** Python이 AI 프로젝트에서 최다 비중  
**H4.** GitHub ↔ Stack Overflow 양의 상관관계 존재

---

## 팀 구성 및 역할

### PM
- 프로젝트 총괄, 보고서 작성, PPT 제작

### GitHub 데이터 수집
**수집 대상:**
- 2021년: AI, machine learning (비교군)
- 2022년: AI, copilot (ChatGPT 직전)
- 2023-2024년: chatgpt, AI agent, vibe coding

**산출물:** `github_YYYY.csv` (4개 파일)

### 데이터 전처리
**작업 내용:**
- 중복 제거, 결측치 처리
- 날짜 통일, 파생 변수 생성
- 키워드 분류 (AI 도구, 자동화, Vibe Coding, 전통 AI)

**산출물:** `github_all_years_cleaned.csv`

### 시각화
**생성할 그래프:**
1. 월별 트렌드 (Line Plot)
2. 언어별 분포 (Bar Chart)
3. 키워드 빈도 (Horizontal Bar)
4. 인기도 비교 (Box Plot)
5. Stars vs Forks (Scatter Plot)

**산출물:** PNG 그래프 5개

### Stack Overflow 분석 (시간적 여유 보고)
**작업 내용:**
- Stack Overflow API로 질문 데이터 수집
- 월별 집계
- GitHub 데이터와 상관분석 (R)

**산출물:** 
- `so_monthly_aggregated.csv`
- `correlation_heatmap.png`

---

## 분석 방법

1. **데이터 수집**: GitHub API, Stack Exchange API
2. **전처리**: 중복 제거, 키워드 추출
3. **분석**: 기술통계, 시계열, 상관분석
4. **시각화**: Python (matplotlib), R (ggplot2)

---

## 예상 결과

- ChatGPT 이후 AI 프로젝트 5배 증가
- Python 50% 이상 비중
- GitHub ↔ Stack Overflow 강한 양의 상관관계 (r > 0.7)

---