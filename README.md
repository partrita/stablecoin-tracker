# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-21 02:35:03 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$299,929,243,177** | 🔴 -0.25% | 🔴 -0.21% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [AllUnity preps Swedish krona-backed stablecoin - Finextra Research](https://news.google.com/rss/articles/CBMikwFBVV95cUxNc1dCMUFCZVBwajNha3dLeldNVjY2eUg5blhMbVBfRDNxTmI3NnJwd0hnaWZZX1RCTFVRYXlVeWtodXQ5c2lnemRHTHh2RkJRZzFCdkV3b0RBSVRjTHZjYTEyTVY3SmdadTRnODBTMGVNWmlTVXlldDlUMXU4Ym9NdzVUQzkxdXM1bHM1SFF5aHRjVmc?oc=5) (Thu, 21 May 2026 00:01:00 GMT)
- [Flipcash Taps Coinbase to Launch USDF Stablecoin on Solana - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxPcVBJVHo5NlhyLWRMVzY0WHlQTDV2TUlxMzJSN3NIZEl2ZjlnRVl3RWNJSzVEdkxJMTV2Vmt2UHNLSVdRVERfU2tjeWZjMFllTlM4VTdVZ2FoYzhvYVctdTZoVHNHb2dsNm5Zdk1ON2pVNU5kV0ROSTNDZWRCa1BmYTZYMXhKVjVOc2kydVFvMC1SMlM1c1B6TVhaYmlpbFFQ?oc=5) (Wed, 20 May 2026 23:36:00 GMT)
- [LATEST: 25 banks join plan to launch Euro stablecoin - AML Intelligence](https://news.google.com/rss/articles/CBMilwFBVV95cUxNNE5ZaUVveVlQR2FRZnVUOGNNOC1KdUwtZm9iVmMwanJuV1I1cjl5ZU1TdzFxTC11ZF9YWjRYbHRZVVp0dHpNQzZYclpQOWdNSVlkTDlWcS1MeU9ISkVxb0M4ZHhVbjRRSXFzWlMyTkhDYnZXcjgyckFDeTI2R0ZTcllmNkc5VnNEN2FieVFEYkVqOUhodXlV?oc=5) (Wed, 20 May 2026 22:13:51 GMT)
- [Sui Launches Gasless Stablecoin Transfers With Support From Fireblocks By Chainwire - Investing.com](https://news.google.com/rss/articles/CBMiyAFBVV95cUxOQndaQURFMmNuYWJIOWYwaUF1UFhsdGd0bHh1Z29JVDk2eHhjelNva1NnTTVZU1VrUkRSRWNaMUMwX3lSZTVJaE03dkZKaVp3SWhSbGE2MVYwOXQ4V1k3a3N4NnRfOHlUYVFCOUg2ZmkwbjE0aFNuWnZmUjI3VVV5eUp0RjM5M3dMM0RmaEdUZnJUa0txazVoZU5xVlZsN2l3MEsyRDUzSHF0LXNjTkhrczlwMUtsNDZOci03ZGlXY0tBY0xtMDVvRg?oc=5) (Wed, 20 May 2026 22:00:38 GMT)
- [Coinbase expands branded stablecoin infrastructure business with Flipcash USDF launch - TradingView](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNQjhzMjFSdmp4eHpEU0lVSnYxZXZoZVpfZ21rTmxvYk13R3pXdm5MSFVRZzVvRXl0YkJCcHdpU0Q3MmpTM2ZkN3llLXp5QzZMTzBkbjEwZTE4MDktTURhdE54YlBtVVlnbXpheURBWGwzamh3TFppSEZZZmh4YTR0TnRrRkFXalAwVG43dGVvSDk0bXJfTFoybWNEMlk2YTVGNERoSGVKOTJVUDBFdk5kVElXS1lCT0F3Ukw3bzBNNzZvakVGVUNlODZDQ1dPNlZORmhSOC1Yc1hyakVrVmJvUzZ6bw?oc=5) (Wed, 20 May 2026 21:37:09 GMT)

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
