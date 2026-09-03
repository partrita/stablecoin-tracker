# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-03 02:15:51 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,910,514,941** | 🟢 +0.07% | 🟢 +0.18% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [21 Global Financial Institutions Plan Dollar-Backed Stablecoin for 2027 - 조선일보](https://news.google.com/rss/articles/CBMijgFBVV95cUxORFVtZlUzLXkwWGQyS2QxSmxyNlByWVk0SGFYVWx1cUUtVTFTWFpkclp2bXJvcF9qXzQ2NlpJYTlJRWg5c19JX3ZrSkdVM0VxTDhKc1dJNi1ZeWRvVFZWNXJaMWN3Y2s5eEJRODdCQ3NlcUk5SEhxdmlrdFlWdF81WXQzUU1pWXRxVHotUmlB?oc=5) (Wed, 02 Sep 2026 23:28:52 GMT)
- [Who Will Win the Stablecoin Infrastructure Race? Companies Building the Future of Digital Payments - Bitcoin Foundation](https://news.google.com/rss/articles/CBMihAFBVV95cUxPOHVvNFFtQnYyVFJndl83eDFjZEl1VXFCSnpMSmtjRThtdHo1bE5MZjY3TkxRLU1BQWpDcjAxdFk1RnY5d2lKX0ZrV0FqRzJkR3NUWEszVy1jaHFXbXJKMmthbWlFUWhmTk9jOHR1T0plVG9ObXM1QWdDUGthNDdZY1VSaVM?oc=5) (Wed, 02 Sep 2026 21:00:48 GMT)
- [Goldman Sachs, BofA Among 21 Banks Planning Joint Dollar Stablecoin Launch - Decrypt](https://news.google.com/rss/articles/CBMibkFVX3lxTFA5ck5RY3BUaFhyUVNZR2ExT3ZpVkdveGhReGp2Ni1UazJsR01VZGZRb09iei1STXUtNXlkN3ZIbGppbUZtYWU2THREM3dLeEloTEx2cUlHMVhNMTRzQTZKcHpxSHVrZmdmVlZFZVJB0gF2QVVfeXFMTXIxajh4cDZNaG04RmEtNWIyWlRuTUJnTmRLWUEydDJsRDgxX3JFSU9RS3ZjNlRqVFFVM3c4Nlg0eE96QUJIT2l5ai1yZEpVdmJaTDM5ckZkU0h1cm5vS2xDNTZYWHdHTzlwY1ZJMXNvY3lNYWFxdw?oc=5) (Wed, 02 Sep 2026 20:01:04 GMT)
- [Wyoming Moves to Ensure State Stablecoin Follows GENIUS Act - PYMNTS.com](https://news.google.com/rss/articles/CBMipgFBVV95cUxNVDRDSGNvQUVDSUlrcnpCdkdkS1ZNNzlTd3Uwd2tmb25OczhxRWhkT01KakxXOXYzd2xuc3RXNjNNYWV5MXB4YlBGMTdfejVfXzNQY2UyZ0djMFB0eXFHWFNhZ3pHWHJZcm1YR2J2NEEzTUQyam8tbjFXMFhTN0lJbXlzc0tydzZIOU9qWTNBQ0tkMFZoWDM5NVBVNWZPNGVteW4zX0Nn?oc=5) (Wed, 02 Sep 2026 17:54:31 GMT)
- [Circle CEO Urges U.S. to Lead Digital Finance With Stablecoins - Yahoo Finance](https://news.google.com/rss/articles/CBMikgFBVV95cUxQSGlrdkJwVWFFMVgxNnBPOE0zZl9uZXVrMlVCMkp2a1hwWHgxd1g4bHVwY0FOcndjWFJ2NXF3cWFSOFM0bXRkVXBKZ29nVTg2V2pzYVpCWnRHUElGRDJjMlpCNS1sVWg1YTJFdDZHa1FnR3VXQnp6VlhIaHRQbDZ5Y09CQlh1LUVkaEMwMnpqdnBaZw?oc=5) (Wed, 02 Sep 2026 17:15:00 GMT)

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
