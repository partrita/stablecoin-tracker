# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-27 02:39:29 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,238,686,148** | 🔴 -0.04% | 🔴 -0.15% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Deel Announces Stablecoin Salary Payouts, New Head of Crypto - CPA Practice Advisor](https://news.google.com/rss/articles/CBMiswFBVV95cUxOY3UzUEJwX2YySWlnbURsMkZMU0pBRUREeXBqcE5xLXJPRWt5Z2hNa0tZYWVySEsxRjdvRm0zZmNkQVJXNTU4RUlKX3dUVjRuT2ZUUTFMd0pyWHdHN3ZMMmhXT0JpSU03blZaa1VHVkVtd1VHdHVzejF6bHQ0YjdwdVlEMWZ5Zll3S1J3X1dJQ0lKZTlEblFsNEpfWVFOMW16MUVlaGowVmEtSjZrU3pRVlIyRQ?oc=5) (Tue, 26 May 2026 20:46:34 GMT)
- [FDIC proposes preclearing stablecoin AML actions with Fincen - American Banker](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPUlVQcDRHSGZjZU9palg0T09YSFg0UVdjUG1wd3hhMHRNZ19zT2pkbkhfdFpLVS1lbU1qUHdfaWJvM1NjYVlWV3VBd3ZDa2dfU2JzLWVRSXA0d1JmWUplYWFpRHlud0RaUWdfc1pOWl82cmprb3ZKc2JkQTIwTUdHWlVtTVVmbnZ1bWFSU002QjRDWjdIS2MzdUR2d0RFS0lVeUNRZjVadEM?oc=5) (Tue, 26 May 2026 19:09:00 GMT)
- [Stablecoin market value now exceeds the reserves of 95 countries - Yahoo Finance UK](https://news.google.com/rss/articles/CBMijgFBVV95cUxQUzV2TTZTcl9mQkxoY1RWcG1Ob0R0REMtU3B0alB1ZUNOOHVUUjU2RUdSaThTcF9DZUZtWEgyLWpRS3U2MDFfNGhBSmQzVFZyMGNXR0RjdVk5QkhnX2FJZWY0eG9sN1A4akRxU1dzcXJjQVp4M0w4QzUyd2VDWW14TF9FX0VYSHJ6dDlMbWF3?oc=5) (Tue, 26 May 2026 18:30:35 GMT)
- [Stablecoin market value now exceeds the reserves of 95 countries - Yahoo Finance](https://news.google.com/rss/articles/CBMiigFBVV95cUxPWlFzbDNuT29qMkRTSlk3UExSSnVyeFdKdDk3M2ZpSEZVbnhjSG9Tc2ZTNENnYmNsSGQzeWhSUmJYZV9Jcy1fdUY5cDF0dmtjcWFrSGFuNXczby13bkFqU2NPREx4SmlXYmF6OTU5NjZnamlBYmxRSXFGZy1GUGJxMjZVeWlPZ1BMdHc?oc=5) (Tue, 26 May 2026 18:30:35 GMT)
- [Tether and Georgia Pilot Lari-Backed Stablecoin Model - PaymentsJournal](https://news.google.com/rss/articles/CBMilAFBVV95cUxOSFFqZDJxRVhvY3g1MXp1VmhpUTJLSjQ3YVFteVZsZVV4ME4wSm5YN0JZY2pJeXFTOGlUdE82Z3V5Snh2UWhNN1VKQVVyajJtWlFUYXhjUjk1NjVCQWphaldXcm42enZ3WTZPSXpDWmFNVEczSy1TQ3YyajJ6SVVWUUJXbTE3WS16SXZqWDhrWWM4UlpO0gGUAUFVX3lxTE5IUWpkMnFFWG9jeDUxenVWaGlRMktKNDdhUW15VmxlVXgwTjBKblg3Qlljakl5cVM4aVR0TzZndXlKeHZRaE03VUpBVXJqMm1aUVRheGNSOTU2NUJBamFqV1dybjZ6dndZNk9JekNaYU1URzNLLVNDdjJqMnpJVVZRQldtMTdZLXpJdmpYOGtZYzhSWk4?oc=5) (Tue, 26 May 2026 17:39:22 GMT)

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
