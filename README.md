# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-29 03:28:23 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,176,044,406** | 🔴 -0.18% | 🟢 +0.22% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Tether&#x27;s Stablecoin Is Iran&#x27;s &#x27;Lifeline,&#x27; Senate Report Says - Law360](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNWXU0aG5mazNYNXB1WjVJQlUxeDJmcFp3R05VbGw2OF9jdnAzNG5qa1kzMkRwUFJXUDJ1NXVtQ1RzMU5namd0YzAzV1c2OVFzY1NmYWg3SUZsVktFM0lPaGxXalhOUVNjWERfRzh1SndTZy1OczF2ZC1aX19LY050MHQ0TjFLMjdCQ0pQNjlqWnJrdG9hZW5LMDExTFNGNXdJY21IZkVwSVFvTzl6Um1ZVU03bWJ4Y29FOHNn0gFWQVVfeXFMTXRnV2p0LVNNNnJvSTIyY3dQc3AzakVla3hxODZGanY4aUF1RmpqMHgxNUhTdTd1X0NxY3h0Y1FmX3hoUWswbGhESzVVTTJZXzdIbUw3eVE?oc=5) (Tue, 29 Sep 2026 02:11:26 GMT)
- [Citi turns to Coinbase to help clients accept stablecoin payments - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNaU9GaTJZb1FhN0Y5Yl9sRTVxSlAycGhYZUwtTUZjR0RyT0RKNUk2M2hCTWw4WHF4cW5PNzI2M3hmRDFYb3pxWm1sVDFkbFRnVmlhMWV2eVk4QkFyNUVKdXNMd29rVmI2b3NxUDk3QldZa0h0RXBDSXZ5UHFTREk3U0FDYXJwMWZ5?oc=5) (Tue, 29 Sep 2026 01:10:00 GMT)
- [Citi Clients Can Now Take Stablecoin Payments Through Coinbase—Without Touching Crypto - Decrypt](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPVlREWjYxa3ZfdFF5SHFNT3RBWE8tbFhzRGs5QW9mWW1jZExlTWJlODFnVFdhTFRGS25rRGREbTN4M3YyZnc2cnAySkZMMmVaM3R0QW9OTVNRdnVNUG9LdjJZaDJxOFFCeG5lTjBCcmJ4eVhFRHhpZnlYNjJEaUJPQUp5UHpZT1l3WDdv?oc=5) (Mon, 28 Sep 2026 20:36:03 GMT)
- [Citi Clients Can Now Take Stablecoin Payments Through Coinbase—Without Touching Crypto - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxNay1OeWd3U1hHM2RMdUZSSXZxVnl6RlVFZ1dnTERIclZubVBUYzJyU0ZEdmdETEIteGRrTmRxOEg3MHR2V1AwUzI4VmFnVlBQZm5ERjBZU05nTTJVS3h4em1GWVNUd19kbFBfXzlucGNIS3AtS3dwakxwRm1ocV9WQktJLWlwR0tYWUFfajhkQ3U1ckRWckpwTzFiREZOdzJ6MXMw?oc=5) (Mon, 28 Sep 2026 20:36:03 GMT)
- [The Stablecoin Yield Fight Is Far From Over—Here’s What Comes Next - Benzinga](https://news.google.com/rss/articles/CBMitgFBVV95cUxOWGthc0N4ckZzYUMtQ2l2MW1IeVVHQldxbEp2dEJuSHR2NExHdUpGSkp4bml3NjVFU0ZzNFFFdWpVMW9hZzc1Vlh1YWdKV1laVzhjN1piZ2s5WjV5bWpOMXhtb0hHVGJoQURtMWdpSmVWbGlqT1lyZlNYdW1ENVdQNmo3N3l3TFZZWmxxNTVZb0F5VVJwbkVuaVdjc1ZodlFmQkMySktoYjNZakJPNkZPRlZOZ3RrQQ?oc=5) (Mon, 28 Sep 2026 20:03:06 GMT)

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
