# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-25 06:16:05 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$271,656,119,824** | 🟢 +0.00% | 🔴 -0.99% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Hashgraph and WEA JAPAN to Explore Stablecoin In-Store Payment Tie-Up Using Hedera - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE96UkE5ZnZ0Qjl2aDJobHRBaFlWdGtXb0ZPV0FQUFZXOEp4WjM1N0FJdXNpdkpobE1ETzBIWHhyWXpCeEFRdU9rRkJ4dDg5RmNwdy02Z3MwQkRRWElZTnd0cE9ZaVpiV0ZPQ0h2QzdwTG84R3MxT3c?oc=5) (Wed, 25 Nov 2026 05:06:00 GMT)
- [South Korea&#x27;s Won-Backed Stablecoin Launch Delayed Until 2028 - 조선일보](https://news.google.com/rss/articles/CBMijgFBVV95cUxNMzF4QVlLWFRCZG5KOE5OY0ZZbDFaMzVLNHlyZG5wVzhrQUw1SmJqZk1jSVZZZHkyYTB6SjczTVBoUkNGOUI0ZW0xdUZLSnBQd1hvTERRb011Q0EzMUhQeUZfczY2OGdCaXlFOXNTdXJFVTZ3X3ZiNW1FUEpqN2JmZ2pYN2xwT2NwT2xXalpn?oc=5) (Wed, 25 Nov 2026 00:43:53 GMT)
- [South Korea unveils bank-led stablecoin framework - upi](https://news.google.com/rss/articles/CBMisAFBVV95cUxQZjd1R0NqRUx2c1ZOWDNUc2JreEd0cXJRYy1iZ3ZDSmljWi1rS2pHSTVRdk1BVmFJcjRiZzYxcldrMjRPOE5xY0o1T2gtWHkxN19DMlpQRlJuYVk5RHZmbmJ3MWl2cFRqMVctMkxVVG9NSkdaX3VVRlJib3R5bENxTTZFdUtja2NqOEVVcHQ5bThtaG1mNzdzby1GamlOMUlmV3FVbWVrSjVBQk42SG95LdIBtgFBVV95cUxNRmp3eXE5ZEphWl9KOHJlQlpzMFVyaDktaWlDbHNJQVBPOXQ3Nk9LMFBuWERQNkRKS0VUU3VaTjJnN21zQ0U2UFc5WjlHSkdnakZ2Y1Bua3NaRG4zZmVmS0ZXZ2pUUFYzTWdrelVOY2ZNN2swaFRGVTdtcThGOFdLUmwxaHpUeGZGYWpOOW9nSFF4ejVZRHVjdXNPMUttdFFzWFRvUWE5QUUzemFxV0Q1cUN6VGJZdw?oc=5) (Wed, 25 Nov 2026 00:05:55 GMT)
- [Codex Secures $30M Series A to Expand Institutional Stablecoin Foreign Exchange Platform - Crowdfund Insider](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOSDhfa3Y5U2JLZnBkVFdxekQ0NDZYeHF4OGhyNi1XcU1odDRvTTk4bjFVdW9tN0djNnBCV3RucjBJUXB3SVVLRUhndmg2QjNGeU1nU0JLV21jRVlwZTNBejFaZXlLR3RnUnY0dUtMYS10ZVpaMzZlUjIyODNWVlBxcWlIN2I3enMwOWdVN2xacnZTR19RR0t5ZW1wRVlpMGZ1TF9lenN4em1WQ0VqWUZpemVPZFpmUzNCQWUyUDNnM3EzSW1lUURKLW5oMV9JbGVXRHc?oc=5) (Wed, 25 Nov 2026 00:02:34 GMT)
- [Stablecoin Market Shrinks About $17 Billion in 30 Days - The Defiant](https://news.google.com/rss/articles/CBMikgFBVV95cUxPdllRMkRTLXFrbFV4NnRTVGhaMUg5cEdCckd4dkU2ZlZpVmxwZUJRV1ZXQks2QkhfNFJqSldZamNoOVY2MkhLQ256NmJSOXVVeTdEdGRjaVRPSTRHWlRlSWZQVnlnWEQwbGtFQ2lTUC0ydjRodi1Yd0VRQ3Vsb1MxcFBFdHJHaFpkaHgyaHo0cjdodw?oc=5) (Tue, 24 Nov 2026 23:45:41 GMT)

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
