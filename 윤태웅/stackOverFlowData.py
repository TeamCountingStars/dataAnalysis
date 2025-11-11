import requests
import pandas as pd
from datetime import datetime
import time
import os

class StackOverflowCollector:
    def __init__(self, api_key=None):
        """
        Stack Overflow 데이터 수집기
        api_key: Stack Exchange API Key (선택사항)
        """
        self.base_url = "https://api.stackexchange.com/2.3"
        self.api_key = api_key
    
    def get_questions_by_tag(self, tag, from_date, to_date, max_pages=20):
        """단일 태그로 질문 수집"""
        url = f"{self.base_url}/questions"
        
        params = {
            "site": "stackoverflow",
            "tagged": tag,
            "fromdate": int(from_date.timestamp()),
            "todate": int(to_date.timestamp()),
            "sort": "creation",
            "order": "desc",
            "pagesize": 100
        }
        
        if self.api_key:
            params["key"] = self.api_key
        
        all_questions = []
        page = 1
        
        print(f"  🔍 '{tag}' 수집 중...", end=" ")
        
        while page <= max_pages:
            params['page'] = page
            
            try:
                response = requests.get(url, params=params)
                
                if response.status_code != 200:
                    print(f"❌ 에러: {response.status_code}")
                    break
                
                data = response.json()
                questions = data.get('items', [])
                
                if not questions:
                    break
                
                all_questions.extend(questions)
                
                quota_remaining = data.get('quota_remaining', 0)
                has_more = data.get('has_more', False)
                
                if not has_more:
                    break
                
                page += 1
                time.sleep(0.3)
                
            except Exception as e:
                print(f"❌ 에러: {e}")
                break
        
        print(f"✅ {len(all_questions)}개")
        return all_questions
    
    def questions_to_dataframe(self, questions):
        """질문 리스트를 DataFrame으로 변환"""
        data = []
        
        for q in questions:
            data.append({
                'question_id': q['question_id'],
                'title': q['title'],
                'tags': '|'.join(q['tags']),
                'view_count': q['view_count'],
                'answer_count': q['answer_count'],
                'score': q['score'],
                'is_answered': q.get('is_answered', False),
                'creation_date': datetime.fromtimestamp(q['creation_date']),
                'owner_type': q['owner'].get('user_type', 'unknown'),
                'link': q['link']
            })
        
        return pd.DataFrame(data)
    
    def collect_year(self, tags, year):
        """
        1년치 데이터 수집 (태그별)
        tags: 태그 리스트
        year: 수집 연도
        """
        all_questions = []
        tag_stats = {}
        
        # 날짜 범위 설정
        from_date = datetime(year, 1, 1)
        to_date = datetime(year, 12, 31, 23, 59, 59)
        
        # 2025년은 11월까지만
        if year == 2025:
            to_date = datetime(2025, 11, 30, 23, 59, 59)
        
        print("\n" + "="*70)
        print(f"📅 {year}년 데이터 수집 시작")
        print(f"🏷️  태그 수: {len(tags)}개")
        print(f"📆 기간: {from_date.strftime('%Y-%m-%d')} ~ {to_date.strftime('%Y-%m-%d')}")
        print("="*70)
        
        for i, tag in enumerate(tags, 1):
            print(f"\n[{i}/{len(tags)}] ", end="")
            questions = self.get_questions_by_tag(tag, from_date, to_date)
            
            all_questions.extend(questions)
            tag_stats[tag] = len(questions)
            
            time.sleep(1)
        
        # DataFrame 변환 및 중복 제거
        if all_questions:
            df = pd.DataFrame([q for q in all_questions])
            df_unique = df.drop_duplicates(subset=['question_id'], keep='first')
            
            print("\n" + "="*70)
            print(f"🎉 {year}년 수집 완료!")
            print("="*70)
            print(f"총 수집: {len(all_questions)}개")
            print(f"중복 제거 후: {len(df_unique)}개")
            
            print(f"\n📊 태그별 수집 현황 (Top 10):")
            sorted_tags = sorted(tag_stats.items(), key=lambda x: x[1], reverse=True)[:10]
            for tag, count in sorted_tags:
                print(f"  {tag:30s}: {count:4d}개")
            
            final_df = self.questions_to_dataframe(df_unique.to_dict('records'))
            
            return final_df, tag_stats
        
        return None, tag_stats
    
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

collector = StackOverflowCollector()  # API 키 없이 실행 (하루 300번 가능)

# 전체 AI 태그 (모든 연도 동일)
AI_TAGS = [
    "chatgpt",
    "gpt-4",
    "openai-api",
    "langchain",
    "prompt-engineering",
    "github-copilot",
    "machine-learning",
    "artificial-intelligence",
    "deep-learning",
    "neural-network",
    "large-language-model",
    "llm"
]

# 연도별 수집
years = [2021, 2022, 2023, 2024, 2025]

for year in years:
    print(f"\n\n{'='*70}")
    print(f"🎯 {year}년 데이터 수집 시작")
    print(f"{'='*70}")
    
    # 데이터 수집
    df, tag_stats = collector.collect_year(AI_TAGS, year)
    
    if df is not None:
        # 기본 통계
        print(f"\n📊 {year}년 통계:")
        print(f"  총 질문: {len(df)}개")
        print(f"  답변된 질문: {df['is_answered'].sum()}개 ({df['is_answered'].sum()/len(df)*100:.1f}%)")
        print(f"  평균 조회수: {df['view_count'].mean():.0f}")
        print(f"  평균 답변 수: {df['answer_count'].mean():.1f}")
        
        # CSV 저장
        filename = f'stackoverflow_{year}.csv'
        collector.save_to_csv(df, filename)
        
        print(f"\n✅ {year}년 완료!")
        print("\n⏸️  다음 연도 수집 전 5초 대기...")
        time.sleep(5)

print("\n" + "="*70)
print("🎉 전체 수집 완료!")
print("="*70)
print("\n📁 생성된 파일:")
for year in years:
    print(f"  - data/stackoverflow_{year}.csv")