# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-19 05:13:36 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$273,519,824,105** | 🔴 -0.31% | 🔴 -1.05% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoins, Tokenised Deposits and the Future of Money and Payments - International Banker](https://news.google.com/rss/articles/CBMirAFBVV95cUxNWHFSTE9wQnpGNGlqVVJ5WFRMX25qQzladkhMTWlmaGxhdU1tRkdrMVd6c203R01OSVRBaVZKNldyQkpUMFFhTVRkOFZJRmF4YjhGNm9qTlhBbkJycVRPNWdHZVlHaDRScnBXd2NYRlBSamRvOC13bjhmTzZkUTQ5TkZaRlM2RTdtTjl4Yy1yVUZnTWNDTUpmalNQMm9MbXVIeFlpc3BadmMxbnNM?oc=5) (Thu, 19 Nov 2026 05:05:02 GMT)
- [FOMO Pay taps Anchorage Digital for US stablecoin infrastructure - TNGlobal](https://news.google.com/rss/articles/CBMikgFBVV95cUxPLTU5YTVUeHFxTVpYTTFkMkE4cE5JQmFrZmNQRU9HSjZrcUUwd25QOFRrQ2xGd2pqQ3U3ek5LZEFyRkpINGVTbHRxb0U5NUQyZW9YS1BTOUZNZDYzaEtHZ0pHZGtrS1prRWJuYUJiYUlmTlBFcDdacjd2bzJQaFlFMC1rY0hqTzRNeTczbm90dDE0QQ?oc=5) (Thu, 19 Nov 2026 02:39:24 GMT)
- [Gonka Bridge Exploit Drains Stablecoins, Mints WGNK - The Defiant](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOaklGWEV1TGhMbFR3ZFB0aEZ5bElweHZHWHA5aE5vZTRueG1vQmhlWWFZQk1vUm5wUnVkQVZaeXlnclhfd3hkNTctU3p2VmdWNUgtV0RoRjlrcEZBMGE3NlZHWnVBVTNfczd1QTZJOGtmbTlQSk9RX0s2X3dZYjN6Nzl3TnQxZVhXOUlN?oc=5) (Wed, 18 Nov 2026 23:29:09 GMT)
- [Senators Press Treasury to Ensure ‘Equal Footing’ for Stablecoin Issuers in GENIUS Act - TradingView](https://news.google.com/rss/articles/CBMi4AFBVV95cUxNYjlsdVJPV1FIQS1SV0piclR1enpvdU44aTNCa2ZrMGJDWmNoWXVJVFY3ak8xYmtZSXM3aFNISDg4aVg5cXI0WDViQ2ZFallfNm1acHNwMGVjUWp5RTZXSEg4TWpleUpfRG5xT3JKcHM0cEV0UmVadm1xODZzMFVWRmNKTzdoTzlsWkdBMU9SZmZoXzNIMFFCZzNVMWRGdFJfcnFhM3o3Qlk2OXA5OWxEb2N6Zi1jZEl0N09hQ2lzY05yUjY5eXBJaTJoTVlpZ0tjRWE0MUg4VXNjbG9HVVdVcg?oc=5) (Wed, 18 Nov 2026 23:04:25 GMT)
- [Senators: Treasury must ensure &#x27;equal footing&#x27; for stablecoin issuers in GENIUS Act implementation - Cryptonews.net](https://news.google.com/rss/articles/CBMiVkFVX3lxTE9JVzZZRnY2ajNSMm9oMU9Tb2syNlprRlFBSFFnMGJBaWctVVYzMmJxUm5QZGlwTE1GQ01pcmVQTGlXVklSUGRMSkR3SnlsbUluTlJoQndn?oc=5) (Wed, 18 Nov 2026 22:21:42 GMT)

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
