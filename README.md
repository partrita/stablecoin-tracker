# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-27 01:28:53 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,142,771,320** | 🔴 -0.30% | 🔴 -0.53% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Opinion | If U.S. banks win the fight over stablecoins, China does too - The Washington Post](https://news.google.com/rss/articles/CBMinwFBVV95cUxOX3B4ejZiWVhFS3l2SXdJczRQblRyM2NwZElnWkswT1BRaDZ3VFdBYk95NEFFRGt3YW5TMWwyZm5DTUtFSFg0OGpiNmY1Rm14ZkZZdF9mMnBDZmg3a2ZBYUVpb3VYMFVENFVWaV9yMWlBQXhKZldxZFJ4NkRkUzVPQjQ3Vzg2Wi1fbGszTy00UF93R1NhOS1YRVE0blBHMlU?oc=5) (Fri, 27 Mar 2026 13:05:57 GMT)
- [North Dakota Moves Forward With Stablecoin as Local Banks Express Interest in Pilot Project - knoxradio.com](https://news.google.com/rss/articles/CBMiwwFBVV95cUxOSmxNdE1CT1MxLXVldjRGcFctTWhyYjgwXzB4TXpWVUJfMFhFSlhnUXNqUUN0TzhkOWZBb0dTZFF5U01nTUpBeXBQOHpPRjBjVkpOUnFwVVNmc1l1UXoyZEtBeHZJLVNQTHdPeVdoXzJ0ZVJldlJwaVZwNWFQR3dsZUs0X3BObWpXaXFONHhZaHo0NHE1Rnd1YzluSU50VHhqTUtSUk05NzhlVzFpY0ZLTFZ6R0ZXOUJrRkVFU0NVRkZrYjQ?oc=5) (Fri, 27 Mar 2026 10:48:26 GMT)
- [USDT vs. USDC: Which Will Win the Stablecoin Race? - The Motley Fool](https://news.google.com/rss/articles/CBMilAFBVV95cUxNbUVHTGc5bmtXcFU0YzI4cXc2eTdjVC10SVJyRmlCTjVyN1B6dUdEUHRLbE5qUVZEUVVkQTJYekh3THRwT2Zkdi0tT28wN0pmVWg4NmFvTGJ2V0JWcTRKRXg0dlIzcjN1NEpaQlBJMTR3Vk5iand2VVU4SWlGblR3X1FqZjh6dEJINlBQeThwNGxOR3Jo?oc=5) (Fri, 27 Mar 2026 09:19:38 GMT)
- [How stablecoin yield restrictions could affect Circle, Coinbase - MSN](https://news.google.com/rss/articles/CBMitAFBVV95cUxNOFozSVc4WHpCTVZLd1FaaTdyV3hGVldCc2VhYi1XbURMS3I1UVBzN2xwT0R4VGVFOFVqRXhTUEJST1JnZXRjY3M0ZnRmaHNLUWFBRDlTZmQtRmtqWWV2NnAwWnFUSmloV1YyR1RZVWd1SmJmVndlQk13cHdXa3FjRVZlMkRESUlYaF91bnRlZWtLdms2Nmg0RVVhdlVKLV9GVzZNclJUWlduQkpOdUpjcHRuREg?oc=5) (Fri, 27 Mar 2026 09:15:25 GMT)
- [Tether signs KPMG to execute audit of $184bn stablecoin giant: Report - dlnews.com](https://news.google.com/rss/articles/CBMimwFBVV95cUxPSU1vbEdWRWdoZklXbzR4aTdoUUZBbHYta0hDcW9jbWs3d0NPRTVWZVhsUTR6Q1JLM2NoSkN3V3BWcUxXOG12aE05RFh5TEsyQnpZdi1FRHJfNzNSRDI1UDV6R2E4aU1IeS1qTUhuZWxyYnpGcW9EeFk2elZzRFNsTWdGTFltWHdYRm5leWRiSmg2eVRYRXhXUDA1RQ?oc=5) (Fri, 27 Mar 2026 08:35:36 GMT)

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
