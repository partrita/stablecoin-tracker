# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-29 03:40:43 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$285,477,541,730** | 🔴 -0.29% | 🔴 -1.18% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Ripple&#x27;s RLUSD Has a Moody&#x27;s A2 Rating and Is Live on Coinbase. Does a Stronger Stablecoin Help XRP? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi6wFBVV95cUxOS3NoV1cxQWtxZGxCck5Oa24zc2hLN2tzWWgxeERxY2lyVFlPcjQwTUJvc3B2eUpMc3pCYVNPdHpkXzBYaWdwWjI0UWtXOWFHdGUyTDdBUVRwTDUtdEVyd3c4NnJwa0U4WW9XTnczc21iaDdSa2dCWjRYX1NFaVZFNFgyLU5nVmpTRVlPdkRXRzhoVTFpNWYyNUZZVW5FekxWcFVZVmNzMmlNeGVGZm5PbU85Q2dkM0JlUjlPV2pFRVpoQjhQbk5TLXdYSnBoZGw5Smlld01BTzVxaWtuc3VRdFktd2N6eWxndUpV?oc=5) (Thu, 29 Oct 2026 02:20:25 GMT)
- [Ripple Expects Its Stablecoin to Reach Robinhood App Users Later This Year - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOc3RsNjZlMW5jbFdUcGxKcVdSWUJqc3RsMFBOdm5ORlJfNmhqV2ZOZ0RpbmUyYXpNVXFSbXp0aThFckp2WlUzOF9KM0JRcDdHS3AxbnJ4YVNyWUs4a0ZrakJaUEhTZ3ZRTGZYaUlMcXBwTENmRkE3a21uTDY5OXlKNDAxRnhTelJiMXEzQmxvZUlhT0d6M2lyMGtfWE9sejBkUnBwNHhPVDl6dw?oc=5) (Thu, 29 Oct 2026 00:05:00 GMT)
- [1TCH Simplifies Fiat-to-Stablecoin Conversion for Freelancers and Global Businesses - markets.businessinsider.com](https://news.google.com/rss/articles/CBMi2gFBVV95cUxQeUFia21PNDI4S0FycHU5LWhja282MzdNaVVmTEpRekNQUEtYZ2pMTHBDcV8xUlhUX0ZrQVRyamZnT1g2M1NZbVJ1Xzk5UlZFeG54MmVLdElNWlZNaENEUDdVUUEwX3dwcklGYXV1UWpXU0dnQTYyU0x0UkhQNnluU0huWTZ2RXU2TEtwUjEzVzJhSWRRMmUxMk5FZXdWVmNqdEtyMEhUUW1JZVU0eGx0WXdjV2FzZWVXNVJNcGp3TGhIV2dEQ2JmdEpaNDR6dElmdVI2cXZxQlVxdw?oc=5) (Wed, 28 Oct 2026 23:15:08 GMT)
- [Stablecoin Payments Are Fast. But They Have a Cost Problem - BeInCrypto](https://news.google.com/rss/articles/CBMiekFVX3lxTE5xQ00wU01qdE9GWXJwVDF6bjlVOGx6R0tLR3BreWg0VWxSMEZFRUViOXdCcDZNUkNBVWw5OGhzMlF3RkRvbmdXbE1CNjZST3Y2RzFhSlJoa1hIR1NkTnEydFVyc21pUlpJMjFvZDRuTndYYUdENTdwUDdB?oc=5) (Wed, 28 Oct 2026 21:47:00 GMT)
- [Ripple Wins Final OCC Approval For National Trust Bank, Expanding Stablecoin Reach - CU Today](https://news.google.com/rss/articles/CBMiugFBVV95cUxOV2ZuZE9kdTQ4d282SHBTTjhHYktRamhTWUZVaWJhd0ZwblZsSFh4Z01CbDlLckxBSnZTNE00NWlKSWxYVGs3ZndmVWZVYkc0LUd5aFJRbG5YZDUtQWhMUWljMS1yMzRlNFdDZHZXbl91TGo2MkZGQ2dFSnBqZUdCaW1paURqamVQNF9CQVpkQlhnT1dOX3FQN1pZbnNpM1ZnZjJtZ1c3YW9pRGozY2gzakwtbVU0dVllMEE?oc=5) (Wed, 28 Oct 2026 20:29:27 GMT)

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
