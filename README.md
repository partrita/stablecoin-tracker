# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-22 02:35:46 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,548,378,213** | 🟢 +0.20% | 🟢 +0.08% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Singapore&#x27;s Stablecoin Regulatory Regime - Simmons &amp; Simmons](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPUUExamIyY05WTHlXZEJmdTdYV2RBcnJROEFqV0hubEcwaE5VelR3OC1wcFktLWI5RDlPMVM4RnFaeE9JUHFQOFlpc2dEdmZLTlhwZ1FjcFJETEM5MDRzd1RUWnFiWEpXeTBLWjVndjVST185MVB4dFhxOW5zcURJS3NXYjBzTlNjZFhhQWpRSzVacFM5UFQzRGJTWENtRWdoaks3c3JvUmh6dmdGRXNqcTlBVmhIbXFWT0JiNk5iSFNUQWs?oc=5) (Tue, 22 Sep 2026 00:18:46 GMT)
- [BANKING OPERATIONS—OCC conditionally approves three more national trust bank charters - VitalLaw.com](https://news.google.com/rss/articles/CBMi6AFBVV95cUxPT09TR2lqdWlDQmJYTnJOY0hnVmQ1MFBpOEo5TzlPT0ZRdkQtQzFORlVldkR4Zm5qRjJuZUkwSkZjSTR0Y0F1azF6MEgwUkVPSGR3SE02cGpYYVFfUEw1Z2lrWnlyRzZzQlBGMi1QTW51ZzlsYkYtb3l4NTM4eU1zenNJa1I1dnVzMklfSWt5UXZSLTNYVW52MmhianlCQUJyMGlBZWdJS196eEZGZllNTUlfTjU5RXZDVTRqOV9SeExOVDcyMEFqZWFnVWhSQzVadnB1R2g2NXVLM3V1emR5d1NsRFJwcC1v?oc=5) (Mon, 21 Sep 2026 22:57:10 GMT)
- [The ECB Just Launched a Way to Settle Tokenized Assets Without Stablecoins. What It Means for RLUSD and XRP in Europe. - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxNQkFNZWNwX0Ewc0x6elgwdE9YNkc5Q1J6Q3JEdXlBbE84RUYtYmgyV2Rsb2FwUkNqZGVRVjc3TGt2X3FxVGRPYWdNMnFqT1paVzlfNmVUVlNHT053a29zbkNUc2N0WUF3YmhCU2dVY2MwbktCeFg4OHFCN1RsVmR0NnZuel9FM1U2UUJpVkV4UHFxbjBCVUdmMg?oc=5) (Mon, 21 Sep 2026 21:54:43 GMT)
- [The ECB Just Launched a Way to Settle Tokenized Assets Without Stablecoins. What It Means for RLUSD and XRP in Europe. - 247wallst.com](https://news.google.com/rss/articles/CBMihgJBVV95cUxQMTRNS2hkb1hqTXlVclZkTFQxdG0yM29kTGRSS3ItcElud3ZIRXpFUS1iT3hxNlBMX3gyNUw4MjNNSTR1SUstUFRsZGM2LVlwVVJUeGM5STRKNjJZNGdreDF4V21IUEtOVE5STDdwTUhFSHhYWkhJX1I4TzBudjRfWHdoOFJlNFVCb1RiUVBqM055SXpOYUdaaGpJcTR1VmtQNUliQ3FlZHFNZEpoM1hEdS1uUlFQQ09xcXEyRTdOU1gtVVJtSUhvcEp3RXliR2g3TmRWdEI1aTdmNmZUb2ZGSExOVHhiY1VpNVNYTnZaQS1XNy1kRngzQW5NYThHTC1yLTVEbWtB?oc=5) (Mon, 21 Sep 2026 21:54:00 GMT)
- [Arc enables Bitcoin liquidity with cirBTC in its stablecoin ecosystem - TradingView](https://news.google.com/rss/articles/CBMizwFBVV95cUxOLVcwc21vdV94YjZFMThOLXZkemhKcXBHRnUyRFZiS0llczJ6ejFwWWs3NkJ5SmZFeGoyTWU3NTlQVXFjZ25GZXM0bFR6N0tMNXQ1Y2ZlMDVwMjJ6REF1Z1BmU093akNQMDVyb1VVMlhaRlNMMTlYRHhQSV9WSHY1ZWgtY2I5ZThXWDdaRk1SWkRrOFdlMXBoT2dibnpwOWdNYU5ZSTZtd3phVW04ZmxlbTdvRHkyYTdfNDZPVnhWZzFoNk9aWndTSllaSzFaeVk?oc=5) (Mon, 21 Sep 2026 16:50:50 GMT)

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
