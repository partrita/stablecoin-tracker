# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-19 02:34:16 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,672,174,634** | 🟢 +0.03% | 🔴 -0.49% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoin Payments Jump 45% to $482B as Visa, Mastercard, Stripe Connect Crypto to Cash: 5 outlets compared - NewsCord](https://news.google.com/rss/articles/CBMi6AFBVV95cUxPcGlibjRwRzU3a3k4d1JnNVpUT3JlNnhDa0JrTlN0U1lQeG1mOEdtdFhLRW03djdpNkVWcWJmbnk5UmJ0OGc0bGU0SnAtWllLdjNXRjdyM3JiUmY2cDNKNzkzX2h1bXdpaHBvQjQ5TnRPTXpDdlIxVW9qQlM5bVhkQm5kR2xBR1NQdDBkQzRCY25wR3JmUm0ybHI4T2VIX2RjeEVfcVdNZkRodmxVbHFtaHJrelNjNXU5N0VoUU12X2VyQXRtRXQzZmd3a2M2NUlxay0xWmY1VnAtZEYyeEZuRDdsdF9VZ2Zm?oc=5) (Sun, 18 Oct 2026 23:55:43 GMT)
- [Higher bank deposit rates are linked to slower stablecoin growth, a BIS study finds - Digital Watch Observatory](https://news.google.com/rss/articles/CBMicEFVX3lxTE10a3AwX0NScmk3UU9FWEtKdHVDeXZKTDhUWFZnczg4bWkzV19mZHVPVWtNeDRHWTdzeDJrWlkwUDhKazZ5emxYM1BIV1ExbVUzLUw3RWhGdzBZQi1QV0VmSXZzRVY2blJ3bmVQTlRnVEQ?oc=5) (Sun, 18 Oct 2026 17:12:10 GMT)
- [Audit a Stablecoin’s Reserves: 12 Steps, 90 Min &#91;2026&#93; - shattered.io](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1RY3ZScTl1VWp2S0ZQTmFEZENRWHAwZFdxaHRUaGxFUW10dnRPaU5iMHRfdy1WYXctV0RMbWpMVXZTUEo3TFBCdTVtVnNVOTVOZVhXWklRYUY5T3ZjWkE3M1N3?oc=5) (Sun, 18 Oct 2026 17:00:26 GMT)
- [France advances tax proposal on crypto-to-stablecoin swaps - Digital Watch Observatory](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1RVXJ3WmpodkZXUkcwc0tkUlA3NkRIU0x3MzBYbEMyazRpUHpLYnZVX0xpdUc4NFZwU3BjMHlveFRkSWJTYkhTLXBzWlBaZnhaN1c1VUkxNEhFMWFVNVlfUl9HbkhCRVk?oc=5) (Sun, 18 Oct 2026 16:10:11 GMT)
- [Two Aave stablecoin backstops shrank $12.4 million as reward rates rose - CryptoSlate](https://news.google.com/rss/articles/CBMimwFBVV95cUxOdVRJaTZZLVY0NGV6WVQyM3ozcUVpRG5tVG1TOU50b2RPQUx0Vk5kNkoyWnJTU1FtdWg0ZjFUNGVuQUJBdDVEVE9RMFZiU3NwVVU4UXBsOHoxNi0xVk1hUnJTWTFWdE9SOVN4Y1c3cVY0Nm9OT3djQzVVSlAzMTlWNzVjekZ2dUNId1c4dmhGVnhBaU1ITVRRWjNUYw?oc=5) (Sun, 18 Oct 2026 16:00:22 GMT)

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
