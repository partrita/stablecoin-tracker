# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-18 01:29:12 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,650,380,725** | 🔴 -49.87% | 🔴 -66.42% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Merkley, Warren, Van Hollen, Sanders Probe Trump-Backed Board of Peace’s Plan to Rebuild Gaza with Shady Cryptocurrency - Merkley (.gov)](https://news.google.com/rss/articles/CBMi4AFBVV95cUxPajhZQk0teGJjalpIOTJ5S0tqVGliMExLeXdwVm8tZEc5a2tOQWFDUmluRlhxVG51dFdHNHkxY0RqeXVNYXBoRTVlMllnaXpfdkxFeUFlN1hseTRaUnhqODNHSG8xcGNWaDdha0VPUEhpWEtqZGljSFFiWEl5Ni1RTXdlVkxFaFNLZ1lSdkhwdzROR3BlRVdQU1hha0VTSldUdUtFeWdEVmktaURfRkgyaHFWUVFYN1MtQUU5YWlORUUtRndIU3FpQ3IzRjZxb21fTUplYk9BZEpqSUQ1YXRDWQ?oc=5) (Fri, 17 Apr 2026 22:19:55 GMT)
- [FASB cautiously advances new stablecoin guidance - CFO Dive](https://news.google.com/rss/articles/CBMinAFBVV95cUxObFlwUF81NkJFQXF2eE1obXQ3bFJueEY5TjVpTmtoeFNOZ1h1RHFKVzh3WmxjYi1UcEg1bzRHeHZuQXFRYW55dTRha3lfUm95Z2VsbzFieHU4UVJoYkJsSmpzdVRPdGtRTGRxUUMydEZfVGlHa2dxQmsyS2xaOTZncDA2SkllbV9kb1FZZ1RFRThqTHJnN3hnNmNmMmo?oc=5) (Fri, 17 Apr 2026 21:00:26 GMT)
- [France Urges Euro Stablecoins to Break Dollar Dependency - PYMNTS.com](https://news.google.com/rss/articles/CBMiogFBVV95cUxOMnVFRjg5enpwakxObXppUm01R3hzZHNwbGlUWlpNWUlRdG95RW9uTG03MVp3YjREcHNsajc1eGdXN1RhUC02VElBanNhSWpWYXFoZmlUOC1ucTh4and0OGhjTVB5Q1Y2b0JhdlFWcVI1Qlo4bkotLUt0a2U5STRMdDZXWm85X1JBRk5Ob3RqSFJoV040S0Zjb3Q1UDEwMDlHV0E?oc=5) (Fri, 17 Apr 2026 19:00:09 GMT)
- [FASB Tentatively Decides to Expand Digital Asset Guidance, Including Stablecoin Cash-Equivalent Examples - CBIZ](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOMDU2eWNRckZvUktqSDg4VWdWR2wzWVMtcVhkZWY5N0lxV0J4QXhwQks5UGVucUNUaERWeDJOVjAyQzBjUlNlbV8tcGtuS2VwTkY5RDlheG12dkVxMndUbmRQcHBndHlrMDZndE94S2M1N1VEV1VxZ3pqYmVabW45dUZnVkdncVJ2NTZaX2lPMnBCV2J4QWNYUGNPa1dGOUpwbDJrV0k4N2hSdTE3WGxpOVBXTWdJY1VxZExubDA4aUFDSTFpdXl6YjNwTXdVcjhJZkJBSFFpcnI?oc=5) (Fri, 17 Apr 2026 18:51:44 GMT)
- [What CFOs Need to Know About Freezing and Burning Stablecoins - PYMNTS.com](https://news.google.com/rss/articles/CBMiowFBVV95cUxPTnlkUFJtUzVTN0c3aEdYS1JTbXVwb2ROUWpSdmVfMnM1ejdXbWttYlMtZVNZZ29uQjVialdMMy1UMmF6Ui1TaUh1dzBxMVUtTzJZd1ZZX0Z5MmtCWUhFWlpOSFFyRXExNW1KamgzZHJGZ0NLNEIzblRtS2N4eXZFbGZBa1BoejNna0ZVTG1TazRoSDlwQjhBYkYxeXlzT3owOFk4?oc=5) (Fri, 17 Apr 2026 17:15:08 GMT)

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
