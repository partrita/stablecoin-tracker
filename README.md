# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-22 00:43:46 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$288,910,922,888** | 🟢 +0.35% | 🟢 +0.75% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [BPI and The Clearing House Association Comment on FinCEN’s Customer Identification Program Proposal for Permitted Payment Stablecoin Issuers - Bank Policy Institute](https://news.google.com/rss/articles/CBMi7AFBVV95cUxNZE85SDBDTk9EcFRkVFNNSEFFSi1qRXB0M05nQ2wxV1JLOEIzR3JoNkxTTFpLRHdqTGlBZEJjOHp0WHV0NzB0MmZUOHRpbmNVQ1hjbUhwOTFudjg2MVdMWUhNSF9oSW11R09XRHdNZVZsVHNnaWZLVWxhOVlhSU1TZTg3ZlpybHl3NXJTRFlIcVhhUlFBQXNOTUZTeUsyaGlGb2VUdXFMbHVYMWx0Z1djZTZzYTJ2Rk1XcS1wRFdfT2thSkRsTC1BSzh1Y0o2Um56bGRlR0NWSW5zYlRWa2pLM1BudWN5Zmk1THVNSA?oc=5) (Fri, 21 Aug 2026 22:35:23 GMT)
- [This Week in Stablecoins: Crypto That Never Touches the Customer - PYMNTS.com](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOT2VNNlNoVi1DTHFhUEo4ZnNreGhjVGk2dVBBXzRvQ3JjR1cxT21IUUxTUUNrWTl5RTVaNVhZaERFanhpYV9Ka2V3N1dRTEtmemp6RHA0T3hFT0ZmR0FERWZsWXJKd3h1Q3BwQXNJVmVqbjRpQjNNS0dPWU5HOGpsMUNpVGhhQTUwWnZiWF8zLTBrdUJ0TXVLRTRHX0c2el8wRjdkVjJGak1Sdmc?oc=5) (Fri, 21 Aug 2026 18:16:50 GMT)
- [GENIUS Act Establishes First Federal Stablecoin Framework - Legis1](https://news.google.com/rss/articles/CBMifkFVX3lxTFBENzhiY0RqNFUzYTNaMDdDQXgxT2s5UGRWd2huSXpQSXpQOXZBOU9yZlFWNWFCM3hzWVd3Z0stYnBKRlNaR0V4eEgtUTRwSFhEY1FZUXBYcWVhdXMtOENkdHFlRzRsdEY0enV4N05sWGZRdzdvWW96ZUx2NGdsUQ?oc=5) (Fri, 21 Aug 2026 18:08:06 GMT)
- [ReconArt Integrates Solana to Automate Stablecoin Remittance and Agentic Payments Reconciliation - FF News](https://news.google.com/rss/articles/CBMivAFBVV95cUxNaWh6aGVKcFBIUlk0SmFmTkVFWmtzdko2ak5nbTNTS18tUUliR2ItUjJYOUxZQksxbVdGQk9aN20ycE11NUJFQVB1M196Vl9jVjg3aWtfbmJ5ZmdFaXpBblZ1U1NGdVN0UldPallmSzVPSklhYXdUaXFrNFJwejNmT0lKUEdMOHpFbC1WM1FJRG42RWRFSld3SWVMWmk4UVNIOWFObEtvekthTW9LREJkb2VqdzExZnJKUFBldA?oc=5) (Fri, 21 Aug 2026 14:29:20 GMT)
- [The banking lobby’s bad faith campaign to kill the Clarity Act will backfire - Fortune](https://news.google.com/rss/articles/CBMiigFBVV95cUxPa0oybnhHYlJpc21GNDlQWC0wRU9mYnlvRWtzZ3VfSElnUkJ1NDRDTjhBc2hEcDkxNzBMY0N4LWViVmpEcGtnRWc1eHg4b1hSRjFrbUNNeWM5Q0RnbWtuMVNyVnZtTTctSjVDRVpTQXlWN0JEZUxKbElQcVY1VENRRUdIbGtKNU5aZlE?oc=5) (Fri, 21 Aug 2026 14:26:00 GMT)

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
