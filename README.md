# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-27 02:06:18 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$287,938,516,563** | 🔴 -0.12% | 🔴 -0.51% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Circle CEO Jeremy Allaire Says the Stablecoin Market Is Going to See Record Growth. What Does That Mean for CRCL Stock? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQTVdDWFVqV1dMM1hZZGtXUFo2WEMxUHJMUXVvT2x2SFpNYVVLcU50TWEyVV9ka0JtazlCdXlDNVVPY0JWTWNDTVZhUldDc0tkM29PbHp1TWlMdWRBZEhtd1ZHd2hnMmpTXzZsQTlIel9ZUTRWWjVOYlZ0bmhKcDkzdTFzYmZnU0tZS2YwMVRNY3pMQ1d5blBzaA?oc=5) (Sun, 26 Jul 2026 15:27:00 GMT)
- [Circle CEO Jeremy Allaire Says the Stablecoin Market Is Going to See Record Growth. What Does That Mean for CRCL Stock? - The Globe and Mail](https://news.google.com/rss/articles/CBMirAJBVV95cUxPZVFCZzBuQ3JWcmlwS29paWRhMUhmcTZybU5XckJHWDNtVTFuSnhiU1V2di1MRXItc0ZFYlZCOWxFOU9XaVpEVGpqTXZsWUJKZnRNTzRqUUlfQmxnZWFZTFNJLVFjVHJ2ZnpmYlpwN29ETjBMcS1oMG01NWxicC1wUTEtZXdMNGwtNjJwM2xiUEp4eFlTTkZqNUNTUGlVcFI0VDlDSFU2VEh2SVRJZWtSOXozWk1RVlZ2U1R0NzNDYlRwU2FValR1SkF3RTN2eHFtc0lWRnRDOVlkRjdNMlpVc1ppaTN3Sm5DdFhoYUphWXBMS0lvRF9TQkR3QWM4aVNocEozd1g1NlVqaE5YaDViQ0NRdzhIRXlhaW5icUhVNUtwMlVZRkpLUmdORXY?oc=5) (Sun, 26 Jul 2026 14:48:02 GMT)
- [Circle CEO Jeremy Allaire Says the Stablecoin Market Is Going to See Record Growth. What Does That Mean for CRCL Stock? - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxQUDAzR05jelQ2Q2czVXhsNzU4NHhYeHNNV2pqb0FoTVJKRVNlT2VuY0Z3SHhaaUNoTldsbWRrTjFOb0ttUGFud012Y0FoMl9NMklHYTA3c2JzYS1ITm9xSERQUEt2OGxFZk5fSENnX1NOc0dSbUtLTUpoSFgxZTBINHJyWVFNUXdWdmo2eWhTRDBQU0pfdHVXTjN5OA?oc=5) (Sun, 26 Jul 2026 14:47:30 GMT)
- [Samsung confirms stablecoin support is coming to Samsung Wallet - SamMobile](https://news.google.com/rss/articles/CBMimwFBVV95cUxNWUpwOHNQdUZXTW5IaWpmME1oc1Vpc1dTdmIzUVFMcFVqZ2U0aVRlU0JZTi0yV2xnZHRya3hha1RCMU1QZ1Y1OXIzbDVhVGFKZERNbk83b1ZzSUR5azdNdmdyMDBzcFk1SUhZdWdnTjJ3YVNyS0ctdzdfRV9YUnhKU3U4QUhVN1FDVTMyV1N5RENTYkMxc0tVYVlMbw?oc=5) (Sun, 26 Jul 2026 09:14:00 GMT)
- [Bitcoin price hovers at $64,000 as stablecoin inflows weaken - Investing.com](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPUmZsZkI1eUp0UjFJZnpsSHdNalhhemQyMi1XRkE5UkhWOW1DU1JVVTJHV1NfUHRlS3BxUG9Gb0NpTl9TS3JJRW9DZjRINGpoN0cxZFdzdllQUU5aRWp2ZW5rd0lDam1sSXZBeGN1WDlESU1wRmJGZ3JUeVptVHB6RWtzSGZSdndrTVRtd3Z2OEtlcHRfNF91Wlcza2xrdUF3WXA0THE4UDRoNkR5N3ZwWVR3VUdJeWxwOWt6YW1CR1hoZVU?oc=5) (Sat, 25 Jul 2026 21:14:03 GMT)

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
