# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-11 02:48:27 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,957,425,388** | 🔴 -0.08% | 🔴 -0.87% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Visa Launches AI and Stablecoin Tools to Power Agentic Commerce - PYMNTS.com](https://news.google.com/rss/articles/CBMingFBVV95cUxOVlhYOEtQdWdVV0ZQU1pLN2E1bFh3ekM3VXFhZmFscmJ1bkVVQXFxRWxCLWpsNUMzZ3Q0ZnBOX2dnZHJLQ1luYmRlU3hIanR1X2xsVXhyRXpyYWs3aFhXb0t1QmJzSmllWS1LV2tZSXRRd1RqOV93UkgwaWs3TkFlV1Q3Y2ZVSFdzV1BiaWcyYzdzdHZjcUFfSzV2bW1Tdw?oc=5) (Thu, 11 Jun 2026 01:38:10 GMT)
- [FINANCIAL TECHNOLGY—Proposed New York stablecoin regulation to harmonize with GENIUS Act requirements - VitalLaw.com](https://news.google.com/rss/articles/CBMi_gFBVV95cUxOa1ZGVVNPOEhlRFlwNWZFdWxEeTlieVV6ZHZBWlRJdGM0N3ozdHhCVU41cUM2VGt6dDdJOURJUkFzaXZOeFpjTXlkUUZPd1dTNThENWNNeVFURmlDU2kwTHk1c3BCRDVMbmVZcnBCX3VjMmR5ZGxEaVUwWDBiMk9yMTktODU5T2xWMXFyRFNjanU1aFk0bVVmVXBrVXRZa3lUbWVOaVFaTVJTT1ROYW9qV1dqdUdPYzZXYW9sNGI1NEFkUXl4ZjlDMUhpN3JXdnljUDUzWUh1QzhBRUkwczdoVW9oSWQwSjFfcXFjY29tTG0tQWhxR041TDBKbTZvdw?oc=5) (Thu, 11 Jun 2026 00:01:14 GMT)
- [Paradigm and Hyperliquid Policy Center Push Back on GENIUS Act Stablecoin Rule - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxOdm9GTHkwWS1oZlZYaTZkanpsM0hvYm1lTmljTVlNdWZCbjJ3TzU2SVNoZzM3VkEtV0ZSeGxiQklzM2ZWUjJwVnpKNzZfaGY4UVN1al9jQU9GcG5LQi1WQmh1NjNkdWtJNV9PUk1nNWdrQkdubHRyWkNGaDllckltWUlPZG1VcTNlOXNFLWwzdHZOX2NvZGNjMnN1MXVZRW1raHUzc0U3SQ?oc=5) (Wed, 10 Jun 2026 23:14:00 GMT)
- [Visa Adds AI Agent Payments and Stablecoin Settlement Tools for Programmable Commerce - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxNeGxaRkc5Z0JEZHVQcTJwVC1wM0tSMERXeG5VS3BTdjRKU1k0b0J0eFpqTkE0YnBrdnR3WUFOZzNCSzlhSkl2b1hxY1dqZ1NHQVRaNjBxTl9Va0ZJcXkzNU9iUTd2d2pXbDR4clA4Uk1iREhvYkJUVFhPYjNXNnlxZWNnQ0dwZkluZENnZUY4bmpWbkxQVTdB?oc=5) (Wed, 10 Jun 2026 22:19:00 GMT)
- [Netomi CEO says $5 trillion AI customer experience market could boost stablecoin demand - CoinDesk](https://news.google.com/rss/articles/CBMizwFBVV95cUxPYi01V0JjWFN1TVFOV1FEUWpNMDBfX0VEOGZuSGlBaHdiclFlOWY0YWZoNVZJN1FNQ3ZSS0lHLXNiTVhNMmY1elFpLUZUVHNzX1BMZGNybDBnaGpIcDk3WDJQRS12X01MZ0RqN3dSTWN1S3VWXzRId0lPR19CTmRSRGM1UERLM3o5S2Y5bXE1QkhrQUI2aEU5cDR6Wnhtb2ZKV3RJcWhFcWNYekQzX3lZQm5pSElsSW9Pd2MwcFVpZFYyTWNfZjh2cUNCdWZWUVk?oc=5) (Wed, 10 Jun 2026 21:51:13 GMT)

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
