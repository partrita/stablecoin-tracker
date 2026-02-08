# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-08 01:53:37 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,463,534,976** | 🟢 +0.12% | 🟢 +1.10% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [South Africa’s Kganyago Warns on Risk of Growing Stablecoin Use - Bloomberg.com](https://news.google.com/rss/articles/CBMitAFBVV95cUxNQ0c1TDFQcjVYYzBtc2gwdmU2VHprSWJRSkR5QTRtb1RmQkwzY21NTk02WkdpWmRFQllBNGZHWldXdG1JTFp1VEkydmROUWRJZlhVSWJmV0Q0eldMR1RZb1B1OWdGMWljQkJJMmxGMFN2UzJTaWZvaEdnS3NtbHhWcllrVHVxdV9SeXpaY1U3QkVTcHZCMmV6dE9VZDRycFdOdV9FczJIcWNXR29WN1dMNWNOY1c?oc=5) (Sat, 07 Feb 2026 17:33:10 GMT)
- [Stablecoins Beyond The Hype: Lack Of Credit Protection For Holders - Forbes](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNZFBzY1JXYzc0UXlqRDk1TXgzOU5URTBIc29INWV2X09XVG5oYkZrc1JZVXYxMndSQ1ZONkdtd0FCUDBHeDhyV2ROdGFLRkVQU2pRUDZoM2FOdU5nczA4ZXQ4OVhFMWxIUG5iOE1WZW1vZ0JINUdRNjBTLS05MkJNQVIwMkVmVGJXZC1DTlBDdHptS0M4dTF3WF9scU1zT0staWJXX1RxZGNqbnVUbUs0OFFDZ2dKNTNCR3pEOUtNdGpUdw?oc=5) (Sat, 07 Feb 2026 14:15:09 GMT)
- [Binance Gives Trump Family’s Crypto Firm a Leg Up - The New York Times](https://news.google.com/rss/articles/CBMieEFVX3lxTE0yOUg3X2h5T05zemFLR2lkWGZrMmJvNHd6Vm92YkNicEM2dXFmb0xTUDNDc1FWY3ZMRGlMOHVOZk82MnJSTjFWbnowUFZXeHVaai00bE1GVHB2ZlNzV0l0VU5iSjJ5b29PMGliUTM4X3ZINnMzV3RpZQ?oc=5) (Sat, 07 Feb 2026 10:02:10 GMT)
- [Tether May Be Forced To Sell Bitcoin To Meet Proposed U.S. Stablecoin Rules, Says JPMorgan - CoinMarketCap](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNSi1pQ0U3bGFxSllLWlo5LUtEaGZ1bGVzdlJZUXN5and4WFYweG9DRUtGZFVPandmLXlsYXlaQlRwb2tiX2FleWpBVjVmMnQzb0dJZUdJOXVTVDkwSVdyME1DNDI4QXZRMVRlVVlwXzFIRFYxSGdNZDBaMDZ2XzVLMEw3OWhfOHBNUS1jZDFOVkhCQ3NhelI1UUl2M3ktZzRMbldEVUh3YkJnV1o4NlpYSFpkTUNpYmVRZDljWFM0d2Z2NjZSMnNNbg?oc=5) (Sat, 07 Feb 2026 07:17:04 GMT)
- [CFTC Updates Crypto Collateral Letter For Bank Stablecoins - Law360](https://news.google.com/rss/articles/CBMinwFBVV95cUxPQVYzY3lnUEpjTUdka1RIQmpYbndWbVZ4SWZmVC1sT3E0U25KLUhxRzJha19obG9wMzhCbXVHTmk3OUZrQWxmYWpVaHl6aFNpRlY3RGx6Y29zdTA4SVRzc0EteDR5Y2xES2tZektHa3lOaEpjSVluRlZxdmhPcVhoc3BLOU1wZ0I5WGNvNVExV0E1dHFHNWFUY3Zpd2ZCX2_SAVZBVV95cUxQT1JDWDNEMWVvTUd3VjgxUC1EeW9CNE9fMUZBU1ZvNnNqVEhubmZwdkRmSXJScV9Za0U5Rzd1N2hIaFJqbHZkQkJsU2p1LW90TURiQWdtQQ?oc=5) (Sat, 07 Feb 2026 00:50:00 GMT)

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
