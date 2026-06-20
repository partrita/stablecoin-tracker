# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-20 02:36:53 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,480,521,863** | 🔴 -0.02% | 🟢 +0.02% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [What is a stablecoin? USDC, USDT, RLUSD, and how they hold a dollar - Cryptonews.net](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5nMXZ3SWJ4TFFXQTFkV0tHb1Y1YUJIMUJYNlZlTGpleDZLOENsNnZXLU8tMnhXMTNjWjNjUWg3SEZKc0VrYWM0VVZWeUdUTmVTSlQ5TW9kTjlRQQ?oc=5) (Fri, 19 Jun 2026 22:32:10 GMT)
- [BIS maps stablecoin yield models. Do interest bans target the right one? - ledgerinsights.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxPTjlwTjJnemx1VE1iTzVQbjFYYTQwRFJtMUMyU0NTdVhHVWNCbXFIeHRlbzBiSTRDUkdndXdULWRXNWh5REdQZnRFNU83Ml9mZ1hTUkQySFdkMHRwQUw0cG9MR0hQYW95aTNva1lmMkJ3djJzazBnNGdrUldYWW1PNVp3Y3Z2THVSelVUZWlTRXFuNkw4U21KODFtckdGeGhTbTU4NA?oc=5) (Fri, 19 Jun 2026 17:52:45 GMT)
- [US stablecoin rules could accelerate adoption of digital identity credentials - Biometric Update](https://news.google.com/rss/articles/CBMitwFBVV95cUxQRXFQb1Mxb1ptcUQ4MjNKMk44czJ4dTN3bFgwRklwUmxnWXczcnZybGh1VTR6cEVncVhYemtEWWZlaEFfSm1TaVo5M0JEd0lJWnRZdm5EZFBCUzBHZ0xPalA3ZERTVDh3UEJ2VVlBVlBuaUcwYzlLS2NqTENBT0E4NHBwZTRGWlZjbHhOakJHQWU2dUh3NDNjQ29qUHktZF9DUDVUOXBxNVZhVlRrOFJoUkM3enVMSHM?oc=5) (Fri, 19 Jun 2026 17:07:00 GMT)
- [FinCEN and Banking Agencies Propose Customer Identification Program Rule for Stablecoin Issuers - The National Law Review](https://news.google.com/rss/articles/CBMitwFBVV95cUxQMGF5NFZ0R05FUDVhRXRDay1SNXFscEhRRzZhVU5IdUl1WlVmbzhuLVdEVlprNm5jVkhuUXNydFJtS3UwbVJYS2ZWbWVGWkNZWFljU1hucWkxSFp1UlFBTzNXeFk0U1MweWJYWGdLMEZHQ0I1RDFVSm9aQS1BdkhEQVk0aDJmRzFXb3lGX1Y0QmUtVjhtRlJPZ3RLd2lNZmlwSHZlVUhYaUZWQ2FseldIaDVXQVczcmvSAbwBQVVfeXFMTkUwcG5ZYnNPZkF2NGM5aVdBT29oOGFGdGk3TFVqVFdaaklHSGRVc0xRWDhjRE9LeVJCaHdXYXBCbkJ2Z19HWlVVbFlER1ZDT1hORnN3WmRmcFpPWFo4THYycGp6V0VYa0lQWGt0Wk5ISV9iTGdtMThwQUlxMzAzT3Y0dmFPSk9TVU9aYno2RGtFZTNFcFBHY3lOMGlTQVJKLWl5aWhRcG95N0Ffa3hlMVJRU3k5bG1rTnNaLUw?oc=5) (Fri, 19 Jun 2026 16:58:02 GMT)
- [OSL Group Secures Australian Financial Services Licence, Strengthening Regulated Stablecoin and Payments Infrastructure in Australia - The Block](https://news.google.com/rss/articles/CBMi-wFBVV95cUxQYnhYWldieFo2MmNsR3EzcURDRG9zUTlyNzhZa2FVZDNLYkx6VmtUdGotaU8xY1NXX3Q2aWhPaUtiOHdLTGdVNXNkcGNsYTc2Z2JFQjN4dVZTbURkTmRTTTRrclptSnlDV2V5NHpnMVZKMkFBeWRwTXpqSXM5dU52MGVWMXoxNkE1dzYxUnNLQ0ZjZ3J6Yl9rRWtVTFV0dGZVUnhHT0ZHLTE5dzMzZ0ZYRHh5NUpiLURNNkZCRXhpYXJNTllDY0JpNmZNVnVMNlVZRW4ydU1sY2tIMkdxbk1kbEhoeDF1SmJwLVhWME9nMWlvc2RBMi1USFoxOA?oc=5) (Fri, 19 Jun 2026 16:45:33 GMT)

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
