# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-30 01:43:01 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$287,172,313,246** | 🔴 -0.15% | 🔴 -0.70% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [What&#x27;s Inside Proposed, Expanded NY Stablecoin Regulations - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBnSGR1MVV3V19iM2JzR3dWRzN4Wk9nNnJYdlV4R0hUcF9GX1p2TU43ZTRScU5fcW1fWUNYY3hlSEF4Z0hSWThhbUZUUXdLZDI1UTZJdHdn0gFWQVVfeXFMUGdIZHUxVXdXX2IzYnNHd1ZHM3haT2c2clh2VXhHSFRwX0ZfWnZNTjdlNFJxTl9xbV9ZQ1hjeGVIQXhnSFJZOGFtRlRRd0tkMjVRNkl0d2c?oc=5) (Wed, 29 Jul 2026 21:57:00 GMT)
- [What&#x27;s Inside Proposed, Expanded NY Stablecoin Regulations - Law360](https://news.google.com/rss/articles/CBMirwFBVV95cUxPbEJmRnJrbmUtRHY5QXM0bVBGNXliZWpfVmRaV2cwOGFRZHNwRC1PWGVjNXdheE5kSzhSTHpkSHF0aVIxNzFQRWhRbV9KRU80d3dLVk8xeFNEME5mNldrTHlzVVJvQjZpeEc2TmJDZUV2RGJlZk1OdlVxN0ladVJxcElDUk93V2N3S2h1bk5IcjNNMjVRSTdvVUp2NU1hN1FTUEVsWUJXRlpBeGxaM0ZR0gFWQVVfeXFMUGdIZHUxVXdXX2IzYnNHd1ZHM3haT2c2clh2VXhHSFRwX0ZfWnZNTjdlNFJxTl9xbV9ZQ1hjeGVIQXhnSFJZOGFtRlRRd0tkMjVRNkl0d2c?oc=5) (Wed, 29 Jul 2026 21:57:00 GMT)
- [Anchorage&#x27;s Nathan McCauley say GENIUS moved two of the top three stablecoins onshore - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNXJxZFFVTXplOVd6MDAwcldDVzBnQlI4TGhyMG1PSlJzZmQweENvSFY2cEo5VTlkYlFuY1dmUzUzZVFVREN4UWNfRVRhMDhCREhFMGUyM2VSSGhwazRfbDlBTmZRWXRhVTlncTR6S0RhdnVDdHltd3dPcEpDTzViTk9iMG5wbmNYZHdwMXIzX3R1QQ?oc=5) (Wed, 29 Jul 2026 20:09:45 GMT)
- [Banking Groups Demand Guardrails Before Stablecoin Panel Begins Work - CU Today](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPekFjNmJ2TU5LMW5aRDdrMDh2bm9uT3Q0eUVwT2VJRnMzOHUxZjhTQ0JBdW9FU3FXcldfdXFOWGVEZ0RHTE9SMHE2OFBNTk9nSms1WWFoZGd6SFhLa2p3VFNTcXRwQ3o4TVA4bkR2UGRGTjh0YWFrT1N0NVBfTFRNcEwyNlFxX0oxRXBGSHFkcVp5WWJyY1pWNjJGWGYwamZsY0RJeGVuR1Y?oc=5) (Wed, 29 Jul 2026 19:41:05 GMT)
- [Visa CEO sidesteps labeling Open USD a challenger to Tether and USDC: &#x27;Our role is not to pick winners&#x27; - The Block](https://news.google.com/rss/articles/CBMitgFBVV95cUxPY2ZOeEV0ekJfeEJyS19pdzNXV3lubkY3OXprMDZ0ckNzZHM2SnkwU3dFX1FrdW5ZQVY2ZURpUzFRYUxNYURua0ZrMHROME5mZXVTQThIZ3BOTjZyZkoxczlMYmVWTEdjcnp6ellYalFzQTZRUWVxUU9nQVZBUjE0dmloNFJuZVBIZEN0WG5TY2lmNmQxN0VYT0J4TFJMeFJCVnBGQTJXaUZvWmJ2WFUtQjRWaXEyZw?oc=5) (Wed, 29 Jul 2026 17:06:06 GMT)

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
