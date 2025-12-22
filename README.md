# ChatGPT와 Vibe Coding 이후, 개발자 생태계는 어떻게 변했는가?

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Prophet](https://img.shields.io/badge/Prophet-4285F4?style=flat-square&logo=meta&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=plotly&logoColor=white)

> 한양대학교 ERICA 스마트융합공학부 스마트ICT융합전공
> GitHub 및 Stack Overflow 데이터 기반 AI 개발 생태계 변화 분석

## 프로젝트 소개

본 연구는 2022년 11월 ChatGPT 출시 이후 소프트웨어 개발 시장에 미친 영향을 GitHub와 Stack Overflow 데이터를 통해 정량적으로 분석합니다. AI 코드 생성 도구가 개발 시장의 프로젝트 생성량, 언어별 사용 추세, AI 분야별 성장 패턴에 어떤 변화를 가져왔는지 시계열 분석과 Prophet 예측 모델을 활용하여 탐구합니다.

### 주요 성과

- **LLM 분야 급부상**: ChatGPT 이후 25만 건 이상으로 폭증, 새로운 주류 카테고리 형성
- **개발 패러다임 전환**: 2023년 중반 Python이 Jupyter Notebook 추월 (연구→애플리케이션 개발)
- **Stack Overflow 역상관**: GitHub 프로젝트 증가 시 Stack Overflow 질문 감소 (-0.70 상관계수)
- **Prophet 예측 모델**: 장기 추세와 계절성 분리, ChatGPT/Auto-GPT 이벤트 효과 정량화

## 프로젝트 웹페이지

프로젝트 소개 및 연구 결과 시각화는 GitHub Pages를 통해 확인하실 수 있습니다:

**🔗 [https://teamcountingstars.github.io/dataAnalysis/](https://teamcountingstars.github.io/dataAnalysis/)**

## 기술 스택

### 데이터 수집 및 전처리
- **데이터 소스**: GitHub API, Stack Overflow Data Dump
- **라이브러리**: Pandas, NumPy
- **기간**: 2021-2025 (ChatGPT 출시 전후 비교)

### 시계열 분석 및 예측
- **예측 모델**: Facebook Prophet
- **시각화**: Matplotlib, Seaborn
- **분석 기법**: 시계열 분해, 상관관계 분석, Log Scale 트렌드 분석

### 데이터셋
- **GitHub 데이터**: AI 관련 레포지토리 생성량, 언어별 분포
- **Stack Overflow 데이터**: AI 관련 질문 수, 태그별 분포
- **분류 카테고리**: LLM, Deep Learning, Computer Vision, NLP, Reinforcement Learning 등

## 팀 구성

| 이름 | 역할 |
|------|------|
| **윤태웅** | PM |
| **원준서** | 데이터 분석 및 시각화 |
| **송민찬** | GITHUB 데이터 수집 |
| **이라온** | StackOverFlow 데이터 수집  |

## 연구 질문

**RQ1**: ChatGPT 출시 전후(2021-2022 vs 2023-2025) GitHub AI 프로젝트는 어떻게 변화했는가?<br>
**RQ2**: Github 레포지토리가 2023년 이후 실제로 증가했는가?<br>
**RQ3**: AI 분야별(LLM, 강화학습, 컴퓨터비전, NLP) 프로젝트 증가 양상이 다른가?<br>
**RQ4**: Stack Overflow 질문 수와 GitHub 프로젝트 수 간 상관관계가 있는가?<br>

---

## 문의

프로젝트에 대한 문의사항은 아래 이메일로 연락주세요:

**윤태웅** - taewoong25@hanyang.ac.kr
