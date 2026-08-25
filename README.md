# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-25 00:45:31 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,125,343,535** | 🟢 +0.04% | 🟢 +0.85% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Treasury Proposes Stablecoin Licensing Rules Under GENIUS Act - CryptoRank](https://news.google.com/rss/articles/CBMioAFBVV95cUxQdmRnVk51M01BcTRiR3NDQVFuS1RhUlZWdlIySExVWU42UXdkYURQX3ZGYzdvdFFiWXJiejVMNWpkSC1pYnZsQWJLZ0hReGhHZW9mUGNFeHlDdjRxemhvTS1Mc3NzUy1VbVhtTHBDQ3M0TkFGcTRyTGc1ZDFTUWxhdC00SEZPdUNBQi00UWpnbFo1dVlvQ2xDR28tUHhDZzlS?oc=5) (Mon, 24 Aug 2026 23:07:05 GMT)
- [Treasury Proposes Stablecoin Licensing Rules Under GENIUS Act - TradingView](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNQmJ4X3gtWGR6NHBrR08xUmRfZDhmZlRRX3YyYTN6LUtNUEVBbE5fRWpuT3V0VkhRN0lTeUZTRS1idTU3WFVISUJ5QWhqTHVaY2g1RmZ6WUFjbkdmWWNPZDI0QVU0VXQzTm5GOWJMWDh6a3l5My13YVpXak5NS3pMNTI1RUgtNDhaWUVtNThoUmJmUFIzTV9IZmpiMWxsS1VQZ2lyZTRaVGpwVC1VcnZCM0RpMEhPUHNBeU5V?oc=5) (Mon, 24 Aug 2026 22:45:00 GMT)
- [Crypto Card Spending Tops $1 Billion As Stablecoins Gain Ground - CUToday](https://news.google.com/rss/articles/CBMioAFBVV95cUxQOU85d1VqQ0cxMGN0SEsxcnFhaFNhMEtENnd5dG5wYVpjSm54RkxIQlZaNGRLOFRubVVMYlJDY0VlVF9lV3paYWhrLWJ6eDlOQ2ZTNkV1akpELXJzZEtHYk1zQk5PSGMyMjJXNHc2ajFGLXpubzZiZk01R0FuRmc5Y0QwM01MRDVvVDZYXzdaMGttbnJUa0dWMTFVTzZ5SzdC?oc=5) (Mon, 24 Aug 2026 22:24:30 GMT)
- [Stablecoin KYC Debate Moves to Exchanges and Wallets - PYMNTS.com](https://news.google.com/rss/articles/CBMinAFBVV95cUxNRDdRN1FBbzVxZV9rMWhJX192cnJ5dllseHd1d2c1OVNFS0lHS2w4UUFBRW45Y1hVcFNOanJobVFHZEw5V3YtWVBjTlRfdzBJUlJqdUdOWWpIdzluWTFtQm1rSUpfdVdwY0oxbl8yQjhYcF9XcnlQRDFjTHBmVEZ4U205cm1xTTNtTnpoMzZldGpRVWh5TWY4VjdOZDM?oc=5) (Mon, 24 Aug 2026 20:07:19 GMT)
- [Fasset Reaches $1B Valuation with SBI Group Backing its Stablecoin Payments Expansion Efforts - Crowdfund Insider](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPUm5tVTNod2EzYXI5R2RIZmlKNUYxVzV5QVA3TGt4YVZvSFZJSnRTOGxIUWVyYk4zQUxzdWFvTy1vamlpTV9lWVg1Q2FmZkRtZ0pHa05JSFZQMVVCdnhWbDZsREhUeVpHM2JmNE81YVNybzhheXZUZ0xOdnRxQ3lhRHY5c0VvTHlBRVhQelpJZHkwYkJla3dnNzdUcktXbHhtY2lOVk1XdGd4WTd1eV9xUlFudzNScDZWV3BLT1VLMXk4VHVfX1lUQ3dlX1dTOG54OVEySmFlTFU?oc=5) (Mon, 24 Aug 2026 19:51:16 GMT)

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
