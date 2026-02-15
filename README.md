# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-15 01:25:54 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,617,933,955** | 🟢 +0.03% | 🔴 -0.29% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [OKX Ventures backs RWA stablecoin with Securitize, Hamilton Lane - MSN](https://news.google.com/rss/articles/CBMixAFBVV95cUxQbmxUeEp5TWNsal9jVDJ3U1BoQl9BWmNENllZdVVLd21laExtc0NaV3Q4aGZEYUZTaWJmclVRU3lpM1pqOVBwX3dTUmxGV25ZYXcxTEdEdTktN09SMVRDTkFiVUpST1JYa2FnTVVBYVQ0OGw5ZjE2WW9jV0pETmtidHNzQnozUWhSWTh1MUxlWWZTODVaNDJPNHlxYS1wMUlNaUxNYmxhY3FPVGVCNFFiTlN6NzU5Wi16UEt3ZVlPZ3FkMXd4?oc=5) (Sat, 14 Feb 2026 16:19:36 GMT)
- [Crypto group counters Wall Street bankers with its own stablecoin principles for bill - CoinDesk](https://news.google.com/rss/articles/CBMixwFBVV95cUxNNDFOV3Zkd3poWHhiVXM2V3dTY3pySGh2RVY4OUJWWkZ6cUZmTk01Qm1oTmVSaXFsN3F4a0FOeTgyZi10NTFjbVVwSEV0TlQ2dGc0d3RUQnVyby1LeGEwdmN2dEFLd0ZmcWxoSlZWODFRWTY2SFpSWlZ4NmZMYnhtTl9RUGFGSlZVdUp3S0s4OXp1VnJzRTJWcUVOTENuYmxhYzcwTmxJMlEySVA5UkNYVzdUeFpMZ1FCc01xNE9PX0o2TzRSOTlV?oc=5) (Sat, 14 Feb 2026 11:21:40 GMT)
- [Brazil to Propose 3.5% Tax on Stablecoin Purchases and Remittances - Bitcoin.com News](https://news.google.com/rss/articles/CBMilgFBVV95cUxQUGhLeXBDU0hkNUw2Nmw0X202b0xtRVpYSnZCNGppcGFIYWFXemNIa3lBcDkwU0xLX1RNMVZEdl9obm9FeHN3T3VWMTByWEJ3UTlobVJSRXVXcG1qbWdTNlgwbmxDQ2lSS1BUVXRMNTZSWk5zdjFhX1c0UG01aEhUZTM0aU5XMC1JeDVfUlU0OXBTOUpocVE?oc=5) (Sat, 14 Feb 2026 10:39:41 GMT)
- [Stablecoin Airdrops and 1,000 USDe Jackpot: Bybit Earn Announces Valentine's Day Surprises for New Users - PR Newswire](https://news.google.com/rss/articles/CBMi7wFBVV95cUxQRU12V2ZubFM5bGNTQ1VRRHAwUDduMTVfZmZXcm1xcDd6S0NVU3pobG9xWXR2Rzh2ZDJjRmJlcnNwblFtQ1d5SGhxUWVBQ01ZOVdpTFZCbC02bTZMM3JLU0toYmc5T0RVcjhMNkNoWk1mQ0QtQkxQUThaSE9KQUNHMjd4NTBfdFI1V1FtdDZkVUE2TkxrNVZPQks5WDU3eGJsSkRYQXZ0aDBnTkFyb1FqOVBQZjNRVjdhSTBTeDFvWWpya19XWENWUVFpcUxoNEZrczlNejAyTVNLNmxPNi1Yb01mbWI5MldteERyUFNUUQ?oc=5) (Sat, 14 Feb 2026 08:07:00 GMT)
- [White House crypto adviser says banks shouldn't fear stablecoin yield - TradingView](https://news.google.com/rss/articles/CBMizgFBVV95cUxNWmlQdFgxZlhxUE1SY0RrTk80eXRNU3lnbG4wc3Z0d09xMjRkTUF5clBiMkkxSXpacXF5NFpaWVBSTXFiUEFkWXZQSVUyaW9jXzlUdGo0MEctSVdSclZsenNUQ3MwNDZkTVlKdGtrZnc1ZmVud1BfWHZtdDd4SGNTaUhpQ1dPN0FjSGdPQXlfXzFNUHllTEJmZ3l6YWNJaHNtSng1YmxxbHRKdHhMVW40V1UtZ0k2a3hzY3VoWVc0VFN2em1tbjRRUjVjTmhrdw?oc=5) (Fri, 13 Feb 2026 21:54:56 GMT)

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
