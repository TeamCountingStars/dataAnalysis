import requests
import pandas as pd
from datetime import datetime
import time
import os

class ComprehensiveStackOverflowCollector:
    def __init__(self, api_key=None):
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
        
        print(f"\n🔍 '{tag}' 태그 수집 중...")
        
        while page <= max_pages:
            params['page'] = page
            
            try:
                response = requests.get(url, params=params)
                
                if response.status_code != 200:
                    print(f"  ❌ 에러: {response.status_code}")
                    break
                
                data = response.json()
                questions = data.get('items', [])
                
                if not questions:
                    break
                
                all_questions.extend(questions)
                
                quota_remaining = data.get('quota_remaining', 0)
                has_more = data.get('has_more', False)
                
                print(f"  [{page}/{max_pages}] 📦 {len(all_questions)}개 | 남은 요청: {quota_remaining}")
                
                if not has_more:
                    break
                
                page += 1
                time.sleep(0.3)
                
            except Exception as e:
                print(f"  ❌ 에러: {e}")
                break
        
        print(f"  ✅ '{tag}': {len(all_questions)}개 수집 완료")
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
    
    def collect_multiple_tags(self, tags, from_date, to_date, max_pages=20):
        """여러 태그 순차 수집"""
        all_questions = []
        tag_stats = {}
        
        print("\n" + "="*70)
        print(f"📅 기간: {from_date.strftime('%Y-%m-%d')} ~ {to_date.strftime('%Y-%m-%d')}")
        print(f"🏷️  수집 태그: {len(tags)}개")
        print("="*70)
        
        for i, tag in enumerate(tags, 1):
            print(f"\n[{i}/{len(tags)}] ", end="")
            questions = self.get_questions_by_tag(tag, from_date, to_date, max_pages)
            
            all_questions.extend(questions)
            tag_stats[tag] = len(questions)
            
            time.sleep(1)  # 태그 간 1초 대기
        
        # DataFrame 변환
        if all_questions:
            df = pd.DataFrame([q for q in all_questions])
            
            # question_id로 중복 제거
            df_unique = df.drop_duplicates(subset=['question_id'], keep='first')
            
            print("\n" + "="*70)
            print("🎉 전체 수집 완료!")
            print("="*70)
            print(f"총 수집: {len(all_questions)}개")
            print(f"중복 제거 후: {len(df_unique)}개")
            
            print("\n📊 태그별 수집 현황:")
            for tag, count in sorted(tag_stats.items(), key=lambda x: x[1], reverse=True):
                print(f"  {tag:25s}: {count:4d}개")
            
            # DataFrame 형식으로 변환
            final_df = self.questions_to_dataframe(df_unique.to_dict('records'))
            
            return final_df, tag_stats
        
        return None, tag_stats


# ========== 2023년 AI 관련 전체 키워드 수집 ==========

collector = ComprehensiveStackOverflowCollector()

# AI 관련 핵심 키워드 (RQ2 검증용)
ai_keywords = [
    # ChatGPT 관련
    "chatgpt",
    "gpt-4",
    "gpt-3.5",
    "gpt-3",
    "openai-api",
    
    # AI Agent 관련
    "ai-agent",
    "autonomous-agent",
    "langchain",
    "autogpt",
    
    # Vibe Coding 관련 (프롬프트 엔지니어링)
    "prompt-engineering",
    "prompt-design",
    
    # AI 코딩 도구
    "github-copilot",
    "ai-assisted-coding",
    "code-generation",
    "ai-code-review",
    
    # LLM 관련
    "large-language-model",
    "llm",
    "generative-ai",
    
    # 기타 AI
    "machine-learning",
    "artificial-intelligence",
    "deep-learning",
    "neural-network"
]

print(f"\n🎯 수집 대상: {len(ai_keywords)}개 키워드")
print(f"📅 기간: 2023년 전체")

