# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-19 01:53:08 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,492,534,085** | 🟢 +0.02% | 🔴 -0.44% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [US regulators miss GENIUS Act&#x27;s one-year deadline for final stablecoin rules - The Block](https://news.google.com/rss/articles/CBMitgFBVV95cUxOUm5VY2ZaaTNYRnJnM1IzOWZMd2VtaEZpR1F4c1RDaF9SeDVQZjNtaG1EUFdRU1FUQ01IdWNXNXJ1SmhfRTVjSHZKT3JqZ0cya1RiQ0dvNzEwVzBBQjAtLTI0S0lBWjlXNDFwQURaWVlHcWpNa3ZUMGZGVURyeXVMNUotQVRKT21BWTFZdGJ0YjduajNQNjZ6QnlCY3JUdGVQenlDbjNqUGczeVV3TzVIQmpnMkhrQQ?oc=5) (Sat, 18 Jul 2026 22:04:40 GMT)
- [Circle: Rival Stablecoin Launches Don&#x27;t Make This A Zero-Sum Game - Seeking Alpha](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQdTI4ZnM5alp6NThSOWtmUHlQQlVTSXRJX1Zac0ZXVFh3NkZCX0pMZFAxdHZOa2lxX1V3YndBV1pWYlZiczh4NzFxVjZEQzA5TGFUdGlHREUwRzV5QmxUVXVMUmQxS1FKNEx3ZzVHd3dOYWJVQ0NGM0xyWUNNakxVVWxlcEgtS1U1a2tNYlVmV1RINkRHYmJJS0x4aURvTnB3b2VhX1ZFelBfQQ?oc=5) (Sat, 18 Jul 2026 12:00:00 GMT)
- [One year later, GENIUS Act just made stablecoins easier to sell - CryptoSlate](https://news.google.com/rss/articles/CBMikAFBVV95cUxObXFCUFpTZXQ2VXBqYnQ5bkZvMHdMWk5SVEo5bU1lX3RQaDFLbldTdVBOV3F1N3JFY1ZVMGNHWkpQQmFJM05kOFhnU1g5UWVHTE1wcHo3Ty1ROXFVeDJqczlWdkl6eEN3R1l3dHE1V01CMjUyaE03SGN4aVdWN0NOYThsMGdrTzl4UjV0eW1lVFk?oc=5) (Sat, 18 Jul 2026 11:20:01 GMT)
- [Paradigm Files Comment Letter on the NCUA’s GENIUS Act Stablecoin Rulemaking - paradigm.xyz](https://news.google.com/rss/articles/CBMirAFBVV95cUxOQm9PY3ZXaG1CLXZyUmpZZTdfNHlGSTYyQnlESkNieVN5WWN3Y1c1S1MxeU4tYUJHOTRLUnlwWWg2djh5RERTUXM2aUpBU2Z5WHMzc09RX3VOdC1aQWV2ZnRtdlpKeEJnNnZha2t3anNFWGRQV3BQbS1mN3JRRHJUUGxnTmNET0RYblczOGFrN1ozcXI4dzRtMUNiRmItU0VndXFGQi1RLW15c0tp?oc=5) (Sat, 18 Jul 2026 01:00:00 GMT)
- [Piero Cipollone rattles Coinbase and Circle with stablecoin warning - Crypto News](https://news.google.com/rss/articles/CBMigAFBVV95cUxNVWhxYU5WMXNJb0dmdDVnZmlINVBlbmlQVnNQa2JIdGhweklWZi0yTGI4TFdsRTBVeU11S2NmTUx3MzhMa3B3RHJXelhqRGVLUWtNSXVoNDdaZ1J2emVNcjBNeUEwd2p5RnU0TkFnVHZOUFRtbVdzQlVHMmtwdnJ5Ng?oc=5) (Fri, 17 Jul 2026 21:25:43 GMT)

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
