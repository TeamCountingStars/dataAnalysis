import requests
import pandas as pd
import time
from datetime import datetime, timedelta
import os

class GitHubCollector:
    def __init__(self, token):
        """
        GitHub 데이터 수집기
        token: GitHub Personal Access Token
        """
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }
        self.base_url = "https://api.github.com"
    
    def check_rate_limit(self):
        """API 사용량 확인"""
        url = f"{self.base_url}/rate_limit"
        response = requests.get(url, headers=self.headers)
        data = response.json()
        
        remaining = data['rate']['remaining']
        limit = data['rate']['limit']
        reset_time = datetime.fromtimestamp(data['rate']['reset'])
        
        print(f"⏱️  남은 요청: {remaining}/{limit} (리셋: {reset_time.strftime('%H:%M:%S')})")
        return remaining
    
    def search_repos(self, keyword, start_date, end_date, per_page=100):
        """단일 날짜로 레포지토리 검색"""
        url = f"{self.base_url}/search/repositories"
        query = f"{keyword} created:{start_date}..{end_date}"
        
        params = {
            "q": query,
            "per_page": per_page,
            "sort": "stars",
            "order": "desc",
            "page": 1
        }
        
        all_repos = []
        
        while True:
            response = requests.get(url, headers=self.headers, params=params)
            
            if response.status_code != 200:
                print(f"❌ 에러: {response.status_code}")
                break
            
            data = response.json()
            repos = data.get('items', [])
            
            if not repos:
                break
            
            all_repos.extend(repos)
            
            # 1000개 제한
            if len(all_repos) >= 1000 or params['page'] >= 10:
                break
            
            params['page'] += 1
            time.sleep(0.5)
        
        return all_repos
    
    def collect_year(self, keywords, year):
        """
        1년치 데이터 수집 (일별)
        keywords: 검색할 키워드 리스트
        year: 수집 연도
        """
        all_repos = []
        
        # 키워드를 OR로 연결
        keyword_string = " OR ".join(keywords)
        
        # 날짜 범위 설정
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        
        # 2025년은 11월까지만
        if year == 2025:
            end_date = datetime(2025, 11, 30)
        
        total_days = (end_date - start_date).days + 1
        current_day = 0
        
        print("\n" + "="*70)
        print(f"📅 {year}년 데이터 수집 시작")
        print(f"🔍 키워드: {keyword_string}")
        print(f"📆 기간: {start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')} ({total_days}일)")
        print("="*70)
        
        current_date = start_date
        while current_date <= end_date:
            current_day += 1
            date_str = current_date.strftime("%Y-%m-%d")
            
            print(f"\n[{current_day}/{total_days}] 🔍 {date_str} ", end="")
            
            repos = self.search_repos(keyword_string, date_str, date_str)
            all_repos.extend(repos)
            
            print(f"→ {len(repos)}개 수집 (누적: {len(all_repos)}개)")
            
            # Rate Limit 체크
            remaining = self.check_rate_limit()
            if remaining < 100:
                print("⏸️  API 제한 임박. 1분 대기 중...")
                time.sleep(60)
            
            current_date += timedelta(days=1)
        
        print("\n" + "="*70)
        print(f"🎉 {year}년 수집 완료: 총 {len(all_repos)}개 (중복 포함)")
        print("="*70)
        
        return all_repos
    
    def repos_to_dataframe(self, repos):
        """레포지토리 리스트를 DataFrame으로 변환"""
        data = []
        
        for repo in repos:
            data.append({
                'id': repo['id'],
                'name': repo['name'],
                'full_name': repo['full_name'],
                'owner': repo['owner']['login'],
                'owner_type': repo['owner']['type'],
                'description': repo.get('description', ''),
                'language': repo.get('language', 'Unknown'),
                'stars': repo['stargazers_count'],
                'forks': repo['forks_count'],
                'watchers': repo['watchers_count'],
                'open_issues': repo['open_issues_count'],
                'created_at': repo['created_at'],
                'updated_at': repo['updated_at'],
                'pushed_at': repo['pushed_at'],
                'size': repo['size'],
                'url': repo['html_url'],
                'topics': '|'.join(repo.get('topics', [])),
                'license': repo['license']['name'] if repo.get('license') else 'No License',
                'default_branch': repo.get('default_branch', 'main'),
                'has_wiki': repo.get('has_wiki', False),
                'has_pages': repo.get('has_pages', False),
                'archived': repo.get('archived', False)
            })
        
        df = pd.DataFrame(data)
        print(f"\n📊 DataFrame 생성: {len(df)}개 레코드")
        return df
    
    def save_to_csv(self, df, filename):
        """CSV로 저장"""
        if not os.path.exists('data'):
            os.makedirs('data')
        
        filepath = os.path.join('data', filename)
        df.to_csv(filepath, index=False, encoding='utf-8-sig')
        
        file_size = os.path.getsize(filepath) / 1024 / 1024
        
        print(f"\n💾 저장 완료!")
        print(f"📁 경로: {os.path.abspath(filepath)}")
        print(f"📊 크기: {file_size:.2f} MB")
        print(f"📋 레코드: {len(df)}개")
        
        return filepath


# ========== 실행 코드 ==========

# 🔑 GitHub Token 입력
GITHUB_TOKEN = input("GitHub Token을 입력하세요: ")

collector = GitHubCollector(GITHUB_TOKEN)

# 전체 AI 키워드 (모든 연도 동일)
AI_KEYWORDS = [
    "chatgpt",
    "gpt-4",
    "openai-api",
    "AI-agent",
    "langchain",
    "autonomous-agent",
    "github-copilot",
    "machine-learning",
    "artificial-intelligence",
    "deep-learning",
    "neural-network",
    "llm"
]

# Rate Limit 확인
collector.check_rate_limit()

# 연도별 수집
years = [2021, 2022, 2023, 2024, 2025]

for year in years:
    print(f"\n\n{'='*70}")
    print(f"🎯 {year}년 데이터 수집 시작")
    print(f"{'='*70}")
    
    # 데이터 수집
    repos = collector.collect_year(AI_KEYWORDS, year)
    
    # DataFrame 변환
    df = collector.repos_to_dataframe(repos)
    
    # 기본 통계
    print(f"\n📊 {year}년 통계:")
    print(f"  총 레코드: {len(df)}개")
    print(f"  고유 레포: {df['id'].nunique()}개")
    print(f"\n  언어별 Top 5:")
    print(df['language'].value_counts().head())
    
    # CSV 저장
    filename = f'github_{year}.csv'
    collector.save_to_csv(df, filename)
    
    print(f"\n✅ {year}년 완료!")
    print("\n⏸️  다음 연도 수집 전 10초 대기...")
    time.sleep(10)

print("\n" + "="*70)
print("🎉 전체 수집 완료!")
print("="*70)
print("\n📁 생성된 파일:")
for year in years:
    print(f"  - data/github_{year}.csv")