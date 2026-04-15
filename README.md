# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-15 21:47:18 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$298,966,552,541** | 🟢 +0.13% | 🟢 +0.55% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Companies Would Need to Disclose Stablecoin Holdings Under FASB Proposal - WSJ](https://news.google.com/rss/articles/CBMiswFBVV95cUxNby1iTEY0R1owLTNQYlY1T3o5UU9nWlVlX3BHeGw1clZLNU1PUmRqa0ZDWGlieVBVbTdlSkQ4Y2pXLXQxeFQtTlBYdXNlYjNpZjVFNzBEdzRlRENtNklkOUxRaEZLeW5GT3VLQjk3akhhTnN1bngzTXo0dnZNdlFsbnVHeWhxQkttOUZRbEFhMUJCdnc3NVcyZDgxUUduQVJnQXVuekt4ZmFIRHhMdEl3QV9SSQ?oc=5) (Wed, 15 Apr 2026 19:30:00 GMT)
- [HSBC plots Hong Kong stablecoin, Brazil&#x27;s PIX expands with PayPal - American Banker](https://news.google.com/rss/articles/CBMimwFBVV95cUxQZlB0enB6dUx4Q3V0b3U3eVVRQ0dQcWF0ZEZoQzZWeC1ZbDBNOFJJa3U4NC1PdDhYUHh5VngtR0hVTkFNUjFvemlqdjg0XzFqSmQ0VzNadlFrYlVrRnVMb2phZVNaWXI3V05Yd19fYnVpY0t4TU9Rb2FydGNlZkREdGNQWGFDWmRhc3hyVEd6MVE0VjIxM19Na19pWQ?oc=5) (Wed, 15 Apr 2026 18:47:00 GMT)
- [Fireblocks Intros Stablecoin Lending for Institutional Clients - PYMNTS.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxOUTI3Qks5TzVRSUN0UmNnU0FLYWo0Q2k5clhWcFZXZFBEQUdudXlENzc1TnVaaEJSS09Lem5iNVNXTWV3RDVmeVc4aG1KNFI2RkxJNkVNMkxZRUFRVURxdWJFVnB6VnFua1ZDSE43TW5CYThUSmZWSzdOYllTSHZyTFZsQ0dpMzAxU00wVzRvUFZWLXZ3TWE4b0oycXlYY3pSQ0xCTg?oc=5) (Wed, 15 Apr 2026 18:19:40 GMT)
- [US Board to Propose Stablecoin Accounting Examples for Input - Bloomberg Law News](https://news.google.com/rss/articles/CBMisgFBVV95cUxQcUVvY19HTy1wR1B5UTl5LU5KeUVwZ0dWU05LV0ZlQ2hZTVB2LXkzNFV2b2pYVlJjWjFxT3N1c0w3Nno2YjBydEl1WkRfVVc4OHQ3QWp0MzRKamt6NU0wLTk1QW9pM3NpZ3ZEZlhpaHFkeC1QLU96MFRrR3MwTUVFbGdEc0g1eFdWa3RjVkNybGhDU3I1SjFFNXR1dTYwUHB5NGVUY3BDU1k5RTJXNVFZQ1ZB?oc=5) (Wed, 15 Apr 2026 16:10:00 GMT)
- [Tether Joins $134 Million SDEV Financing as Stablecoin Infrastructure Expands - Yahoo Finance](https://news.google.com/rss/articles/CBMimgFBVV95cUxNd0FuTzkySmtGRlZHVXZfVEM4enBZeXJlVjFlYTI0Tm1LX3ZoalBPYXpXMWt3N1l3OE9nSzBvNURRNWx1SE0xTHBMYkJlb1FKaUV4NHFUalMxRy10RVF1cW5QR3BOOW9YU0Y1NjY2bEk2SmpYV3VzRTd5emNndFd2MFhyR3NfMkI5eHV0ZnoyNGtTOFhFY3E0bVln?oc=5) (Wed, 15 Apr 2026 16:08:00 GMT)

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
