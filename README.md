# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-22 01:24:58 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$298,719,957,565** | 🟢 +0.06% | 🟢 +0.07% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [The CLARITY Act's Biggest Obstacle Just Fell. Four Steps Still Remain. - FinTech Weekly](https://news.google.com/rss/articles/CBMirgFBVV95cUxNQ1BaaUMwSzIxT2VLWGdUc3JCRnNSSUYtY1V5RmVWVUlwV0pXbnByb21VQ2NHVmV4c1NGRHMyb1ZJSG53bllNaVFObGJpWHM4ekFIYng2eTBuZzdBUUhtX3lfSWJrVl8yUmIyeGlwSmhXZW1HSENhejZ4YmdUQ1FRSDVfUzFKVEtMSWk4R0JZNjhBWl82Q2JwYkQzcWhsVVJRR25CdHIyeHNqNHlXeUE?oc=5) (Sat, 21 Mar 2026 19:13:00 GMT)
- [U.S. senators reached an agreement with the White House on stablecoin yields - incrypted](https://news.google.com/rss/articles/CBMilAFBVV95cUxNRVl1Ukl6UUIwZTdlSmNQNkV4dnVFdG00Vkc3aVQ1bTc2LUl6TzY4NzlGV3lxMkVvM3poaUltTU9FQUJpV1VSVEZubUdtRmV6MXJTMGdKN2RiajlSVng5cGpoM2o4enJlU2ZtUVJyRVQyd1o3ekdJSDVRMnBBS3dHU01Ka0JBUEU2MTZXMjdwZDlmODcw?oc=5) (Sat, 21 Mar 2026 08:24:54 GMT)
- [Stablecoin yield is testing Asia Pacific regulators - East Asia Forum](https://news.google.com/rss/articles/CBMikwFBVV95cUxObWlzVlFMR2xTSGxYTFpZX3h6ZnhHZW16Wk5WLUZ4NTYzN0I3VHdPbEZJa0FVWGtCUTNrSkRfRzFOaVNteVFFamN4djBJMlZXWFZVQlMxU3NzU1A2a2VyWk5XME1Hcl9hSDFWTU5Ddk9Ka2FwNkc0Y0tQeWZzanVUeHJ1bzlaU0tjY185Q3pjOFcwdkU?oc=5) (Fri, 20 Mar 2026 23:00:00 GMT)
- [OCC Leaves Itself Flexibility On Stablecoin Yield Question - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5TaVZidFpUQUxac3ctczZ6Mk1udTh2LVYzSG5tUWZkdnNaMXVmTjJCQjFrTzdoQzg1OEhpbWZ0VlJYSUo0TVN6bWREYngweXJYcGc5VGhn0gFWQVVfeXFMTlNpVmJ0WlRBTFpzdy1zNnoyTW51OHYtVjNIbm1RZmR2c1oxdWZOMkJCMWtPN2hDODU4SGltZnRWUlhJSjRNU3ptZERieDB5clhwZzlUaGc?oc=5) (Fri, 20 Mar 2026 22:37:00 GMT)
- [Lawmakers reach breakthrough with 'agreement in principle' over stablecoin yield in sweeping crypto bill - The Block](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQclZTb2R5dC1POE9yNTFDYVJhZVowTy0ya2tqdVZOdjRzc19aM3BFS2pIMlJiREQ2U1EySTVaM05aV1JVdm5seTFXSlZjU1dJU0cyQ2h1QVJINWIyREpRZTByRU1sazZjcTdLTTU5eXpFMGVKYS13VmdIVldSOTZwYV9EZ0xfS1k5Nl9sTXJ4UU13U192b25zbWpwbGo1cDFtYTVaU01nX1E5endyUEotZnlReVJvMTJGVURN?oc=5) (Fri, 20 Mar 2026 20:02:41 GMT)

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
