# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-11 01:04:08 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$287,007,447,711** | 🔴 -0.03% | 🟢 +0.13% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Brazil finalizes 24 hour delay for crypto, stablecoin transfers to combat fraud - ledgerinsights.com](https://news.google.com/rss/articles/CBMirwFBVV95cUxNbWE3aFRpTFNKeWQ3UENIQzR2czY0czg1Y2dQLXhpTldaUkRKRFlPT284X1BfTEprV3dsS0F3YTliNmJzbEtTNFgxUmh2OFhWRWNXME5WWmVxV1ZXa25qYVpJUzZDR3lxRXRsY3hyVTN6WW5TV3JYTWVKME5JREdzMjYxTDBVSTJnemJuOFQ5Wmw1dmNfSG9WTUlSN1RsRGVlUzB3RXR6aTVxOFRPUXZZ?oc=5) (Mon, 10 Aug 2026 23:03:56 GMT)
- [Wells Fargo Brings the Stablecoin Fight Inside the Bank - PYMNTS.com](https://news.google.com/rss/articles/CBMimwFBVV95cUxQcWtLUnp2djUycld0Zm9aU1VpdHEwTnRIOU51U3BuSEZhRXdYcUxST0RPTWtsMXM5eVBXTlRGLU5iZlQ4alNmenBzaXpjZmh1TFlrbzhlc1gtaHZCUTRjZ2FEZXdZejhpbll3eDJfR2JGbVB4eFlTVHdXLUNLeXNubW5Jbnh1WnBLeEd4dnBwNU5DbENRN3p3bGJPaw?oc=5) (Mon, 10 Aug 2026 23:02:55 GMT)
- [Bitwise Sees Stablecoin Market Growing to $3 Trillion-$5 Trillion, Says Circle Potential Is Undervalued - bloomingbit](https://news.google.com/rss/articles/CBMiVEFVX3lxTE1UMjhaeXRxN1czeUdOS1dkMXFVNThENmpfeksyd3FoMmk4WHM3ajFNbFFCVEthUjR2a2VBbmRvSWdoNG5EelhYLVAtbzdjaXFRV3hTXw?oc=5) (Mon, 10 Aug 2026 20:56:12 GMT)
- [Solana&#x27;s stablecoin supply has grown 11x in three years - thestreet.com](https://news.google.com/rss/articles/CBMimwFBVV95cUxNdEdvQkpPSTBka2xLNlQyc2p6RlhQdHBCSmt3Mmt6cnd5WFNMSHJEazcxTHBwWjEwVTMxNDgyazJIY3pxSUpaYnduS0pxbkRLMVNLeVR1TkhSMzRWRnRsNEFuMVlUWXRhaE1DVjJIQnVJVkxCSmxMRzRNa0htZDI0ekFsNmxkSzBpOWJpQjUtT1ZQSE1LNk5KZjV2TQ?oc=5) (Mon, 10 Aug 2026 20:54:00 GMT)
- [Bitwise&#x27;s Rasmussen: Circle is mispriced as stablecoins head toward trillions - CoinDesk](https://news.google.com/rss/articles/CBMixAFBVV95cUxQQjVSNklDanZYWjV5ckpqbUVKanNPeEJ5cklNYThJcnA1cy1NTFFORzZjLU5YTWQtVm5rdG9QZzJVUzIzdVo1VDdDcWtITGM2R0pjN1l6WnJKblBHaWlxSWdxYWFFczYzYm81RjBHX3g3T2syQlFqeFFuZzlGSWhKWGZxZk4wbmdteUUwd2Z5SnM2b1d6WV9jM3dXaGlqNlI1Rm1NSXdFWm5EODJKN0lvXzhia2V0V3VNc0tIYWFwY3R1d0xM?oc=5) (Mon, 10 Aug 2026 20:21:41 GMT)

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
