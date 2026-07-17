# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-17 01:54:48 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,176,086,314** | 🔴 -0.02% | 🔴 -0.54% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Visa Launches Visa Stablecoin Platform for Banks and Fintechs Using Open USD: 17 Sources (Western Alternative: 9) - NewsCord](https://news.google.com/rss/articles/CBMi5AFBVV95cUxObFpxdmNweWYtQVZGYTBwTms2TUlHNnc0bEI3YmhmMVlIdUF5dmx5V3ZOSUZLelMxM0l1MDlSQWc3NGdUN1d0M2IyZnJqVzl2dW8xaHhpSlN4VmUweTZ4VlFhZXlTMUhYNWN4NUJzSUNFcHlOUEpCVW1URHRmUFlHMXctT0ZkNkdMYWMtX2g2ODhVZUNmbWtQaWhsaHZaMnNLUXJVbllXX3h6dV9IVmlsbUhPaUFtWHF3NTBCQXhpWlIxdXdDWWhYOXdIMF9ZbF9INzB1akFobUtqNy05VDRIaklzTzQ?oc=5) (Thu, 16 Jul 2026 23:17:48 GMT)
- [Roundup: Trump’s social posts / Lilly’s psychedelic bet / Visa’s stablecoin push - Baton Rouge Business Report](https://news.google.com/rss/articles/CBMisAFBVV95cUxQeHViYlJ5V09SSU1MTk5PQU1zTGo2UFYyV0Y3VFF5X3ZfU0czU3RUVll0SE5QaC1rNkRwS2pyOC1xU1ctTzY3R3RuazdRazRPaEVuLWhyMGZkbW96bG9oeDc3UFhETF9jbDZQa2h6SURZcjZ0ZllmYXh1V01iX1c1azFweS11VVozQ3Y0TU9MR0JydFRpRVdnbTBuZkVfak1RZkJBcTJESmRQZExkM0xmNdIBuAFBVV95cUxNdVU1YWx2SG9QR3lkZ2Vjb1FkQnBaeGVUdkhnR3JCcGtES1FDSVJXTTA1WDJQZDE0ckppb09ydnBHWU5WT1FjT2VRcTEwbFFoTWlSakNEeDZjNXhYZ3hSdE93TnptVnk0MDExVDJBcUIyMFptakxBYTdEbFI2bjdWYmY4a29TRWpYUmw5OTQzVG5VVGIyQjF2SlhTemE5T2FEb0NGNXhtcDd3X184eEh0dVVUc09hUExS?oc=5) (Thu, 16 Jul 2026 20:07:30 GMT)
- [Visa launches stablecoin platform, taking the opposite path to Stripe - ledgerinsights.com](https://news.google.com/rss/articles/CBMiogFBVV95cUxNVmtuejNFM3NjZDdSNFVJN05KRkhxOHFwU08zTFF6dFpXc183OTBNajBzaDRSSmtlRXdTdzFmNG9tVklRdHpvUnh0VnpjenZLZ1VicEI3RWtiTzhnSVBwSkVYSnpyZE1oWVNrTjQzc0ZiS25SdkhlQy1nd3RVRkRmUVZZaUxFaFN0NVRJZkNuVHU2eklod3VaQWtKMWoydEJucXc?oc=5) (Thu, 16 Jul 2026 18:27:29 GMT)
- [Visa Unveils Stablecoin Platform With OUSD at Its Core - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxPckJWczhSTDJCYlE4UEtfbWhUWTdEbVBuQW4zVm1rQW8xU2EyaE5xcDBBTG1haWxWWGlhSFU5cVQ5YWwtU0pkU0tmakNsMVZZbWZ2ZFJtb1czUTRSMHZmU3k1a1hJUGIyR0pvbklXSTBnQlVXbVk2Rk5Dd1lMYmZrYTdrVkp4VHJ2MGhuUUhHRnB4eEt0QXJrVVc2UnVMbHZXVjRwNg?oc=5) (Thu, 16 Jul 2026 18:26:06 GMT)
- [Visa Unveils Stablecoin Platform for Banks and Fintech Companies - Yahoo Finance](https://news.google.com/rss/articles/CBMipgFBVV95cUxQSDNwQ1QwYjFoamlvUWdQN1MzMUw2NFN5aTk1X2hJdFJGd21xWXNoOXJUVnRoRjFDNVRxYXR4Vl8yVUhSaXNSSkdueUtnLVFnTDdHeG5PZ0hJOFFnc2JBVGptVkU0SU92Z3RVX2NYYWhCZkZWT0I3WEt1VUs2dTlpcHdHRENLUkRyU0kxWVVvSFB5UjFLbUdVXzRJTFpENnRHcTBpeE53?oc=5) (Thu, 16 Jul 2026 17:57:57 GMT)

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
