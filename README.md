# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-21 00:48:06 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$287,893,265,386** | 🟢 +0.31% | 🟢 +0.41% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Opinion &#124; World Liberty’s Stablecoin Becomes a Partisan Target - WSJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxORjRZOEZ3bnoyWFlNc19ZeUdCNWNoWFM3UkF3NzdObVlrWDJxTzJ2dVVhZENlRk0zTzhkZHlzU0dWRlRXbjJ6TGw1RWFOY2hhcHFWN3Z6SEtPM2dFenM0aUpfWEtUUkxQUzFPM2c2RXJzM1V2bkZIUVBYdURkR3R4Z1RvZlJvTzhwQlFFck5ZTXZEUQ?oc=5) (Thu, 20 Aug 2026 21:09:00 GMT)
- [Federal regulators rush to set stablecoin rules by November - Northeast Times](https://news.google.com/rss/articles/CBMinwFBVV95cUxQYXR6YS14SHRMX193VkZGazdoY19zVHJNSmZfdGptT3FmcGZaOXdnZ0NRZS04WlVUVTRlRzNzR3l3RjJKOE14M0VRMGE1T09ST0FTWmREZ2VOeDN0SUEtT3hRb0NwdHRBekNjdmp1TTNmcGdpSWRHRzBDUWZxTWJNY3EyVG1zUU9jNndjbUZwWXp3RGF5NXJWOVN0aENVWjQ?oc=5) (Thu, 20 Aug 2026 20:03:00 GMT)
- [Deel and Mesh Partner to Secure Global Stablecoin Payroll with Instant Wallet Verification - FF News](https://news.google.com/rss/articles/CBMitAFBVV95cUxOc0t6ZEdoUHhWNjFNWEVQU0RhcWMtNGVMLUtFQzZmTkVKcHl1WjVfbUs1emhSa2E5UmU0eTE0RFR5cHkwOUM0WTRMTVBEUHVPVXFNRlhSY21Ua3pKU1dhVjlmcTYyVm9iMkpzNnlaSXdIc1BQblljS1luU045WHBSVHYxOFFhTkxBS3MxRW5Gc2t3SXFjOTl5T2lTMkJwdTQwWkhGM0M3dThuamNGNGVrRkJiTWs?oc=5) (Thu, 20 Aug 2026 19:40:01 GMT)
- [Stablecoin issuers face an operational test before 2027, Telcoin president says - Crypto News](https://news.google.com/rss/articles/CBMieEFVX3lxTE1xdmtQRlBWV3g0N0JmNG1RQ3B6bG41blZEcGxDVnVYRGRRbHNHcVp0a195RHhZREJFdS12Z1pTNE1zbFlyUDdEWmpUSjVCcTlGc21pUEpqc2lmdm1fQmNoeGhVWEs2R19RUHhOVVdUTE5PaWZqa2psYQ?oc=5) (Thu, 20 Aug 2026 18:33:28 GMT)
- [Stablecoins join the payment conversation at X - Yahoo Finance](https://news.google.com/rss/articles/CBMijwFBVV95cUxOOWVQNnRfSTU4LWxCMXpwSHhELS1SSzZ5U2VBNTh6MUhldEZQTl9VZ29vaFNQMlh3WDBtZ21qRDNhR2pmSExtYVBtdkdkZXBVeWdibDhTM29vc05jTXVVR0JYYjd5QV9VVkZpTmwtc2NWbmpYSC1XR2VrSHc4Q2dDMlV0bUxwVDVJVWJyX2ZUUQ?oc=5) (Thu, 20 Aug 2026 18:23:00 GMT)

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
