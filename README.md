# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-11 02:26:29 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$301,013,726,712** | 🟢 +0.03% | 🟢 +0.24% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [FDIC and OCC Both Want to Be Stablecoins’ New Boss - PYMNTS.com](https://news.google.com/rss/articles/CBMimAFBVV95cUxNVVA1SmlGNmg0RUpjNTVSUmJIdFY4T1QyOHdEOUY1SUVUMW5BN1hOblB5cEZfQmprRGhYMWM4UXNFcGpuekVxRmNiLUZIM2ZrVFpJS1AyOVBjbWs2TVlfU0FodlpxTjc1a0oyVHB3VllWMjVJdnk2ZlBkeV9SU2VZMXVoc0MxRURlVW5MUmttMWRaYzJQMS1NZw?oc=5) (Mon, 11 May 2026 01:38:07 GMT)
- [Stablecoin Firm Circle Reports Earnings On Monday. AI Will Be In Focus - Barron&#x27;s](https://news.google.com/rss/articles/CBMisgFBVV95cUxNYXBYRm5DSVNycmZRcDdMeVM5X2dBaUNMMGNtX3ZWTW4yZHB1Y2NkN2JTVG5FWHozODNxemI4UTUtcms4cmhYTDlCMV91bHhGZDBzQ1E2aUw3NEM4SHJRWE5CZFVYMTBWYkFVUTJrS0gyR2JfUXVSalNqdG1FX09lb1NiWm5yeWVIQ3JjangwSE5VY3lRV0FDWm4tMkt1MmxRS3Jhdk5PSzZMeGdpb3poYVln?oc=5) (Sun, 10 May 2026 20:15:00 GMT)
- [Cutting Through The Stablecoin Noise—What Credit Unions Actually Need To Know Now - CU Today](https://news.google.com/rss/articles/CBMiugFBVV95cUxNS3VpV3VLVEd0YlJBU3ZPcHFHdU9WX2RBSzZJZjBad2tHdGxBaXJ4YnZHOUpUMkQwYUdYampYY0d5TzVCUC1nRmFMLWZ3NHk5ZEdWTUI5bVpmTGZVYlc0NDEtSEdRX0c1a3VIekYweDJXWmo1d3VjVTViRkVJaWNBSERwa2hTZEhJS01xQzBrSXJiMzFFWTlCLU1ZMXVFMXZRTzdQZUhXcnBTMEtCQ1ZPckt6cmpsOFQ2MXc?oc=5) (Sun, 10 May 2026 13:28:42 GMT)
- [Bank of Canada Says Stablecoin Rules Could Arrive Later in 2027 - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxOUWR1X216M0ozb0NuaUhHV3Fzc3VoZXFod05xMV85THlaclptcGFyNkpNWl9QUGxpcXVaaEdLcTNhMThGb3prSUlmTllfMWxROFhtSEV2S0NXZF8zWEhnV05ybzVrZTNwN01aeTJhU1phOVlXRHpXdWdTcHE1ODZHeGpZMnYwaVltN3Y3SWJzdDN0X0VoV3owTk9TVTR0cEk?oc=5) (Sun, 10 May 2026 04:28:00 GMT)
- [Banking groups and crypto advocates clash over stablecoin rewards in Senate bill - Investing.com](https://news.google.com/rss/articles/CBMi1gFBVV95cUxORFFZRVpxampiQ1RVYkNoZHNxaFRnbS10bjhXSEdXN2EzWTRxc3AwZS1raEoxbXhFUDRrdFJ0N0FXcDlMNjRCaWo1c0JfMHU5SmQ3WjJyMmFSdkp0SGc3TnI5WU8xQ2VFZVQ1WnN1SlhMYlhPS0Zzc0pNNUlUdWVUeTlxbGZTZEUwaEhyTUc1c3phMXhFLW5wZ1pZWTB2RTZjWW51N19hRWwtWE9IOFBIQ2F0T3N4V0t3QWhNSGRWbm1pTjFnTlZqRFZZNU5JZElzMDBvVkVB?oc=5) (Sun, 10 May 2026 02:03:52 GMT)

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
