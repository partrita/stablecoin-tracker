# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-28 08:10:28 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,508,098,519** | 🟢 +0.04% | 🟢 +0.56% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Dunamu, Visa Partner to Explore Stablecoin Payment, AI-Driven Financial Services - blockhead.co](https://news.google.com/rss/articles/CBMitgFBVV95cUxPaW1namRTbG9xem1veVE5ckVEWE8tZ19oMnh6bXJBVTh6ZUR0dS1fSUlYWWJTNDhfWWlObldWUzllcTJQWDZfaEtIVEc5OXA1ZXJKWjhWZkZIblV0MjFyZVRjY1d6MG9wQUhubGdtV2FJQjFNV3lvWWpiczFlRldkcWRrRGxFeXlCT1dJUkcySHhlak1zdmFpUFVHQ0tIN055eFlwaERaRGNpNEF4T0JKeDlHOEtiZw?oc=5) (Fri, 28 Aug 2026 07:30:27 GMT)
- [Bridge founder Zach Abrams sees an opportunity for ‘tokenized local currencies’ across Asia - Fortune](https://news.google.com/rss/articles/CBMiogFBVV95cUxQMDltRmZtdEV2anFxMGZ5WnNGanhNMHdQenZmenQ3eVNkQ3FIR2hpOUhsTXRtc1pEOUNJdU9fcFpybll6YVg1T1ZEMWFYZHdmN0dDS3k4bWFSUlJ1QXZJM0IxcmxHekFienFfbWNHRDhUdmN2SGxydTNac1FNMk51NUpDTXR4bnVTYWxsVTFXa0lqanAtc3lmaWt2VWVBOWQzNmc?oc=5) (Fri, 28 Aug 2026 07:00:00 GMT)
- [Bank of England’s stablecoin goals; can stablecoins fix US debt? - CoinGeek](https://news.google.com/rss/articles/CBMiigFBVV95cUxONkNxNnA2SldxY2VpNmNWaGNKLUl5R3pDRElkTU5VT3dVSDhHU3A1Z2E2N2VFRUQzS3BjREpONTlKY1pMRHpaWmhUbVFpb1daZkhJLWNCRnNCMzJHQ19OelBCTTJjaUJTYUVlczdab0RPbkdrR2hFTHQ2cEtQN1dteDQ5NnBCaE9aVVE?oc=5) (Fri, 28 Aug 2026 07:00:00 GMT)
- [Dunamu and Visa partner on stablecoin, AI business; Open Standard&#x27;s OUSD under consideration - The Block](https://news.google.com/rss/articles/CBMimgFBVV95cUxQbVdFal83RGwzX01ROGxaQ01kMFdWOFRqLXUyTDg4dlFybmpLZk81R0VkU0kxMnRsMjlTc0FpNGExZmJ6b0t4WXN1VXZWSkhWVmZjaHk3bWFJNDlMM2hScGtBUG4xQkR6dVY5bWsyR1ExLUpZUXlMMkhIY3d2WGd0Ykt5YUJySWNIZHk5Tm5vMEpRZ1VXTjFEZkp3?oc=5) (Fri, 28 Aug 2026 06:00:22 GMT)
- [Treasury Proposes GENIUS Act Rules for Stablecoin Issuance and Sales - The National Law Review](https://news.google.com/rss/articles/CBMingFBVV95cUxOUlFwT2ZBYVd5NjRvZ1VqR3NxMWtDcVdxUlllZnpJVTM4NFQxbDdhZ2J3RUpuMTdmd1h6clU1aEppNnh1a3IyLXdPM19hNFZ3QlA5bXdzNTQ5c3k4Sld3ZmcyNzUxZkdlUHZfZHEwcm5PY1oxTG1BS0lKMzVMRHZGQ01ITWdqS011MS1RNUpQSVNCekVxLVBtWVJ1VXVkZ9IBowFBVV95cUxPR0FvUlkwSERnRlBCR2lqWGxaZEFra3k0NmV3ZU5GZ3JBV2VmMTJwYmNJUUZfOWk5VFVPLWpsQUQzMXNaMDVSUlRNc2t2VTAwaUJSaHRCY0VGSlo4QVNvd0pycXVvd3BTRUFua3NURlRuM0JybTh6WUNHd3ZZZFhKQi0xWV8yOG1YN1oyX2lZRVI3ZXQyNkFsdVR5MXlmN054OG5B?oc=5) (Fri, 28 Aug 2026 00:25:30 GMT)

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
