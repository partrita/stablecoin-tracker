# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-18 02:19:02 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,575,827,831** | 🔴 -0.04% | 🔴 -0.52% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Circle defends USDC economics as stablecoin rivals court its partners with bigger cut - CoinDesk](https://news.google.com/rss/articles/CBMiygFBVV95cUxNQjVkOHY2NE1PVHZRZVEtckFySlVGa3ZWcWhxcG1vblhjekM0VUhYemVwYWRYQzlDTmxoUkNrYUtLd2tsblFJY2UwazBWV0dWZVJxcDVxdWIybDhvc1U2eDlzQ0Z0VGtza1JyQ0taZzBDRjlZR2hMLVZSbXFwTWtDT2tQM094RTgxa1dVSWlXdEh5aGdOQ0tRN0NfVDZZTUFuNXZMZ21KOVMzUE1ndlJ6RXQxVXNDd0E4VC1jV1RzdDBvTXFYZmlyVkRB?oc=5) (Sun, 18 Oct 2026 01:06:00 GMT)
- [Visa Direct Moves Stablecoin Cross-Border Payments to Commercial Production with Inyo Global - Forkast News](https://news.google.com/rss/articles/CBMitAFBVV95cUxPc0hjZGxJSER2NDFQRElFRDhVV2hidXhnSzhrRHpJcTJGdzJYTTJpZVh2REw4bXhxbGx4RXB6dDdXOGdUM1p4Rk9RMEZMWDZWMjlRdlJNZWpoZ1l3VzBGem9DVlF5bUU5UmFTYnhCRjBfZzM2Y1hfajRJSkNtaVBMTEIyZHAzXzdVNjltcy1ndFdjOTVMR1BHNjhhVFQ2b0gyeGs4djhCSEZYZld3czIxdVFvRXA?oc=5) (Sat, 17 Oct 2026 21:12:39 GMT)
- [Visa Direct Moves Stablecoin Cross-Border Payments to Commercial Production with Inyo Global - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxNWU1hdEtGczliY0NOLS02bzNnVVNBNFFXTHpDRkZkSjdCaXlsTnBlV1FjRU5JNXFSZk1BRjBOQV9USXYzeGQyU0tmQ3ppTUpDZVhlbGlVNC1WUWplQVI3eDV3UlNvY2F0cEo1c2RUdjZnemhRcGFObDBYZGphMXhQMURVUERwaXoyaVBNWk1ESVpQUmxIbjFTaENHdjFuZjlN?oc=5) (Sat, 17 Oct 2026 21:12:39 GMT)
- [French Assembly Backs Tax on Crypto-to-Stablecoin Swaps by One Vote - The Defiant](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOUHNlRURPVjJQMzFkc3gwMGZmMHlBd3lBQjVIMUJvcTFWbU1ld2ZVQ2ZQNzduWEF0SDExQXgzVmNLUmFXc1g1eDlOa3gydXEyWVdZejhsSEhQeGRnTkc4VC1Vb3BpbkktNnhDQ2dOZm1wQ3F1RXRZR3RONklOZWRGbnVqS3hoUEgxWnF2VFczU01wRFh5WW5ONC12N2RlN21VUU05eXA3RHY?oc=5) (Sat, 17 Oct 2026 20:44:46 GMT)
- [How Megabank Stablecoin Pilot At TISI (TSE:3626) Has Changed Its Investment Story - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxQXzFRTmk5dWlCVm9PdFpteGl4TWxqSWt0dmlyemVLS18yUVNYa1g0OElETi1aYlNzWGpObWFjaEVzUUpwWTk3NzVjNkVheHFKLVlWQmZPYzh4LTRRVHR4MXQ5aHJHUWc1S1NWYV83R3JZMEdVLWpQbnlCZnVaajdrMUpNWlVpZmxVUUo0Vk5NRTRzN3BaM2E5Z1dYS1g4Y0li?oc=5) (Sat, 17 Oct 2026 19:15:23 GMT)

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
