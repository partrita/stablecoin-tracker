# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-31 10:34:49 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$296,781,836,788** | 🔴 -0.04% | 🔴 -0.46% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Circle Taps Mother Design to Reframe USDC Stablecoin - Little Black Book | LBBOnline](https://news.google.com/rss/articles/CBMihgFBVV95cUxQd2RNd2VJS1hZVzJabTJCcUZ1VzQxZjJqTWlBWFVSeGw5VzZfa3YxUE1zN0RiVG0tV093bHpaeklrR01Xb2ZHOUV6SG5GNWowRkg0ZDRTSVV4aHpxVEoxb0RiZ19BRkhpZkNGUVVRN1ptdGp4cmtoOVNuLU9jU19KOXJrSDRRZw?oc=5) (Tue, 31 Mar 2026 09:02:12 GMT)
- [US stablecoin compromise making enemies on both sides - CoinGeek](https://news.google.com/rss/articles/CBMigAFBVV95cUxNTVUwN1RYLUJuSmF3c3laZlpha01PV1d2YnhzZzRjZk12eXBaLS0zWGxuTDNzWmlRTWpDQWhFc29VUnJGbWhBemtNdlpQLVVGdDBrc0w1Sm1ETTJQQmNnQ3lVSlRwNzZxdTlVOGxLTDc5WkM5MXhoT3RkQVk0bldibg?oc=5) (Tue, 31 Mar 2026 07:00:37 GMT)
- [Structuring A Fintech And Stablecoin Infrastructure Platform Around IBEXIAL - ActusNews.com](https://news.google.com/rss/articles/CBMiywFBVV95cUxNdE5Tb2dDM2I3YmZmblQ0TktBT0lPNFVORnY3NjZsQko3ZUZlYTh1TGdRVHNBOU9TM2c0c3FmbU13MkMxUzB1RkF1QmNpMGVfN1dYaXRxUy1EZnptN2FqQlpiUEJULWJraUxZUnBIaW93QUdOTjRLTTFpdFpVTXpMRFhacDRMOXlWRGpuXzVYcmVGTHJtWEVBSWJzYVR5Rmx3Z05YeW9YWV9WbTlGM1phV0hVdW1BUDVnWXB4eE9iREZzVXA4Y2l4TVV1NNIBywFBVV95cUxNdE5Tb2dDM2I3YmZmblQ0TktBT0lPNFVORnY3NjZsQko3ZUZlYTh1TGdRVHNBOU9TM2c0c3FmbU13MkMxUzB1RkF1QmNpMGVfN1dYaXRxUy1EZnptN2FqQlpiUEJULWJraUxZUnBIaW93QUdOTjRLTTFpdFpVTXpMRFhacDRMOXlWRGpuXzVYcmVGTHJtWEVBSWJzYVR5Rmx3Z05YeW9YWV9WbTlGM1phV0hVdW1BUDVnWXB4eE9iREZzVXA4Y2l4TVV1NA?oc=5) (Tue, 31 Mar 2026 05:46:17 GMT)
- [The CLARITY Act Goes Into Recess Unresolved. Here Is What That Means for April. - FinTech Weekly](https://news.google.com/rss/articles/CBMiigFBVV95cUxPNlNvcWs5TG5mOGVpZG5WU3JERkZ4dko2QkNUZHlmbXBXM3IwMTRfOV9aWHI1NC1ycDl2ckNYZTJFb3Jka1N3UkFmeUlLVnB6aHVYWm9Sc191MzEtSjZXUGhMSWJCN1JXVU5vRXNvbURKYTUyQkNlMms0LWR6WG1rTVFUNmF3cjhVakE?oc=5) (Mon, 30 Mar 2026 19:51:00 GMT)
- [Nium Rolls Out Platform for Issuing Stablecoin Cards - PYMNTS.com](https://news.google.com/rss/articles/CBMinAFBVV95cUxOVllBd3JKSzlYQy15MXNNdndKamtOd3hTREJxRm0tQjdZNGZQbHdELUdITmFfX2lGaUJtRkozbGlJMG9IM0R5M2tNN1ZPY01vTS0tYXFOWEE4YjJPZ0VsRzVhWVBFWUpwaUJKTllvcmZjcVRyOXM2R3BycVZUWF94MkRhNEpCbGtZX2NqUC14bGNCZ1BKc3R5NDBUMWM?oc=5) (Mon, 30 Mar 2026 17:39:42 GMT)

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
