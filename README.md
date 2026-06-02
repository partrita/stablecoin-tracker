# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-02 02:47:14 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,546,158,196** | 🟢 +0.05% | 🔴 -0.94% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Who Is Who in the Banks vs. Stablecoin-Yield Battle - PYMNTS.com](https://news.google.com/rss/articles/CBMimgFBVV95cUxPamhmbzZYNWJodkJ6aGNPZEVBaHZJQllURUlCYnZ5OF9ZSkpyTEFGdDRtQjJ3b2RjMFdZek8xeDlTX25vWkFLZ2tzNk1VTEdIVm5FNnVhVmdsREwxQU0taDlwNU55RDRfTlVTb0Q4b2MxbXpxRHFHS3ZPYlNOSFQtVWlLRU81c0xEcDFndVNIeVdKR3h0Y0duRWJn?oc=5) (Tue, 02 Jun 2026 00:21:21 GMT)
- [GENIUS Act &amp; Stablecoin Regulation FAQ: What Broker-Dealers and Banks Need to Know - Nasdaq](https://news.google.com/rss/articles/CBMizAFBVV95cUxQM203amVKWFFCU2ZmNFNDcWlkYnZHYVpfNk9iMjR1VmNtTENFT3hoTEFUMk9FSEhkMTVBd3FGWU9MZmRBMXBTZnZsSjdDbUhvdDVTM2FxV1A5TnpBeGZFRVlRTEk1UnU5TnVOcF9fTVQ4VUxvUlp4bkU1Slp0NnVPM3FXVnZHWjZqcDI2UmQ5WFJ2WC11WjF5bFBuQTQ3bUlIWmdvVG0yS2NiZVQ0VlBVcFk0SWYxaC01UXpIaWpZRFJWcXF0RlptSDVJamQ?oc=5) (Mon, 01 Jun 2026 22:42:34 GMT)
- [Agentic AI has holes. Circle and Nium are trying to fill them - American Banker](https://news.google.com/rss/articles/CBMilwFBVV95cUxQSVllM09aNE9zdHRNdWcwdWVpUmhlb2Y1c3VfbzEzMlI3bi14T3liNnlBZ2RZOHFydVZiaVNZSi11ZDdqamF6bGhaa2NoUllKNzdHU0VwWjJST2Q2QlkwdEFRUVVYcFF1NUd3Z0xock1neUhrY0JZR3FUNThwaUZYdzVvcnpWNEZjVFU0ZXRyT3pJT1hDa3NN?oc=5) (Mon, 01 Jun 2026 19:17:00 GMT)
- [SoFi Launches First Bank-Issued Stablecoin (SoFiUSD) on Consumer Banking App - Loeb &amp; Loeb LLP](https://news.google.com/rss/articles/CBMivgFBVV95cUxPZ3lncWI4akNBeEJfU18wTVJtQkRER2RBMVEtUm1YWl9nREpDTFlFQ2dlODctLXNFSkVKekpNUGFfR19WOGxLdGdYeDE5TXVaWkljQVUtOWpRaGdNR0FkTVA3THZ1dW5qSUNRQ2FFcldMOUZIdDBYQ25JSnctV1pYX3MwMGN1eW94a29oRXFDc3FnYjlNNnZxbXphYW41N0tlWjdaNkRpeTJvVkJrb1BQT2k4MHMybVJDUDJYaWl3?oc=5) (Mon, 01 Jun 2026 18:23:06 GMT)
- [Stablecoin rewards: JP Morgan’s Dimon says Coinbase CEO is full of s!!t - ledgerinsights.com](https://news.google.com/rss/articles/CBMioAFBVV95cUxPUUFQaXZMazIzUDFFeFh4alcwX2RUNFh6Mm9hak0tTWRWOVd2UTVxeW1GcUFuR2dsODg4WWpGS0k2NUtvb21RdHExd0R0Qi01N0ltWDlFcEhvZU1MSjhJTE41X3RUd09qZzJWUU9TSHlwNHMwWkdEcmtyWUdJVFF4OGE3VmVVMi1SVktmUl84Y2xKeGZ4bVhmTG5jS3BFMVZa?oc=5) (Mon, 01 Jun 2026 15:15:00 GMT)

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
