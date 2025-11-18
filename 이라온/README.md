### 1. Stack Overflow 데이터 수집
- **BigQuery 직접 연동**: Google Colab에서 BigQuery API를 통해 공개 데이터셋에 직접 접근
- **서버 사이드 필터링**: SQL WHERE 절로 2021-2025년 데이터만 추출 (id, title, tags, creation_date)
- **효율적 처리**: 전체 테이블 다운로드 없이 필요한 데이터만 Pandas DataFrame으로 직접 변환

### 2. GitHub 데이터 병합 및 정제
- **데이터 통합**: 연도별 5개 CSV 파일을 pandas.concat으로 단일 DataFrame 병합
- **품질 검증**: df.info(), df.isnull().sum()으로 데이터 타입 일관성 및 결측치 검증

### 3. 공통 전처리 및 파생 변수 생성

**데이터 클렌징**
- 중복 제거: id/repo_id 기준 drop_duplicates 실행
- 결측치 처리: 핵심 열(ID, 날짜, 태그) 결측치 제거, 텍스트 열은 빈 문자열로 대체
- 타입 표준화: creation_date를 UTC 시간대로 통일, tags를 소문자로 표준화

**파생 변수 생성**
1. **period**: ChatGPT 출시 기준일(2022-11-30) 전후로 'Before'/'After' 분류
2. **AI_field**: tags 키워드 기반 AI 분야 대분류 (LLM, Computer Vision, NLP, General ML 등)
3. **키워드 플래그**: 'ai-agent', 'vibe-coding' 등 특정 키워드 존재 여부 Boolean 값 생성