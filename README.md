# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-08 01:21:04 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$296,192,528,733** | 🟢 +0.03% | 🟢 +1.05% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Bitcoin purist Jack Dorsey says that his firm is reluctantly giving in to stablecoin craze - CoinDesk](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQZzFUODk5LW90YkJhZG1BZi1jZVJJLUlyZy1GNFZNaVRnbC1JcWp5TnphenlVWExsSlJBeTVhTnlTVkRteVY1YnJZX1FQWXI4UHZKYUtiaGtraVFiUUQxN0VEaHVvUWNLd1k4LUowVjlIZk96OXROYkpGSkJkRVBfRDhHVmdnUmZFc3NmN2ZBTDFQVi1uM1IzMDlaMWZXbTdJSjVBMWxGSEU0d0VWS1QyZU5fVEFsMDJEMHczZGxHY28?oc=5) (Sat, 07 Mar 2026 23:14:55 GMT)
- [Florida moves ahead with state-level stablecoin regulation - dlnews.com](https://news.google.com/rss/articles/CBMikwFBVV95cUxORXI0X2lqT25hWkRibERlaTJiR3dVOS0tcmpIOG8zYW1NQ3ppcVFSaWVMOS1MY1BNY2FyTVBtTlcyTGdXM25vYTE4TG9kY19tajJnZEFVTFJOV3E3emJSZjhSSmpXQ3dkUTl4c0F3ZmdwZmxaTk5fQTRhQW5WUjh1azVUcW5MQVVmNGJjODlfZEYxbUU?oc=5) (Sat, 07 Mar 2026 18:50:33 GMT)
- [Visa Expands Stablecoin Cards Testing Blockchain Rails And Valuation Story - Yahoo Finance](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNM09OUzRwVG45QXBEa21IZW9LYTlMRnVpREJybTNHMXJpOGI1ZHk1NWktTnVMNVVGSjI2MXZnbEp0aUh6c1ZqQk0tMi1YTk5sMmVjd3NPZTdUc2g2Z2o1TFo0SzhNcjd5Q082Z2Q3aldTTXFob1VLd2FVTTFaWWtFa0R6XzhtdzdYSEhv?oc=5) (Sat, 07 Mar 2026 18:07:29 GMT)
- [AI Should Be the First Defense for Stablecoin Payment Fraud - GovInfoSecurity](https://news.google.com/rss/articles/CBMimwFBVV95cUxPYXlZS3pRRTRmaWVaZmwyVmd1YWw3ai1Ed1ZrMmNrbE5jd3pleGVaYkk1VUJRN3pSQ1hTdXNCX2w5akc2MUxDekxDTEF4WDU3Ni1fM21HeFNaMmcyQ3lTaTkzZHpRcUNzU1dVWVhOYTRBQU9xNFI5dWFOb09ieFY5cmgzcDJDWndzbGlfVW84M2pia2VRQXE3YmRBOA?oc=5) (Sat, 07 Mar 2026 15:17:23 GMT)
- [CRCL News: Circle shifts $68 million in internal payments via its own stablecoin to bypass legacy banks - CoinDesk](https://news.google.com/rss/articles/CBMiywFBVV95cUxQWDRKcm5QZFE5Q1dsTXBWejVMdmdjZ25obzRqa1NSOWVISzZ6ckdlcDRuamVkUEtQM2lyQWdwODFvbGZlMWxVOFUyV010NHNTeXczVHlUSEpRNTJOaFVqSmloTFc1V3dpdTRIZUMzam85TEhUV2VuUzM0ZXBHU2U0VHVyWlRXbmdPQ0RUd2ZlV0FHN3RDbzdZUC1uX29mNVNGUVRTQnM0RXBiMUZZb19JRV9kUzFlbVk0dVRSZ25fQmhadXNKZ3dyZ1U5MA?oc=5) (Sat, 07 Mar 2026 15:06:27 GMT)

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
