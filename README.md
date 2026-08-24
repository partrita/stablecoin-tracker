# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-24 00:46:23 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,008,910,685** | 🟢 +0.01% | 🟢 +0.81% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Eskimo Expands Stablecoin Payments for Global eSIM Plans - The Fast Mode](https://news.google.com/rss/articles/CBMisAFBVV95cUxNbzhldjcyYWY0dHNtNkhhcnRBazVsUUpvVEsxVUJUSHVEWGRoZjBYckxFUndXNlhJMnl0bm92QXRQQkQ1NlhJSThUaXVZOGFBcDhWMmRnNkZKcWZnUkY2dUlhUE5fYmRqZlNibkRkY1N2NWF2ZFdYYUM0X2h5VkRNMVhIdmtrZnhxRGpyWnJVNFF5a1M3by1oZDRhN3Nad0hHUnNXLUF3c0ZsREtHNW9yQg?oc=5) (Sun, 23 Aug 2026 23:17:33 GMT)
- [X Explores Stablecoin Payments for Creators as It Scraps Revenue Sharing - Memeburn](https://news.google.com/rss/articles/CBMimgFBVV95cUxPc0FJSW44VlJRN1NmQVF1UWFOcnNRSE5HVVc2WHBrazl5VXdGN0xicjNZZVl5OGM1dmYyUmRuSmQ5X0Yxd0xVRmxuMDRZMkczdnZYTkhRYTBITGhGSWtMQ09lWm5CSTVCRU9EeUFNdDRkbmJGOWNFbXVtR2tjVVFwc0hqeG9ubE10d0hVNEZKMFV0OFhWT3dWZUF3?oc=5) (Sun, 23 Aug 2026 22:25:29 GMT)
- [Crypto card spending tops $1 billion as stablecoins move into everyday purchases - CoinDesk](https://news.google.com/rss/articles/CBMixgFBVV95cUxNUW5obHE0ck5sMXpuX3M4YUcyWW8wTWZhVUhZWElNWloxTU9ySDJZbmVkYzV3bGJtSVpfQTZGSTNlMHUtS0VVOUpFOGxMY2xDdUt2R0tuMFlwblotZEd0U0NjSHIxVW9ST1hhUU0zQVltUVY4NVZyS0k1eU9VRkdycThKYW41czE1RmI2OTRMSjBnN05nU2l2N2cxTUtnMkRnMHFKRm1JSFJfbk1DY1VlYnkybDZRcUl0ZWJYNEdWRnd2MHlqYWc?oc=5) (Sun, 23 Aug 2026 15:00:00 GMT)
- [Miracle Pay Partners with zerohash to Enable Stablecoin Payments for U.S. Merchants - بوابة التكنولوجيا المالية](https://news.google.com/rss/articles/CBMiREFVX3lxTFBQTHhEMUtqVGczZnRjZHBjemtDY3hpMXVwUnVWNkpKOXRoM0pVN1c1bXMtZ3VuVDd5NzBFSjJiTjJRWlVZ?oc=5) (Sun, 23 Aug 2026 11:24:22 GMT)
- [As foreign investors dump $29 billion in Treasury bills, Washington pivots to stablecoin issuers to back US debt - CryptoSlate](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPX1ZUaWtYMGt2X2l5Q1BzdmYyaDQtbHc2dUR0cG9MS2dmb0JzU25KNGl6cTFFWW9NYlFiMVZJeHNxSkNnTW95VzRzTU9mSTB0WnZkT3B5ZGY0bzhVZEtESDlFWVRESXFkTktHRTJsUDFkQ3lGck1STGY2M1JpakQ3TU1zQ3d4OHJ2enpvV2FiWGxkRGZWdUJuX24xWHN3N1dnOFkxZXNBLXczbjZHU1k0bWtvUXBvLVdwLTA5MjNtQl9XNDVPWGo2Tm13ZHJYZUVs?oc=5) (Sun, 23 Aug 2026 11:10:14 GMT)

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
