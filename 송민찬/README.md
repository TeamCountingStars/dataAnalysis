# dataAnalysis

## 빅데이터활용사례를통한이해 과제

# 밤하늘 광공해와 별 관측 가능성 분석

GitHub Search API를 이용하여 "chatgpt","gpt-4","openai-api","AI-agent","langchain","autonomous-agent","github-copilot","machine-learning","artificial-intelligence","deep-learning","neural-network","llm" 총 12개의 키워드에 대한 2021년~2025년의 레포지토리 데이터를 수집함

데이터 수집중 기술적 문제
1. Rate Limit 문제: 인증된 토큰의 분당 30회 요청 제한 극복을 위해, GitHub 계정을 새로 파서 3개의 별도 GitHub 토큰을 활용하여 병렬 수집 파이프라인을 구축, 데이터 수집 속도를 3배 확장했습니다.
2. 1,000개 결과 제한: 단일 검색 쿼리당 최대 1,000개의 레포지토리만 반환하는 제한을 우회하기 위해, 전체 수집 기간을 일(Day) 단위로 쪼개서 요청하는 세밀한 쿼리 분할을 적용했습니다.
3. 키워드 길이 제한: 하나의 쿼리에서 사용할 수 있는 논리 연산자(예: OR)가 최대 5개의 제한이 있습니다. 12개의 AI 키워드를 5개씩 청크로 나누어 쿼리하여 모든 키워드가 검색 결과에 반영되도록 했습니다.

21~22년도 데이터 수집기간 10시간 23,24,25년도 6시간 총 16시간
