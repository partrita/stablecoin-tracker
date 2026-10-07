# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-07 03:30:22 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,906,162,790** | 🟢 +0.05% | 🟢 +0.28% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [OKX Launches Standalone Stablecoin App, With Up to 10% on USDG Balances - Blockhead](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNeEVuV1RBUGtxelNnR3d0Q0dzUlBVMnJOT0RadFRFUjlDREptd1FMV05pd200RXhheTlyZjNtUzVRaUVLaW9rMHJFa2VtMW5sbzBXZDl6Q2puanl1SGV2MUczUUZ2Qnh5T1J5OWVLNF9jRUpnSFZybndmNmRLYUhKQmNUV2FXR3dtdkxCLWdlbW9xVGNkUmVUaVdVZVRzVFJRM1lURi1jQmJqQQ?oc=5) (Wed, 07 Oct 2026 01:01:39 GMT)
- [Crypto Card Payments Hit Record $12.5 Billion as Stablecoin Adoption Surges - CryptoRank](https://news.google.com/rss/articles/CBMihwFBVV95cUxNd2hRY0JkeTZhS1VkYlVtaTZxYW9aZkJuOUNuTWFQV0xVek93aTV3U0lDT0hVVGlIckpXdW9keWVFWG1DUU5PaGV5dUFrVUl5Z3dVYnRPZ0NCOGdYNUREVjJIeWJZSGd5UUh4aVZEeTlHSXlxU2MtOFFwNkRtS2M1N2hWaXpILTA?oc=5) (Tue, 06 Oct 2026 22:20:40 GMT)
- [HSBC Prepares Hong Kong Stablecoin Launch With RedCoin Brand - Payments Industry Intelligence](https://news.google.com/rss/articles/CBMilgFBVV95cUxQYUtQM0k2NlZfcE1rWTJMcHpJank4a0F0TjJlQzdtVXZwYnVUdVpibndOXzA3YUZpQ3dXU2plN3FvWE1hSXpKR2ZWLVhIUVBxRVh0LUlPQldVeXA1VTVIeUI3cGVhaWZkZXN1Um42WWQ2YVZwZEJrWE5kOXM1dE1hRVZaSjZGY2tfOG5CVURzbmFlakZRaWc?oc=5) (Tue, 06 Oct 2026 21:57:05 GMT)
- [Majority of community banks express concern over stablecoins - American Banker](https://news.google.com/rss/articles/CBMinAFBVV95cUxQSVRkaXZMTXk2elpFMlJvNXYwSzExS3ZOeVlzdnVaeHgtb0t4R05JcUEtdVQ0SS0wZVhXWlFWOFNGNXQwU1RuTXVabmxGaW9SbUl3X045Y3U1S0xBbG9PR2IyOWZla1hybFFlWHFZcUtqZ28zTHJlNXJkZHl2M3NCMTd5OFpEaVpIU1BpM2k5Q2VSM0F2TEE2VnZCczk?oc=5) (Tue, 06 Oct 2026 20:23:00 GMT)
- [The Fed and PYMNTS Intelligence Agree: Stablecoins Have a Demand Problem - PYMNTS.com](https://news.google.com/rss/articles/CBMisAFBVV95cUxPQzFadldzeFRkeVVVLXlFZG4yX2Y5WFpRUnVWSjdLZ2JzbGZ6NkxCRlFlWkwwaC1JQlY0RHN6dkFQVDNFR0ZOVFVvYWdRY0R1b1loSDE1dk9kT082X1puQUZQRXl3eEhYTFgtOHg3cnFkQ0M3TjRpcHdIczF4b3lQQ05La21JMHFwa0hnYk9yN2R1NGZuV0JFbDYzZGhKb1I0YlJ5dWVFTjI3WmZKd0ZWWA?oc=5) (Tue, 06 Oct 2026 19:54:59 GMT)

<!-- END_dashboard -->

주요 스테이블코인의 시가총액(Market Cap) 변화를 추적하고 시각화하는 프로젝트입니다.
매일 자동으로 CoinGecko 데이터를 수집하여 시장 흐름을 한눈에 파악할 수 있습니다.

## 📂 프로젝트 구조

- **`data/`**: 수집된 데이터(`csv`)와 시각화 결과물(`png`)이 저장되는 폴더입니다.
- **`src/`**: 데이터 수집 및 시각화 스크립트가 위치합니다.
    - `fetch_daily_data.py`: 현재 시점의 상위 10개 스테이블코인 시가총액을 가져와 CSV에 추가합니다.
    - `generate_plot.py`: 누적된 데이터를 바탕으로 그래프(선 그래프 및 파이 차트)를 생성합니다.
    - `update_readme.py`: 최신 데이터를 바탕으로 `README.md`의 대시보드 섹션을 업데이트합니다.
    - `get_coingekodata.py`: 특정 코인들의 전체 과거 데이터를 한 번에 수집할 때 사용합니다.

## 🚀 시작하기

이 프로젝트는 Python 패키지 매니저인 [uv](https://github.com/astral-sh/uv)를 사용하여 의존성을 관리합니다.

### 설치

```bash
# 의존성 설치
uv sync
```

### 사용 방법

**1. 일일 데이터 수집 (Daily Update)**

현재 시장 데이터를 가져와 `data/stablecoin_marketcap.csv` 파일에 추가합니다.

```bash
uv run src/fetch_daily_data.py
```

**2. 그래프 생성**

수집된 데이터를 기반으로 시각화 이미지를 업데이트합니다. (선 그래프 및 시장 점유율 파이 차트 생성)

```bash
uv run src/generate_plot.py
```

**3. README 대시보드 업데이트**

최신 데이터를 기반으로 `README.md` 파일을 업데이트합니다.

```bash
uv run src/update_readme.py
```

**4. 전체 히스토리 수집 (초기화용)**

지정된 코인들의 과거 모든 데이터를 가져옵니다. (기존 데이터를 덮어쓸 수 있으니 주의하세요)

```bash
uv run src/get_coingekodata.py --output data/stablecoin_marketcap.csv
```

## 🤖 자동화 (GitHub Actions)

이 리포지토리는 GitHub Actions를 통해 **매일 00:00 (UTC)** 에 자동으로 데이터를 수집하고 그래프를 업데이트합니다.
(`.github/workflows/daily_scrape.yml` 참조)

## 💡 참고 사항

- **Cloudscraper 적용**: 일반적인 요청과 달리 실제 브라우저처럼 위장하여 Cloudflare 봇 감지를 우회합니다.
- **안전한 수집**: CoinGecko의 IP 차단을 방지하기 위해 요청 간에 적절한 대기 시간(`time.sleep`)을 둡니다.
- **데이터 인코딩**: CSV 파일은 엑셀 호환성을 위해 `utf-8-sig` 인코딩(또는 호환 형식)을 사용합니다.
