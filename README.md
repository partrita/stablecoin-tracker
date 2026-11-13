# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-13 04:19:01 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$275,701,331,248** | 🔴 -0.26% | 🔴 -1.59% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [SoFi Takes Bank-Issued Stablecoin SoFiUSD Live on Polygon, Opening It to 17 Million Members - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE1wSlNIS2JuSnVqaHBpN0pUSG52MHVrbnJqZHZraWs5dURlbTJnZlFMajFFdjdySGU4bzdHYWtPV1dIMUN0X1B2YWpuNU5VWGRrMDBKZGUyNGdwS1VvcEI4RGZXZDdRWnd6RzkzT29kdjYtYkFxZkE?oc=5) (Fri, 13 Nov 2026 02:25:00 GMT)
- [Visa and Anchorage Digital bring Western Union stablecoin to settlement network - Finextra Research](https://news.google.com/rss/articles/CBMivwFBVV95cUxPNndkRnJiQ0twLXBIbHR3cmFDVFd2U3o5aEh1ZW9hcGkwWjRIQ1dyMXZub1VZZ19samRiRWhzMkZhTXFpYWw4Skwya2lXWmJNd3owLXNPaW4yS3gzMkR3R01mSmJRVmstekM0Q2xIMDZ2eHV4UWI4UzA2ZGc0SnJRSkJyR2labVprUUZIbGE1ZkZScWVScDdUendhR0pFd1Q0WXFOWkw0aXBMYzQ2bkM5MVp4QUQwaDlCVTVQdkd5dw?oc=5) (Fri, 13 Nov 2026 00:01:00 GMT)
- [US Details $2.7 Billion Freeze After North Korea’s Binance Hack - Bloomberg.com](https://news.google.com/rss/articles/CBMiswFBVV95cUxPeW1GTEtDNFJteWJfNTQ3X0hZbFp6X283dU1aWkZ2SnlVNG5EQmdQcHhQeXpPMHJmUkxTMlNYUUNsZXN1aGVjVzhQMzFaUzBKZXlHT1ZYc2V4dlh2Y1VfM1pYSTB5SjhQWnRjZFVvQ01RTHllbGtvVmktWmp5cTBYV2FCUWpUNTVTd3dHM211Q1BpV0RJcEJURXJSbnlOcVQ4U213el9WX1pGODJmUDJORWxHZw?oc=5) (Thu, 12 Nov 2026 21:40:07 GMT)
- [A New Blockchain Payments Survey Shows Stablecoins Going Mainstream. Here&#x27;s How to Buy Into the Stablecoin Investment Trend. - The Globe and Mail](https://news.google.com/rss/articles/CBMirwJBVV95cUxOdXdtMVY4cEFYaTU5MWg5WmpKNnlzVDVrc19mUERqWFR1VlNWUWFCOWlNQTVQMGU2MnVraXlpRVN5aDlXaUVUZkFnV2VhN25pOU8zRkRhbXJMbzkwNEVzR3JwcXJ5UG41M2lKUE9qcWtob2dhYnhjZ3F3aWNJNFA5bWRDZlFVSWYxUFZGNGhBMFk1LUc1M1pocFNtMFI4MXJBYy1IWTlxS1NPcDlRc1pjS1lLMEFIbVdrYjZaWkM2T2g5UjZWUENGSll2ODlnQVhHWkRyWU90Q0NqWmdHcHFxR21OeUN1Y3B3cjNZYnplMDBQeXFjVFZrUUM1alpoRjRSczZ4SnZkTTBoaU1WZXdRZ3ExNVdtZ0xuSzN1cDdQaktQSzc0NjNmdy1VY3RNbmc?oc=5) (Thu, 12 Nov 2026 20:42:55 GMT)
- [Visa Expands Stablecoin Services With Anchorage Partnership - PYMNTS.com](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNRmU4N2N1XzZRSTh3YkhtdkxCSjlMVFM3SDBKR01WU3pqbk0wUk16eG9Sb1F3NHdaczZTMW9YSVVXemxFT180SGV1VXVtTE1WQ0V3SVRESUZVU3JzdG1YSG9KUXhxUzFHdm9Ya3p1eVhpR3hZMFVVb2lvNDB1SVZONTZZdzk2S1dRdF9TOXBCRHVoOHg5a2JXbS1TRlpVcXItTEc1N1BFcldIdw?oc=5) (Thu, 12 Nov 2026 20:34:56 GMT)

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
