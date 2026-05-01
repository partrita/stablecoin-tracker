# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-01 02:12:40 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$299,673,034,541** | 🟢 +0.16% | 🔴 -50.13% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [FinCEN and OFAC Propose Rule for Payment Stablecoin Issuers to Implement GENIUS Act - orrick.com](https://news.google.com/rss/articles/CBMixAFBVV95cUxPRzI5elhFV2s4eExzUmYzZXQ0dzlGWjkzN0lMdnltLTMyTzR3eWE0Z1ZINzRDeUx5eThFR1dRZXVRdmNETG4wWkwzUVNqZk5lUk5WTjZLM2dyVFhheW1SbmpRZWlWSUkxTkJUMXg4bVQ2aGlxeHBuejJqUVl5WjEwd1lvX24zNHA4OWFzUUlGTDFDLXU0N1RxSE9nVmJSR05lczBYRURQd3VZYVp1S3JmRDA2TmtRZnNBelJfVzdzMDJLbkN5?oc=5) (Fri, 01 May 2026 00:40:18 GMT)
- [Anchorage Digital Partners with M0 on US Stablecoin Issuance Stack - thedefiant.io](https://news.google.com/rss/articles/CBMiswFBVV95cUxOR2Myakl3T2tHWlJ6Rkc3ZUwyckY0SjNBWnYwNUVoTGN1UEY2bXVyUHZfOVQ0TTJPYlM4cklnQnJrZkRQWUNyY0M5S0lJMVJiVTBaLVRUdTRTamNDX0E4anA5ZzZJMnR1UkcxamhkV3R2Q09yOTVqTk9RdUhCem9YTG5uQjE1NXNvcS1Ib0xfZkFXYWt6LVJUa2t4NXMtZnNiVmxRaGx1TXBKaFFKazIxSGROSQ?oc=5) (Thu, 30 Apr 2026 18:57:45 GMT)
- [Meta Brings Stablecoin Payouts to a Massive Global Ecosystem - PaymentsJournal](https://news.google.com/rss/articles/CBMimAFBVV95cUxQcGZyemRCQ01rV0lzeEN2RTNoc0ptWkNWZmEyMlh6VXMwWXpMdTE0WWdLcWQwODUzcmZVZF9RM2p3SHl6SXVkdTdxcXBfT2k2ZVF0MGV4ek8zYWE1ZTRnN2NZT1Bvc1JYWXRPeTNyeDNWN0xUbUFwSDFlM3YyZkNmM0NJNFlLcHhwZnBsanROREZpWWlSZ1VPN9IBngFBVV95cUxNRmV3c0RscVo3dktRWWNwZ2RhdjZMT2pFcWpsZVpFbC1XeEZ0OXFCQndwcnFJVE1hbDhqUWhLb1VMMmtqMnQyNXZfNW1iV3VtNkxxNVVlVGYtVGZiaXdyZzZBZXRHakNWZUdIQTJqbm9aZGtRaXNxdEFWUjdZVXZlNUo4ZGlDVFVPUS1yazBPME15RXh2MFd3S2RkdkZ6QQ?oc=5) (Thu, 30 Apr 2026 18:30:00 GMT)
- [Coinbase&#x27;s &#x27;CUSHY&#x27; stablecoin fund to launch tokenized share class via Superstate in Q2 - The Block](https://news.google.com/rss/articles/CBMirgFBVV95cUxPOXFMaUEtZGZETDU3MHU2UzRfVUNMSnIxWVdUTFdfRDlzQkxmd09KSHVaUUZnRy1hbkdmMGNKNERMYUx0WnloUVQ0T0RwSldrZzZiMGY1ZUFNd01WTnhiQlhCd3VWVm5aeU1LMmtEQU1IMG1sWnRhU1BNU2RUV0ZMdHJsREFOQThxQnBFakNGWnMzMG9fYkZsTURNOWFweDFVTzVtVnIwWXl4MXlZc1E?oc=5) (Thu, 30 Apr 2026 17:37:58 GMT)
- [Tether pivots from stablecoin issuer to full-stack bitcoin player - Yahoo Finance](https://news.google.com/rss/articles/CBMisgFBVV95cUxPS1ZyZUsyNlE4U1FTanlNZVduQnRscGRmY3JLNnpTYUdoZWctMjRuNTZ1d1BwZWE3Um9LbDY1MHR4QXpCLTF0WkplMmZuOVN3STNkQl9LNmdwM0hJcWc3MUlxbUZibVRxVkp4TVRRWE16MGV5SVlFUVl6anlsOFF0a09rVHA5MXdmbkhfcEZLcXYyektMMmhWc2NtcHNPRXQxYkZxU0gzNUg0LUpURWNZQVpn?oc=5) (Thu, 30 Apr 2026 16:28:20 GMT)

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
