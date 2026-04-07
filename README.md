# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-07 01:44:46 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,162,197,085** | 🔴 -50.02% | 🔴 -66.63% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Mapping the Digital Dollar Graveyard of Failed Stablecoin Pilots - PYMNTS.com](https://news.google.com/rss/articles/CBMirAFBVV95cUxPdENJdmsyYkhIc3djczFNSzFyRm9FWFRRMVBWLUNiQVZ5Yy1JNzlZcE1uejB6cnltWjhmXzJSQnpNalhYWW9lSDhtTGkwLUhZclFld01lN0t1Q3V5WmxVU3N2bjd3eDNsdGNUdlNRNFNvOUxrSFRtRHh6TklrOFhVekVXcGNNVWFmb2JrUnFrWkJXN1g3THc3bTFfWnIzVzV4QjNiMHlHUUM4eWJl?oc=5) (Mon, 06 Apr 2026 21:58:43 GMT)
- [Polymarket reveals a &#x27;full exchange upgrade&#x27; to take control of its own trading and truth - CoinDesk](https://news.google.com/rss/articles/CBMiywFBVV95cUxNNl9DeEZCNFM4UXZPWTlTS0xlTUlhWFBwLW5tbk9qVkFacmRXR1Mzb3BaYVBqbzFiSjR2SE44NHQxQ2Q3M0hsZnhPVHVBRlBDcVZETVlXcVJTWkg5S3lfSkNuOElYNE1FSVJnV0N2dC1BRGRCekhDcFhlZEJweUZydHdaSGxmeWpVbUxvdVlzWFdES2Q5Y2YzelBBaHRXMGMzTDI0UUhRT2s5aHBkS1RURWJLUXhMT0M3TzBoRmNWNWNlMFJzMGM2eTd4TQ?oc=5) (Mon, 06 Apr 2026 21:01:55 GMT)
- [Why Stablecoins Are Becoming the Everyday Money of Crypto - Ventura County Star](https://news.google.com/rss/articles/CBMi1AFBVV95cUxORnNhc01sTmpUUWNUTnlWTG1Mb19jQkhNSnI2VlNab3owWVJOMEJ5b1N5Qlc2b1RLMF8xTnZtSTk2WmFQMVloMHo1V1Z1cGZIOTMxWTVWQk5mc3VoQTlLcG5YYmQ5RzFabHVCdVdiWTJoa2xrQllGWVN4eWcxSHd1eXhla2RyYmVnMXFFdml1TW1tMnZndnpIZWhIUHRmeGQ5cS1zVkI3M1NzaWdsSUp4VXFuUzZhYnNFZnhVYXl6c3F3MDV3R1BtNVZYb1ZsUlAxWngyTg?oc=5) (Mon, 06 Apr 2026 19:36:00 GMT)
- [Polymarket Unveils Exchange Overhaul, Native Stablecoin As U.S. Expansion Looms - Bitcoin Magazine](https://news.google.com/rss/articles/CBMieEFVX3lxTE1faG1DZkdPdnJZRHJJSEJrYkdYUjdXemNZcWYxelI4WHRjUnhSbG12Y0ZKVEZBUV9DblVBTVpTLXJfRzNhSHUzRHVxZE5UTjcwYWhzT1RQY1lsMUozaU1YOF9OaF82S0RDaXdQWU9nM3o4a3gtTlRpZw?oc=5) (Mon, 06 Apr 2026 19:21:53 GMT)
- [Treasury issues first proposed rule under GENIUS Act on state stablecoin oversight - JD Supra](https://news.google.com/rss/articles/CBMihAFBVV95cUxQYnpfemI5TVdPRk9semVZbGIxOUViY1VqWC0wa1RrQW95RHkzb3VwN1c2dFo2UFIxWXJMcExIeUZxX2hWd01LdUFmcFNRcFA0ckduMzhtS1NZTW5pbk04Z2V5TEZmSjJNM0tNdnh2MEFCQ3Q4TExOUV84aXotRHdheTJsSWI?oc=5) (Mon, 06 Apr 2026 19:09:47 GMT)

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
