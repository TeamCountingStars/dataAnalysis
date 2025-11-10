import requests
import pandas as pd
import time
from datetime import datetime, timedelta
import os

class GitHubCollector:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }
        self.base_url = "https://api.github.com"
    
    def check_rate_limit(self):
        url = f"{self.base_url}/rate_limit"
        response = requests.get(url, headers=self.headers)
        data = response.json()
        
        remaining = data['rate']['remaining']
        limit = data['rate']['limit']
        reset_time = datetime.fromtimestamp(data['rate']['reset'])
        
        print(f"⏱️  남은 요청: {remaining}/{limit} (리셋: {reset_time.strftime('%H:%M:%S')})")
        return remaining
    
    def search_repos(self, keyword, start_date, end_date, per_page=100):
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
            time.sleep(0.5)  # 속도 향상
        
        return all_repos
    
    def collect_by_days(self, keyword, start_date, end_date):
        """일별로 데이터 수집"""
        all_repos = []
        
        # 날짜 파싱
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        total_days = (end - start).days + 1
        current_day = 0
        
        print("\n" + "="*70)
        print(f"📅 일별 수집 시작: {start_date} ~ {end_date} (총 {total_days}일)")
        print("="*70)
        
        current_date = start
        while current_date <= end:
            current_day += 1
            date_str = current_date.strftime("%Y-%m-%d")
            
            print(f"\n[{current_day}/{total_days}] 🔍 {date_str} ", end="")
            
            repos = self.search_repos(keyword, date_str, date_str)
            all_repos.extend(repos)
            
            print(f"→ {len(repos)}개 수집 (누적: {len(all_repos)}개)")
            
            # Rate Limit 체크 (100개 미만이면 대기)
            remaining = self.check_rate_limit()
            if remaining < 100:
                print("⏸️  API 제한 임박. 1분 대기 중...")
                time.sleep(60)
            
            current_date += timedelta(days=1)
        
        print("\n" + "="*70)
        print(f"🎉 수집 완료: 총 {len(all_repos)}개 (중복 포함)")
        print("="*70)
        
        return all_repos
    
    def repos_to_dataframe(self, repos):
        """레포지토리 리스트를 DataFrame으로 변환 (중복 제거 안함)"""
        data = []
        
        for repo in repos:
            data.append({
                'id': repo['id'],
                'name': repo['name'],
                'full_name': repo['full_name'],
                'owner': repo['owner']['login'],
                'owner_type': repo['owner']['type'],  # User or Organization
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
                'topics': '|'.join(repo.get('topics', [])),  # 쉼표 대신 | 사용
                'license': repo['license']['name'] if repo.get('license') else 'No License',
                'default_branch': repo.get('default_branch', 'main'),
                'has_wiki': repo.get('has_wiki', False),
                'has_pages': repo.get('has_pages', False),
                'archived': repo.get('archived', False)
            })
        
        df = pd.DataFrame(data)
        
        print(f"\n📊 DataFrame 생성 완료: {len(df)}개 레코드")
        return df
    
    def save_to_csv(self, df, filename):
        """CSV로 저장 (다운로드 가능)"""
        if not os.path.exists('data'):
            os.makedirs('data')
        
        filepath = os.path.join('data', filename)
        df.to_csv(filepath, index=False, encoding='utf-8-sig')
        
        file_size = os.path.getsize(filepath) / 1024 / 1024  # MB
        
        print(f"\n💾 저장 완료!")
        print(f"📁 경로: {os.path.abspath(filepath)}")
        print(f"📊 크기: {file_size:.2f} MB")
        print(f"📋 레코드: {len(df)}개")
        
        return filepath


# ========== 실행 ==========

collector = GitHubCollector("토큰을_여기에_입력하세요")

# 초기 Rate Limit 확인
collector.check_rate_limit()

# 2023년 1월 데이터 수집 (테스트)
print("\n⚠️  테스트: 2023년 1월만 수집합니다")
print("전체 2023년 수집은 약 1-2시간 소요 예상")

repos = collector.collect_by_days(
    keyword="chatgpt",
    start_date="2023-01-01",
    end_date="2023-01-31"  # 1월만 (31일)
)

# DataFrame 변환
df = collector.repos_to_dataframe(repos)

# 기본 통계
print("\n" + "="*70)
print("📊 수집 결과 미리보기")
print("="*70)
print(f"\n전체 레코드: {len(df)}개")
print(f"중복 포함 레코드: {len(df)}개")
print(f"고유 레포지토리: {df['id'].nunique()}개")
print(f"\n언어별 분포 (Top 10):")
print(df['language'].value_counts().head(10))

print(f"\n상위 5개 레포:")
print(df[['name', 'stars', 'language', 'created_at']].head())

# CSV 저장 (원본 - 중복 포함)
collector.save_to_csv(df, 'github_chatgpt_2023_01_raw.csv')

print("\n" + "="*70)
print("✅ 1월 데이터 수집 완료!")
print("="*70)
print("\n💡 다음 단계:")
print("  1. 이 코드가 잘 작동하면 전체 2023년 수집")
print("  2. 중복 제거는 전처리 단계에서 진행")
print("  3. CSV 파일을 친구들에게 공유")