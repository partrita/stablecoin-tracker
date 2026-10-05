# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-05 03:14:51 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,485,780,497** | 🟢 +0.06% | 🔴 -0.07% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Visa, Mastercard, Stripe, and Coinbase Commit $1 Billion to New Stablecoin: Is Open USD a Challenge to Tether, USDC, and RLUSD? - Yahoo Finance](https://news.google.com/rss/articles/CBMipgFBVV95cUxQaE4zNmxuT1g5ancxRVNJSWhlSHRlMXg4UGhzMmVuMXFjS2lzZ1RfNTNYclNqdF9hVU9XdjVZZ1F5bEtjZy1CTjA4RjN6TG9OVHZ1dG9CWERZM3hsYUpXNW1RRXlwbmRrMXJ3MWkzcnJqNW14R0JpcjBXZkgtR3BNczd4VWFWWFgzSWIxUVJmM1FhRU1pYldyWDk3RzRHLTFtZTV3Rm93?oc=5) (Sun, 04 Oct 2026 15:00:08 GMT)
- [Visa, Mastercard, Stripe, and Coinbase Commit $1 Billion to New Stablecoin: Is Open USD a Challenge to Tether, USDC, and RLUSD? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiigJBVV95cUxPVUFITnotYmk0M0hoOHNQWHZJMktIdXhRd05IV2ZuY0FCZldFbExyMW1UWUdYMEdLN3U1em9HMEZUVFNXZU9icjhhMnlpNjFydnBaZktwZHpzeGgyN19ZYXpOWlVGdVZ4ZUtxbWJpb2Z4M3ZxR3cyTWtlU1ZmUkZzZFV0Y2lvSFdfd3FqUEJ2eThmRzdGMURReWJuNjhUWS03REFHRC1wX2lBWTBIZDhRYkI1MFdQemMyTzNqSm5sRUxnN2NuaUpVem0xWF9nQXYwelA3ZUpSUE4zT3RuOTcxSWtpMmMxUF9ENUVYTUotOUlHOEl1SGFsSHFfcWhBaWF4MDNrUHFKRF9Vdw?oc=5) (Sun, 04 Oct 2026 15:00:00 GMT)
- [Tether Brings Its $184 Billion Stablecoin Back to Bitcoin: Will BTC Regain Its Role as a Payments Network? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi9AFBVV95cUxNYzZ0TWxMWTB6TUh6Z3hMVl9COTAwSldXbmlmZU5mUVg5aFYwZEx5VmE0eV9KcWt1YWNJN1lmc0w4NlkyVWRNUGtJLUxWbmF0dkhROC1jTGJ2eHVyY08yY1VoU29EZ25YRHpfeHk1RW9XVU4zYlo1aE16QXA3c1YtSTR0NDFrTWw5V1dDeERJUXhia3NQSE5OMFJKbDRnUDN5akYyTXhLRDJhUnlyTm1oVWdoN2Nfb3hwMjJLXzVTSXlXWHE0RXBSS3pxMERnZVk5dUJWRnVDclBrR3ZFalRFVWV2OEpRd3VTRG1VZkRXa0o2ZVM3?oc=5) (Sun, 04 Oct 2026 13:00:00 GMT)
- [Can Coinbase (COIN) Turn Citi’s Stablecoin Partnership Into a Durable Institutional Advantage? - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxQeHJSUGw2Z0lYdEE0azh4blFwZFJpYmpZN2xVNnNyWUVHZTNfMXZ6UktOOXRHeklaX0xrdVpBOE9FVzNnYmkxSXYwVktxMEw2U0hWQlludS1xSUZFRndSMTdzVVBRdGhvay1XUXJkVzI1SnQzOGVnUFUwUDdtOE14RGdZYXpIVGpDRTJUVTlhaDJLcmlrT3E2UnJjdVZwX1hF?oc=5) (Sun, 04 Oct 2026 02:09:00 GMT)
- [SoFi’s US$25 Billion Card Portfolio Shift To Bank-Issued Stablecoin Might Change The Case For Investing In SoFi Technologies (SOFI) - Yahoo Finance](https://news.google.com/rss/articles/CBMikgFBVV95cUxNdWN2Q2tYbXVvejlQWndFcl91SXZfV0pBNnBKTTl6ZFRCU1NMaDFEWHc4cXllZjR1STR3eFJEbFRIdGZrTUs1dVA3TkxhRmI5RXRwbHlFVVFJU1JiNFV1UW8xSi1sVm5JeXVxTXN5blhhWF9TRS1Nam80bEN6TmdVN2VPQ2tBYXBaOGpTY3VKSUZjUQ?oc=5) (Sun, 04 Oct 2026 02:08:00 GMT)

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
