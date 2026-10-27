# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-27 03:03:47 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,943,864,021** | 🔴 -0.20% | 🔴 -0.58% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Circle exec urges room for banks, startups in Asian stablecoin regimes - Nikkei Asia](https://news.google.com/rss/articles/CBMivAFBVV95cUxPYmRjQnhXenlBQW13Z05ySExNME9fSmRHaDJmZ0Mxd2F2RFFyU0lQckxseHVjbEdtaWlzYlVnN1JnM3RGZXMwdTRFZzJZdkp1WHpnampWOHVKVVhRS2I4ZTlwNEc5cGtPbmF3SWRsMDNuUEFUbEhLR21yVThUNzFqbFZidHR1RlBaVUNLRGhTOWRLaDhxbWZFM0pfOUhGWE4xSUszRkx6MEw3cGdfbFdHRGNOcHg4R2VjRkFsWg?oc=5) (Tue, 27 Oct 2026 01:26:00 GMT)
- [Visa’s Stablecoin Funding Moves Beyond the Pilot Stage - TradingView](https://news.google.com/rss/articles/CBMisgFBVV95cUxQY3VIUU5zYmd5SlZVNTRfUVJpdWV1T1VMN25ISkRNSERwSUdqWUtNMFBmTVVNZkRRV0R5akQzSUdhVVRxLXJfQ3VHS25xTm9rd1RxM2lFMmNWSERDV1NlVmhnd0p2YlNMQ0RHNm56SzE3MjYtaldJOExyR3VBbC01MS1RRUJoZUtmVU5pQ09TSjUzQ0dabmw5b1lSbXAySkFFXzEwNDRkcFo1eTVoN2tvNHFR?oc=5) (Tue, 27 Oct 2026 01:00:00 GMT)
- [Canada Opens 60-Day Stablecoin Consultation, Caps Redemption Fees At 1% And Bars Interest: 9 outlets compared - NewsCord](https://news.google.com/rss/articles/CBMi6gFBVV95cUxOV1JRcGRCM3FtYjFWdlFjdmlxQWJFVnRnNWNaOE4xdXk3RVZjYmhLcUg3Uk1taXNISEZIc3pmaFhsT29KNVByU19GVE5ldjgtLTI2OUJ4bXRhWmNkeFVodWJrSmdUa0FzUHJnTks2WUZOTDAxb201bkUwVFU1VXhWdm5HU0RUYnp5MjFtSENYYmRZZEYxLU42X2g2SWpkM0RIZkF4SU90NVBCdTRWSm03enN3NTlQTm1WbnJtNk1JVnY5a1V6c09ncDJ4Q3Z0TXo4UWtDRWRaYzJrOWtxb0w2ekw5eG40cXZIdXc?oc=5) (Mon, 26 Oct 2026 23:27:16 GMT)
- [Canada Stablecoin Rules Propose 1% Redemption Fee Cap - Bitcoin Foundation](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQR3ZNWjdIN1hwZDRSbWxaTGpaWVNKbERBQlIyWDd5Wk56SmRwQkZXTm95akt5WXU2SlA5UHBRQ2dDZW5Sb0xQOGVZak5XMWJvaFBDLXpyMjRCby03cm9UQkdVa1BXRVBEVzJJWUlDeWlzYWxjRXdVbzF5N0dnaEhFdDVUYWM1alhGTWhwOURNUzFCckJYbVI1ZWtieFNxTWJ5MUV6YmU1Tm5FbU0?oc=5) (Mon, 26 Oct 2026 22:55:18 GMT)
- [Canada’s Draft Stablecoin Rules Cap Redemption Fees at 1% and Ban Yield - Decrypt](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFlkdFBvR2gzQ1pWU2p1Ny1fSTAtc0ZzQXF6dG95bUo0RzZpV1RxZTdUaXgwVjBoajRNY2F3bm5idmN5cENxcmlOX29TVGhyNUJFQVU4eU1USExHODdKMjlPODlDTTRZMWxORnJIblRfUW82TkNDQjdIdGVOYm0tQnRBQUJvMHdR?oc=5) (Mon, 26 Oct 2026 22:16:03 GMT)

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
