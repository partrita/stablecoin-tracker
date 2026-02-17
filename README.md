# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-17 01:21:44 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,768,510,041** | 🟢 +0.04% | 🟢 +0.01% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- ['We do not do illegal things': Inside a U.S.-sanctioned stablecoin issuer's race to build a crypto giant - CoinDesk](https://news.google.com/rss/articles/CBMi3AFBVV95cUxOUVR1a3pDN0M2bmVIMDBIX0Q3NU5UaUVaaDk1SHhIZHF0MWw4eWZaclZBNF9ncjYzbXZpYmdYOUZLWFA0ZU1oSmYwb01aZmVmYVU0aHVqX2NjRGlLVnFTc1QxbXA3T09TWjVBQzF0TnEtblhLcHZYdmZ6SmhTYlNFYnpHRnZpRng2czVyYjltVnVuYzdmbTZsWEVVYXc5VEZtbnBJVi1vR1ViX05IT1NmLVFBNmJVS2p3S3FPN0plUWE1RkJQdkZKSm5GYXltUllhTjNjRmxjZjZ1M0tJ?oc=5) (Mon, 16 Feb 2026 21:56:40 GMT)
- [OKX Ventures to invest in STBL to launch RWA-backed stablecoin on X Layer - thestreet.com](https://news.google.com/rss/articles/CBMitAFBVV95cUxNMWE0NjhNaWlPYUlGVXRISFFtMFh6NU5LV1Y4VXl5V3d5UFJyb2txNUVFb0l6Nnp4bVZKbWhoeEI1SmluRl9hNEg0a1pQc19rQzdXRFFMeGdXS0xTWnBLR20xM3o0WTNyY0FsVlMxYWo1S2hURUlENkdZYmFoSVllOUozbDU3VDZmRE9TRktQYWJjWXpzM0cxeU9fQ01FdHpoS3BrX0lCS0RKaDdORlM2WVZJNWw?oc=5) (Mon, 16 Feb 2026 21:02:07 GMT)
- [NCUA proposes new stablecoin issuer application guidelines under GENIUS Act - JD Supra](https://news.google.com/rss/articles/CBMihAFBVV95cUxOT0ZsZGtVYmN2NVVIOUFrNm13Z1owdXh4T3JoS3o4Y2FxZ0NlSWZjdFA4TUZ4X3RfdkNocWNnV3NnS0huR1NrcTJ4akNaeFc4Q3F6cU53UlNvVW1Cby0zbzZtMmdXMmJOUWdiQXpUTmhVOVpPLTdkV2hNOUNmbGxCMi11bUM?oc=5) (Mon, 16 Feb 2026 19:12:49 GMT)
- [ECB’s Nagel Touts Euro-Denominated Stablecoins for Payments - Bloomberg](https://news.google.com/rss/articles/CBMirwFBVV95cUxPYVB4ZVNQUXgtTmZDdTVoTWo2WFlHMUFYY3MtN09MZzVELW5UeHQ0WER3MFhDVlpNamIwckhwRzVBZUI3VTdMNkNOMzlkNmhZNGd6Nlc4dnMzS2N5Q1F4SzhTcnVXdWdvWktNcnN6LTljRnhFNFdzcHhkYU04WldmRGJhNVZydEpVQU1fNU5uLUdUem02TktHQnVldnI0TmJocjhIZXdfTl9aaFcxRVNv?oc=5) (Mon, 16 Feb 2026 17:45:00 GMT)
- [Banks sharpen stance on stablecoin rules during White House clash as key crypto bill remains on ice - AOL.com](https://news.google.com/rss/articles/CBMihwFBVV95cUxOVVNaNk9NSXJVTG1pLThSVzI0NlpUelAzU1lZT2dNR1VlbzhVNFdFM19icUtNMkx6bWR1eWRhVE9jdzRNQzdsWWpQQmxMbnJxaEdwTmdUdHlCQzNfV3NqdkxRaXVYSmIycC13ZHhLOUowRWUwbVYxVC1ScFdXN2pwa0xCejlySzQ?oc=5) (Mon, 16 Feb 2026 17:15:12 GMT)

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
