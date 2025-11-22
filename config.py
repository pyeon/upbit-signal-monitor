# ============================================
# 업비트 모니터링 시스템 설정 파일
# ============================================
# 
# 사용법:
# 1. 이 파일을 'config.py'로 복사
# 2. 아래 값들을 본인의 정보로 수정
# 3. config.py는 .gitignore에 포함되어 있어 GitHub에 올라가지 않음
#

# 텔레그램 봇 설정
BOT_TOKEN = "8230667492:AAG2_-o3dd3VLMdVqi9s-jTzslcBYFA5ej0"  # 텔레그램 BotFather에서 받은 토큰
CHAT_ID = "-5091161755"      # 그룹 ID (음수) 또는 개인 ID (양수)

# 모니터링 설정
SCAN_INTERVAL = 300  # 스캔 주기 (초 단위, 300 = 5분)
VOLUME_THRESHOLD_WATCH = 1.5  # 150% 이상 주목
VOLUME_THRESHOLD_STRONG = 2.0  # 200% 이상 강력신호

# 신호 강도 설정
SIGNAL_THRESHOLD_STRONG = 7  # 7개 이상 지표 일치 시 강력신호
SIGNAL_THRESHOLD_MEDIUM = 5  # 5개 이상 지표 일치 시 준비신호

# 출력 파일 설정
EXCEL_FILE = "upbit_signals.xlsx"  # 엑셀 파일명
