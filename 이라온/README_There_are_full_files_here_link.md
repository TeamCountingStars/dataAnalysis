이라온의 폴더

https://drive.google.com/file/d/1FbENciQlJTse7JeWKtpE2nKqNnD9Vc8e/view?usp=drive_link   //깃허브 완성

https://drive.google.com/file/d/1pzLPA0hda0wYsaeircOQlRWC1odvmpXi/view?usp=drive_link   //스택오버플로우 완성

https://drive.google.com/file/d/1kWSq5dwslTKfQSGN0cUd_YkaJ8g606lP/view?usp=sharing      //스택오버플로우 raw데이터

https://drive.google.com/file/d/1kQZwLFtXGXgBzHeEF7DqJGFZ_bzd_V9O/view?usp=sharing      //깃허브 raw데이터

데이터 수집 및 전처리 파트 수행 내역 보고서
담당자: 이라온
본 보고서는 "AI 코드 생성 시대의 GitHub 오픈소스 진화 분석" 프로젝트의 핵심 데이터셋 구축을 위해 제가 수행한 데이터 수집(Data Ingestion), 전처리(Preprocessing) 및 파생 변수 생성(Feature Engineering)의 전 과정을 상세히 기술합니다.
1. Stack Overflow 데이터 파이프라인 구축 (BigQuery 연동)
단순 CSV 파일을 다운로드하는 방식 대신 분석의 효율성과 확장성을 극대화하기 위해 Google Colab 환경에서 BigQuery 공개 데이터셋에 직접 접근하는 방식을 채택했습니다.
1. GCP 연동 및 인증: google-cloud-bigquery 라이브러리를 사용하여 Colab 환경에서 Google Cloud Platform(GCP) 인증을 수행하고, BigQuery API 클라이언트를 초기화했습니다.
2. 서버 사이드 필터링 (SQL): 방대한 전체 posts_questions 테이블(수천만 행)을 Colab 메모리로 모두 불러오는 비효율을 피하고자 BigQuery 서버 단에서 데이터를 사전에 필터링하는 SQL 쿼리를 작성했습니다.
WHERE creation_date BETWEEN '2021-01-01' AND '2025-12-31' 절을 사용하여 분석에 필요한 5년 치 데이터만 특정했습니다.
ELECT id, title, tags, creation_date를 통해 분석에 필수적인 열만 선택하여 네트워크 트래픽과 메모리 사용량을 최소화했습니다.
3. Pandas DataFrame 변환: 쿼리 실행 결과를 client.query().to_dataframe() 메서드를 통해 로컬 파일 저장/로드 과정 없이 즉시 Pandas DataFrame 객체로 변환하여 후속 전처리 작업을 위한 기반을 마련했습니다.
2. GitHub 데이터 병합 및 정제
Stack Overflow와 달리 GitHub는 연도별로 분리된 원본 CSV 파일(github_2021.csv 등 5개)을 전달받아 Colab 환경에서 병합 및 정제 작업을 수행했습니다.
1. 데이터 병합 (Concatenation): pandas.read_csv로 5개의 개별 CSV 파일을 각각 DataFrame으로 로드한 뒤 pandas.concat 함수를 사용하여 이들을 수직으로 결합, 단일 통합 DataFrame을 생성했습니다.
2. 데이터 정합성 검증: 병합 직후 df.info() 및 df.isnull().sum()을 통해 데이터 타입이 일관적인지, 특정 연도 데이터에서만 결측치가 대량 발생하지 않았는지 등 초기 품질 검증(Initial Quality Check)을 수행했습니다.
3. 공통 전처리 및 핵심 파생 변수 생성 (Feature Engineering)
수집된 두 원본 데이터(GitHub, Stack Overflow)에 대해, 연구 질문(RQ)에 직접 답할 수 있는 '분석-준비(Analysis-Ready)' 데이터를 만들기 위해 다음과 같은 공통 전처리 및 파생 변수 생성을 진행했습니다.
A. 데이터 클렌징 (Data Cleansing)
1. 중복 제거: id (Stack Overflow) 및 repo_id (GitHub) 열을 기준으로 drop_duplicates(subset=['id'], keep='first')를 실행하여 고유 식별자 기준 중복 데이터를 제거하고 데이터의 무결성을 확보했습니다.
2. 결측치 처리:
dropna(subset=['id', 'creation_date', 'tags'])를 사용하여, 분석에 필수적인 핵심 열(ID, 날짜, 태그)에 값이 없는 행은 전략적으로 제거했습니다.
title, description 등 텍스트 분석용 열의 결측치는 fillna('') (빈 문자열)로 대체하여 이후 str 함수 처리 시 발생할 수 있는 TypeError를 원천 차단했습니다.
3. 타입 표준화 (Type Standardization):
오류 해결 (Timezone): creation_date 열을 pd.to_datetime으로 변환하는 과정에서 BigQuery의 UTC(tz-aware) 타입과 Pandas의 기본 (tz-naive) 타입 간 비교 오류(TypeError)가 발생하는 문제를 발견했습니다.
기준 날짜(2022-11-30) 또한 pd.to_datetime('...', utc=True)로 명시적으로 동일한 UTC 시간대를 부여하여 해결했습니다.
tags 열은 .astype(str).str.lower()를 적용하여 모든 태그를 소문자로 통일하고, 검색 및 분류 시 대소문자로 인한 누락이 없도록 표준화했습니다.
B. 파생 변수 생성 (Feature Engineering)
가장 핵심적인 작업으로 원본 데이터를 가공하여 연구 가설(H1, H2, H3)을 직접 검증할 수 있는 3가지 핵심 파생 변수를 설계 및 생성했습니다.
1. period (ChatGPT 출시 전후):
연구의 핵심 기준점인 '2022-11-30'을 pivot_date로 설정했습니다.
np.where(df['creation_date'] <= pivot_date, 'Before', 'After')라는 벡터화(Vectorized) 연산을 사용하여 수백만 행의 날짜를 고속으로 비교, 'Before'와 'After'로 분류하는 period 열을 생성했습니다.
2. AI_field (AI 분야 대분류):
'LLM', 'Computer Vision', 'NLP', 'General ML' 등 AI 분야를 세분화하기 위해 tags 열의 키워드를 기반으로 계층적 분류 로직을 설계했습니다.
단순하게 if-else 대신 np.select(conditions, choices, default='Other')를 사용하여 여러 조건(예: 'llm' 태그가 'nlp' 태그보다 우선순위가 높음)을 효율적이고 명확하게 처리했습니다.
3. 키워드 플래그 (RQ2 대응):
연구 질문(RQ2)의 핵심 키워드인 'vibe-coding', 'ai-agent' 등의 존재 여부를 파악하기 위해 tags_processed.str.contains('keyword1|keyword2')를 활용했습니다.
분석의 편의성을 위해 'True'/'False'의 Boolean 타입을 갖는 has_ai_agent_tag 등의 플래그(Flag) 열을 생성했습니다.
4. 최종 산출물
위의 모든 파이프라인을 성공적으로 완료하여 최종적으로 다음 두 개의 정제된 분석용 데이터셋을 도출했습니다.
1. github_all_years_cleaned.csv
2. stackoverflow_all_years_cleaned.csv
이 데이터셋들은 즉시 후속 분석(시각화, 상관관계 분석, 시계열 분석 등)에 투입될 수 있는 상태입니다.
