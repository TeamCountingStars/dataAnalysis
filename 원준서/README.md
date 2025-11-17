# Q1. ChatGPT 출시 전후(2021-2022 vs 2023-2025) GitHub AI 프로젝트 생성량 분석
![alt text](results/image.png)
![alt text](results/image-1.png)
![alt text](results/image-2.png)
---
# Q2. 레포지토리가 ChatGPT 출시 2023년 이후 실제 증가 양상 분석
## 1. Top 10 언어 'Trend'비교
![alt text](results/image-3.png)
## 2. 키워드 생성 추이
![alt text](results/image-4.png)
## 3. Top 10 언어별 키워드 생성 추이
![alt text](results/image-5.png)
---
# Q3. AI 분야별 프로젝트 증가 양상 분석
## 1. AI 분야별 프로젝트 생성 추이
![alt text](results/image-6.png)
![alt text](results/image-7.png)
---
# Q3-1. 분석 결과에 대한 미래 예측
## 1. SARIMA 예측 모델
![alt text](results/image-8.png)

결과 : 실패

---
## 2. Prophet 예측 모델
![alt text](results/image-9.png)
![alt text](results/image-10.png)

결과 : 평균적으로 ± 2,217.07 개의 프로젝트 수를 차이 나게 예측

---
# Q4. Stack Overflow 질문 수와 GitHub 프로젝트 수 간 상관관계 분석
## 1. 분야별 상관관계 분석
![alt text](results/image-11.png)
## 2. 언어별 상관관계 분석
![alt text](results/image-12.png)

## 언어별 회귀 모델 학습 요약
| Language | Model (Y = mX + b) | R-squared |
| --- | --- | --- |
| Python | Y = -0.38 * X + 11527.15 | 0.352442 |
| JavaScript | Y = -0.13 * X + 2229.14	 | 0.360368 |
| TypeScript | Y = -0.51 * X + 1608.32 | 0.343246 |
| Java | 	Y = -0.03 * X + 325.48 | 0.467990 |
| C++ | Y = -0.03 * X + 250.41 | 0.579037 |
| R	 | Y = -0.01 * X + 166.78 | 0.170623 |
| C# | Y = -0.02 * X + 187.60 | 0.482109 |
| Go | Y = -0.24 * X + 184.14 | 0.400200 |
| MATLAB | Y = 0.30 * X + 82.00 | 0.704192 |

* * *

## Q1. ChatGPT 출시 전후(2021-2022 vs 2023-2025) GitHub AI 프로젝트 생성량 분석

![alt text](results/image.png)
**전반적인 급증**: 모든 AI 분야에서 After(2023-2025)의 프로젝트 수가 Before(2021-2022)에 비해 압도적으로 증가했습니다. 이는 AI 개발 진입 장벽이 낮아졌음을 의미합니다.

**LLM repo의 급증**: LLM 분야는 Before 시기에는 거의 존재하지 않았으나, After 시기에는 약 25만 건 이상으로 급부상하며 새로운 주류 카테고리가 되었습니다.

**다양한 ai의 비중도 급증**: 가장 눈에 띄는 것은 Others 항목입니다. 약 15만 건에서 80만 건 가까이 폭증했습니다. 이는 기존의 전통적인 분류(CV, NLP 등)에 속하지 않는 새로운 형태의 AI 응용 프로그램들이 쏟아져 나오고 있음을 시사합니다. (이는 세 번째 그래프와 연결됩니다.)

**General ML & Deep Learning**: 기존 머신러닝과 딥러닝 분야도 2~3배가량 성장하며 탄탄한 기반을 유지하고 있습니다.

---
![alt text](results/image-2.png)
**Python & Jupyter**:
Jupyter Notebook과 Python이 압도적인 1, 2위를 차지했습니다. 특히 Jupyter Notebook이 50만 건 이상으로 급증한 것은, 완성된 소프트웨어뿐만 아니라 실험, 튜토리얼, 데이터 분석 코드가 활발히 공유되고 있음을 보여줍니다.

**웹 언어(JavaScript, TypeScript)의 약진**:
가장 주목할 만한 변화 중 하나입니다. Before 시기에는 미미했던 JavaScript와 TypeScript가 After 시기에 급격히 늘어났습니다.
해석: 이는 AI가 단순히 '모델 학습' 단계에 머무르지 않고, 웹 서비스, 크롬 익스텐션, 챗봇 인터페이스 등 실제 '애플리케이션'으로 구현되고 있음을 의미합니다.

