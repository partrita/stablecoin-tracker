# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-08 03:37:06 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$278,651,602,245** | 🟢 +0.01% | 🔴 -1.98% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoin Adoption at the Periphery: Why Local Appeal Has Yet to Reshape Global Finance - https://economy.ac/](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1FRXpHbjRwWHI0XzRQWnI0eHBnZGN1R0hyVVpKRGh5V05iX0o5dmkwOWRrRkFabkRSZWN0ajBCcDVGc04xN1pnRFAyWXRiRWI5T0hBTDIxakpRQQ?oc=5) (Sun, 08 Nov 2026 00:27:30 GMT)
- [Stablecoins Shrank by $5 Billion in a Week. Can Ethereum Rally While Money Leaves Crypto? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi3gFBVV95cUxOc1oxb1VLeUdpVWxHOC1pMzdpMUFVeVZhRDE2a2l3bTRhRnZCYUZfUjM2U0RQLUUyYlM0RV9mYnlsZGVOTGlXUXI3ODJ0SXZ6d0FJR2J6UEFOTVl1d1JxcTFQRm16dUMzZGs3cW9OODJXdWpJMWdwcVRPWDRsRG5qSmVpcDVnUmNEalhUZEYxNmk3aTd4RXZrVDVrWC1SMVp1eHRDakZ0WnVaQlg2OTQ2STNfSmpfVENkZHJYbzYwVXhfOWgyM21GblBGQUZKVTJfMlFKMXJ4NWZja1h2ZHc?oc=5) (Sat, 07 Nov 2026 22:59:00 GMT)
- [Nigeria Sets New Stablecoin Licensing Rules and Capital Requirements - TradingView](https://news.google.com/rss/articles/CBMixAFBVV95cUxOcThiLVA5MjFON2EzenZ2NXZ3RkZUSEVDNTQ5OHl5M2RPSzdKMWlsWmxjZ080UHFRWXZoR2ZZeHhpdXFLX2M3emFLeFBnZ25oaUZraEpDclotYnZtMWhnbEgydGRCN2l6dFF5VmlmSXdDY1Jhai1VR3JHX2tWWER4RHdyX0NkQjNIQ05BaVhNLW9JSUViVENTa2ROUUJ0VjFFd3pZRThlZm5qeHFfc3AwR3kzZlpOeDRwSEVqWkFRMzBvX2Yz?oc=5) (Sat, 07 Nov 2026 22:00:00 GMT)
- [Samsung Wallet’s USDC on Solana Is Live — Here’s What the Rollout Actually Covers - TradingView](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQNlZTUDZWSzVXZGZ2VHR2Umh1dWpuWjN4ZXktd3FtSEE5YVJSa1NuU01WcTVVdnhOM29TUUs3TjIxY1NxbmMwbFNwMUI4RW9MYjl4WmVEWllYWWhqSHdGd1lGdHdvcVBsMW94M3hsZTRaM3JYVjVWVGtFZTdTWXhNSW5Nd3YtLTE3aDB4SDEyLU90SDkwQXljYU42a3R2UnZ4QWpnemZxY3FCRlRxdEphYWhPYzFKYmZ1Rk9ZX1BkNDhmd0NGTFFVTGc0UWZ3TzdXYUlN?oc=5) (Sat, 07 Nov 2026 17:00:00 GMT)
- [Stablecoin contraction forces Bitcoin drop despite Fed reserve gains - CryptoSlate](https://news.google.com/rss/articles/CBMimAFBVV95cUxNMUNZS2pQNmVYM0oxWGhnckFuT3cwak5NejNESlBNNDcyYkE5QjNORkQzVmk4YTBMc0s2WEFDbW1OLUFUTnVtMjZZNzBrZXQtaWhnQXZEbnkwSGVjTVJ4RmR4OG1USzJMNWJPak9oV3N1SHJITVR3NE9qS2pGRVBTdTNCbEZtVENEWFhJSjJua1hzQzk1dTZMNg?oc=5) (Sat, 07 Nov 2026 12:40:07 GMT)

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
