# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-06 05:51:44 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,308,290,543** | 🔴 -0.00% | 🟢 +0.14% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [42% of CFOs Express Interest in Stablecoins as Payments Use Cases Grow - PYMNTS.com](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOYWFRTVlveTNkdWNCRnY0ODFsTXlXaDNleGRZR3NQZ2dBRzlNN29rdnE5OGdFNWY1NmRHQjBvX3ZENEpkbXA2T3pYRHJfNGF6OHBGYWRWZXVZbnhscUFsWllWbjRxeFk0Ymh1ckxSV2Nia080ckN0SURFSmR4NE4zUk1Uc3VPdE81QThpUjlndXVkNVVCTUJrQVhkRUp6YldPUEVxTFVQdF9tcGxERFNtZkR0UVdSOXIw?oc=5) (Mon, 06 Apr 2026 08:03:16 GMT)
- [Guest columnist: Close stablecoin loophole before it hurts Ky. communities - State-Journal](https://news.google.com/rss/articles/CBMirwFBVV95cUxQM1U5ZG54WnhJSHBBMkpSZ3NTNF9Kekl5Sm1STkNyY1JGOHNaMnpwR3JjWng4QTlLQlRNRjRhOXNndEdtS0g3NUNhb094b2phQ2U5YWJqZmc0c0UwRkx1NUVLcWtoVWtreE5DR1lmc2VYUlhvY1ZCdFAzQXhiWkptNU5pTmxLaUpYcnJpZ2pSQmxmLWdtejREWG1ZZ0c2ejRIYTM2NjBwd1F5Q2Z6Umlv?oc=5) (Mon, 06 Apr 2026 05:03:26 GMT)
- [Editorial | Stablecoin launch delay shows Hong Kong would rather be safe than sorry - South China Morning Post](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQNUUya1RPbXdQUDhlYmc3TmtTM1kyVUVTS0NQLW9jU1BUeC0tM1dJX21pMmxXWGI0b1RzUXRwMkQ2UVpwNV9yS2RpNVZiS1J4Q05zVkwxSG44cTZCOWN5aFdiVXVZUE5YOURCdlduSTlud3VKSkc4U29qakpnZmVNUHE0SEhSRVRYTHRqU3JiejdqVmk0SnZEbDRscWg3d21YNlpmNFdqal9wM3hrbWJlNEpld3ZoejgtSnlJ0gG7AUFVX3lxTE9sczdPbm9EaGVrbEtqZ25NYzdrT1FGaVRyMkU5Yks2eFI1WGR3TjdPOHo5TmhCNnZEbW10SER6MzQ5TGRfZE9zNmt3elNWMy1hLXRoNHA5Y2ZJSEVNaTBiVFhPWVNGSk0wWjZ3dUZtVEg5bzNpNkE3a05JaWNyM2ZHSS14dUxobHRIek9IeGlxR3lKM3BBdG4wREdiQlhRVVV4XzVtclZyLUotWjZoV2JBdEVTTS13SDUtekk?oc=5) (Sun, 05 Apr 2026 23:15:16 GMT)
- [Nium launches stablecoin card issuance platform across Visa and Mastercard - msn.com](https://news.google.com/rss/articles/CBMiwgFBVV95cUxQbjRyTDBSQzZfZVl6Z2JTS3BhV3EtOWZOa1VSeWZ5djJEVGp5cVdHSXZNX1FyREtPUmszcElpR01meWhGOW9qbTdYQVR4Q28tYWhqZnItSlRKdWhjLUJMTXdBYTdraTNYNTVMR25JSmNDUXZaTmxvY1pCdHcwdDlYMlAwZDdLdDZoRnRVYnBfekk5b2p4bDR4SUI0N25CaWY3UTFORHNlTFI2WWxxYXFqVXlvOVl4RFV6NXRESmVOazlXdw?oc=5) (Sun, 05 Apr 2026 13:53:18 GMT)
- [Mercado Pago winds down the Mercado Coin - eMarketer](https://news.google.com/rss/articles/CBMilgFBVV95cUxNaWlKd2NDVGdMZGgtZ3ZRVF9oTWFEcmpyRm0ydTJYNV9zeF9xYzZuV0dwZU5EQkFUUVBxMTVSZDl1aVNra3V4VzJlZ21URHFJaW84aG5YMGNJQlJIZ0VLZ0w2VEFoZkI4VTFKVl9teUxBQWh0REtPblc3Nm8zT2RMTnRVMXdrNFRrdWF6M3JBUjlJVEJvbEE?oc=5) (Fri, 03 Apr 2026 21:40:10 GMT)

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
