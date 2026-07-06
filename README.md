# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-06 02:25:19 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,775,492,714** | 🟢 +0.11% | 🔴 -0.94% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Circle (CRCL) Faces A New Stablecoin Challenge As 140 Partner OUSD Launches - Yahoo Finance](https://news.google.com/rss/articles/CBMipgFBVV95cUxObmt0OV9aVWM4clprRktib1FVaU02UHp1LW4yZTlyd2FpUW9uNWlJdGtFcEFsNDNwUXozenlWYVBNNXR6QVZUbFFRTHA1TEYxeTZxeHVHVnZDV0NkUm5zMHdtWEtubXNpT0hqMTRJelM2a1ZndW83b1h2SzN6M0dCUDRVRmZEbFFpNHNGXzRfR012X1J1OEY2c3hURG1ldno3V1hJWkZB?oc=5) (Sun, 05 Jul 2026 14:08:23 GMT)
- [How big banks plan to capture a quadrillion-dollar market - CoinDesk](https://news.google.com/rss/articles/CBMiywFBVV95cUxPVFRIMnI4UHBRMGxzcEFxakdVd3JPcGVzaFQyVEVLdXJHeXBLekZydDZCNTJtYjZmdEptRUQtdTZFZ29MQlZYMXdWdFFvM1A0dlEzZHNSY19nQnNWY3FCNXE0U09TaG9WVW15aVFNbkNOYVJhR0Y5WFBWOGo5YXNPXy1aMUpEN3BrTHRHd19KRFFzb3lFYXh5M05EOWMycUhHY01PZUg3MzhnTF9wNXpfQjBTX25FaVNBZXowZ19WQm5PQ0U3NzNaWDd0SQ?oc=5) (Sun, 05 Jul 2026 14:00:48 GMT)
- [Collateral, not yield, will decide which stablecoins win - CoinDesk](https://news.google.com/rss/articles/CBMinwFBVV95cUxNWUpzcEdDZTRtN0pGMGVBSGpETy1ZRm1sVXZkSGNPRlJYLWloM1Faa2Eyd0FVYWsyamVJYmQybVNTcVB4OW9xU1lqMlpVbkhyNEhuQ2QtTUVYaTliWU81cUh0cEJUQ1JYSXdsQkpueGhHaTJXVGtfTUg0aFBiTjhSYlZQNEtfR3ZGMHhsbGVkUkxBci0zRmNvZjE3bUVjTGM?oc=5) (Sun, 05 Jul 2026 13:02:27 GMT)
- [Why Binance’s reported $2B Mesh investment could decide who controls stablecoin payments - CryptoSlate](https://news.google.com/rss/articles/CBMilwFBVV95cUxQNWhpZEgwOTRXd3JUV1pNenRzcXh6VzV6elA0d1g5dmRyYm9TQWMxUnQ1Tk9RTjBTb0l0SVl3VUthQXlZVk4yZE8ycDdlRzN1S1RDajFqRUxSczQzZGxNRXNaMVBGSi1VX242bUxnbWdxUEpoSXlDUDlzejB3UkhiUXpBM1Zabmk4WGJfVTRCODNDejhRZEFJ?oc=5) (Sun, 05 Jul 2026 10:00:28 GMT)
- [Coinbase (COIN) Joins Visa And Mastercard To Launch Open Standard Stablecoin Network - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxQeTItMERYbVkxRHN2cnM0YkZkYXNpNnc0REJaVWZVMGJHcC1VR1NIQVhRNzdFakR3bFZmN0hfTnZxSERrbXpYV29ocmVPQWx0WHJmWnk5czdfdVFKVlBaOERsV2MyRThENmNyUGlTWFB4VWVjcXU1OGl5dWgyRUtwck5yMkM1SG1XWjZ6b2Npd3M5elBja1hDYl9lQzBycXlIUWc?oc=5) (Sun, 05 Jul 2026 06:11:00 GMT)

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
