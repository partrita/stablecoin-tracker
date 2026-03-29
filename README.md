# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-29 13:17:45 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$296,721,359,038** | 🔴 -50.00% | 🔴 -0.67% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Finovate Global Africa: Stablecoins, Digital Payments, and Funding Infrastructure - Finovate](https://news.google.com/rss/articles/CBMiogFBVV95cUxPRFVBdGZMcHhiUUQ1RUN3emxBX1dyN3NYa2Z1dnVEZlRsSk42eUQzWHBoMU9TakM0UC1DWHB4Vnd3OE9nQlFTVURJcEZXWGRSenZ2M2FXN3pnc0dFV1kza1JxWDlZa0Y3RDhnNVM1Ul9PSHJDWkFHcjlRYjFGbm9zOTVKcDNzdGw5dGhSaWxsbEdEcHJsaGhoOFpkRWdXTW9aeUE?oc=5) (Fri, 27 Mar 2026 22:54:55 GMT)
- [&#x27;What the hell?&#x27; — Crypto frustration boils over as stablecoin fight stalls bill - The Block](https://news.google.com/rss/articles/CBMisAFBVV95cUxPTWpubC11WVlSQzFtaXJ2RzFIOEdMR293VzNmSUtUbGhHTE9MalhNSEFyekdrQ2tRQWFHVkhpaFF6VkdVTVJRWWh1akIzcHNEdWZtY29Za2F2aUoyckZfUE1EWHRrVnNSOU9pbGs5bnNFaFRrQk5FOF83S0EtUmgwdjZrY25kY2dNd2NSOXluNGpPaDh1TUlJQS1Xd3AxV3c1TzhSejJmNnFTNTBPeDR4Vg?oc=5) (Fri, 27 Mar 2026 21:40:39 GMT)
- [Smaller Banks Are Talking About Stablecoin Payments for Business. But For Now, It&#x27;s Just Talk - The Financial Brand](https://news.google.com/rss/articles/CBMijAFBVV95cUxPS3hKSllhRlJ0b0hocU1XbVlSLVE1TGg1eDlDeE9lWkFUUmQ1ZDhHQkVyRWt4MFg0U2JmbmxaUGh1eDlzdEEtRmtTS0FYb2tNSm11SlZPSkY4YnJRMEwxOGlEQTM5MzY0LUN1Sy1SY2xRQXZRVjVqQ2trZlkwR0lSeXJOVXRSME1LYVVGNg?oc=5) (Fri, 27 Mar 2026 21:22:47 GMT)
- [The 2026 CFD broker’s guide to stablecoin integration - FinTech Weekly](https://news.google.com/rss/articles/CBMimAFBVV95cUxOV0JrbVl4WV8zejBFeEd1Y05DU0pmOEdHMi11b2pNQmVpYm81M2xvZ2JqR2VWaWFkNDVZWTRkWDAwbGl0NTBWcnVNcmRMVzZPczJhakgwVS1xUy1kZzRBczBPSk5RV0ZabFZsYWNueDVFQjgtdGJwV19Tc0UtNjI4ZVM0MnVwZl9VRGZrMTNfRl9nZWdNQ090cg?oc=5) (Fri, 27 Mar 2026 20:41:00 GMT)
- [World’s top stablecoin to undergo a Big Four audit - CFO Brew](https://news.google.com/rss/articles/CBMimAFBVV95cUxNS2J2VTFfRGpyR0ktNGJtaWJQclFjODV5VWU0WVF6V05oZWVIS3F2NWplNmhWRUwwaUszWmtCQVlram5reXVkcWZBeC1ORURPNXV1cXo0X1JoajZ3RDVRM1dNR1Nic3JsRFV4bUJqNzdiMTVmb1Vyb0p5QjdnLXBncXA1cFhqZVlUbXR6ZnZPN09MZzJvMWE5NQ?oc=5) (Fri, 27 Mar 2026 19:25:56 GMT)

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
