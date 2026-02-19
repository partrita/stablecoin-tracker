# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-19 01:22:41 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,702,445,706** | 🟢 +0.07% | 🟢 +0.04% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Japan Experiments with My Number Card for Stablecoin Payments - 조선일보](https://news.google.com/rss/articles/CBMijgFBVV95cUxPeGVRcWpZQXhlU2o0Smlpd1BIUEk2bjhoQVo5SE1OQXo2ZFpPNDZad3pzdk43ck51LWRrR1ZiMlZ2d2R5WVdWb1lHQzUzREFqdnBmTklsRDVfUkhCOVNnX0htb3lWaUpPbzV2N3Z3RDFNT21BWml6RVNndDdLa1dTMENRSnh4OGxuRFhwUG13?oc=5) (Thu, 19 Feb 2026 00:12:47 GMT)
- [Bitcoin poised for another leg down as stablecoin dominance climbs - KITCO](https://news.google.com/rss/articles/CBMiogFBVV95cUxQZDQ3TVh3Z2lSVTlMbGxkNENWLVQ5MUg1Y0pHaEtVdlk2TWd1NHVvam5mQkNubXZQZFpOSlVPaG5oTGFWd2ItVnVBTEZ5TE0ySUdmOXFfRUh0QktLMmdBb0RrOTB6Qlc2ZDRlME1wcnFicFJDdmVKTzRzNmZURHFHRUNtR01PYVBIU3F0cjJZV3dIak9FV3lBZHozMGI2V3ZJbXc?oc=5) (Wed, 18 Feb 2026 20:44:19 GMT)
- [US Congress Ramps Up Push for CLARITY Act as Stablecoin Tensions Loom Large : Analysis - Crowdfund Insider](https://news.google.com/rss/articles/CBMizgFBVV95cUxOaW42TFJUSFNlM0Uzbk5aYTNuWVZvdFdjQW9LSEpfaXo1TldjNmduM1F2a0tIZVVSa3hLX0ppb3k1R0VZNGM2aFhVb05vNFgzcWdXaC1KeXVLR2FqbnowR29lTnZNSDRqRW9pTWQyZ1pOVllGTEo2dnloaldrNDVGdTliWENJaVJheGtFTmM4dGtjY3N3YU5ybEJ1NDBPSG1xcnpKZlJvME9FYktmWGdwZjQ3YlBRU2Z0ZkNQX2RJY1c4aWNyTkpWNXlfTVBvZw?oc=5) (Wed, 18 Feb 2026 20:29:55 GMT)
- [Visa Helps Wirex Provide Stablecoin Payments for BaaS Clients - PYMNTS.com](https://news.google.com/rss/articles/CBMipgFBVV95cUxOTHpTQkloeDR6ODlBbUs5RWVRZEZZb2VKclZjcnZURmEtSkhfQ0VZZGIxZVEtRWFYTGhMZEJaWXk1SG00MEFLQno1X09SNmJKMFNGT0VYTzdaV2ZoemlwamlyTW4zZ2l2MjJGejN2VTNxWnpic3k5UVFuVlgwZEN6YVl6M1RMMVBKNlNvbHpZM2w2MFBLU2U3a2JqSHY4blVuS0NsT3JR?oc=5) (Wed, 18 Feb 2026 18:06:31 GMT)
- [Loyalty becomes lifestyle: Rain and Uptop on stablecoin rewards - The Block](https://news.google.com/rss/articles/CBMinwFBVV95cUxNd2pWdGRNckYxaW5hTF9tT3Rld3E5V1BOTzlvcndWbWtTVWhMZk4wYXRsUG1mYkQ0MUtoOWJwY1ZXakxtNFlzMWV5YVZaNXZWVE9qV25zQkQ1UjlKNTdNSE9BYVRwX2NJV2tKNFV4d29sei1yd2hRR25IVG9aTS1LVjF2ZGZoVTlyYWk1TDFOQTJGWmxSaDhxRkRRNHBOWHM?oc=5) (Wed, 18 Feb 2026 17:31:45 GMT)

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
