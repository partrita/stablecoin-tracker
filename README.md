# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-05 01:20:00 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$294,970,316,855** | 🟢 +0.33% | 🟢 +0.66% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Eric Trump, World Liberty co-founder, calls banks 'anti-American' over stablecoin fight - CoinDesk](https://news.google.com/rss/articles/CBMixAFBVV95cUxPcWh2RVg3eWRMLVAwM281TjNTXzJXV2h4OXlPM3NFNzZ2YTJkZzRoek5iOUI2OG5tUWNIMmptZUlqaEhLSk5WVTluWGk0ckt5dkFwemR5UVBOdFlRcW84X09RU1NYLVNwMHBJeVF5RlhYU09DeVNXeV9WVUQ0bnJhOEJWeHBHSnpUbDRXVUxZV1hmc1lKMGNlWWs3WldVRFRqOHM1Sk9UX05wbVFISHp6M3IxRlRKVVF5VklFLXo3bGZNVVBD?oc=5) (Wed, 04 Mar 2026 23:14:05 GMT)
- [Ripple tweaks its tech for lurking stablecoin wave - American Banker](https://news.google.com/rss/articles/CBMimwFBVV95cUxNYTNmczJDYmMyUEwzbVR4SGNINFlMY1p6M1VZbXZMQjRIUGRBZnBaQWxkQ2dBb0IzQlRnZ3JUSzNJWUIzWFZkTnVFN01jeEFCeV91WXgxR3ZjamFqMDhGSDNvMTVZMnk2TUtyUGd2SW5JZzVpVm94di05RjlDQUtjWnlLWnZ5Q2UtV0FDQXVHYV9VWlotOVNUck9mdw?oc=5) (Wed, 04 Mar 2026 20:22:00 GMT)
- [Stablecoins in spotlight as Bitcoin rebounds and Trump backs crypto vs. banks - InvestmentNews](https://news.google.com/rss/articles/CBMixgFBVV95cUxPdGJRYmtvcXVXZGZ5eExsWWdPOE9PQW53VEFpNFZFdERNWXFZdU9HMDBGS0xITDQtc0ZROGRuaXMxd3pyYUxtaG9xUGJDSEM5dk11bzdpVjBwc1Ywcm9xc1FVSkdJMFRhMDAtQlZNZkpwNlEzTVFoeV9Eek1aSkNsMkRkM1RFc1pqWUg2bFlNXzdfM3BRb2tRTUxCZW40ay1rRGw5R0ZDSFp3SWQ1QWNKeTYwVGRHZkoxd20ySmI2RldQZDJ3U0E?oc=5) (Wed, 04 Mar 2026 19:05:21 GMT)
- [Sui joins stablecoin race with USDsui mainnet launch - The Block](https://news.google.com/rss/articles/CBMikgFBVV95cUxNMjhWQU80eVg5VHRmb3o5djZtMVNjQ2ZkcnpfWjkzX0pBcDd4Vm9TOWxsVzBwVW5Ca01PUGJCeUdEaktDQnAyazFYbGg2N0ZLNjRZSGtHZE9HdjB2SXVSb1kzd21XTEU2Ymc0dWI1WVNGelRjVXR3dlA2d0lzbVE5NnhGYUhuLTVMa0g2YXJQVDR5QQ?oc=5) (Wed, 04 Mar 2026 17:59:40 GMT)
- [GENIUS Act Stablecoin Loophole Threatens to Let Crypto Kill the Economy - Better Markets](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNLUppNjdFcFA0dkY4ZTVkNE0wbExteWoxTXR1ZE9EZS1xYnlkQWowbUxYUXVBQVQ1WUttS1h1ODVuekhUQnlOYUp0N2tRRmNMbjhmQW4wVVhnV2RqY3M4QXc5V0dhMjBoS1pFRTNCWnBWRGg0N3JPa2c3S2hXNFpIZ3VXQ3RJU2U5cFRSNG1MRmMza1JQdG5KalZSUU4yQ3M5cExjRnotSk51WUU?oc=5) (Wed, 04 Mar 2026 16:52:13 GMT)

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
