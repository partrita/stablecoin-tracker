# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-08 02:48:03 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$295,179,330,325** | 🟢 +0.04% | 🔴 -0.75% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Paymentology CTO Says Meta Program Shows Limits of Stablecoin Payouts - PYMNTS.com](https://news.google.com/rss/articles/CBMiswFBVV95cUxQVnNmM2UxMFRVNkJxQXFtRHpUT1lOU1R6RmxMTnFlTnhSVF8zWGptRXpGQXJRdl9CbWVBR0hYenpEOXNWVGJyYnpxUFdCaHJTQmVKSFhwUWVpMTFOM2VMd1JjQXg0ckVUVUVrcE5WSDhIVHg5OVR5d3hMb3ZtaTN2cU1YbXE5YktBbHJZMl80Ri1mUERjNUIzRktwb2o5UFBseXMxQlNuU1hSOFRmcjFBb0lwWQ?oc=5) (Sun, 07 Jun 2026 23:36:08 GMT)
- [WasabiCard Raises Nearly $10 Million In Pre-A Funding To Expand Stablecoin Payment Infrastructure - Pulse 2.0](https://news.google.com/rss/articles/CBMitwFBVV95cUxQaUI5U0tIWjF1bGxIbERYNWN0ZGFsTnlLNVRydHNzNmRHcThXOHVIU1BGVzItal9CdFBJZjN6ZUdKTTRZS0xFQnp1Nmt4Z1FKNXpnMDdWYWg0Z1pJelE1eG9BOFAyTFBjTkRyazNKS2d3aEpTendaLW13N0JpQnoyOUFtSnIwakE5aXprWC1ydE1pU2Z6RmRCUTl0bExaczA2SWljRUNYcEZfT0RaV2YzRS1GQU9BOXPSAbwBQVVfeXFMTjg5OU5xZjhnWGR0dlR1Wkx4RGFfbmZaWkI2bXpycGpVV0plLV8yZW5KdUVDb3RrbHhkNjM3bzhMd3lXRlpKYnpONjNRbGtjWDNDZXlXRTdlbTI2UHd5QklfRXNkbHBJd05rTFgxYUx5d0c5RDBYbDh5UERsMVhrMjN6RmFvaVhfNTRqLVduNmZWYktCTTdVcHhNb2xZQXM5WWh5UXVTek5uV3B1a2VhbFVrRkZzWC1Qa2NpaXQ?oc=5) (Sun, 07 Jun 2026 19:46:55 GMT)
- [Checkout.com and Fireblocks partner to provide stablecoin settlement capabilities - qz.com](https://news.google.com/rss/articles/CBMilgFBVV95cUxNS29BbWRfWl9sbUlIZlFOUGdjbHUtQmM0OUVXQ21QUXpoTGdMa2hXWmtMTGYyRzR2Zi1FRll3LUJzOU43X2NjNE1COENFSEYyR0NicG1tRTVkdGxIci1iYjNRdnVjNmVSTXU3b3dpTS04QmFfdEM0VDdZTDJJcnY4QW01dTlOY1NZUEdlSTB6WDJhT0l5b1E?oc=5) (Sun, 07 Jun 2026 15:44:10 GMT)
- [Does Fiserv’s Devin-Powered AI Push and FIUSD Stablecoin Bet Change The Bull Case For FISV? - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxOUzJlNDY5YVVXV0xLRHJaQmJyMmNxTktLNFJIR2hBYW9lYUc3c3ItNGRiQVhWLXBZNTFIX1VnRVNvOTNKNGlrZTRoVkJGcWJpYnZVYnI4WWNpZ1Zrc1d6N2ZVaDd4UjQtODFDODBwNmtOUlNSdU90YVVVY2VoT2xCMFRDU2dEMEoxZWdVWGlkZ0IzbWFKTVo3QQ?oc=5) (Sun, 07 Jun 2026 15:12:31 GMT)
- [‘Safer Than Palantir’—The Startup Building Stablecoins For Governments - Forbes](https://news.google.com/rss/articles/CBMivgFBVV95cUxONG9yQVdEWnZzaEpFbloycnA0TERKX1FaZ2tpRGtFSVRTaFE0SkNpY3RPeDdoOEtTR0toX2RMazlvUFRjNkxKYlI0Zm1sbERMZ1RqeWUyUzUxaFJpcUVnOVRieEliMEhHeUVuNG9Kd0RjMjEyWVNlZG9vOWt5aXVLUWV3LWpZU3k2ZzFqeTd1V3h1V0FrVXloNXJneEp1YzBQR0VpcGktdXh4ZWxRMlF3OVlJSlRNc002YVRHdGhR?oc=5) (Sun, 07 Jun 2026 01:19:15 GMT)

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
