# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-13 02:26:46 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$301,044,557,871** | 🔴 -0.11% | 🔴 -0.02% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Private Payments Are Live on Polygon - Polygon Labs](https://news.google.com/rss/articles/CBMid0FVX3lxTE9lSzRvTTR5WG1DelNITmlFc1hSNTFlVFBUU3pwQ0ZTcTQ0STVKTkE4Q2FmUU1FdGowRjRUZVVodzhEdWkySEZPTzdrN1E2bU5qcDNLZHdpSjJyanpnOVY1X3NTZU5rYUVNSkhHMk9EdjYxeHk0T0NN?oc=5) (Tue, 12 May 2026 23:36:42 GMT)
- [Bakkt Leans Into Stablecoin Payments After Sharp Q1 Revenue Drop - Yahoo Finance](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQblZDWjFldVlaZmsyazZMNGRBc2dnV0NXTHNrSjllLWNXMnVqS2NBWUcyMXE5bE9OQV8zbEZXNlFoZUdkeFF4ZE5GZkVWQzJUM2docXVPZGx4VEFfM0RWdFRhVHA0Tl8yTnNlWURuS0ZmeHdUUjR2X2tPR1AxT09uaExTSDJlMjNWWS1z?oc=5) (Tue, 12 May 2026 22:47:00 GMT)
- [Clarity Act Text Reveals Stablecoin Rules, Crypto Provisions Ahead Of Hearing - Investor&#x27;s Business Daily](https://news.google.com/rss/articles/CBMikgFBVV95cUxOdS1iMXR6TWQtWkhLTWVLY09WaUt5d3o0OEc3eEhmM2FORXhZVjVkeGJrQTAxcFpjZ2Q4Nkctck1TQ1pxN0dHcFgzZWptM1pSemRhcmk1MndMYmNSbDJ1QTZKLWdfVnBsWnp5MUVQVmRTQURwSk0xSEtVekp6VjhkUTI4dF9QTmVib3V6U3NCaVB5QQ?oc=5) (Tue, 12 May 2026 20:33:00 GMT)
- [Explainer: What is in the US Senate&#x27;s landmark crypto bill? - Reuters](https://news.google.com/rss/articles/CBMimwFBVV95cUxPWHZoTENMZFF0OG4wSG5BZ3V2ZGZXTk5WekpiQjZlNnFVRzc3c3M5Z3JJSXhjWGE1Qk1hYlhlRlJ4WklSRFJrU2U1d2Rvc2xZUV9lQnJmSmhMYkw5MjFqM2lBTlZ1U2xPbFdTMDBoNG5DT3NzSDNsYV9Vb3Q1VFRlTzFXTGpOUUdyNWZ1bkxIcGNIelBCNXdKSzRtdw?oc=5) (Tue, 12 May 2026 20:21:24 GMT)
- [Stablecoin Debate Intensifies Ahead of May 14 CLARITY Act Markup - ACA International](https://news.google.com/rss/articles/CBMipgFBVV95cUxOVTROcEg2LXNRTm1oaVE3aTk2X1VMakF3X1h3cUxlbFFrYlhwTlBmT2M2bjA1am5POTFVbm92NFN2ekpTYU9MVjlwV3RKbnlJaHY5OE9za2FQMDRlVVlTQ1FoaTlTaUtOOWc3dzNDbkJEeUY4VldlRzM3WnU1MzFEcXZpVjd4SXltb2NrVWpTWDJJVmI1S1B4UTFvZmNwWTZZZEVwVUl3?oc=5) (Tue, 12 May 2026 18:59:27 GMT)

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
