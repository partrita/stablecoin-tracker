# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-02 02:00:01 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$299,958,511,648** | 🔴 -49.95% | 🔴 -0.11% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Tillis, Alsobrooks drop new stablecoin yield compromise - American Banker](https://news.google.com/rss/articles/CBMilAFBVV95cUxQRGkwMTlXRlJqU0hYVDlJcjNzQ3BPNHZfR281RFBLSDc0aWUyYl9lYzJ6cDF6RnVmTkh3c2w4ek9DRnI1VDE0a0w2aG8zQTFCdTQ5MTdOcnM5QUZYUFEyZEZkVXFHcjF0LW5uYlBNUTVjY1hWVm44MEkxQWhNWm14SnUzYjVHWGpJMDZiV29BWGYtM1h6?oc=5) (Sat, 02 May 2026 01:29:00 GMT)
- [Clarity Act text lets crypto firms offer stablecoin rewards while shielding bank yield - CoinDesk](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNeVBxUFc0LTFlOG9hMF9rckxCQ0ZoNkRyOWxZb285MUU1YUxiakl6ek9HS3BFT2xrY3M0UXA2eG1JcjFmSzdFNWRTTTB4T0R2aFpZRTdSUG9XZHdfOU1jT3FJXzZPTXRfMi1CeGtrbE1zNW55RXBCQlJoTTk1WU1udlBta1NIYzRsbjNjSFJRdnBGS2p6ME5teWlmZHNqT2oxR2EwTWlsNXVyV1BrMGplSHlQdDF0LXVuT0FQRmVSTUxHRVpVcmVVOA?oc=5) (Sat, 02 May 2026 00:56:15 GMT)
- [Coinbase secures stablecoin yield compromise, paving way for U.S. crypto bill - Investing.com](https://news.google.com/rss/articles/CBMizgFBVV95cUxNd21vQ25LbXNLOEI2ZHZDUW5jWHd2Q0ZWQ0xDX1BHdUJhUFF2SmxZeUpHR005bEw0T2NjRFRGZGY3WnQ4TVl4aHhxVGstOUwxNHhmU3EtcjNweWlZVVRiZlhGYXBJMnVnZFJBWjNlUFU1amhBdndzQ3IzZVF4LWR1UHhHeEhqUG5KSmlBVklqUmRBM01TMzNidi1SREpnVVgxZWRMTHNOd1RPYkp0cmEtaWExWVZ6cGY3dXFvNG9FakV4bDNMR0NXSEFOTFFYUQ?oc=5) (Sat, 02 May 2026 00:10:53 GMT)
- [Public comment to OCC on implementation of the GENIUS Act - Brookings](https://news.google.com/rss/articles/CBMimAFBVV95cUxOaWM1MmtLUlJtUHdqOGhhOWlmbC01RVpNeEJNMFc2RlBsS1E0bmRTZWJhamdpQlZ5N3lWMTVFa1dsdVNZQUd2aEt1clJfeDRuckdvMTBlLWx4Sl85VU5KYThCRHBYS1k2TWRaR21BOWNtU2F1QzN4VzlaNk8wN0NLTHNkX0lzX1AwSUoxMEpMNllKY2JJa0ZXVw?oc=5) (Fri, 01 May 2026 21:20:14 GMT)
- [Vault: Tillis-Alsobrooks cinch deal on stablecoin yield - Punchbowl News](https://news.google.com/rss/articles/CBMigwFBVV95cUxPRlNKWkVmSFBhSmNBNVF6ME9jT0c3ZUMyMDdia3p2bThKekxLM3ZKWmRFLVV3NXptaHljR3NqMUhHcm9jUlBxSHRTZlVnYU9nX3ZrQVJJTUE0YVJWam1SeHhuY3VPUWdMUE9xeFZpVHg2OXI0REliVW12RXBTVjZVTjk3RQ?oc=5) (Fri, 01 May 2026 21:02:09 GMT)

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
