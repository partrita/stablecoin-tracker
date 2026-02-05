# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-05 01:18:13 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,971,466,600** | 🔴 -75.00% | 🔴 -0.53% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Moody’s warns of hidden risks behind $300B stablecoin boom - thestreet.com](https://news.google.com/rss/articles/CBMinwFBVV95cUxOREJDcGNvbXp5NGc5Rmt5X1NJSS0yS2Fta3R1dnRLS29KYzJVUjNqSlFwdjJ3VFRzVmlnSlRqUDRLSFVOUkFGUDQwalhqWko3aFUzQThmTUQwY1NnVE40ZDd2WWN4QnplSmtUblZwWVpaVVd5VGZqa05BLXFhMnJyd3NoeU41cnlJLURKa3VkSkZUOFAwTWFpZmhGVGxNcFU?oc=5) (Wed, 04 Feb 2026 20:46:01 GMT)
- [Y Combinator’s Stablecoin Funding Move Gives Blueprint for Enterprise Crypto Finance - PYMNTS.com](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQcFYwbTZ6b3NWV3RZNjBZekFaY2Y1alFESlA0dDZkOVFROWpIV0EtTS1IU1dCTTNDNlR2dlZWb0M3RV9UMmk4WHdTNEI2SFRzcVY1a0lTSEZHZk9LZllQSU81NXdRMDF4UmZ2YXVXYXVUTkpQRVprR01tWG5ONjQ2T2JWZ3EtcFRFYU9tLWI3N0FWdDNPMlZ1SHRQamxZR0JnQXhhTGVzbkVtTVUwbVl5VEpFS2x5aUZBa19HMFl5eGU?oc=5) (Wed, 04 Feb 2026 19:03:37 GMT)
- [Moody’s sends chilling warnings for $300B stablecoin market - Yahoo Finance](https://news.google.com/rss/articles/CBMihwFBVV95cUxNWDM5Zm9DLXFvVHdEOEV3YjMxaVBQLVk1VC1JVmFYem96NGduVVFMampHRUg1bXhfSkh2a0p0bl83TkpnNGhBcXoyNDNSRVpjQ0twTHlmc0FsT29JdFdnbGFacTZLeVdMc2dlSHN3bG5PN05rX3o4V2pIYTJDcm1mRnZJNzVid2s?oc=5) (Wed, 04 Feb 2026 18:33:48 GMT)
- [Nick DiCeglie proposal to allow Florida to accept stablecoins as payment clears first Senate Committee - Florida Politics](https://news.google.com/rss/articles/CBMi4AFBVV95cUxQS25XanhvR2otd1JRQW1RNUxJY0NOeVdsdHB2SXc0LW11cElDNVpIZ2NBdlhRdmV4NlRLQXJ0QVQ0cWxuSnIxY2FySnZUU2NFcmF5dHp1a2ZrazJFLXhjRW5xRFNYLVdmYUdwUnBMbnFPbEFOLVV6V2VZRnNzT1BtcWRxZUFGU0lDU3RlN2U3S3FFWk5pNVRPcERmbFZVcVNjRGtBRlNmZEltLXlFNUtzQXd6QjZUenhPbkhhS1hOUW5MUTBIdFFsX3owUE8yWS1jd0lmYkUzS25aZzFHMDFKeg?oc=5) (Wed, 04 Feb 2026 17:51:00 GMT)
- [Spanish lender BBVA joins EU banks' stablecoin venture to challenge digital dollars - CoinDesk](https://news.google.com/rss/articles/CBMixgFBVV95cUxNUVBHbnNkZmVsZ2FXdm1FVGItU01yVVRhU3VFTVdmTEJsU3lwZ0tCMGpndTljamR6YnZJZHl4MjBpQzAyeDM3ZG8tSkZQWWZlakZ5aTVITm5HaDhiSkg4V1JSLWN2d1ZqVmxXNE5pZHp5YTNwcnh4bE92eFVDbzR3U3FnckYtRUlOMndvSjFJZWVPcVJZU0stMkllUkxHVVQ1VW9pNXpUV1JCWmxhQ2QxTmZ4Q2Z6aEVNZHgzLUszbTBVME9Demc?oc=5) (Wed, 04 Feb 2026 15:47:28 GMT)

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
