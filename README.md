# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-26 06:07:50 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$270,990,515,740** | 🔴 -0.25% | 🔴 -0.92% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [HSBC sees over 100,000 users of its stablecoin in first month since launch - South China Morning Post](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQYTdtYTU5YkNZeWJuWXY1VnRPYm1haFFsSEtsa2ZCdW1semlqNkQyNVZJNkdmanVYTWNoelM5bl9pS1RFNHlDd1pyRk9XaVE5VnYxelVCbUQ3N2h2T1BqVGZ1TlpCenItVGVrUk52bDc1c3F6ekNWUWwtcjBXbUxNOVNrR3RaWWdsRmJSVlpfd1Y3a1Z4REpsUTk3d3JIdms0dGhoRzFPVFRmTGM?oc=5) (Thu, 26 Nov 2026 03:00:11 GMT)
- [BlackRock Launches Its First Tokenized Fund in Asia, a Hong Kong Dollar Money Market Fund Open to HKDAP Stablecoin Subscriptions - HedgeCo.Net](https://news.google.com/rss/articles/CBMi-AFBVV95cUxPWjBnX24wcEhXRmNFbkxYQ3lVVl9xMWFtSXVsc1F4dHpoaDB0OUo1cnl0cnd3SlM2Sm9xTl9BM0tjMnY5bFZldzV4czdSYkRwMEtXSEJCTHBfZzNHQ3pWXzZEUU83cDdyaWtVU1pnY05CdlNyaE84amN1Nk9hSFRzZDZHUXJxN0lLNmZLZDhweFJUWFBMYnB4b0tnQm9CUzRiYUl5a0hCMjlRLUk0Wm4wNTRSWDNqM1ptNlFjT3V4QUpMNXpnRFBJM3JBZ1VMcGJ1bXpsMkJlSzBzcWVMWnN1RVpwcFc1NEJzUURGUkxDWlY1YWp3ck5NNQ?oc=5) (Wed, 25 Nov 2026 21:51:12 GMT)
- [EBA cautions over stablecoin risks in decentralised finance, eyes MiCA review - INSIGHT EU MONITORING](https://news.google.com/rss/articles/CBMi2wFBVV95cUxOYkN5Nmp0U1JEYlU0WnJmbnZwb1VoUE5wcS1MQWljUXZTMUV0WTU5YXctQUZoQVNVUE9kdDZ2WXNLbjdqVkhPcmRVcGJFZVlKSHdqNmdudms5bFJaSklRRjZDdzVET3RybTNwa0EtQXo1NnlPWjZTSDRYNzZzNURCY1R1SXlKd2xLd1RZR2dfTXN6Q2UwcFVEVDB6LWN6dnFvUDdZSHM1QVUwbUhZNl9OdmlwX1owOXp4bTR4N2phTVEteGlVVUtMREZPUlRpdGdQOXVrU1pIeEpiRWM?oc=5) (Wed, 25 Nov 2026 21:40:14 GMT)
- [Stablecoin: what HR needs to know for payroll purposes - Canadian HR Reporter](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQZkNrR3I3a0JxbkRMWFM3NEtITkRSTUF0RXY1TV9RZm41cGRfZG1JZGRSXzhGeWY2a3lRSF9pdDI3Vmx1UlIxeXJFTlJXM3VmczFuSW9TMmYxS0k4c2FsbnlxZ2Q2UFMwY3Fid2JJVlUxSDM0ZDNpUVBnaE5KdlhUSGx1TjRBak12bTdiYWRuUzkxVW5oYTVWalVEQnU1MG1aOEF1cy1jU1I2cGs?oc=5) (Wed, 25 Nov 2026 20:11:50 GMT)
- [Payoneer gets conditional OCC approval for stablecoin bank - American Banker](https://news.google.com/rss/articles/CBMimgFBVV95cUxQRV9PMHlJYzVjYXZUYjNoR2tmcWpFdzZzTGtLcnVXeDZZTk9wZDdIcUdZUzRjazFFWk05ck1HOVlUcThraVVNa2t1R3pZOVVneUxQVEJuVHI2Qmp4ZDJDcHR5Q1ZUem0zYTNJYm82X1g4Q3dBTGZWbDNVWEx4M0ZqQ1RHZUtDZzBBNkJDNUlYNnh5ZWdrMGZFWC1n?oc=5) (Wed, 25 Nov 2026 19:46:16 GMT)

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
