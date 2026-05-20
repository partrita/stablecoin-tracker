# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-20 02:33:38 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,678,978,166** | 🔴 -0.07% | 🔴 -0.12% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Blockchain Association warns FDIC against favoring big banks in stablecoin rules - AMBCrypto](https://news.google.com/rss/articles/CBMipgFBVV95cUxPRHZ5OTBacWZXMjExeUZoQUtOcHRSVHFBWmtUeVBKTjktcUNPOTFCd0RxOXFVWlB5M2RKTm80R3Rsa3hwemdUVWJCMEpVYlp3Vmd5X3dJRUFRVkk0cllMMGdrMTEtUHE4NExrOHFzX3R0YWdhR3ZpcWdwa215MzJ2Y2JJcEloZG9VRU9LbXgwb3J0TEUteVFKSWp2dlVOZUVfWFJFbURR0gGrAUFVX3lxTFBYUDhJTVNUeGludlNsZ0JrUWV1bUNGeDNRSlAtT21tc2dmVjdWOVk2Q3RXT1c0c19ueEZ1eW5JcjYzRy1rcXNYdkJWdjM1NXhrcHExS0FyaWpXam1qMWdDVUdHdDh2aDM4LW45OUpEY2tybjljcXQyMVlFaXg4YnRhT0VwYmhJeWNFa0JRMHl3ZVA2REh5eE9oR1hqSDdNVlNOekZwUnVtVFpmSQ?oc=5) (Tue, 19 May 2026 19:22:55 GMT)
- [What the Hyperliquid Stablecoin Deal Was Really About - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxNMWFva0hqTWZnd2FuUlhaTnVBd0tOU2MwVkhuQXhkSlRnR1ZzaTF1dUdMNTNwcXk3NVkwTGYzR0M2SURldUgwSE85SXBDR21Cc0c5MnBBOXI1NG5xU05mYjJyS3R2YS04bE1iS1p4d0dxTU5FaDh1ZndtYmlxOGZFYkI5M1EwamJQV1BHWm1JSnJYTmF0ZmZrcXNYbl9vYTVG?oc=5) (Tue, 19 May 2026 19:22:23 GMT)
- [Stablecoins As the Missing Link in B2B Marketplaces - Circle Internet Financial, LLC](https://news.google.com/rss/articles/CBMihgFBVV95cUxOeWgtamVHV0lPRWo5bzVnZE5nTVBickYtQW9UOFFHRDhXMmtLaGxURHBycmpGQXhCYkdNUEFXaTZsWmpGV3VrS0JjX1hKV2NOT0FDdnVBdUlORzE0bjVsRVVtTHU0a1pDbE9PTFJVX0dQZzEwVVFVQmNTancyUEFwTy1IVWw2UQ?oc=5) (Tue, 19 May 2026 18:18:22 GMT)
- [BoJ Deputy Governor asks how much ‘singleness of money’ stablecoins need - ledgerinsights.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxORElMb19vWVpEMWxtRl9wOEYxV2JjZ0ZUdUJ5SzN1S0JUcUFtRkx4TFZFeVo2RXY2bFhmNjFJNTBlWVptLTJ0SUtabUZUeVh4ak5UUnNFYVotbW10Sk51ajk3a3BuczhveGFOcWY2dmN2TG9UWWtiRXVCTUZFbjRWY0hBRWNNQWJIWEo1VE1JTVVoMS1CSWl3ZTV1enItYzBXb0RuYg?oc=5) (Tue, 19 May 2026 18:15:19 GMT)
- [Checker raises $8M from Galaxy Ventures and others to build stablecoin infrastructure - Crypto Briefing](https://news.google.com/rss/articles/CBMie0FVX3lxTE1jdUNVQVlLODVKdXpSelV0c3lKSHpkb29IaXJ1VUlSbGIyOEJGQmd4ZzhmRmFVMUYzQkJZUmhQNTQ4dFBIYnRGY21SWDNuOWlKZDFNa21MTi1hQ0JtRFpRekxIZVVuT0FTUEpiOU4tYVBMd1hRSTBQclVlYw?oc=5) (Tue, 19 May 2026 17:55:15 GMT)

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
