# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-02 01:57:50 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,617,973,759** | 🟢 +0.02% | 🔴 -0.57% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Visa Stays Neutral As Open USD Draws Comparisons To Stablecoins USDT And USDC - Crowdfund Insider](https://news.google.com/rss/articles/CBMixAFBVV95cUxPbDB4TXIwV3hvY19VNGcyaC15OW1HRlVXYWFfYUlUdklRbGc4c2ZqMkNqcFhmWDBYb3VVbFJIYkIybmF6LWRQVlI0QlozZjVtMlprZ3g5MnVwelJIM0h6VVN5MG00VkpWVXllcjlsc0RlUXVSNHhFeXljSXZQbTJLUW9kMkNNREtxMFN3X1BlTFRHcm9pMjg4S2kyd0hiQk5JbHV5R3dNUEJRWnJlVFpJM0NCTHByU29RWVcxaTVfbXktN1JJ?oc=5) (Sat, 01 Aug 2026 22:56:34 GMT)
- [$7B net stablecoin outflow for 2026 as demand collapses - cryptoquant.com](https://news.google.com/rss/articles/CBMidkFVX3lxTFAtQUtsNVFiRkpLWGJ3Y2ttWGc2SlAzbkhfTXg4bTFtNzlaVk5UMXRvRUcyUW93cDdKNFZkRENiLVowb0EyOHl6Tk5hdFhXNEt6WFc3S2I2QTI2aXNsTjdHVzNTVklqd2FrMy02V09pdWxiNGZwZGc?oc=5) (Sat, 01 Aug 2026 17:59:27 GMT)
- [Bank of Italy research suggests stablecoins aren&#x27;t necessarily cheaper for remittances - CoinDesk](https://news.google.com/rss/articles/CBMiywFBVV95cUxOZVMxWHg5OFg0bHBhWHpaZkljcE9xZVBIclFtRHlwU3ZJYnM0dzE0R19IaUx3elVZUFdDeXJ0bzZpb09peXFYTXRfWDNyNFlXUWF5WFk1QjNzczVQalNJeHFfSzJaYWN2cWZGWTJRMXFGMklnN0I4MTMxdkdhR2lGbWV4UGNYZUFNcE8tWlRsaFVVSVNyck9EUzN1ZzZhdEpncVlHemdDcXJnSnZ6bzFrUHlqR3RBNWJ3OU1FZDNQSC1scHJHclRoNzBFRQ?oc=5) (Sat, 01 Aug 2026 16:13:13 GMT)
- [$7B Stablecoin Outflow Raises Liquidity Concerns Despite Bitcoin Holding Above $60K - TradingView](https://news.google.com/rss/articles/CBMiakFVX3lxTE1iS0poZzhpNkpzYm5kM1VnTzh0Sm9idm5CNC12RmRGMFZweVcxUFl1OEpaZldFUXI4SmdwMmpsVGliQnA3b1dEcXI5eUpfbDNNUGZ4akZ4MnJSaU10WTRfZGtBZC13d2VyWEE?oc=5) (Sat, 01 Aug 2026 13:41:55 GMT)
- [CASE STUDY &#124; Fiat Rails, Not Blockchains, Drive Stablecoin Costs, Says a Bank of Italy Study - BitKE](https://news.google.com/rss/articles/CBMigAFBVV95cUxONi01bkJTQjR4elBLTU9CZm5vdTNKYmxYSGNuTkFscGY5VUFOcTJyR3FKRlQxa3J4SGxMQmU1TFg3Ri1uOWdENEhCZFhwSjFKT1U3UWF5RnVnTUZUdE1GTXpZNlFDOGMxN2hRcGJtN2o5U204d3BaajVNLTZMSlMyTg?oc=5) (Sat, 01 Aug 2026 06:00:35 GMT)

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
