# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-05 02:11:59 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,771,564,024** | 🟢 +0.09% | 🟢 +0.23% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Singapore Stablecoin Rules Have Issuers Deciding If License Is Worth It - bloomberg.com](https://news.google.com/rss/articles/CBMitgFBVV95cUxPMWIzUW1DbUNjU25FMjB2cFpsRk53UTk0bmh3a2liTERNV2pqY1hDdEVZbml2TTZORTdFWGF6cVlPM3phbDRXbHNqdVhldlN3WnQzUU83THo0QlVBMkF5VW5nMXc1a2g5TWtzQnNLc0o0c0s1QnVSejUydzZkY3BGTS1lNEZGeDhhTVRTaUdvX21iNkpIcTI0bVVJNTVjTExvLXRiUHlidGFwbDB3OFNUaU1PNWJwUQ?oc=5) (Sat, 05 Sep 2026 01:00:00 GMT)
- [21-bank stablecoin has global backing, but can it rival USDT and USDC? - Crypto News](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9UX25mV0tqbUd6Z2dyVVo3enJNMW9wbjJ0Mm13TF9fb190cGV4TzU5WVhGcThuSHVXaDJuakVjY2VIV0FnTS1GMnA0bkl2cExBb2YxU1J1dmJQYVJUVmVTYWZ0ZE5jQQ?oc=5) (Fri, 04 Sep 2026 19:17:00 GMT)
- [Int&#x27;l banks plan stablecoin, OpenPayd enters US market - American Banker](https://news.google.com/rss/articles/CBMikgFBVV95cUxPMU5qT3MwUHVDR1FxanFrajFJSl9mcmhIX0tNZDFLN3BnT1RjajZVOXlTd2k1VUVTNUU5SWxMcHJYNGlORWtheEpvYjd6YTg5U0RiQzJmOFk4MHg0c3RnYTJTXy1QY0tPamx2RHJrSTk1OUNpR2s2Ul8xVkxKQWNkcjV6WnZsQmRwYXl6RlFCSGRfUQ?oc=5) (Fri, 04 Sep 2026 19:01:12 GMT)
- [Does SoFi–Kraken Stablecoin And Liquidity Partnership Change The Bull Case For SoFi Technologies (SOFI)? - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxPMDNBZnRZWHpUMUN2bkZoVmxZdXJEUGRNSTMwZE9nM2hMcU5nd1FaNUJjSXdNbXFlVVdTTGhqOUtvREtuNEVCSmxMVVZ1QTJ0SzBMMHQtajRKd2cwcVlHdkc0WmVvOWwtMGZMckYyZmVlck9MNU4zNHFlSmpsMEFGWnA1TGR4QVI5QlFHR291WEUybzVUTWVxSnNNRldpNlNlSHN6bA?oc=5) (Fri, 04 Sep 2026 18:15:44 GMT)
- [G20 Backs Digital Assets Growth While 21 Major Banks Target 2027 Stablecoin Launch - Stocktwits](https://news.google.com/rss/articles/CBMijgJBVV95cUxPZlR4RjR5XzVhSVFyX24yY0VHWHJjdHh2ZkRKUmhRQjJsbDlxSmRYQnpmb2JCd3pCUDFrb3JBUTFUWFBRLW8wSDN3VUNMWlBxdFpNQjVCZHctQXB3ZU4zMmVEWDdTVnZHQlp3c1J4Mm8wamRocTN6dEZvSHJZM2tDaWNnOFFTdHBRS2VKUXFBQzJKMG1SQUQ3M3VKc2ZQTGx6V0pBcF9sOWtKREJpWE1kQUkwdUtjYXRpVE9OWElRYksxWWxkZkFMS25BaFRYSERWU0tiVks5aGp3X2djU1YyTm95RVlBcEF1NUdfQlpvWHZRdWViZmpNR2VGdkZZNmhqZGcyaHZXRDV0eDFIcVE?oc=5) (Fri, 04 Sep 2026 18:13:03 GMT)

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
