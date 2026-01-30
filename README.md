# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-01-30 01:16:57 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,003,641,720** | 🔴 -0.52% | 🔴 -1.02% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoins: A quiet revolution in finance - bondvigilantes.com](https://news.google.com/rss/articles/CBMiigFBVV95cUxNQVltZVhJZEdGc1c0bFRmWjIwUmFneS1wSlNVa0syTVE1ZTlsckw0MTFvYnNEUHdYRDNBSXlIRVVrQ1JUdVRReFlsVURmX0Y2bHozVlFyV21aZDB3Rm1Tak1yLUQyVFdzR0tlbGJwOFUyQktiMlR1T0JoUjZ6S25jeVRlRkpSQWRlaFE?oc=5) (Fri, 23 Jan 2026 12:13:37 GMT)
- [US banks may lose $500 billion to stablecoins by 2028, Standard Chartered warns - Reuters](https://news.google.com/rss/articles/CBMi5AFBVV95cUxPYWhPOTRzLWN4T0tBV3BQMFFmODhZbzlVa2JZZzdDcE1mNjFydDd6Nnc5YkNUU0hiUGNvWi1kZWdIMDBJaWFnQURoMGl5dVYwdDlUSUlUemVYN29yTUxaUW1mcWROeDZ2MHZVTEg3dy1sRl9RWXhsSkJnbFN2N1F6Mm5GenJmN09XRldfV1FLUE9IRHZNSW1KRG01Vmlhdlhpa1IxRGNuTm80QWxHVFJlVE9Sd242QXlMR1k3NHpnVktIVzgxZmY5ZVppSVBCZGhnbjMwWUlMR201M3BGRmVOcklOYWs?oc=5) (Wed, 28 Jan 2026 16:10:11 GMT)
- [Fidelity to Launch US Dollar-Backed Stablecoin Designed to Support Investors - PYMNTS.com](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPT1djT0VQQVd5WHU5ZFk1TzJMbUVkbkJUT1ltYUdXQWxzSjZjTDB3QjJQV29yN3FJZlRYMmNMUFFaSjgtTlczZld0cGduSFhpTl81MFJyWXZ3UGp1elhCRTd3aG9pUllobkZraG5ZTF91akE0S29qWHpldXRXWkoxWDNqY1JKbEJmV3VqSFRkTDFDa0V2WThmNWZzMjBDNHBBbzF0S2ZrNS1yM0w5TzlxVG5tMmFTbWNXbHM0TU81aUU1Vlk?oc=5) (Wed, 28 Jan 2026 17:23:04 GMT)
- [Fidelity Investments to Launch Stablecoin In Coming Weeks - Bloomberg.com](https://news.google.com/rss/articles/CBMirAFBVV95cUxQcjI1dXdOSkFXT1FPaFNCeS1IZld5d1ZsV3Vwd19Pa3JfOE9WOG1oTzNTTG5mZWR6TDIwbWNyZzNHUjJ3SmJURkU3TXVGZlpXVnVnQWNKeVFMbDVRazVaMlhwYmZySTVuMTBrclFxM0VSazZEOGN3WUswZXpMNDk5anVpS2pOWUFfd1ZXNlFpWnRvLXd6d2xZbjM4UnNxclE3TldlY28tVUwwZkNq?oc=5) (Wed, 28 Jan 2026 13:30:00 GMT)
- [UAE central bank–sanctioned US dollar stablecoin launches to boost digital-asset settlement - The Block](https://news.google.com/rss/articles/CBMiugFBVV95cUxQZ1QzaUpQNVhfcWdHUnJGOHJ4cjVvZnpYejVUYUVoc193OUZnLTlES3lsZEduc0l6ZjY1WVI3aVFwWkljSXJLZEFWZ1lYX3A2VHBYZ1BvZEs5aG5zY3pwMlByOWRKbzQ3ZzIyeEVRcl9UUGZlcFl0ZmViUDZvQjBfcHA4Um9HdG5OQkdaN3RkeTh3MjY5Q2x6aXBhby0ybEN0eDBVX2l4aEpKc3NYRm1uaHluLVN6VTh3alE?oc=5) (Thu, 29 Jan 2026 06:00:00 GMT)

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
