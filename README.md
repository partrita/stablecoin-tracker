# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-28 01:47:36 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$287,834,888,148** | 🔴 -0.04% | 🔴 -0.54% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoins and Credit Unions: Preparing for the Next Payments Rail - Credit Union Times](https://news.google.com/rss/articles/CBMipAFBVV95cUxNd1RtaEczYkstWUtWbTdJdWd5NldKZlJLS291NUQ1Q2ZoTnJMVzlucWpzb3pkbVdMS1dXemEtSEczaGpfRVdhRi01QmFNZHV6STh6UXRlZEEyR2pJcDdHdkxXeVo4Y01fRVlRRloxMEJ3Q09FcFBtdXI1TmhRTkZfejZoQ2U4Z0ptQXRYUmpXcWNNY19rS0FESlZXSHRLeXFnY05FWg?oc=5) (Mon, 27 Jul 2026 23:44:02 GMT)
- [The Stablecoin Sandwich Is Missing the Trust Layer - PYMNTS.com](https://news.google.com/rss/articles/CBMilAFBVV95cUxQWGZPUElObWhrZWtmbWc4TVlnM2lJNEZVOU1mUVNKOWZKOEpiTXZ6UUFKQm56Z0dBLVhZUUVlaTlHaExBcXpBMDdCMFR6cVg5Q2QtTnhyTGEtTXN5NHhLZ2U5SlplNlllNHNCWFZ3aEZBRGc5UGp6NXZTcUpRa1h1VkZqTVlsdmZ4MWRDNlBaQTV4eXRP?oc=5) (Mon, 27 Jul 2026 20:51:02 GMT)
- [TD Bank (TSX:TD) Joins Stablecoin Reserves Custody With Stablecorp - Yahoo Finance](https://news.google.com/rss/articles/CBMijgFBVV95cUxOcDV3dEdMTzZqcmJKcGJ5RVNiZTFIUGRMSzhKSVJwRWJ4MWJ0ekRoNEgtaDVNX0lDWUpNRWthb0RXLXZTWWVBd3I2LV9VUEhwcnZhR1dyVDdRcGNQbE9SWGlnT014MXJja3ZrZHgzdmZpalJnTC13SEROTHJpR0RwSUJVZ1VJUGRHV1JxXzdB?oc=5) (Mon, 27 Jul 2026 19:07:42 GMT)
- [Florida creates licensing regime for stablecoin issuers, pilot allowing stablecoin fee payments - JD Supra](https://news.google.com/rss/articles/CBMihgFBVV95cUxNYUN0bW9VTzVZWlpPdTRZcnpPVjJ0RG54TUtIcERvOF9xdXhOLVRnc0hEX05KeGgtVk9zanhQYUpGa3ROb1c3T1o1ZFhWODc5MDVkY3N5ZW84UHhtSmVuVUtoQXM3YzdQd0tKRUpXY01wNEJ2ZW1qc2htV24zaEdkWnRaTW84QQ?oc=5) (Mon, 27 Jul 2026 18:59:26 GMT)
- [Stablecoin Firm Triple-A Suffers $11.8 Million Theft of Assets - PYMNTS.com](https://news.google.com/rss/articles/CBMipwFBVV95cUxPMF9WT2oyaFRoRDRQU1lJVERpR3lVN3BkbGY1VE1iTEJoYkRmRzhFZ3VCb3Y2N3dLSGJKNVdYMnBhYUpMQnhQanlLeE9nSU52c2xYQ010RFE1c0lGN0NTNGphbFlOOUEtZ1BJVnlCWUNseWFfQXdtNmpKWHFpaE0wTkk4VExOd2phRlIwSHRkZExhd21WUWFJbE51dy1GaHgzRzJQY2hOZw?oc=5) (Mon, 27 Jul 2026 18:46:01 GMT)

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
