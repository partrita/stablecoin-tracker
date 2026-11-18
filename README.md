# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-18 05:18:42 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$274,365,713,324** | 🔴 -0.12% | 🔴 -0.92% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [New Stablecoin Regulations from Thai SEC Aim - Cryptonews.net](https://news.google.com/rss/articles/CBMiVkFVX3lxTE4xemtVSHIzcTg1bWVBMTRvTnM1Mko1VnBXdEp3N3o1NnlXTnFPTXNsT05hY1ZZZEdLZEV3TUM1SndrNlU5eUxRVElGMVJ4NlpPRzgzZnp3?oc=5) (Wed, 18 Nov 2026 04:47:34 GMT)
- [Visa Direct Advances Stablecoin-Powered Money Movement in Asia Pacific - PR Newswire](https://news.google.com/rss/articles/CBMiywFBVV95cUxQN05UMUJNcUVRSUZfTlVrZ3k4RWRla2ZucUYyWFp3NUtTd3REeW9qZFA5VWxGcW5fcWtpb1RlYUJleHBHZEFvbDQ2cWkta1Y0XzBHQmJGaGkwZVIzMk1Hc2F4ZDR4X2pfb29hUWI0MXlyQUlTUXhualdkSGNheENkcmJtaExCdEh3NndxdUNVOHlMWUlMQlhxUl96aVlzXzY3T0oxbEJYd0RGcXV6d0NuZmtPSjA3cjBkOW5mZ1JkaHFvMVZrS04wbWhhTQ?oc=5) (Wed, 18 Nov 2026 04:37:32 GMT)
- [Visa (V) Plans Stablecoin-Powered Cross-Border Payouts in Asia Pacific - TradingView](https://news.google.com/rss/articles/CBMiygFBVV95cUxNRk5BWVlJX0Z0cVpLelo1UHNCTGFGbEZVNHlCNDZwbmFkbER4N0pYbWpva1M4aVJ6dGM2UXd2QXRmOUFiYkhjbEE3QmJ4VUIxZUZINVNRSzhRS2pvUEFMZ1FGWnkwTEMteGdDUEhVVEltU29lQlpaN212Z3dkRm9tM2ttRFA4eG96bVB1ZmF1YTUwczdmWVVPMGZxRkJpVTZucFJUZWpJb0hSVXJwZG1SSDdzZ3JuNTV1NDRzcTh3OWpOQWFFRngxc0dR?oc=5) (Wed, 18 Nov 2026 04:30:00 GMT)
- [World Bank Group taps Circle and Citi to test stablecoin-based fund disbursements - The Block](https://news.google.com/rss/articles/CBMipgFBVV95cUxNZmd6RmdaUFVzbXpzNXZyQVV1UWdaUU52UTY0QXZaS0UxbFBubUVIY2llMnFjckowMU52c2FYWmpyY3oxVDBnVEh6LWpmZVMxNUlIZ0dZOENNc1dBTFNKQkt2WTI5amJxLTUxRGtPM25xTGFHVkx0TXVBaHhKX08zazdHeGJmQ0tkNHQ5OGVpMHlaY0J3eDdnZHdFMkNrRXU0dng5aUxR?oc=5) (Wed, 18 Nov 2026 04:21:00 GMT)
- [Cardano Ecosystem Stablecoin DJED and Reserve Token SHEN to End Service on January 1, 2027 - TradingView](https://news.google.com/rss/articles/CBMi5wFBVV95cUxQdEI4RjhaMTVGMGNFYUlzeXZraU5PUEJsME1aYWRhNlJFVTR0MTdWdllhWFpUVFM3eGVMV2drbDJ4dVluSmM5WWhqdXRZTWR1RVgtZTdUalVTZzlNd0RhTU1xenlCa2FmOU04TWJBWl9PazhqalRCVHVGVTRVbndHc1AwbTNobG1vY3NmOFFzQ2NOOTFNRDJHR0l4WHgwaVdfTGxGYWU5ODhHUDl3dlNXeVlJcmpYZ3R1X18xMGtHMHBrSWpncXVHODNyV3JzU0Q1aHlsajhQdXcwSHd0QWFxYXdrbVJfclE?oc=5) (Wed, 18 Nov 2026 02:31:00 GMT)

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
