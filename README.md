# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-17 01:21:25 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$298,568,786,468** | 🟢 +0.04% | 🟢 +0.48% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [How Mastercard’s Stablecoin Settlement Push Could Reshape the Investment Story for MA Investors - Yahoo Finance](https://news.google.com/rss/articles/CBMikwFBVV95cUxONzk1YTg5TldUTlFxS2VZMC1BX21CSy1hMzhoMzIxNUEwaEFWcWJqbEhBOHdEbVFhRXdIVVlNWGItUEZMZUU1T05IQmgwX1REaGtVUUNmdXJzMjJIOWVjTm5TZ1Fnd3p6ZWZvMUk5emVhYkZzRkVhMkNvWjRxb0ZlV2JIQlB6dDc0WWdCR0s4cHk4U2c?oc=5) (Mon, 16 Mar 2026 22:12:52 GMT)
- [What BVNK’s Report Reveals About How Consumers Are Using Stablecoins - Finovate](https://news.google.com/rss/articles/CBMikwFBVV95cUxPbWpHZ2EwRDdyMmlLaWFZWm9OQU1sc0MwYlBaeGdLRExZNE9OTlBVMl9fTnNPVWFEVlFwUzZLR0VSOTZFLWlkbVBzR2plblluR2NWdTNlanpGTEZVRTREekZCYnVLYnZ1Y1dKclJtTHBHMzc4X2Z1VDBxRE5KY3dxT0tZZURxZW5GenZRMkhaSS1mSkU?oc=5) (Mon, 16 Mar 2026 21:32:46 GMT)
- [FDIC to make stablecoin move - Payments Dive](https://news.google.com/rss/articles/CBMiekFVX3lxTE9yRjhwWlRKMGRUMlFoeWJWNmp1bEdPbUhnN21fYV9TRXlzS1B6M0V6c0F6OWkzR1FaTm1sbWNPLTdaVXhyTktjcDVuTEpPLWhZY1B2SDRvQkVIODdBNFBwQWdUNnZTc1h2QTRrVTV3V3p6OHQ1Mk5oZFF3?oc=5) (Mon, 16 Mar 2026 21:22:59 GMT)
- [Circle Internet Group Is Surging. Why the Stablecoin Stock Just Got an Upgrade. - Barron's](https://news.google.com/rss/articles/CBMijwNBVV95cUxPX25iXzRMaGZOcUNueUJxV3FRbHJUY0h3a25NcTNkSGs1aDdzWmhNY1E1MDlMMlhmZUdqTU5PR1QzdTJTdGlISUJWenhUMy13R0NzYW14RWtyT1VGaFNjNGFKdVpQZDBHaGNDVGRPSWRnLWp0MHozanFHemcxSUJ4U090VUNnSVhYRnR4UFRoekpBWWwtU3NHeUZrMUJJcTd6X3IwZGFDQTc5UEdBbFF6VkNMQjlWOHJ6NFJPSTlmRE4zSjh2TnMxZ25jYWFBdlZUX1dXNmhzYS1vMDRWOG1xQ1JZTVB5SGdwdUZvLUhJZHdWejFCM3dILTZJMlE5cnI4clBJUFlOR0hmZnFZdXk3RXItQTJoTlREUjFDc1FpSE9nb09hU2Z3SHdsS2JERDhJWTUxVExadFo0dDZ5azRrTnFINEdUXzF5ajFDUWZGOXFobDFjNlB6VGRSaUNRcTJyT0FMTHFxc004MHRQcDUzNmp6MThOOFdvSEczOTFKWndYWVAzTFRqZ3V2Z2hDN28?oc=5) (Mon, 16 Mar 2026 18:38:00 GMT)
- [Sorting Through the Issues Surrounding Stablecoin - Federal Reserve Bank of Atlanta](https://news.google.com/rss/articles/CBMirwFBVV95cUxNMm9VbVF3TlFCSVFtMHhDY2dadHlIMmRWNDk0ZmFHMVJzSnpHVEdRZk8zaHlKUmhWNEJQdDh4dkJVZXlEM0hlUWYwUEFnLW5rejlEMmdNWnpkUm5pbUlLeWh5RUhzYmRUa2dCd01md1JrOTM2UVA0T1lQT0Rjd29wczJTTE9jT2VDT19KbW5vUG1Bd1pYaExrVWJNUGVHMFJzVGw1Y0I0NkNaN2hQWncw?oc=5) (Mon, 16 Mar 2026 17:59:45 GMT)

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
