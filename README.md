# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-15 02:31:43 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,509,916,418** | 🔴 -0.21% | 🔴 -0.57% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoins in Latin America: Why Mexico and Brazil Lead - Ripple](https://news.google.com/rss/articles/CBMigAFBVV95cUxQMVhWTFRKYW15alZZaWZ6UGk1eGllZnhMYkVaRXY0d2tVNXBfUUxZYzFWbWZ5dTVGOUduWm5rbmNRRnhYYzI2a3NZLVhTZktYNkllRGJ0bHRyMG5NUERSVWpjZVdrTnlkcXNGU3U2cnNFd3ZFTUZMUzAzZ0hWSjFITA?oc=5) (Wed, 14 Oct 2026 21:25:11 GMT)
- [Qivalis: EMI licence for a euro stablecoin - CryptoTicker](https://news.google.com/rss/articles/CBMib0FVX3lxTE9Fb0pSeHNxT0lRUWFreHNZTkpNall3cTMwWEdnV0Fmcm41eVlqLTN4a1ZxXzJZQmNqRkZPcGVMMEhFVlhPM0xlem1yZEtORnpESWFCSFQtazVPdGFySEIxTFFUUHI1eUJOeWllSnNMbw?oc=5) (Wed, 14 Oct 2026 21:21:58 GMT)
- [FSB outlines AI risks and stablecoin oversight &#124; Inside FinTech &#124; Global law firm - Norton Rose Fulbright](https://news.google.com/rss/articles/CBMiswFBVV95cUxQSkI2ck5iT00wTlBGTm9HWjNrXzRkbVMxZzI5Q3RnWWdYMlFITFlrR1U2SVFlc0RzMTl2cVV2UmVIZWo0QlByOHRxLTN0bHhKZVdvby1qZnhCaGRFdnNJYmRnZGZEWTFlVGkzZXNZam43ZnF5ZXgxWS13ZWtJOUItWnpiX3pPN09SeTJaY3Jsajc4RnVBR1VVcDVsMklrLVBJdDR2SmQzTEN5Q0pzVmd4NFc4TQ?oc=5) (Wed, 14 Oct 2026 21:03:10 GMT)
- [Stablecoin Firm Qivalis Moves Closer to Issuing Electronic Money Tokens - PYMNTS.com](https://news.google.com/rss/articles/CBMisAFBVV95cUxPSEdUUDZXZFZBcWp3bFU4YS1VbkJ5VEt5LWZacEF6SUo5bEdJWmVwLWdzYUl3TmJBemRyRG1KeWc0T1BlSjR5bjFKc3ZXVW5oZk1NVWhmaU1Ocm15S1N6eHNYLVB0aldIOFM0ZDZDaUpmODNPRWMwS21JSzBKVWlNNUM0Y0hzNG85cGRjUkhWaXhfYlJfeEZkOWxHZmJHZDJwSEp2U1ZJYTBXRFNlOEc3NQ?oc=5) (Wed, 14 Oct 2026 19:43:37 GMT)
- [France&#x27;s 31.4% stablecoin tax proposal risks driving crypto activity offshore, warns Chainalysis - CoinDesk](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPNW43UjByZ0pBWkZucXpEalprQ1ozN0VSOVF1OXRmaFhOQUp5Q2llR3haZHdWcDlIT3A0OUd4cjRGWU1YSUMxSjRHcTRqRUFPZWhRXy1TZVptTS1MVW55OFJpeVdURFFDZEZhM2hOeFBHRE84UXNRSFVJMzVaZUJGWFIwczFUVno3aDZwVGdQMV9Nal85cHZzWTBlaFIzaUc0UnRqWGVmQXFod0c1cG1tUFlyb3h3TV9hRzRSRS1BbDQ?oc=5) (Wed, 14 Oct 2026 19:33:00 GMT)

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
