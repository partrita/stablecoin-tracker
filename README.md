# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-11 02:14:27 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,811,179,871** | 🔴 -0.07% | 🟢 +0.10% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [U.S. Bank Moves Real Money With USBDC Stablecoin in Live Stellar Cross-Border Pilot - Bitcoin Foundation](https://news.google.com/rss/articles/CBMixwFBVV95cUxQMXJpc3lwSFA3cjJXbmhjQV9FZzJpSDNqQ2xieHl1MXcwaXRGQ2g2ZW8tbUVvQWd4bWlrajg4Z29ILV9DZEtQRUdBNGVTOHlzUm1uOUhtX1d5Z0RLdjlWVWRrTTkxVWJLblF6R2hwdWw4d1VRRXhDSFpwbkx6ZHVWbEpFemlZdlhQMmZiM3NPaWJhX09MUjk3UGZWQ2RHRGdiX2VnRkZUYlE1cnNpcW1IcmxtaGc5N0cwYU45VkxZTWtjU1hZNy00?oc=5) (Thu, 10 Sep 2026 22:00:00 GMT)
- [This Week in Stablecoins: Everything but the Coin - PYMNTS.com](https://news.google.com/rss/articles/CBMilwFBVV95cUxQTzdzaHIwNGtaNXhBcU1yWUJhUkRHejhaM2tXZnVFQlA0eUF6bWVPVjJqSV9fb1VONEhRaXdSNzQ0Mm5oUUswcHM5TTg3OXd5b0NDaGN2OGNrZUF0QkJRTjl4QjZ1Q1BscFVCcEVEVkVSa0pja1lCN2FiRC1lTUlqRzFPa2lhcmZLaEw3aC1ObE1ROHRBWWNV?oc=5) (Thu, 10 Sep 2026 21:28:09 GMT)
- [U.S. Bank partners with Stellar to test stablecoin - American Banker](https://news.google.com/rss/articles/CBMimgFBVV95cUxQU3Y2cTVSZU84V0didG9PTDNzZ2lqXzdRdWJadklNRGQzeUxUdjhBV1BWaEpISnhES0ZmT21KV2FRYnJpcGhhY3hOcFpDOGJxTWx2VS02TzVBQ2MzUEtMcGp1OUFXOF9TVUVnZTc5SThLdDk3eTQxdnE2M0VUYlJhOEtmMjB1dUowRTNNMTNCQWFxVkljN01RUXNn?oc=5) (Thu, 10 Sep 2026 20:35:00 GMT)
- [MoneyGram Launches Stellar-Powered USDC Visa Stablecoin Card in Colombia: how 13 outlets framed it - NewsCord](https://news.google.com/rss/articles/CBMi3wFBVV95cUxNUjBvZ0ZFTGY4NFhlcHBDTWh2dmNIUmFCYkNpQzEzWTBjWWlOdWU4MWlEYmR1aGR5OFQ0TndsRi1kSU5kX2R6REZDSHRmNjdPSHI2SElTalMyZ0hHNjA1a3BmeWQ4WXM0UkxxNVgxTEgwMlZDaGJCVWdyTE9xdllYVDNJdnN6am01cll3NnZLbk1CV1h3djZETmVUbU1BMUNDZWFpSzEzRTJxSVRHZE1mU2daVDh1cmswbWRkLVFMTlY1R0pQczQ1d1ZYNE9Za1lTNko4dlppVTB0SkVxeFR3?oc=5) (Thu, 10 Sep 2026 20:00:41 GMT)
- [US Bank tests its own Stablecoin for Cross-Border Payments - Payments Industry Intelligence](https://news.google.com/rss/articles/CBMiogFBVV95cUxQbDB3eERRaEdqNlFHaW5tcVdlQUwtMXN2UjVBczZnUXZXQWlFVnVYZEk2b3lFcWlCSFQtUUc0UlpJbVRKUEVneF9YamJadU9GWGZpSF9lS0prOFV0Tld0RFd1TjdMVjUwd2FsM0FsMjJMNFJoOUdkeFF5cXhjWmZDUE5yUENKSGE5NGZvWFVDLTY1di1ROFFXUGx2ZEZXVkprcnc?oc=5) (Thu, 10 Sep 2026 19:27:27 GMT)

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
