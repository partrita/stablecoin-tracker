# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-11 01:52:46 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,695,336,723** | 🔴 -0.02% | 🟢 +0.30% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Circle highlights mobile money frameworks as foundation for stablecoin adoption - Crypto Briefing](https://news.google.com/rss/articles/CBMidkFVX3lxTFBGcVktZ2lZOU9DQnRhWWVpT2tWWlpVS2IwRUVVWjdYRTAyelY5RVZjb2EzNzQ4OWVQUEFyQzRjY2FZSWZTaDRJOWNnSW11aU9vOWZiLUFma2lGVHotRDlCLV84bnFsQ0VhT0FNTjBZTTkyZHByb1E?oc=5) (Fri, 10 Jul 2026 22:44:34 GMT)
- [Stablecoin Adoption Runs Into the Treasury Back Office - PYMNTS.com](https://news.google.com/rss/articles/CBMiowFBVV95cUxQbHVsc3REWS1vZnVOREJ2SFJBS19aWDdiS1BBNWtwbF9adjdBRjNPanZKel9STjhYYTkzZWdzNmlrclM3azMxN2xNUEhyTndETEtoaktjeHhwUFU3RjhScTJ6QlJQS3RCdTNWNnJZQWhxbWdUcWRyVUhhSTlubDdidFRVNkgxMHgwa0dQTld1NkJNWEk2QWp4Qk1BRzJ4NHpBUUJr?oc=5) (Fri, 10 Jul 2026 21:05:09 GMT)
- [Stablecoin-issuer Circle wins approval to operate as a national trust bank - CNBC](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNaGh6MWRsMHZ5T2preG5ocTFKdzZINWJCai1ER0l3bllvUGptTU1KNjM1emthOGdPQkt4UTNkZmw3SnlfallNd3dOTE9fZ0Z4VmNVbUMzbVdjUmJxTXNxRGlQdkkzQVBYQk5qLVdPUFUycTJ4V1lKNWVtU1dWYXpXNDUyV3BrWUQ4S29kak9uaWJfVEpzcnJrVFVyU0pUdXlFM1g0X0dIREVpNlBaLWRZRTZPalNia1lM?oc=5) (Fri, 10 Jul 2026 20:17:23 GMT)
- [Stablecoin Spending Appears to Rise -- Market Talk - Moomoo](https://news.google.com/rss/articles/CBMikwFBVV95cUxPbWpRNE9EZGxPb1lta25kSXpBWmFITzZCeHVMM0lRaDRZN1UyUVpZVHl1RHctbTVXeEhHVlUxOUtQREdmVUpDSlpWOHpFM1dhMUtOaUZZM1dtM05NN0phbEthVmxmLS1UTlBoUjBoWGZDNW1NU0lBd05XX2FDMG4zT0xKQ1kwZjM1bEFBYnhacDJEdGM?oc=5) (Fri, 10 Jul 2026 20:00:00 GMT)
- [Circle Wins U.S. Trust Bank Approval As Stablecoin Competition Intensifies. Shares Jump After OCC Green Light. - International Business Times](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNNWU3cnd1c29JYXVVQjJyb1hIb0RmUWUxbk5zVlpjc21qTEJ4WlZkb3hxYklpeHhhanF1MThLbndFeU1KVDZ2cVZFUTVoRWMxYV96d3hleTkybE1talBxblAwTVFlWGhGZnZaaVI2RkpBdnJmZXdlZzEwMjQ0b1d6d3Z0aWh3SUNTMlVqYzEwa0x3NHNITHp0b1Q5cy0wbUVSNV8zbVNRTmFubFFGeUN6SjRuMVhZYXMtbF9VcnRoMXI?oc=5) (Fri, 10 Jul 2026 18:45:02 GMT)

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
