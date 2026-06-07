# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-07 02:44:41 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$295,053,847,922** | 🔴 -0.25% | 🔴 -0.89% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Meta is paying creators in Stablecoins. Spending them is someone else&#x27;s problem - CoinDesk](https://news.google.com/rss/articles/CBMivwFBVV95cUxNbk1POXctUlR2RVNaUk0zYm8xdzhiRTQ4cjczb2xMaGM5aVN1UjMzVE9JX3BZcGM2NklxeklGSDRCQ2l1UU5oV1pTdDBKQmJicWh0a2tmTS1OSTZoSWhESldBUlFDVFphT1Y0REdSdU42UWtmUjUzUGR4X09aUXYyMFlVLUYxdHRPTVV1QnQwZldxY19HaWVoaFo3ZFV5dVpvTkFMalMzTFVEeUtxTXRrbmp0V3R6YjhuVE41eHQzSQ?oc=5) (Sat, 06 Jun 2026 16:32:26 GMT)
- [Zebec Network scales real-time stablecoin payroll and payouts with USDC and EURC - Circle Internet Financial](https://news.google.com/rss/articles/CBMiXkFVX3lxTFB4T3ktOVhGaTVUbjluZ09jUTA4Z1lpRXRyeXN4Q1JCMHo2emxxTVoyaXRwQW1yNEtqeldxUjEtMzZNMGxucG5zN3N0VUNiRktkakdLcXp2MC1lVVpVZlE?oc=5) (Sat, 06 Jun 2026 06:48:03 GMT)
- [State regulators object to Treasury imposing OCC stablecoin rules on states - ledgerinsights.com](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOWUhNUEFqYlR3V1JiQlM0VGo2dl9OcDV1VmEwQzQ5T1FYWEg4dVpyMXN0Mm00YldYdm4xcEhub3NrTEI1V2FmVTJzUjB2Nm9sVlRNU0lqT0RtOEx3cDBfY3VZSk5TRmxpb0ZnME5hVUU5NDBXdGZLTkl2cG1JY1NRTWtwUGtCTXNfMG9JWXVKcWZtMFU0NlBzaldpbnFfNTg0TjBiR1dpWjk1Q1E?oc=5) (Fri, 05 Jun 2026 18:23:01 GMT)
- [This Week in Stablecoins: Ignoring the Crypto Market Rout - PYMNTS.com](https://news.google.com/rss/articles/CBMimAFBVV95cUxNb0plTUdqUnFlajFvWGM1aTRKcHBpODVJN3Nza1laZGRXa09mbnd3M2d0cVlpRHl6LXNnbU1DZzR3WEZsV25iVHl4dm9BZ2lLWER2SW93ZTVfRE0wclVScFU5d2FLN25TRFVDV3JoMnVJWDJKTmNKRFNXWXZycFV2UmNsVk12LVRBdmZfU21hYXNjbVhldXltSA?oc=5) (Fri, 05 Jun 2026 18:06:45 GMT)
- [Government Stablecoin Payments Would Fuel &#x27;Tax Evasion Economy,&#x27; Lawmaker Warns - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxOcXNSd2drT2tfNzdwV0liRzBpT3I5MkdQRVh3SmNxYndVOWNlUVZaY01tQWtYZmRKR21sRzJldm50akNueTg1WTRlaTdyVy1vOUU0THhGSnNtRHJBSVBLRFNaczlneU9KS21GQmtSWGxSYnB5UkZlMTRfS0UwUEJ4Y09ONWlEWTZ2ZDltNHFKMHVnTXl3NlFnM2RtTXRFMHQ2Qzh2YXZyRQ?oc=5) (Fri, 05 Jun 2026 15:52:15 GMT)

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
