# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-01-20 01:06:15 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$295,637,948,408** | 🔴 -0.06% | 🟢 +0.69% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Ban on stablecoin inducements should be included in Clarity Act - America's Credit Unions](https://news.google.com/rss/articles/CBMirwFBVV95cUxPWjlwcGdLRFR1TUJMYUpod2M4VzFKcGFMbXRnWVlkYklpZ0QtLS1aNFU0ZWNzaW10V3MtcnBaRTJBTGNIWUtCMEh6UEpDcE8wU3BaY253RTRhVzRRNi1laVpOaDYxNE9HVzFodWNvejNKZTFIR3ZjMWNRcDZQeUgwZjJEQ1dFLUtlbWRaX05Ka3JKX0IzQWFTRkxyMlpBNDd1dm1SMkV6cTVScVNiTW0w?oc=5) (Tue, 13 Jan 2026 08:06:48 GMT)
- [Visa crypto chief bets on stablecoin settlement, sees volumes growing - Reuters](https://news.google.com/rss/articles/CBMiugFBVV95cUxPendZWC1EU0dhSENsWTFPS1BGQXlVc245aGF3NjVLaTcxbW5rR2FlVmUxdURtQ1JPbDlLTi10d1JHRTE2aDhIQTZwalUzQlpONktmbk9CWnkxaTJVYm5ZcDRBc2RPV3ZvRFkyaGRKaTdjUmc5bVNNbms4VXQzeGVoT1BxbTNTMFNSaHRxbGhjbUZRUzZhUDloRy1ZQUZvZDlWT1lkVGItaDJFR2FHMmNUT3IzcEpBOGU1NXc?oc=5) (Wed, 14 Jan 2026 18:31:29 GMT)
- [Unstable Coins: Stablecoin Regulation, Market Structure Legislation, and U.S. Security Risks - CSIS | Center for Strategic and International Studies](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNOGNrcUpzSzhla3JnMUdKYW5vaEV0TzJaMDkzenk5ZHdHQm02cFFTaVFpWV9iRDFsSGZFUkdMdnhrSDlkUUYyRjFpdlhycEswWU9DMlpUZ2l0bG14M0l6N1ZCTjhsbk9uREFTZm9XeVlPSUIybUh6RW5rRExyZnd4SWw4dU5RcTEtR0wzNzhmVXo5VkdEN1JqXzhtZW15S2J3Q1RxRDRXNm1udHl2M19yT3pCdmptTGxo?oc=5) (Tue, 13 Jan 2026 01:11:43 GMT)
- [Stablecoin Rewards Paid by Third-Party Platforms Should Not Be Banned - Cato Institute](https://news.google.com/rss/articles/CBMilwFBVV95cUxPSXRTTkNZVk55SWlBWWJBZ2FyWndFZzBDSGtSVzdQYVdmM1JBa0xfUHJVc3JIUExMYlNLRDdWTVhHck1qUTVfblYzYXVnUzR0YkEwZS1yYjlzOUV2UmVvSUJlV1ZZSkxESDlFXzlZSVhwalRJTlhWWndkZUEzdVJPSDRIbkVaS2lJT1lEOHJEWC04OHZITV9j?oc=5) (Wed, 14 Jan 2026 19:26:54 GMT)
- [From Stablecoins to Infrastructure: Circle Charts the Rise of the Internet Financial System in 2026 Report - Circle Internet](https://news.google.com/rss/articles/CBMi1AFBVV95cUxNQ1RtWjNaRzlydkd6RGZVcTlWRm5qNlFHV2dtZS1zN1V0cEpZd3N0aW44WFZRdHk5aEZJN3l4Q2JuQndPRjNCbnpCcGNTNS1pZDdWNTBfWGdFeTZGRERFNy1oT0RUeEl0b1lDNGZKUmlicmNXNldjWWZzcWRlUFpPT2VYZVFBZHBQRVZIVHBzaW9adXpzX1djWGVZYVRvd0daWVlnWnFUQmhZUklyNW1KdFdxblQ5QUZUQWRHUUxtcWhITTRLakpQaVNCMC03Uzl1blhUMQ?oc=5) (Tue, 13 Jan 2026 14:06:32 GMT)

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
