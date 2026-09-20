# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-20 02:35:58 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,901,222,094** | 🔴 -0.00% | 🟢 +0.01% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Treasury Drew the Line Between Stablecoin Issuers and Everyone Else. The Stakes Are Not Equal. - forkast.news](https://news.google.com/rss/articles/CBMitAFBVV95cUxPVGxRNnZLMHFwRXY4S3VkZGZVcGNQWjhmaERQY3ROb1ZzMlVhTVVZZ2o3VE5mWE5KbmstNmxDTFVXbUl0eDJOZGhWVF9rdzZ5a3JtS09WV285b0liUjJWQlB5dlZkVkc3WEZJcFJmNGtIbHZ6cENpOW9ESEhjbGZxT0d2Z182TV8tTFBZcFVTVTZULWdGQWhWaVhSWXlqelQwY2RQX0txdWdEWDdBelZvZUFWLWQ?oc=5) (Sat, 19 Sep 2026 23:40:53 GMT)
- [Stablecoin Reserve Requirements Explained - The Block](https://news.google.com/rss/articles/CBMilAFBVV95cUxNMk1SUU9qaUpfM084TWZ2R3VVZjRiMWZQbENydlFJdV9Yc2E0czFjOXltaFAzWjZTWnBJaFYybFFhZFFVenZmOWlCUC1SaVlfTC1FSDFReHhQTUFSYkV2SmhDclVWaXVhQjdaeWFKN0NPdnB2SDJ4WFV2bVloZzNabjNjOWFWUko4VHhEdUlOZmF0cDZ0?oc=5) (Sat, 19 Sep 2026 20:13:37 GMT)
- [Injective: USDC Becomes the Canonical Stablecoin Standard Across 20+ Chains - 19 Sep 2026 - TradingView](https://news.google.com/rss/articles/CBMi4wFBVV95cUxQOTFhdldZajZNcEwza0I1dGVkQWcxQUYycEZsRjhSYTBablB1WVpBRFRRY3hTZ0xoWUpRTVZPUktSQlRBaW9xQ2JXZU8xT1ZaWDZJMHNnakIwYmcxa2k5c1pCWU9pSjV2QXlVekItZ2VZcHBjLU9KS1U4d3ZmWmJHYzBtRmJRbEJNWkNzMUFzUS12MGh2bm9iQS1CVlFHVXFWekthbjJUdnAxaUw4NkR5d3FiWVE2MFVjTjNocmZlS0kxUXBrREVlVjdaajU3MDZfUmdjUy16NzdMSVIxcDl2UGttdw?oc=5) (Sat, 19 Sep 2026 20:00:56 GMT)
- [dtcpay Raises $25 Million Series A As SBI Group Backs Regulated Stablecoin Payments Platform - Pulse 2.0](https://news.google.com/rss/articles/CBMisAFBVV95cUxOcTcwdi1lVXVPSFZNR0ZSc01BanVYampVSHF1aVcxTENxVlZtU0FrLTlqMzhwX3FVWlFmSElGXzh0QklFYXVEU29sY1FNcTMxX0M4TllEb0FadkxCTWQtQVpFb1gwQ3ZsSGhFNGczWkFJcFNETi1LM1BKZXlXY1ZWSmFsSFM4M1piMWxERmV2S2c5WnNVUEVsbzRhOC1lM0hjZksxeDdYRjhRcXFwUG1tTtIBtgFBVV95cUxPZDF5U2FIal90WVhoSk9jTW9WS0Zsdkl2RVVvTm82UzNGbHVYUjZrNElQaUZ2TDFjYVJZYmtQMncxcDQ2aVJEUWJJTThtRXp4ZGpFOGIzWkhuSjFCbi16d05XZU5wQzEwT3dreG5DWmtQNWVKc2RTN3lSc3hSVnpsVDZOaWQ0ODRPSWF4a3J5b3ZMNnhfM0RXUUdYTGpRS253cWVPYUE3WjRFWFRsWUl6bjFLT3hHZw?oc=5) (Sat, 19 Sep 2026 12:52:50 GMT)
- [Tokenized Deposits, Stablecoins, and the Interoperability Challenge - Oracle Blogs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPV2Y1UXJKZTZMOWhHWl9wbVdMdzhJdTA4STVkUzU4R1lYaE5IWmtmRWhnVm5PT3lyODJkemd4S0cyaGlJNHM0cjZCT0dCSi1oUVJ2LVJVZlFTblFaUHRzWGVYMjlaOFNPYVdRWnhhclRBNm9PNUNYSFhBTV9DUlZZMTI3WHJWVUg2bHdaS2w3M3laV0RJZk1MQmJWUzRYdFZ0cTByM0l3ZXhmV0dKQzdXREpySzFSTkFQ?oc=5) (Sat, 19 Sep 2026 09:01:53 GMT)

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
