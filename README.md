# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-26 02:44:44 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,900,391,558** | 🟢 +0.08% | 🟢 +0.68% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Feds&#x27; Stablecoin Review Committee Rules On The Horizon - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1xbU1aSTNRU2pneFNNWDRTZlA5dDdodU5ZYWlpd0YwR1QteGFxSU91VGJZMGJmQUpZR2dhcXFxVUtjNjhSUXhOcjdJcTFTYVgxTlg0eWJR0gFWQVVfeXFMTXFtTVpJM1FTamd4U01YNFNmUDl0N2h1TllhaWl3RjBHVC14YXFJT3VUYlkwYmZBSllHZ2FxcXFVS2M2OFJReE5yN0lxMVNhWDFOWDR5YlE?oc=5) (Sat, 26 Sep 2026 00:04:00 GMT)
- [FINANCIAL TECHNOLOGY—Fed seeks comment on GENIUS Act framework for stablecoin issuers it supervises - VitalLaw.com](https://news.google.com/rss/articles/CBMi-wFBVV95cUxNQ1hfaGxJZW9jWnZUd0lwdXpKSGhmM0cwQTdVZzloYU1aY0hsUW1FWUtjbFpxNzg4aWZ1ZWZqV2I1N0JwM0Q5cEpCbnVuendwRm9qRXh1ZUQtTEdRZlU4TkJmWF9hYnE0V0tGcUJjcHVSeTNVT1BxYzN2SzFINUVsQVlzN2dIelRsQkJhM3laNTNnQWVkSlZJajhWVFNGUWNvdHhjcE1IdXJMNFNOTlRBYks3STVYUGpfZFAxa0ItNXVqbXVCV3FfbEJ6czh6SzkwMlhUeEgybXZZRVV2LWtwaHB4VGJKMW1XcFkyLVg0bVVSNUUwZ1RjTlVSNA?oc=5) (Fri, 25 Sep 2026 22:45:59 GMT)
- [Stablecoin firm Circle finance chief Fox-Geen to step down - Reuters](https://news.google.com/rss/articles/CBMisAFBVV95cUxQVGVzOHhoSzBMYlFJN2Z6WmxsRkk3NS1LWnpBVzNJRnpyRUFibVR4TVY5OEdMb3NIaTVsc0RXenVUbGl5VnZONFAta2RnVndEbWp3NDVSVDN1aGFlTTY1Ymp2MXYyOTlmLVRHVDJGRFFQSV9yOTJqUllYR0p6a2RkOFNxOWtDN3JfTXZkbjNhTkFaYnpIcjdKVGkyQ3RkZVBhaHprbEJKS1h2U2o4VE9XOQ?oc=5) (Fri, 25 Sep 2026 22:34:37 GMT)
- [Department of Justice Seizes Stablecoin Tether’s Bank Accounts - Futurism](https://news.google.com/rss/articles/CBMickFVX3lxTE9IeEsyUHR0eWVKNDVYUDFYWUhRQUUxb0lkU292OXJZWkk4cFFjbXEyT2VZU0FUdU1SRkViS2l5akZjeTJxb3hSYzk2QnFyNXNMZXVZbGZZVm9PLWUyYzB6bzRTbmNLSjZVclBZNkY0RkxqUQ?oc=5) (Fri, 25 Sep 2026 21:34:41 GMT)
- [ARK Adds Fund On The Blockchain. Fed Proposes Stablecoin Rules. - Investor&#x27;s Business Daily](https://news.google.com/rss/articles/CBMizAFBVV95cUxQd0YyLUFKb25CbmNrYi04Z0JMTk93YlVJdTRyeXhFSDZtYTlCNUk0ZnpQNVVZZEVPQXR5aUFVaTBpUjRFbjhQd1pMbktDMEI3YlBsLUJPeEVlX1dIY3U1S0ctbDh0WFJGeTd6d2tWY2xwUW44YjczVG4ySkZVVmZ1eXhTZmlEZTAyVTBITUJfRFJCVC0tU1E5T3Z1bHVxbFhrSUFmRV9FWWRnXzVMRFpZTXRKbFZkM3Z6NEo0YUFybWVLcVdHNFl0X2ltSFQ?oc=5) (Fri, 25 Sep 2026 20:19:00 GMT)

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
