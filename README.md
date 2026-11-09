# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-09 03:50:35 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$278,640,586,758** | 🔴 -0.00% | 🔴 -1.82% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Tagged: Stablecoin Regulatory Frameworks - Crowdfund Insider](https://news.google.com/rss/articles/CBMiekFVX3lxTE84TUllNlRsYjhnS0JvQXNPUU5LZkt5MDAxRGlONlF6eDRFV0JPLTdlQXNreVNhNW9TNjRzWGZrU1QzUUlqVDhJdWxVV1FXX0VINVZwN1FjdWpRdDNJeDZNc0lEc2ZpUHkyQzB1QnRhdmpNRGFOTS1RLS1R?oc=5) (Mon, 09 Nov 2026 03:19:38 GMT)
- [Stablecoin Regulatory Frameworks, Travel Rule, Bitcoin ETFs, and Ethereum (ETH) Tokenization Analyzed in Crypto Regulation Report - Crowdfund Insider](https://news.google.com/rss/articles/CBMigwJBVV95cUxPQXBDMUFPbFhYczZxZ1doQWw2YmJ3VWlxR1FCemtNVGxWZ0tPOUg0OTQ5WTgwSnREUTB1aHZUX1ZZbW5VN1hxUHNTcXBMT0NvcUZkblk1andRbmlMSVEteVJwakR0S25SSnlaeEM2dWZNWDJILWotYi13clc0OHJnWTR5YkctRGFodlB6eHA5N0t0RzRFeEhkNHFaRzMwWkhKa1NHalE5RTNfTWl0OGQ1NzlaNUFaSlBMUExVdkotc0x1M01iaXFQU19Nc1lRZWhQejJyN1ZOTXZ4OGdHakRXZjE3X0gyMlhZQThha0lTOVdOMDJPZ0xiVk43YVQzNzFtSE9z?oc=5) (Mon, 09 Nov 2026 03:19:38 GMT)
- [Stablecoin Supply Stalls as Payment Volume Jumps 45%, Signaling Broader Real-World Use - bloomingbit](https://news.google.com/rss/articles/CBMiVEFVX3lxTE1odmUxMVZ4aVFpTkRjb2FjUTFtUmdyeEd5WWhSU0l6Z2wxcUM4MGdxU2hOQ0d0aGhFaXF5UTlkMy0yS00za05NZnJhbGJkNS1Kc2xjTQ?oc=5) (Sun, 08 Nov 2026 22:39:26 GMT)
- [Stablecoin market cap is frozen. The money inside it isn’t - CoinDesk](https://news.google.com/rss/articles/CBMioAFBVV95cUxPMk9zVHZ6aDBkQnEwUFp5VkdoMGNWUVJ5allCemtiWEhZZFRUcFVacUZfRG9WVGhHMzZiNFFLM0ItWDB4S2Y4MjdlQTdzNUwtakNWY28xMWIyZmVId0F2THNwbzdQS0JFbFB6Z2QtWXBNTXk5NUloM05aZGFpNEZhb0hJOVZRYnMwQ2FlbFhjSm1iVDhZOUY1RFdfWVNvbFhH?oc=5) (Sun, 08 Nov 2026 19:16:42 GMT)
- [Bridge’s OCC Approval Opens Path to Federal Stablecoin Trust Bank - The Defiant](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOWGstd2JPa2ZsbjRsUGJsNmFnT2ZlVlphRU1aQjBQRHhVb2ZkVmVJRmFjX3cwME9mb0xiSWpzS1Nha3BNNkc4d2Z0bDBWeVpqX3U3UEpyYXVhRkhlWGx3a19xWEtXVG1RNUE1emJQOVVMQVdEcVRGLU9vbHRBcDgzWk9SUmNmSnNobDAxZ2l3c3VlSFJPZm1lU2xmOUl5Q3JpS2owZ0R3VFhGcGs?oc=5) (Sun, 08 Nov 2026 17:36:15 GMT)

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
