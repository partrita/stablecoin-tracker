# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-15 01:47:04 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$299,458,363,729** | 🟢 +0.29% | 🟢 +0.72% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Delaware Eyes Stablecoin Edge With Banking Law Overhaul - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTFAzMEc4a2NudUhqZWZDbEdMck1EN0NwU1pOQkhsTHVxQjJWanpzLWZGNXFwaElLRm8tblRTNWJnckhscWJSdXU4X1E5YVlIa21JaXFEaVhR0gFWQVVfeXFMUDMwRzhrY251SGplZkNsR0xyTUQ3Q3BTWk5CSGxMdXFCMlZqenMtZkY1cXBoSUtGby1uVFM1YmdySGxxYlJ1dThfUTlhWUhrbUlpcURpWFE?oc=5) (Tue, 14 Apr 2026 20:29:00 GMT)
- [Stablecoins remain little used for payments - Payments Dive](https://news.google.com/rss/articles/CBMijgFBVV95cUxPckJZaG44RkNtWlFBdHRobDhIUFQxdXRyNFJ2TXZvMkt0TnRJN3ptcm5tZlZ0NlZxUlpwR3dJVFNJRWlkWHZfRm8xS0VLVjFZZjB5ZXptSWd4U1hhcDc5QXpUYWdWY3pPV0pkQnR0UndlNnlKRFNxa2JLaVZhMEQwcUtTOWs0OHJFUE5pV1hn?oc=5) (Tue, 14 Apr 2026 16:23:41 GMT)
- [PPI Responds to CEA Report on Stablecoin Yield and Bank Lending - Progressive Policy Institute](https://news.google.com/rss/articles/CBMinwFBVV95cUxOdEpwbUM5cGdoc284UzBBaTZKdTFrR0RydS1SXzhrNnp6ajJxTElEeDZHQkdEWnFIdC1qQXpKWjR6TzR4WnUyZmNvZU9neV9SbnAyelpBbmJtWlRBQXBuX3BieGVhQkhuU2VpR1VBZ05wNmd6ZjZaRG9OUVRYSnBHS19TUGpFQlo5ZlE2d0N0TEVyRkdEQy1EMll2VF9rZWc?oc=5) (Tue, 14 Apr 2026 15:55:45 GMT)
- [Crypto regulatory affairs: US Treasury proposes secondary market sanctions compliance for stablecoin issuers - Elliptic](https://news.google.com/rss/articles/CBMimwFBVV95cUxPOWtwbkwzaUpFZHBidmU1aEFMZmg4ZTVFY3dxVVBoZlFKcjU5RWx5RHpuZVJDSWxnaUxKYWJ0Wjg4WWJwYWZkRFRKeXJJMm90M1VRa0VSUXdJRG0xOG90X202S1FwaWRlVTNXbjZOOHZ6NmpkSlk0WkxXOVU5RG5MS21pT3hoNk1PcHYxNF9WYUZGYV9ab3F1RkhFZw?oc=5) (Tue, 14 Apr 2026 15:01:56 GMT)
- [Treasury Issues NPRM on State Oversight of Stablecoin Issuers Under the GENIUS Act - Consumer Finance Monitor](https://news.google.com/rss/articles/CBMizgFBVV95cUxNRUpDd1ZDWlRLNVloOEQyWHhoWkxiZF9PcGpZbjY0cDdxQ1FQT2FGcDBNRlZYM1NyTEtPbG1aczFXVWxRSGFfb29ReTNVTkw3cW5WNkFQSXJnQWh5c3JBTWVsWVVEUVlwQkJodjBwQTB2bFk5QTF2NkZhbEV3YXBpUm1KcDVwZzBXTExXNFEwQXZCcDNMaEkyQ3U2b3lhX004Q3N0ME9MXzRCRml0b1JwVktvTk5RbHBtYnNMMnkweDJETU83RU1idWRWLUlKQQ?oc=5) (Tue, 14 Apr 2026 14:56:50 GMT)

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