**정적 언어들의 성장**: Java, C++, Go 등도 전반적으로 상승했으나 Python 생태계의 성장세에는 미치지 못했습니다.

## Q2. 레포지토리가 ChatGPT 출시 2023년 이후 실제 증가 양상 분석
![alt text](results/image-3.png)

**Python이 Jupyter Notebook을 역전** 이것이 이 그래프의 핵심입니다.

**Before (2022년 11월 이전)**: Jupyter Notebook의 트렌드가 Python보다 지속적으로 더 우위에 있었습니다. 이는 AI/데이터 분석이 주로 '연구/분석' 단계에 머물러 있었음을 시사합니다.

**After (2023년 이후)**: ChatGPT 출시 직후, Python의 추세선 기울기가 Jupyter Notebook보다 훨씬 더 가팔라지기 시작합니다.

**2023년 중반 (The Crossover)**: 마침내 Python의 트렌드가 Jupyter Notebook을 **추월**합니다.

**결론**: AI 붐은 '단순 분석'(Jupyter)을 넘어, Python을 이용한 '실제 애플리케이션 개발'(AI Agent, API 연동 등)로의 패러다임 전환을 이끌어냈으며, 'Python'의 수요가 'Jupyter'를 압도하기 시작했습니다.

## Q3. AI 분야별 프로젝트 증가 양상 분석
![alt text](results/image-6.png)
**"LLM"의 폭발**: 'LLM' 라인은 ChatGPT 출시 이전에는 거의 바닥에 있었으나, 2023년 초를 기점으로 다른 모든 분야를 압도하며 수직으로 폭발합니다.

**기존 강자들의 성장**: 'Deep Learning'과 'General ML'은 AI 붐 이전부터 꾸준히 성장해 온 기존의 강자들이었지만, 'LLM'의 성장세와는 비교가 되지 않습니다.

**Y축 (Log Scale)의 의미**: 이 그래프는 Y축이 로그 스케일(10배씩 증가)입니다. 그럼에도 'LLM'이 이렇게 가파르게 올라갔다는 것은, '절대량'이 아닌 '성장률' 자체가 다른 분야와는 차원이 달랐음을 의미합니다.

![alt text](results/image-7.png)
**Observed (관측값)**: 1번 그래프에서 봤던 'LLM'의 원본 꺾은선 그래프입니다.

**Trend (추세)**: '진짜' 장기 성장 흐름입니다. 2023년 이전까지는 0에 가까웠으나, 2023년 초를 기점으로 기울기가 급격히 꺾여 꺾이지 않는 강력한 우상향 추세가 시작되었음을 보여줍니다.

**Seasonal (계절성)**: 12개월 주기의 반복 패턴입니다. LLM 분야도 매년 상반기에 정점을 찍고 하반기에 저점을 찍는 뚜렷한 연간 주기가 있음을 보여줍니다.

**Resid (잔차)**: 추세와 계절성으로도 설명되지 않는 **예측 불가능한 충격**입니다. 2023년 초(1~3월)와 2025년 여름에 **위로 크게 튄 점**들이 있는데, 이는 "ChatGPT"나 "Auto-GPT" 출시 같은 **거대한 외부 이벤트**가 시장을 강타했음을 통계적으로 증명합니다.

## Q3-1. Prophet 예측 모델
![alt text](results/image-9.png)

>prophet 라이브러리를 사용하여, SARIMA 모델에서 '이벤트'를 '계절성'으로 착각하는 문제를 해결하기 위해 holidays라는 특별 파라미터를 사용했습니다.

**Actual (검은색 점)**: 님이 가진 '실제 데이터'입니다. 2023년 초와 2025년 여름에 거대한 스파이크(폭발)가 보입니다.

**Predicted( 파란색 선)**: Prophet 모델의 '예측'입니다.

Confidence Interval (하늘색 음영): 모델의 '불확실성(신뢰) 구간'입니다.

### 해석
장기 추세와 계절성을 바탕으로 훨씬 더 합리적이고 안정적인 미래를 예측하고 있습니다. 왜 이렇게 할 수 있었는지가 바로 모델 분해를 보면 됩니다.

