# GitHub & Stack Overflow Data Analysis

## 연구 질문

**RQ1**: ChatGPT 출시 전후(2021-2022 vs 2023-2025) GitHub AI 프로젝트는 어떻게 변화했는가?<br>
**RQ2**: Github 레포지토리가 2023년 이후 실제로 증가했는가?<br>
**RQ3**: AI 분야별(LLM, 강화학습, 컴퓨터비전, NLP) 프로젝트 증가 양상이 다른가?<br>
**RQ4**: Stack Overflow 질문 수와 GitHub 프로젝트 수 간 상관관계가 있는가?<br>

---

## RQ1. ChatGPT 출시 전후 GitHub AI 프로젝트 생성량 분석

### 1. AI 분야별 프로젝트 수 비교
![AI 프로젝트 생성량 비교](resultsImage/image.png)

- 모든 AI 분야에서 2023년 이후 압도적 증가
- LLM 분야가 25만 건 이상으로 급부상하며 새로운 주류 카테고리 형성
- Others 항목이 15만 건에서 80만 건으로 폭증 (새로운 AI 응용 분야 확대)

---

### 2. 언어별 사용 현황 분석
![언어별 프로젝트 수](resultsImage/image-2.png)

- Python과 Jupyter Notebook이 압도적 1, 2위
- JavaScript, TypeScript의 급격한 증가 (AI의 웹 애플리케이션화)
- 전통적 정적 언어들도 성장세 유지

---

## RQ2. 레포지토리 2023년 이후 실제 증가 양상 분석

![언어별 트렌드](resultsImage/image-3.png)

- **2023년 중반**: Python이 Jupyter Notebook을 추월
- AI 개발이 '연구/분석'에서 '실제 애플리케이션 개발'로 패러다임 전환

---

## RQ3. AI 분야별 프로젝트 증가 양상 분석

### 1. 분야별 성장 추이 (Log Scale)
![분야별 성장 추이](resultsImage/image-6.png)

- LLM 분야가 2023년 초를 기점으로 수직 상승
- 기존 강자(Deep Learning, General ML)를 압도하는 성장률

---

### 2. LLM 분야 시계열 분해 분석
![LLM 시계열 분해](resultsImage/image-7.png)

- **Trend (추세)**: 2023년계 분석
![언어별 상관관계](resultsImage/image-12.png)

- Python(-0.59), C++(-0.76), JavaScript(-0.59), C#(-0.69) 등 모든 주요 언어에서 강한 음의 상관관계
- **예외**: MATLAB만 +0.83으로 강한 양의 상관관계 (ChatGPT 영향 미미)
