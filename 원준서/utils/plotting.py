import matplotlib.pyplot as plt
import seaborn as sns

def set_project_style():
    """
    프로젝트의 모든 시각화에 일관된 스타일과
    한글 폰트를 설정합니다.
    
    (Windows 기준 '맑은 고딕'을 설정합니다. 
     Mac의 경우 'AppleGothic' 등으로 변경해야 합니다.)
    """
    # Seaborn 기본 테마 설정 (배경, 폰트 크기 등)
    sns.set_theme(style="whitegrid", context="notebook", palette="pastel")
    
    try:
        # 한글 폰트 설정 (Windows: 맑은 고딕)
        plt.rc('font', family='Malgun Gothic')
    except:
        print("Malgun Gothic font not found.")
        print("If you are on Mac, try: plt.rc('font', family='AppleGothic')")
        
    # 한글 폰트 사용 시 마이너스(-) 기호 깨짐 방지
    plt.rc('axes', unicode_minus=False)
    
    print("Seaborn style and Korean font (Malgun Gothic) applied.")