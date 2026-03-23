# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-23 01:24:47 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$298,600,275,160** | 🔴 -0.04% | 🟢 +0.05% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [CLARITY Act Unblocked: Stablecoin Yield Compromise Reached - Disruption Banking](https://news.google.com/rss/articles/CBMipgFBVV95cUxORm5VNUE3bWc1VU9JMmliN0VUcDhtcGVjYXU2a3dlNDFjZUlrTm9PODZWZThWR0M5aDFsX0xvaDFfaWdJU0RwNWdzN2tJTV8xNVo3YzhBSHdkckZuXzdkVWsxQnB4dkdtejBQME1YZDZNZlpOaEhteVVIYmtvRVhHTXlJUTFPN1RSekcySEM0YmVpTWNzeUJtU204ZXRod1hHTXdGTk13?oc=5) (Sun, 22 Mar 2026 12:54:29 GMT)
- [Stablecoin-sceptic BIS exec set to become new South Korean central bank boss - dlnews.com](https://news.google.com/rss/articles/CBMivAFBVV95cUxQeE40RmFTWVZFdWFkX25HcEE2dXF5cHhvUC1Ja0VjZFpiLUl3UTc3cHdJb0dDWnBwUTE3NTl1Y3BmaUNiaW1tcHFsLWZKaVZ0eWRVZmdhTW5VOV9MenRBYXM1LVV2R1ZRQ0MzMEVtemNsbnZETDhPUUhpeThFVHhoUWdFSUpMTG9jeDVyTXZfNXR1U2laeXVYWkdKNzllb0FnZzhVeDBOX2lIeGw0dzBnVi1YWE9Oa2lRaEJfTA?oc=5) (Sun, 22 Mar 2026 12:43:50 GMT)
- [Senators, White House Near Clarity Act Stablecoin Deal - Bitbo](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1HLXptcThROC1uSnBpZi1ZZjBnMGR5dERxQXZ4RnNWZFdDTkpMVXlial9USXNGajdnblB5TjR2dWlKeEhlN0pDRlFGTnVlUFc4OTZWbXp6bU5mclFOdG5r?oc=5) (Sat, 21 Mar 2026 19:35:00 GMT)
- [The CLARITY Act's Biggest Obstacle Just Fell. Four Steps Still Remain. - FinTech Weekly](https://news.google.com/rss/articles/CBMirgFBVV95cUxNQ1BaaUMwSzIxT2VLWGdUc3JCRnNSSUYtY1V5RmVWVUlwV0pXbnByb21VQ2NHVmV4c1NGRHMyb1ZJSG53bllNaVFObGJpWHM4ekFIYng2eTBuZzdBUUhtX3lfSWJrVl8yUmIyeGlwSmhXZW1HSENhejZ4YmdUQ1FRSDVfUzFKVEtMSWk4R0JZNjhBWl82Q2JwYkQzcWhsVVJRR25CdHIyeHNqNHlXeUE?oc=5) (Sat, 21 Mar 2026 19:13:00 GMT)
- [U.S. senators reached an agreement with the White House on stablecoin yields - incrypted](https://news.google.com/rss/articles/CBMilAFBVV95cUxNRVl1Ukl6UUIwZTdlSmNQNkV4dnVFdG00Vkc3aVQ1bTc2LUl6TzY4NzlGV3lxMkVvM3poaUltTU9FQUJpV1VSVEZubUdtRmV6MXJTMGdKN2RiajlSVng5cGpoM2o4enJlU2ZtUVJyRVQyd1o3ekdJSDVRMnBBS3dHU01Ka0JBUEU2MTZXMjdwZDlmODcw?oc=5) (Sat, 21 Mar 2026 08:24:54 GMT)

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
