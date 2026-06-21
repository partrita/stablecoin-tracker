# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-21 02:52:50 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,580,251,633** | 🟢 +0.03% | 🟢 +0.05% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Circle (CRCL) Faces New Fed Stablecoin Rules As USDC Oversight Tightens - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxNLVJqcElTejBDeEJVUnFaeE9QTC1URVpLMkl2RVU5cWI2enh5XzhOOHNNelJxdXRZNDNZSkEtM204MU14djNFaVMwbC1ZWTdEWHZzN1pkblBWcFk2TDNCWno4MGtlcDh1MEpIUDJmaGhYNFAyRU1YaERtZFpCZ1hEMnh1emhDMDNzVnlkN0V0S1EweGZ4VkxVM1FyUmR2QQ?oc=5) (Sun, 21 Jun 2026 01:09:00 GMT)
- [Main Street msUSD Stablecoin Loses Dollar Peg and Crashes 90% - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxPbnhDVmVzcW5vN1RXbFNPS2VaVERpZFVXbktUZXA4R2NmSUJQbU5MRldyN2xVcWVPWTVKRXF2X2lGMVhIa3VSOG51UW5ZWGJ5b3FLbGZIQWZEcENYdGRkcEpSeEJSNUVtSkVueXM3aU5LVEFHMGl6bWFRYkxTX0hIdk5fVGdWaEx2OVpJOHMzU1dFTktTTUlzZ3ZTektPUTR6?oc=5) (Sat, 20 Jun 2026 20:12:16 GMT)
- [Stablecoin bill passes House with bipartisan support - The North State Journal](https://news.google.com/rss/articles/CBMilgFBVV95cUxNc0RwaDNOd2ZzVnk5Ry16eEFidTQzd0VDUkY3NDFYdXJkZDlFeTMtbDl6cTd6Mk9yclZkUTBCMHcxelRvUWZCWF8waVo3WERickNhM0RtdVV5Q1BIZ2hoNlhPcU51dEZ1TXQzVzJ6aEF4Z3JOTE1WeDY4UVNSSnZfUGh3MVdZc1BCTS02V2d3ZFEwdkdTMnc?oc=5) (Sat, 20 Jun 2026 11:55:24 GMT)
- [DFS builds on stablecoin framework - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxNcTVvT3hFc2xzUUZuMFN0aUkweXR3WFljczcyQTNLdC1BQVJtOWNYcUltTVZIYVB3bzVRWEdEcWxGVWwwUS1HaGFoVkI1YnNUZVJhWFlTdGcxV3VnanBncmQ1eWJWYmcyVi1xUU1OMXlOMjFKeThad0Y2RlhrX3NpdGJxSTNDRTF3SlozZHdyc1ZpdHpzdi1PUnB3NVA?oc=5) (Sat, 20 Jun 2026 11:36:00 GMT)
- [Stablecoin issuers face new customer verification requirements under the US GENIUS Act - Digital Watch Observatory](https://news.google.com/rss/articles/CBMigAFBVV95cUxQYkFSMDlmREV4LUFZQ1RORjJvZlZWN0ZvUVlOeXl3WnBxWlVFSWVhTmltRUFJY1hzdm02aFBiTGtrcEVOTmFkdWhDa0F1NTlpZEhaLVZabFc3QWRXamR4M3RWbmhRaklheUd0T2taQ1JLUVJWSjR4enFPazVGVHNrTg?oc=5) (Sat, 20 Jun 2026 10:00:00 GMT)

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
