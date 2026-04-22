# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-22 06:38:58 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$299,709,811,006** | 🔴 -0.15% | 🔴 -66.62% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Nium partners with Coinbase for stablecoin payments and settlement - Fund Selector Asia](https://news.google.com/rss/articles/CBMinAFBVV95cUxQYVdfcG1GT0NFTlZCdUhxWS02NWpVZ3BoMm43Z0JJZnJ0b05Db0ZsbjhZWjhDZ0dLY095OFRzWW85VlVrSzdpQUl1UzREUlhDU2hEYjJoYmVzbkxvQWRGYlZabHg0ZTZ4dmxaaG1EZWh5QnBWajVYd25FWTNZVGwyTE9xMlFTYXpDZEpYQlF6aDRNOXVvdk83di1na0Q?oc=5) (Wed, 22 Apr 2026 00:20:00 GMT)
- [How a community bank is handling uncertainty and a new crypto age - marketplace.org](https://news.google.com/rss/articles/CBMirwFBVV95cUxNMUpfNmhNSEZWT3JJMEZTUk1jMk5fS2FBT0VVUzdldmVEWWxqeWRqU2RvczdkUzZtLUpBZUVJb3dlU0RiSGkxdWdUSWFEVkgyd2NMSDNGQXUyMWJ6X25WMElyUG5BdURoZHU4dmZzaXRldEZKNXBvdy1fMnFlS1FtMlBLMzV0U09keVB0WEVkaUFneHlBemNDaHU4c0NTNXRNSElvWTZnTDhlbzBRN3VJ?oc=5) (Tue, 21 Apr 2026 22:30:00 GMT)
- [Non-USD Stablecoins: A Guide for Enterprise Payment Teams - Polygon Labs](https://news.google.com/rss/articles/CBMiwwFBVV95cUxOMXg3YW9IUE5OclJjUDdmTGpBM211bTN5RTJPa2NGN0NCS3cyMnlGVUVGNUhHRzVpZUxCTjIzV1FEQTNmMXpWY2V1RndPQWZpT1ZyLWVESVVKX3psT0poeXRIcE45NW1LdDc0eGk3dFN0dmhySlg1ZjV6eDVuU0xQNUl5ZEpHa2V4X2JDbkY4bmhSTkxsblY3djdQWHpWalJYSjFPTlFsbGs3d0RodVZNWDNPZHdtWWRaNklySVJuM2Fzdlk?oc=5) (Tue, 21 Apr 2026 22:27:27 GMT)
- [Trump family crypto venture lobbied for Stablecoin bill, hosted Idaho legislators at Mar-a-Lago - East Idaho News](https://news.google.com/rss/articles/CBMizgFBVV95cUxPeVhFdjJBdXQxRlVySXdNSHVnb2xYTHI5ZTNxNS1BSHI0SEZmdkJIU0RPamFBZ0JJZVJnajczZmhfaUFiX3dvOF9sWDRLY1RMeV9iWFNubTdjbng0VWg2YW5ueGZhZ1E0WGFMVkROYm1RaE44QjdLc1ppS1VMSmdiNTlDeG9ORFlTUHpjbmR1a3ZoR1BxaUJRZW9pNjlHdElkcTNwS1dRaXdsOUdmY2hNb2QtU3h3bDBSQU5OZFl5MkMwTHFVT3p0ZGhKNmxYQQ?oc=5) (Tue, 21 Apr 2026 21:30:00 GMT)
- [Nium partners with Coinbase to enable USDC stablecoin payments across its platform - FX News Group](https://news.google.com/rss/articles/CBMizgFBVV95cUxNYWNhcDRubnNJRWtEay0tZG5zYXhabl9LWTlTemlXN2NBa01XcHgzVXB1aVNvZUNGMUEtUUctNDNoNzdDdV9VVUxFR1hrZExuTEstbnJQdnJybXRhSkdzbmNBX19yUjQwMDgwLW04QjQtbXdiZThPWE92alNQVUgwV2IxdjItZ0xOQjZpZldrVXpReDFtVXRXc0x4QUF5WUlnQ0VlVTB3VVlEYnN5WlptMWYtUlN2MTdPazlIS1pkTVRaQjdzUExHY3VFMWh2Zw?oc=5) (Tue, 21 Apr 2026 19:11:54 GMT)

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