![alt text](results/image-10.png)

이 그래프는 Prophet 모델이 데이터를 어떻게 분해해서 이해했는지 보여주는 요약 리포트입니다.

**trend (추세)**: 장기 성장 추세입니다. 매끄럽고 강력하게 우상향하는 기본 성장률을 완벽하게 잡아냈습니다.

**holidays (이벤트)**: 이것이 이 분석의 핵심입니다. Prophet은 우리가 events로 알려준 2023년 초(ChatGPT/Auto-GPT)와 2025년 여름의 스파이크를 **1년 주기 계절성이 아닌 별개의 특별 이벤트**로 정확히 분리해 낸 것을 보여줍니다. 모델은 "아, 이때는 이벤트 때문에 5000개, 2000개씩 튄 거구나. 이건 '추세'나 '계절'이 아니야"라고 학습한 것입니다.

**yearly (계절성)**: '이벤트'가 제거된 후의 '순수한' 1년(12개월) 주기입니다. 매년 상반기(1월~5월)에 높고 하반기(7월~10월)에 낮은 규칙적인 패턴이 있음을 보여줍니다.

>결론: Prophet 모델은 '이벤트'라는 외부 충격을 **노이즈**가 아닌 **별개의 정보**로 현명하게 분리해냈습니다. 그 결과, 미래를 합리적으로 예측할 수 있었으며, 이는 "'이벤트'에 의해 주도되었다"는 가설을 통계적으로 완벽하게 뒷받침합니다.

# Q4. Stack Overflow 질문 수와 GitHub 프로젝트 수 간 상관관계 분석
## 분야별 상관관계 분석
![alt text](results/image-11.png)
>이 히트맵은 "GitHub ↔ Stack Overflow"의 관계를 묻는 초기 가설(H1)이 완벽하게 틀렸음을 증명합니다.

**GitHub ↔ GitHub, SO ↔ SO**: 좌측 상단과 우측 하단은 모두 강한 **양의 상관관계**입니다. 이는 "GitHub 내에서는 모든 AI 분야가 함께 성장"했고, "Stack Overflow 내에서도 모든 AI 질문이 함께 움직였다"는 것을 의미합니다.

**GitHub ↔ SO**: 이것이 핵심입니다. GitHub와 Stack Overflow가 만나는 지점(우측 상단, 좌측 하단)은 모두 강한 **음의 상관관계**입니다.

> GitHub_LLM ↔ SO_LLM = -0.70 / GitHub_Computer Vision ↔ SO_Computer Vision = -0.67

**결론**: "GitHub 프로젝트가 폭발적으로 증가하는 동안, Stack Overflow의 AI 관련 질문은 오히려 줄어들었다"는 강력한 증거입니다.

> **이는 개발자들이 문제 해결을 위해 Stack Overflow 대신 ChatGPT와 같은 AI를 사용하기 시작했다는 "패러다임의 전환"을 시사합니다.(이건 윤태웅이 마지막에 발표)**

## 2. 언어별 상관관계 분석
![alt text](results/image-12.png)
>이 히트맵은 "AI 분야" 분석의 결론을 개발 생태계 전체로 확장시킵니다.

**"ChatGPT 효과"는 보편적이었다**: Python(-0.59), C++(-0.76), JavaScript(-0.59), C#(-0.69) 등 모든 주요 언어에서 동일한 강한 음의 상관관계가 나타났습니다.
>**결론: "GitHub 개발은 늘고, SO 토론은 줄어드는" 현상은 AI 분야만의 현상이 아니라, 모든 개발자가 ChatGPT를 사용하기 시작했다는 것을 증명합니다.(이건 윤태웅이 마지막에 발표)**

**"MATLAB"이라는 완벽한 예외**: 유일하게 github_matlab ↔ SO_matlab의 관계만 +0.83이라는 강한 양의 상관관계를 보입니다.
>MATLAB 생태계는 ChatGPT의 영향을 받지 않고, 유일하게 "질문(SO)이 늘면 개발(GitHub)도 는다"는 전통적인 방식을 고수하고 있습니다. 이 "예외"는 다른 언어들의 음의 상관관계가 우연이 아님을 증명하는 완벽한 '통제 집단(Control Group)' 역할을 합니다.