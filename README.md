# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-01 02:41:52 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,020,667,374** | 🔴 -0.30% | 🔴 -1.06% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stripe and Co. Take On Circle and Tether in Stablecoins - The Information](https://news.google.com/rss/articles/CBMinAFBVV95cUxPbFE2aGF0UDJCWWpTYy10SE9aNEVDWlFlekI0SFBZMzlpek9RVm9zTWk0NzdGTzI4elNZaGJZVGY3cERNVW8zT3NlME9wZWQxN1V1dTNNWUY3Qk5OYWdnYjdraERxVE5UQllLVVNqLW1nVm1DeUxNbDV1WVZld01PWGFaczhrTzhhR0lIOElMQjR5VER5Q1B2U1RCaWc?oc=5) (Wed, 01 Jul 2026 00:01:00 GMT)
- [Visa, Stripe and 140 others back new Open USD stablecoin to challenge Tether - SiliconANGLE](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNc3BBa1RoQ2gxZlpfYk5yWUtIREhKUTJ2N2VWc0t0Y3k5NUhMb2tVY3ktVHdHVTFfRVlFaDZtMndrLUN6aGlWaV9tRVpZdWl1dk5OTXdzeldkLVNDVE45RTlCb3FsY3ZKYUNhamtLd18zM1AtZ3ZZa0psTnNzTlpHWmotZFhreEhsWktPeGJiR3lEaU9qTmVMYnNiUFA5dUdSYXlsdlVtaDE?oc=5) (Tue, 30 Jun 2026 22:47:05 GMT)
- [Open USD Just Turned the Stablecoin Race Into an Ecosystem Battle - PYMNTS.com](https://news.google.com/rss/articles/CBMirgFBVV95cUxPQ2NDYU5wMGg5Q1hIQmswMkU1bVRNSHRwYlBYQlJyNGh2U0dWNTJmdlg3eldNdnJlWTNfMkpYbnQxQXpZeWVjZktWT3Q2TE9NRHdkSkdvQ19NaE0wLUhVaENwYmRmVkJfY3NDNGxVel9CaGdvd3RSVnNYTl9BbkNYQ0ctYUs3c3pTOWl5My1TRUltU1NadW9lV19WaDVUdGthT2dMS3hKX1M0SVpZWlE?oc=5) (Tue, 30 Jun 2026 20:56:48 GMT)
- [How stablecoins reduce the “weekend settlement gap” - Thunes](https://news.google.com/rss/articles/CBMimgFBVV95cUxOSmdBR3hjY3NQMFRkV3dwN21ZT2liTDdVTmJ6TnBuNWI0cmZnUnVEZkJrQ0Q3RFJTazBRajl4YmpBZ2xqVkdLM0FMVGN5VERuOW1GaXRPeEZvVFVIV2xsSElJQzRVUHN5b2d2ZjliYlFwa2R2OXJGdURQb1hucDk5eXU5bFh1QjZpTm9kZVoxLWttQ2hYWS14OVJn?oc=5) (Tue, 30 Jun 2026 20:16:37 GMT)
- [Financial companies join forces for US dollar stablecoin, keeping reserve earnings - TradingView](https://news.google.com/rss/articles/CBMi3gFBVV95cUxPcEdFMTZmUlF1dGNuTVpyZTMtbDJ2QUtxZlZIaHpTVGJHZ3g0bEo1TTJIQWlCZ3pMZXYxME1OREtPdnFrU0FPM3A2YWNseWxFZGpnZ01zVUYydEVmTzRiZFpNMjY3WnNPbHpvc2xldnVuckduUkt6WVlXN0NyS19XaWQ2a2FxTkdOVWJ0WHoxckcxb2hFeVpaVzFvRUlWTGFUOVlUNS1pdmp0SExwS2dIcDZMN1NVWWhSSzBiNVVEa1R0cHBUU3pnWXdIbWZXUHdQeFE3aFgwMW00cHVISmc?oc=5) (Tue, 30 Jun 2026 19:31:41 GMT)

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
