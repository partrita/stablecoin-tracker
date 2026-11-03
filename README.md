# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-03 04:43:22 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$282,345,080,012** | 🔴 -0.51% | 🔴 -1.60% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoin Dollarization Is Widening the Dollar’s Lead Over China’s e-CNY - https://economy.ac/](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5PMWY2SnZHWm5KcTQzcDF2Wk4zS1N2YXFUU05KX1NVNHgxLTVRVVppSEVJNV9fWVZLcHUxMFBGczZGNjJCQmxzLXM1ZFNvVHdFX2ZIRGM4d2VLQQ?oc=5) (Tue, 03 Nov 2026 02:48:28 GMT)
- [SBI injects $100 million into US bank, betting on stablecoin access - Moomoo](https://news.google.com/rss/articles/CBMipAFBVV95cUxNS1N4N1ZKbExTdUo4bm1JMTlzNDRnaHhmeC13RmxNR1lfZkFqMEZURmpOYi1aeGVsYlFTWXhqTzlFczdVWTdwWXNCTG1HazhhaDJXaDhQbkVxc3VaTF9yX0VJTmF2TTZnRWtBSDAzaDMwUEYxMHgwOFVJUW4wbTRLVXd2RFF6aHczQlpvUzJYQXhEVjF4Um5taUUzVnAzZVdjOUs5Ug?oc=5) (Tue, 03 Nov 2026 01:48:52 GMT)
- [Weekly Blockchain Blog - November 2026 - JD Supra](https://news.google.com/rss/articles/CBMihgFBVV95cUxQUm1kZ1FuOXpRd2ZoMDNpOE9vWkQ2LVFFNy1uZTJxNUN0UmNqUUhOWjJHaDIyU3RGbzZHS3NnSWF1ZTAyY1g0Umk0bWpMSzMweHJiZ0tHOS02Ym50RnVBd0dyTUUxWXlrclJ1M0NsSWpuTERHWHlXb1Vtd3ZfM0FyQVJiLUNBUQ?oc=5) (Tue, 03 Nov 2026 01:44:48 GMT)
- [This Money Market ETF Was Built with Stablecoin Issuers in Mind. Here&#x27;s What That Means if You Park Your Cash in It - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi8wFBVV95cUxQamUweUE2SEFjYTktcjRrNmUtUHIyV0VrWk8zVTE5aFFLTUlWYjRob1RfUzREbzBjVDkybDVTam03RmtJN2VMUk5OaVFpS2hkYnlLR3pOVk1BUExvdmY3VFpQYVZwYkt6Q2tyWklGMG5zUW5EUlF1d3NYYkQzRXVwaGgxTzI4c2Q2c3EyWVhCaDc0UmZjM0RJaUQ5NHpaaENWSmFtd01zV1JGM2JQT01CcHpHRkNrUHNjSnFlM1UwT1o5Ym9RbUl1a1dqQk9hTE5BbUgtbTJOT3l5bmJoRUZLaGZva0hKWXR5cEp0RWlVYmJscWc?oc=5) (Tue, 03 Nov 2026 01:33:00 GMT)
- [OKX and Mastercard Bring Stablecoin Card to Most US States - PYMNTS.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxNVEJyT2xIRU5kaWQ4TXVqbXB0cDNQQkpzQmxKUUZyc1BIcnNuOHVjZTExUE1UZnh5ZVBtRE9ON2gwdGVKckhDb1hiLUVIVVNpMUR4MXpkeUd6OGMtNTBiUDFlT3l1TXJaWkR6azUtUmZIaUE1VkR6VnlBekF0ZFZKUjV0YTV0RFQxcW5DQUxVQzAwd2dLdmxOc1RkU2FzWGNkYWwwWg?oc=5) (Mon, 02 Nov 2026 21:40:22 GMT)

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
