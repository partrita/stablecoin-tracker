# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-07 01:15:51 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,099,906,702** | 🟢 +0.85% | 🟢 +0.96% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [MegaETH Foundation to use USDM stablecoin revenue to fund MEGA token buybacks - Yahoo Finance](https://news.google.com/rss/articles/CBMikgFBVV95cUxPMjJCbFc2RUhmQ0pBaUtqYzNkRmEzaTZVaXloX2M3dGhTUEJHeUV1a2FqcVZTOXZfZVFQRnZ3TENIaEVDZ3RwX2g4WUItY1FrQVlxUDJtd3QwLURCdUxWTkNqa2o0T21KVHN1OEdnWTVHQXk3cTRRTE5LTjdlNXZOM0V1dmhVWGo1VUR4d0pCS0t0dw?oc=5) (Fri, 06 Feb 2026 19:34:13 GMT)
- [TRON DAO Advances Stablecoin Dialogue at Digital Assets at Duke Conference - Bitcoin.com News](https://news.google.com/rss/articles/CBMiogFBVV95cUxOYWhUNktOdFRpbnBKbjBVTnEwVDlNVFhxdzJhbVk3M3A1WHBZNHBTREktVWxrbWlGUTQ3YmxYek1vVWxoSVEwV0ZYblFlRGM0QkZzMVl6R3JMVW15Wlk0SlowN1ljRFhUaEY0M3NYLUNKNEZVSk9QcmtIb0tOVmhfUjUxZkdIdWlKOXBYdVRsX2Q2QXVjalZyR2t0SXJMN3pyMWc?oc=5) (Fri, 06 Feb 2026 18:12:03 GMT)
- [BBVA Joins EU Banks to Launch Euro Stablecoin in 2026 - Mexico Business News](https://news.google.com/rss/articles/CBMikgFBVV95cUxQS25FNzVxNnk0a1NkUHJ2SUMycHIybDZPZy11bEIxNk9OanpPdENpZmdOY3B6V3JWa190NUFfSHpLTE9OLXI3aUsxWmRHcXpaRGs4MEs0bmo2cUNfSGZjbVRSVmIzbUNFQm9yR2dHZkM2MHd3cU9kVzdfdkFINVI1V1pHY2VOSUtTNGxnUWxNRHZhZw?oc=5) (Fri, 06 Feb 2026 17:52:09 GMT)
- [China Formalizes Ban on Yuan Stablecoins, RWA Tokenization - Yahoo Finance](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPZ2twWV9rYWhrWlJJVkxTVExVTW04bWp3Nm9NT3hUNnBpMF9tN05mRVJUSFBxeXVvYzhMUTBVeV95UGV6ZjRDbzl5UmtaWFRLOGpGSVRGQldWM1c2ZkhjNmt5NzRNZk54WXlydlNtLUtCdmFUNl9aWkNILW85bTFnNEpDaVlPdGJtbVNB?oc=5) (Fri, 06 Feb 2026 16:36:13 GMT)
- [China expands crypto crackdown to stablecoins, asset tokenization - CoinDesk](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPV2xsSDdNU05qMlY3eVI2X3IwWlJHbHA4MC1BR2hmWFFKU1BISFRlS3Q2RFdOLVgtdTdfYVY4cUtlOHZXalRtcF9oQVFLb2FaV3otVU9yZDlZbU1wdENGRThteERYLTFoaFRDTk01VUh3Ty03RzF1NjRuLTRWNnZjRXJVX25TZmoxVUlrVHRYcXlkbklIQTVTV29hVWxuWWJ1RFNSMzZiLVo2Zlk?oc=5) (Fri, 06 Feb 2026 16:13:49 GMT)

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
