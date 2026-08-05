# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-05 01:47:43 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,953,149,308** | 🟢 +0.11% | 🔴 -0.22% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Samsung Pursues Digital Assets With Crypto Exchange Deal and Stablecoin Push - PYMNTS.com](https://news.google.com/rss/articles/CBMivAFBVV95cUxPUWtFVTUzamotd3RqcHZmbnRTVnA2eEh4LWhyd3Y4cVJWb2NsVFdmYkxBajRtN0xxV3g1c3p3Q05aNjdNM01zaVRjX1owUGpWYUdwRm9kMjdxR0ctWGhkdTN1YWM0Y1RqSTN3eDYzeHRfcUh5YjAxTzBNVzFpamhnT281TThQNHFyZ2w2WUVURDFjcmwxZkl6M2w4TmxiUHhtNHZ0bGZDUkVfZURuY1lRVjJGZGtob2lpZEtPUw?oc=5) (Wed, 05 Aug 2026 01:21:03 GMT)
- [Meta Ads introduces stablecoin payment options - Social Media Today](https://news.google.com/rss/articles/CBMilwFBVV95cUxNNV9HSzVSRzVINFZEMVdWUkhVcWpqdjJBclUwQnk0Sk5yVkRjR3BxaXpHX0hKNXp4SjRoTUZGTUd4eFdRNFVIeFJmRlE3RHJPc0xud0l2VHJnTUlPMnhxbU1TNTJHSFJIQWFtbzRhZ2xDVy00ZU5vMk1TamtHUTcyZWczcUVqSW1jc2NNby02M09JVGR5NkYw?oc=5) (Wed, 05 Aug 2026 00:31:29 GMT)
- [Stablecorp CEO went from &#x27;ridiculed&#x27; to running half of Canada&#x27;s stablecoin market - thestreet.com](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOaXRqb2FOdVRsWlg4SF9kUkhkMVpYSjlQZHJVMlFrZkpKS05EU2RvVHB0aTZ6cTBwZV95UWdyNWpWUUxEekZWVE81T0hwTlAyVnZzOC1BS0ZUWU5kMmdGa0RyTWlKejVQY1N5Q2JhdEpYWTV1WmNRLVNfcWlvUE8yS2JmSld3RnVTeU5Pbi1yenhnVjI5ek1nMXJTT3VsVEU4S3dwMlBxMWk1UWdJc0VNRnBLUGdJNTBiSXE4?oc=5) (Tue, 04 Aug 2026 21:59:12 GMT)
- [Cloudflare Launches Stablecoin Wallets for AI Agents, Opens cloudflare.pay Handles - The Defiant](https://news.google.com/rss/articles/CBMiggFBVV95cUxORVY4Um41blkwMGRKbTltZHIwVVRoVnVJOXhfRjZpQlhrNnIxQjJiaFNZY09uNFByWGh5enN2Zk93ZW1qaDZwLVUydUE2SWxaUExBTVFBTGsxYzU0bWFtTldEZlJpbW53cUUyRDktNzBjTUYxaklZcW1OWGRiaXZkU2FB?oc=5) (Tue, 04 Aug 2026 20:44:14 GMT)
- [US, UK reaffirm support for stablecoins, tokenization in joint financial regulation talks - TradingView](https://news.google.com/rss/articles/CBMi5gFBVV95cUxQVjEyTHhYNGpRd20xcWJZeTJWM0l0VGxrTXpnVnNGSXZ0cEl3M2JWRS1SUi1ST1Z6SHZldTdfWWVlbWRqel9OZk5VSmFiYzdWVFI1RG9jdER1SlJocVFzYVZ2eUV0Y1FnY3dvUVIwMkFPeHBaVTFtcE5ocmg5UnY4VXMwTVhKTXQ0Skg3ajRsUWlSRmhZOUxiNHNyMFpvUmItbUNkeGYxR2pZMVJqUW94UHhSa0tBTFZwMnUyYXIxQVBFNHV6Yk9tOFZoekRKV0JaQTI5RW1PVW9LR1dZQjF6WG9palAwdw?oc=5) (Tue, 04 Aug 2026 19:58:48 GMT)

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
