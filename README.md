# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-27 05:58:49 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,399,233,299** | 🟢 +0.08% | 🟢 +0.84% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Visa joins BLOOM for stablecoin settlement. Shinhan adopts Visa Stablecoin Platform - ledgerinsights.com](https://news.google.com/rss/articles/CBMitAFBVV95cUxOQTZpQUVmS21Wc1BPcTFBYkxwTWczOHJqMk9qTnR6V2xMX3V5MGNRcDMyUS1QLUVSb2NMQWlNN254VDlnRmtCYmpuNzRRR1lQSVk1RnRXbVhBS3BpMjVFOU8wSWE2QXpabUljQ2MwX1dRaHFKc19QRkR4QS01T3JFUmpSMG9SMVozZkZSQzdVcFMybU5QN2pPTFNfMWZjbFduVGVUT2ROazNGeG9IcjdVeVduWGI?oc=5) (Thu, 27 Aug 2026 00:39:48 GMT)
- [Revolut Launches EURR, a Euro-Backed Stablecoin, on Polygon - Polygon Labs](https://news.google.com/rss/articles/CBMikwFBVV95cUxOenE1d2dBR09RSDRrYnc3dFZaUldEQWlTamUtMzJTRC13NFlGTlA5cWN6RDkxVzdtSG1teTlNbWFkUERmSlNPa0RkXy1XNkJPaVFqT2FLTUZXTW5EejR0eHFHZTVZekNCaGxmcDY4aVpROEZIZWZkM200ZW9qNUdPZTVFNHJVLU1sMml2bjBlbjZBWDA?oc=5) (Thu, 27 Aug 2026 00:28:08 GMT)
- [KiiChain Adds TRON to Expand Onchain FX and Stablecoin Settlement - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxPTTZOcnhNSllaZVlHeUFQV0RxUjV6MUpRN0hPQXFQdmdwaklQUlRTWnEzQ0NUQWxVV2FDeVFEODlDZVF4NkFBb0RzT1kyaWRzQ0FsWU1pdXVBajRvZG5BemZvNVNWQWkxY2xaeTloODlORmJlMHVwTW9nOFQ0dXUya3NYcm5hbXpGbTNWSk1kUmpWN0w5bzhSUnhZWG1fVDQ?oc=5) (Thu, 27 Aug 2026 00:07:00 GMT)
- [Stablecoin Card Spending Projected To Reach $50 Billion By 2028 - CUToday](https://news.google.com/rss/articles/CBMioAFBVV95cUxQMEYtbjlrMHJCQ0RaZTRJb2lsTmhwRFBWQUw3WWxGcUdIdFB4Yl9XMDFpSFZQbk4zcE9tMEpxR042TlVCUHBhSGYydzJ5OGxDOWpCR3JxcjNMYUVxZmxxd2NMeHd3T1dkQ2xVem1zVHZJSjZkQ1didGFQSlBxYzlfcTMydHRTYWw1aGEwSjNPdkNIdWtEbFh0UU1sXzFsUXgt?oc=5) (Wed, 26 Aug 2026 23:43:24 GMT)
- [Stablecoin Card Spending Projected To Reach $50 Billion By 2028 - CUToday](https://news.google.com/rss/articles/CBMivgFBVV95cUxOYmswTGF5NXU1TWJQNk8xNEZ1MzhaQ2V2b05NQWlPR3dnLXpkZllzRGpGb0RBUjZiNml0RHVTSE5YTGxmX3J2TWw5MTVRYjJwRkc5Uzdia0ZWQjhNWkNWN3FnSFV1UldOdUhwbTZzMURUVi1wY3V2cWg3YmQxZ0ZJRzJJYmxYZTFBU3E5OFB0eGtPTEpmMngzZkVMbDVLMlRlRFVqSEwzX0daTzR2SzF3aHFpZUNpcDdFdW9jOWl3?oc=5) (Wed, 26 Aug 2026 23:38:40 GMT)

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
