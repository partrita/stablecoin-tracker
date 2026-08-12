# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-12 01:20:08 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,894,087,088** | 🔴 -0.04% | 🔴 -0.02% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Lebanon’s remittance lifeline has new gatekeepers - OMFIF](https://news.google.com/rss/articles/CBMihgFBVV95cUxQNXRhUzRfb1FIYW1vaEhuTDBFdmcwc2cySWxWbWRTaFhNWExpZGZGM0dnNHp4RmpjbkwweHZMVzhkVm9la3pXZ3QwdC1Fek9xSE5teGdOVlpnSVg3a2tOTDR2bk1FVUxoU2FPTGV5aWtfRjczS1JxSnF1dVdtcjVqSDV4VTNxUQ?oc=5) (Wed, 12 Aug 2026 03:41:32 GMT)
- [Coinbase CEO Brian Armstrong Says ‘Crypto Doesn’t Get Enough Credit’ for Unlocking Global Financial Access With Stablecoins, DeFi and Bitcoin - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxNdnZEajBTSWN1UWhlek45UTBLVHhnR2s1VHE3OXRxb1FyZDV3cl9aVDVyT3NPeEd5TXoyWEtvckk4dGRHRTJYMm5iSlIyMUlDaUV2d2htbG9ScTg5S0tDMUxuX3Jhd1VoQWFhMnVJQ0lJbDVPTlhuc3ctQXJtVk42Q0RsTlUwdlpmQ05yVGh2MTNGSGt3TERCTnFQLXNIUms?oc=5) (Wed, 12 Aug 2026 03:31:00 GMT)
- [Cashi launches stablecoin Visa card in public beta - CFOtech Asia](https://news.google.com/rss/articles/CBMigwFBVV95cUxPUWl2dzQ5blpMREQ3XzhvbHJjemtNQlhoN2pocUhpQ1hSSWtYQXRIVmhjdW1xRGpNUDdHYVNiX2xlWE5jajh3aVJCYUpSNFVCei1PNmZHUnl2ZW1kRXMtVFBSMDAtMUh4SXRncE5fWm5XZHN4ejNBQ3pILTVoNjJlQjdqdw?oc=5) (Wed, 12 Aug 2026 01:40:00 GMT)
- [FDIC Chief Says Stablecoin Users Won&#x27;t Get Deposit Insurance - Even Through A Back Door - Yellow.com](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPTjFzRkRvVEpCbm9tTjBpY3ItWHlLMWdjcFdXVWxENHZPTHVuZnVMZ2NMcHowc0dVSTg1Q2RpZVRvQ01pbUZRT0xEZkdhbVNrb293V05nZXhSOE9vUzFoWXRQekFEMk5iQlRqS28wZllWRXFBYVFQbmFuTG9IZlNzdDBIRzBEZjhBVmRkblVOOFN3cUd1cWdNTmNjTkhldFc1c1doUy1ZVUZXMXRwRWd1ZVJucmdsa3lTSWJB?oc=5) (Wed, 12 Aug 2026 00:18:12 GMT)
- [Stablecoin Development (SDEV) files S-3 for 212.9M-share resale over warrant deal - Stock Titan](https://news.google.com/rss/articles/CBMivwFBVV95cUxPMFJmN0FVLUhxWU5Pd3F2dWNaZGpsRlhsczVmbkxsQUhXWm1VWlRrcWowVXY3ZDhKLVhUeENGVjN1UWZ4a1lhaWs4X0RDaDBGa0VXUGJraWxSSEFDUXR1cWZtcVRsT0lDekZpQVRscjNEMkVOX3JrQ0tMLXJJR0EtbWJUcTNVX21QOWE5aUJLTXRTNHlfc0E4OThPUUlKaGp1cTUwdER4WEdweG9hSmVaVGZDNS1jclhmVktTWERxcw?oc=5) (Tue, 11 Aug 2026 20:17:44 GMT)

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
