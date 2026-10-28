# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-28 03:15:32 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,295,229,003** | 🔴 -0.23% | 🔴 -0.76% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Anchorage expands Bitso partnership for US-Mexico stablecoin corridor - grafa.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxNV3Fjb3hQT2dNRlNOLUZaYjMydWc1OF93MVRZYXYwbWtIQ3p1MG9CTDVhbUp4M05mZy03TUNmMXRSUjBfdXM4ZGJ4bnZhTDY4dURQenVsTHpsaVRTZGk2TTNqMEVBM3h6bW8zRU5fdkhLaWQ3TW5zQXBPdHpvZm9VcTVRMThmVGQwMHR0WUxYSjdYQk8wbXhnRGJXY3ZFdG1SeFliMg?oc=5) (Wed, 28 Oct 2026 02:10:58 GMT)
- [Canada Begins 60-Day Consultation on Stablecoin Regulations, Aligning with U.S. GENIUS Act - Crowdfund Insider](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNV0hnYkxVSXgyNXVodnczWTR0UWptTnQwcFc1MHhWaUtWaWV3X3NrcmRQUHdFeWcyYlJfMjRRVHdrNHRsbUxJYmdOQmlLS2ZHQnNiUzhDRUQ5dFFMTDlQNVRzbXBrazNub2NYeHVhQ3lIbUxlOG1BcmM4Rkk0ZlA2bllfekVhSEI2WUQwX2lkLUpWeTZEWU41QldIeUlod2lCMEdaTkRzU1NQR0NFUkxUZzAxaGFkM3EwRG14ZjM4RmlfM1V6aUU2YjJ1TU52QUEzNnBF?oc=5) (Wed, 28 Oct 2026 01:35:46 GMT)
- [Coinbase Converts GYEN Balances to USDC as Stablecoin Winds Down - TradingView](https://news.google.com/rss/articles/CBMivwFBVV95cUxQV29vdDRMMURBMEJPMGlGUUNSOERYSjhvLXJmNjd0Vy1kR2RlRDYzbV9YdkJxVHVVeTBOODI2MzFBQThJYlM3QWdaMFZ6WEFNdmpwMXowcWtWZ2lFNHVEem1VWTdMWExvdHRZWUpBV1l6QzZsQW42QVZwMEpyejVtLWtZV2J5Y0xIV1d2TEpHU1A1VzJQZGVLNGk2MWw0cV95c3Nicy1FQ3pEc3ZiVmZFeHdUSDVWZEZadXRKTnFGUQ?oc=5) (Wed, 28 Oct 2026 01:00:00 GMT)
- [Refund Approved, Transfer Pending: The Second Risk in Stablecoin Payments - KoreaTechDesk](https://news.google.com/rss/articles/CBMijgFBVV95cUxPVUs0ZnZhQ2tMNk11V2YzNklfaUFGT0VlTWlGVlZlY2VtdVNxME5oQnNNRy1Qd21oZ2xmTVZWdlVIWTZoMzlOelZySzFrNmhma1BxbExPVUNkSm1JV3k3N2Fmc3lsMVpwb2dWYTFwX2hwTEFnYzJoN2pjdHI5NVViaEh6azhRNzlEUGsySTFn?oc=5) (Wed, 28 Oct 2026 00:30:26 GMT)
- [HSBC bets on retail base to drive stablecoin adoption - Asian Banking &amp; Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOQl9KRWtRRUJrYWNta2hEcEp3MW1pMTkxd0ZYMVJEZF80OUlxbEYyUEpfZENoMU9IZTdyZFY3SWNkbG5jZi05ZmdGLXVORFdkMmdQLXZpN2N6RHlWdnU5OUlKeFFEQzNlV3YwbDlaOG1MNXRuNHJmZ0l6QV9NWHN6ZVZTbGRMQ2xGd1BfS0RsSmw1OXZVOUs2M3cwNmZGVUdaYjVRSFEtM1huQQ?oc=5) (Tue, 27 Oct 2026 21:30:00 GMT)

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
