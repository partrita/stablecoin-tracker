# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-26 01:28:34 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$298,030,695,165** | 🟢 +0.00% | 🔴 -0.32% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoin Regulations Put Wallets at Heart of Digital Cash Adoption - PYMNTS.com](https://news.google.com/rss/articles/CBMirAFBVV95cUxQZFUzQlJqOUZ0SHJCM1ZMa2MwWGpqRXNYTkFTalg5SmJnYnRnMGlaSmcwbi1zZlhpTV9vWEJ6UGxsNzA2d203YmpYeGdNOTMxOGJsY3RZQkoxVDU2WDhHbWFtb0RIWUx2Q2NLdmtIdnVuQ1JpVWxFdFU3YUNoZ2pwTDVnekh1Vm5BVXF6NDlkNl9wZnBRSHo5M2kyUHN1eXRHMnJrME9janFFVWJp?oc=5) (Wed, 25 Mar 2026 23:31:48 GMT)
- [State-Level Stablecoin Push: Delaware Seeks New Regulatory Framework - CU Today](https://news.google.com/rss/articles/CBMipwFBVV95cUxQcEc0LWxBVjlBV1gzSTgwZWltcGl5bGVVUUhWTC1pUFN0NmJKNkpnQ1M2U0M3c0VqYk4tS1RsMHhnLUcxNjFLWlRPOWVpQWJXdVZvQ3E0cUZsdjU4XzVoM0tUam1hTDFsNEJRb0lxUnFLWVhGX05QczFTNllBM3A4cmxCVXJnbFVlY0ZWblR5QUtmS2w1SnRVVnB4clVmMW5tY0ZBSDNZaw?oc=5) (Wed, 25 Mar 2026 22:20:02 GMT)
- [As The Clarity Act Clock Ticks, Cathie Wood Buys Diving Crypto Name - Investor's Business Daily](https://news.google.com/rss/articles/CBMipwFBVV95cUxNYk1hd1BDTkZ0Tk84UWxrNjB5cUQ2U3JFMnJYNG1RZUExSk1JRkF0OTM5aDZCNnZKaVN3alMza1k4eHdpNW12Z0FyekVCakVvRFYyc19tQk9meU0xellMTHRDcGMwZ0NlSnFWbVVMakxGWnJpb29mN3Myb0tONzViblJjTzNLV2FlbHZ4cnJjWjcyYWg0YzZNOFVnQmMxUVMwSFNNZFVuRQ?oc=5) (Wed, 25 Mar 2026 22:06:00 GMT)
- [Ripple taps Singapore's central bank sandbox to test stablecoin-powered trade finance with RLUSD - CoinDesk](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPZnFPTGNZbUhaellQczQ4VHd2VXg1SzdTUGxGcWlpV256TnBjUndad0VOUUNIdWQ5Zkg1ckMxc05tWEVfOUJSa0lFR0VGdDN1SXdGcWlQVEZiLWtQV05Va0JVdVZfdUJyVUt3NGhGeHpRQnVZWjduSUswVkFoNmJNSkYtN0xQVDhIVG1ack1nb3lERkVhZ1R5cWxOeW1fTzF3XzlUZnFkWWtUdVVfdFhpT1l3NF95SlN2TDFMQWNYOGlrOHE1ZnBIZlpBSXREVHJsb01SOFMtR1g?oc=5) (Wed, 25 Mar 2026 21:13:07 GMT)
- [Stablecoin Yield Reform Raises Stakes For Community Banks - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTE84VlZUV2llQ2xod19SRlBWQ2FSV195ZG51UE9TU1lvRG5MeVhXNVRxWjdHUnJWV01zdDFtTkNlUUNtMEtyZVBySlRhT3ZFV0xoOGZXbFNB0gFWQVVfeXFMTzhWVlRXaWVDbGh3X1JGUFZDYVJXX3lkbnVQT1NTWW9Ebkx5WFc1VHFaN0dSclZXTXN0MW1OQ2VRQ20wS3JlUHJKVGFPdkVXTGg4ZldsU0E?oc=5) (Wed, 25 Mar 2026 21:00:00 GMT)

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
