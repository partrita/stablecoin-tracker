# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-20 02:46:42 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$288,611,265,254** | 🔴 -0.37% | 🔴 -0.79% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Tether Says Iran-Linked Stablecoin Volumes Fell 94% as It Rebuts Senate Report - Blockhead](https://news.google.com/rss/articles/CBMitAFBVV95cUxQQjZYTTFTdEhZTlR3bUs1djNpS1NpeHoxcHVVZkpWbnJMZU13V3Y5OHJTWUotUExSdUh5Rmg0M29TQWFXNmNLSWtpRjJEaVgwZVcyQUhxemFZQm4ybV9RQ2JWYVZNcVdaRFJRZHRYWlhRek9kZHg3dlp3MjBBUVFDNnhJX2ROdXNqdW5ULWl1S2xlRS16SlBzaDVGN3U5Yk5SVkdmT0YxcF9zaXRQQlBPQV9DZjA?oc=5) (Tue, 20 Oct 2026 01:57:12 GMT)
- [Visa Moves Stablecoin Prefunding for Visa Direct Into Production, With Inyo Global as First Partner - Blockhead](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOY1JsTF9acUJKbEVObG1PRkxPbURRM0lrNHZqUDdkWTZ4OGlQZjJFTURwWjlEeS1ZYzdFY1JvTWJ3b3Raa0Q0ZXhSTGlvYzZHSHZXQW1fYi1FdmpqdmNMYWZlTzdGY2tDLUlEZ3dVVE44dnVXU3NTRVdMUEhocUxXSEgzc1hKcmZ6NFQzczVUQlhONlNKdHlHVVlxd3pRMHFwUFpVdnM3XzFmd2p3U2dLRnFvR1lQbEg1bEJwb1kzVFgyZ25yeFBTZmNOb3VyMVU5?oc=5) (Tue, 20 Oct 2026 01:52:12 GMT)
- [Visa and Mesh Partner to Make Crypto and Stablecoin Balances Spendable at 175M+ Visa Merchant Locations - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxOWFJUZlZxcE91XzlnaEZfeUhGTUMzNlRYZWJqSDM3U3J4clZKZWVnQlF2cFpxaFlHOW1POFI0c2djcHBTZWZOVVJHeXl2SnBLNVlZbmlqTl9SVlFtOGNGT3Q2MVFDQ3NlWUh1d3FDWDRkZ2RRX2VPcExaemFYb3pMc0RuUm1xOVNjSDZ5dUxkX3d2enFzX2lLaTFRRUpMZ1hsOEE?oc=5) (Tue, 20 Oct 2026 01:13:00 GMT)
- [Best stablecoin yield in 2026: 6 ways to earn on USDT and USDC, ranked by where the money comes from - Crypto News](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNT0VnTWJDS1JKWlBPR21JVlVwQ0lDMmxjdzdkcjVsSHNnSXpKOWstRzJkalhNOUItRHZkR1NsbG50NjM1eDl6ZHdfclo1YjFpNEQ4V3ZBbE1SNzRWcWhCNnhZZ1NGZi1tbmpMM1diS3J3MTRHaTltWHZoQjJVSWl5eVRQRkROLWYyZkZPdzlLU3lKakphS3BjTWZnS1lscjAzVmVmMV9LdnJFMmxyTGNZdHZ4Y3NxVjFvcmtF?oc=5) (Mon, 19 Oct 2026 21:00:00 GMT)
- [Stablecoins Are Writing the Banks’ Obituary - Brownstone Research](https://news.google.com/rss/articles/CBMilwFBVV95cUxNU1B6cFVnOWVIT1JWODNHaUlTY3Z5WmU2RHZMbnF2alJNV2xra25HZDFoNlB5YV91VzRCWUlVcGN6eVQ4dlExZUFZYV9jbWc5Vm82OXJFanJub3NXTHNUa0NRY1RjMzZ3eWdQeWs1MXduaXlOVDljRWctYTMwYkg1UFpxNGtXTkFvSXQ0OTNCaTBHY2NsQWpZ?oc=5) (Mon, 19 Oct 2026 20:26:20 GMT)

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