# 2023년 전체 데이터 수집
df_2023, tag_stats = collector.collect_multiple_tags(
    tags=ai_keywords,
    from_date=datetime(2023, 1, 1),
    to_date=datetime(2023, 12, 31),
    max_pages=20
)

# 상세 분석
if df_2023 is not None:
    print("\n" + "="*70)
    print("📊 상세 통계")
    print("="*70)
    
    # 기본 통계
    print(f"\n총 질문 수: {len(df_2023)}개")
    print(f"답변된 질문: {df_2023['is_answered'].sum()}개 ({df_2023['is_answered'].sum()/len(df_2023)*100:.1f}%)")
    
    # 조회수/답변/점수 통계
    print(f"\n조회수 통계:")
    print(f"  평균: {df_2023['view_count'].mean():.0f}")
    print(f"  중앙값: {df_2023['view_count'].median():.0f}")
    print(f"  최대: {df_2023['view_count'].max():,}")
    
    print(f"\n답변 수 통계:")
    print(f"  평균: {df_2023['answer_count'].mean():.1f}")
    print(f"  최대: {df_2023['answer_count'].max()}")
    
    print(f"\n점수 통계:")
    print(f"  평균: {df_2023['score'].mean():.1f}")
    print(f"  최대: {df_2023['score'].max()}")
    
    # 월별 집계
    df_2023['year_month'] = df_2023['creation_date'].dt.to_period('M')
    monthly_counts = df_2023.groupby('year_month').size()
    
    print(f"\n📅 월별 질문 수:")
    for month, count in monthly_counts.items():
        print(f"  {month}: {count:4d}개")
    
    # 주요 태그 분석
    print(f"\n🏷️  가장 많이 등장한 태그 (Top 15):")
    all_tags = []
    for tags_str in df_2023['tags']:
        all_tags.extend(tags_str.split('|'))
    
    tag_counts = pd.Series(all_tags).value_counts()
    for i, (tag, count) in enumerate(tag_counts.head(15).items(), 1):
        print(f"  {i:2d}. {tag:25s}: {count:4d}회")
    
    # 상위 10개 인기 질문
    print(f"\n⭐ Top 10 인기 질문 (조회수 기준):")
    top_10 = df_2023.nlargest(10, 'view_count')[['title', 'view_count', 'answer_count', 'score', 'creation_date']]
    for i, (idx, row) in enumerate(top_10.iterrows(), 1):
        print(f"\n{i:2d}. {row['title'][:70]}")
        print(f"    👁️  {row['view_count']:,} 조회 | 💬 {row['answer_count']}개 답변 | ⭐ {row['score']}점 | 📅 {row['creation_date'].strftime('%Y-%m-%d')}")
    
    # CSV 저장
    if not os.path.exists('data'):
        os.makedirs('data')
    
    filename = 'data/stackoverflow_ai_2023_full.csv'
    df_2023.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"\n💾 전체 데이터 저장: {filename}")
    
    # 월별 통계 저장
    monthly_stats = df_2023.groupby('year_month').agg({
        'question_id': 'count',
        'view_count': 'mean',
        'answer_count': 'mean',
        'score': 'sum'
    }).rename(columns={
        'question_id': 'question_count',
        'view_count': 'avg_views',
        'answer_count': 'avg_answers',
        'score': 'total_score'
    })
    
    monthly_stats.to_csv('data/stackoverflow_ai_2023_monthly.csv')
    print(f"💾 월별 통계 저장: data/stackoverflow_ai_2023_monthly.csv")
    
    # 태그별 통계 저장
    tag_stats_df = pd.DataFrame(list(tag_stats.items()), columns=['tag', 'count'])
    tag_stats_df = tag_stats_df.sort_values('count', ascending=False)
    tag_stats_df.to_csv('data/stackoverflow_tag_stats_2023.csv', index=False)
    print(f"💾 태그별 통계 저장: data/stackoverflow_tag_stats_2023.csv")

print("\n" + "="*70)
print("✅ 모든 작업 완료!")
print("="*70)