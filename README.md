# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-07 02:11:54 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,921,850,317** | 🟢 +0.03% | 🔴 -0.03% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [MoonPay launches stablecoin platform for businesses - Finextra Research](https://news.google.com/rss/articles/CBMimgFBVV95cUxQQmhSVDZSNk5Bc1JnaUl6RDJ2Q1VKTk1ZMmxZRDZUWmtQRV9ZRHY4NU9rTk5IQWVjakNwYjJMSFJBbUFwM3dKN2N2VHhqcUM2eEdueHFGUkEwYzQ2TFVtUmlLcU9XYU5aUi1jdHZWUFVoT1h2SUVTaE9PMjZNV2FJVGZZc3hmNllVWjNJQ1M1V2VJRkhzc0tKRC1B?oc=5) (Thu, 06 Aug 2026 23:03:08 GMT)
- [Mastercard (MA) vs. Visa (V): Stablecoins or AI Fraud Defense? - Yahoo Finance UK](https://news.google.com/rss/articles/CBMifEFVX3lxTE1ZQ2NwNzdUMkFEaU40ZHNJdVJWSXgzdWE0a1luZlluZ0pVdG91Z094bWdlbWFHYjY4VTVsSlZwRS1HdHlFOXc4REVkUnB5YVZ5VkVwanQzaHdnX3dRZjgzN3hxdXI5MmgyOUk1bmtQMEhLd3RtMWFTbm9mQUQ?oc=5) (Thu, 06 Aug 2026 22:22:46 GMT)
- [Transatlantic Crypto Framework: What the US-UK Stablecoin Deal Means for Markets - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxQUUFuRUJkblJ0YUpraGdTZ0NkRXFIbWVDdjdpNmpKMzBDRWZNRzhycEQ0cXpkN1lPYXk3U0J0SVJrM0ItblpCUEo2VVZTZGMyeDhWYVliLTIzTzZQMFRhTzhMdWs2eTBvWjZFMkVkN3QyS1VLSU5wYllBdjJBZlBNXzdqS0pRV0F5SmxfX0ZVQmRRakl6VDhyRzRJRTVBcVl4X3NZ?oc=5) (Thu, 06 Aug 2026 14:52:11 GMT)
- [Japanese Yen JPYC stablecoin issuer extends Series B to $38m - ledgerinsights.com](https://news.google.com/rss/articles/CBMilgFBVV95cUxNcW9sSFlSQ2JsRVhrVFhfcnl0cFNkTXZzVkQ4OHY3bUtXWUI2ZG1YVko1ZFBvWDBJamdPclM3QTFFWjZLTlR4ZTFCLWhiLVJLaTlNX0EwTzBWeHZVeEJGQ3NxRjdsVUsxRDJ3RG1mY2J3ODRxZzJyOU9mY2d1QXV1LVotX3lTOGt2MlZ4QXl0NmtNUklKT1E?oc=5) (Thu, 06 Aug 2026 14:29:42 GMT)
- [Yellow Card Raises $40 Million To Expand Global USD Accounts And Stablecoin Infrastructure - Pulse 2.0](https://news.google.com/rss/articles/CBMirgFBVV95cUxNaldYNVR1R2NGU2xiWko2dUNpc0lMSEQ5bnJlQzd0LW1wWGJjdElfV3hXLVNsN2hkeld5am9UVVNhUW80YXJsRDdqWXhrSFlXT2NPMDdhY3owZGptMklfMVVuMDRnOFRUYTRYRWRrYlhRcC1NWi1OY05Vd0I5bTNIVExkR2NiYzJWSXpOdDZDbW1XbmRMcTlvS1AzY3pFWWtmTFQ3NFB3ZHFHQUdVNkHSAbMBQVVfeXFMTkg0NDc3b2JfR0RPYm0wSnNmd3RpcWpqYURma0tTU1MtUFQ0NW43cUFvQ1MwZFlTT3pXcmJ4WDdGY29ObWY1Y19JTm54dW9yYjJRX1lnR1VHX2x4LVl2c1NQazF2REktVDdRSFh0ZkFiYzE3YVRnTzc5R2E2VVNOMFhKMElyNVFEYnNWSzVNUjFPd1JrY3Q2QTNjR09Bc1BaXzFrS0pOd1I3Ml9uNFg1YV83NlU?oc=5) (Thu, 06 Aug 2026 14:13:11 GMT)

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
