# 📊 업비트 실시간 모니터링 시스템

업비트 암호화폐의 거래량, 기술적 지표, 호가창 분석을 통해 매매 신호를 자동으로 탐지하고 텔레그램으로 알림을 보내주는 시스템입니다.

## ✨ 주요 기능

### 📈 거래량 분석 (4개 지표)
- **거래량 MA 돌파**: 20일 평균 대비 150% 이상 급증 감지
- **축적 지수**: 가격 정체 + 거래량 증가 패턴으로 세력 매집 포착
- **가격-거래량 괴리도**: 거래량만 급증 시 큰 움직임 예측
- **호가창 분석**: 매수/매도벽 변화로 지지/저항선 파악

### 📊 기술적 지표 (5개 지표)
- **RSI (14)**: 과매수/과매도 판단
- **MACD**: 골든크로스/데드크로스 감지
- **볼린저 밴드**: 상단/하단 터치로 반등 예측
- **이동평균선**: 5일/20일 교차 신호
- **거래량**: 평균 대비 급증 여부

### 🎯 신호 강도 시스템
- **강력 매수신호 (⭐⭐⭐⭐⭐)**: 9개 지표 중 7개 이상 일치
- **매수 준비신호 (⭐⭐⭐)**: 9개 지표 중 5-6개 일치

### 📱 실시간 알림
- 텔레그램 봇을 통한 즉시 알림
- 엑셀 파일에 자동 기록 (최근 100건 유지)

## 🚀 설치 방법

### 1. 저장소 복제
```bash
git clone https://github.com/YOUR_USERNAME/upbit-signal-monitor.git
cd upbit-signal-monitor
```

### 2. 필요 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 3. 설정 파일 생성
```bash
cp config.example.py config.py
```

### 4. 텔레그램 봇 설정

#### 4-1. 봇 생성
1. 텔레그램에서 [@BotFather](https://t.me/botfather) 검색
2. `/newbot` 입력하여 새 봇 생성
3. Bot Token 복사

#### 4-2. Chat ID 확인
1. 봇과 대화 시작 또는 그룹에 봇 초대
2. 아래 URL 접속 (YOUR_BOT_TOKEN에 실제 토큰 입력)
```
https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
```
3. `"id":` 뒤의 숫자가 Chat ID
   - 개인 채팅: 양수 (예: 1234567890)
   - 그룹 채팅: 음수 (예: -1001234567890)

#### 4-3. config.py 수정
```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"
```

## 💻 사용 방법

### 로컬 실행
```bash
python upbit_monitor.py
```

### GitHub Actions로 자동 실행 (추천)
1. GitHub 저장소 Settings → Secrets and variables → Actions
2. 다음 Secret 추가:
   - `BOT_TOKEN`: 텔레그램 봇 토큰
   - `CHAT_ID`: 텔레그램 Chat ID

3. `.github/workflows/monitor.yml` 파일이 자동으로 5분마다 실행

## 📁 프로젝트 구조

```
upbit-signal-monitor/
├── .github/
│   └── workflows/
│       └── monitor.yml          # GitHub Actions 자동 실행
├── .gitignore                   # Git 제외 파일
├── README.md                    # 프로젝트 설명
├── requirements.txt             # 필요 라이브러리
├── config.example.py            # 설정 예시
├── upbit_monitor.py            # 메인 코드
└── upbit_signals.xlsx          # 출력 파일 (자동 생성)
```

## 📊 출력 예시

### 텔레그램 메시지
```
🔥 [BTC] 강력 매수신호 ⭐⭐⭐⭐⭐
━━━━━━━━━━━━━━━━━━━━━
💰 현재가: 95,234,000원

【 거래량 분석 】
✅ 거래량 MA 돌파: 2.3배
   └ 20일 평균 대비 2.3배 ▶ 강력신호

📈 축적지수: +45.0%
   └ 가격 정체(2.1%) + 거래량 증가 ▶ 세력 매집 의심

⚡ 가격-거래량 괴리: 15.2
   └ 거래량만 급증 ▶ 큰 움직임 임박

📊 호가창: 매수/매도 비율 1.80
   └ 매수벽 우세 ▶ 지지선 형성

【 기술적 지표 】
✅ RSI: 28.0 → 과매도
✅ MACD: 골든크로스
✅ 볼린저: 하단터치
✅ 이동평균: 상향돌파
✅ 거래량: 평균 대비 230% → 급증

━━━━━━━━━━━━━━━━━━━━━
🎯 종합판단: 9/9 지표 일치
⏰ 발생시각: 2025-11-22 17:35:22
```

### 엑셀 파일
| 시간 | 코인 | 신호강도 | 현재가 | 거래량비율 | RSI | 판단 |
|------|------|---------|--------|-----------|-----|------|
| 2025-11-22 17:35 | BTC | 9/9 | 95,234,000 | 2.30 | 28.0 | 강력매수 |

## ⚙️ 설정 커스터마이징

`config.py` 파일에서 다음 값들을 조정할 수 있습니다:

```python
# 스캔 주기 (초 단위)
SCAN_INTERVAL = 300  # 5분

# 거래량 임계값
VOLUME_THRESHOLD_WATCH = 1.5   # 150% 이상 주목
VOLUME_THRESHOLD_STRONG = 2.0  # 200% 이상 강력신호

# 신호 강도 임계값
SIGNAL_THRESHOLD_STRONG = 7  # 강력신호
SIGNAL_THRESHOLD_MEDIUM = 5  # 준비신호
```

## 🔒 보안 주의사항

- ⚠️ `config.py` 파일은 절대 GitHub에 업로드하지 마세요
- ✅ `.gitignore`에 자동으로 포함되어 있습니다
- 🔐 GitHub Actions에서는 Secrets를 사용하세요

## 📝 라이선스

MIT License

## 🤝 기여

이슈와 PR은 언제나 환영합니다!

## 📧 문의

프로젝트에 대한 질문이나 제안사항이 있으시면 이슈를 등록해주세요.

---

⭐ 이 프로젝트가 도움이 되셨다면 Star를 눌러주세요!
