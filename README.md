# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-30 02:08:44 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$299,196,136,137** | 🔴 -50.15% | 🔴 -50.16% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [&#x27;Nearly Two-Thirds&#x27;—Stablecoins Suddenly Hit $4.5T Q1 Volume Record - Forbes](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPQkhNcDJIanNyRmItR0hMWmpUZ0Y3RFhhZmhHM2wzTm1TVTBIRzRpVUR5MDRpMEN2OXRzTDdfZlViVWpWOXhWcEY0WUQxdmRnWlJxc3ZYZnBiV25Rd1dZMFZ3UlRFSWh6aHh2N2hoSXdWSFNQbUlKUXR2SHBZeUhXSWpyQU9PdWFLWmVmOTV6T1dVTUhHMTQ2YzBOVll3aWIwQWhLLWNJUFlVazFfRzJjSTZuX19lMVRLRzJv?oc=5) (Thu, 30 Apr 2026 01:40:35 GMT)
- [Meta (META) starts stablecoin payout to creators in Circle&#x27;s USDC on Polygon, Solana via Stripe - CoinDesk](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPMXNTRmctTHVMZEFYUnVPVjR3XzRVM1lVdFQyOURaaUFVc0twdXI2N3cyM3ZRQUR3NkJNRVpHeTlfcTVwNThXV3IwY1BETnE2anRIZXNGMWxjWm9LS05lMzBWWGp1c2xXYXFxOEE0TlJJWVMzWmpaNm5RYS0xazR3aFFENjJ4NXpDR3pwYVhZUkdUZF9LYVFqTVNlbS1Cd3ZFS3h5WFFRSlJMdnlyM1JXdVdMbnNjWldycFlINGltVHBCZw?oc=5) (Wed, 29 Apr 2026 22:42:10 GMT)
- [Meta Launches USDC Stablecoin Creator Payouts on Solana and Polygon via Stripe - Decrypt](https://news.google.com/rss/articles/CBMipwFBVV95cUxPZERIa0MzY0N0OXFjUXpIRjdPdFVtQjF2T1p3WmZHZXVWSm9TNFI5aUZMalpCeDFXT3FBNWcxUnZNRkF3NTZBWjgwREJpMVpnQ1d1ZkpPZ1B5a2M5aFFvdW5YY1Zkb0VjUVNQRVQ2VVNlWTZpckJHdHZ5MUd3YnVYcjdRQ2JPZ3c0VmprcGh3UDVfTjVFbEFmUWFUa1hxZkI1MnRkWlNzVdIBrwFBVV95cUxOb1g2d05abzdleUx5VHJMTm04OTQ3cDFidjVidmwtTFduX1BoQ0FMcWhaMC0yRTJlbXZGTi0yNnV3RFNqdVMxRGxsNzBWM0VndWRma0g5dHRjdUQ5N0RaUHVURS1iZVVsQW9CZy1kRVdRRUhxZ2FYaE5xMDJ4MEo4UmluQ2h3UVJsMVhDSGY4bDFIeF9GVHF5cmIxZl9PQndLNjdIVko4Y083d0FGWEhj?oc=5) (Wed, 29 Apr 2026 20:10:14 GMT)
- [Walmart-Backed OnePay Joins Tempo Blockchain to Launch Stablecoin Payouts - PYMNTS.com](https://news.google.com/rss/articles/CBMinwFBVV95cUxOVE5oaGVQUTNhcHAzR1pKc01SZGUtUFE5b0NZUUpTcnlmNWNBNmpWTjJFb0V0enUzc2FsZHdwNVR2YUhlRE9Hc3M5UWFsNE1KNS1UdE5tdkZDSV9RT0R1Wi1oY2lwV2YzSXBaYTZyTEtJWVRkRGhzSk1GMnFoT1FJM1NqeElvNl9RSW9Hd09BLXRsR2JPdnA0OERSSjFqSFE?oc=5) (Wed, 29 Apr 2026 20:00:55 GMT)
- [Meta Platforms Pays Some Creators In Stablecoins - Yahoo Finance](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOeTV1MzhsRERLVjl2b3lNVGEzS1NXbmxsTDJBdUlld2ZyRUpvNmN5UUUzN2tSQjNRSjk1QXJQdDRrSFV5V0xHS1R0T3ZkczhvUXdaZHdmY2Z6VWY0THpGSzg0MXhzeVdtbHlxMENOUUZoZ1FVS0F0X2dCV0k3LV9MeWN3RzlEUW5kWW1mNU5VN2lLUmhMSEVDeXFBY2xjSFBHNlFxdUdUTGc?oc=5) (Wed, 29 Apr 2026 19:34:00 GMT)

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
