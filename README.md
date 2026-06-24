# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-24 02:31:14 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,135,640,401** | 🔴 -0.12% | 🔴 -0.20% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Global banking body issues blunt warning on stablecoin boom - thestreet.com](https://news.google.com/rss/articles/CBMiogFBVV95cUxNZko0OVVuSkl6MXZIRldkMmFFU2FYZUprTThFaVR3RHJGcUZ3QlFMbEFtWGtCM1ROaHZ5eGJtekJTY0dZVnM3R2pidkl5VmNaUVlxR0FETnNQTlp6WnU3Y1Q2WDUteHRDSGVnWW5sc3ZocHAwbV9icWZ3VFkzT3o0N21aOXlJazRxdXFScXd6OXpUeGM2NzFaaWxVOVc3RkVXNEE?oc=5) (Wed, 24 Jun 2026 01:30:00 GMT)
- [Breaking News: FinCEN and Banking Agencies Propose New Customer Identification Program Rules for Stablecoin Issuers (AML / FCTM) - Lowenstein Sandler LLP](https://news.google.com/rss/articles/CBMimwJBVV95cUxNX2Q4SV9VVE9ST3NlNURydkYxSHotOERxQ3dnMlkzd0NWY0JUbUQyd0VTMEJ1WWt3T2d4ZnVHdlJtbGxFeUJkYVJuREswU0VHZElqMVVuUHJDZzNJbW42RFBNaWFucHV0bWFTYUthcENPazhPVFRJRy1jb2g4Z1JFTlQ3cEZKNU9INkdoOVQtem5QYy1TRktBOUU3VGNORTVqRjRXWkFLOUM1eVdzemZ2OEJ1OExEeTlhNWFaTmN6MWN4cGNGWjB5MXBVaDNpNG9NN19uZDl3T1BrU1Nzc1BPM01vaFhBWTVsMFh0NndFYUNkdUNKa1pyUXB4aWxhdU91ZEdKMU9wQjBfQll1Y29JN0Q2VVNrb1pHZHhF?oc=5) (Tue, 23 Jun 2026 23:51:00 GMT)
- [Chainlink Helping Banks Launch Cross-Border Stablecoin Trades - PYMNTS.com](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQYnN4eDRwRG1RS0VRbHpXM0ZjVS1FdWM0eWJOc3B4d01id0ZmcHNST0l4TVUwQUsyb1h1QkNWdVdMYU9nbUJ2Mmp6eWpoa0djdnY2dGF0TG0xU3RmeGhTSEZ3LVZpVGxQUzc5bkZNVXd1YjNuLW12NDV3QkRkdnduY3puTjdBcGJqOUFFS3lwWjdjeVVNb1h4RExSam5pRDFnLTQ1Y0RRcHAyQkt2WS1MOFkzOWdnODdY?oc=5) (Tue, 23 Jun 2026 20:33:55 GMT)
- [Agencies ask for public comment on proposed stablecoin regulations - Financial Regulation News -](https://news.google.com/rss/articles/CBMinAFBVV95cUxOTy1aUzZDVkk3Q0w2UDZ1NmUtYXNEVEc0MEtfU3dpRThuM3dBemFOQmVCYy13V3dKOUlmYVZDSzVIbk9teE9jUFhDd1AxVDc0c2JlZ000X2owVWlTY01CYnU1SXhyU0JKdFBmQ3VKRjc3cnVTSEFaV19SNlo2X3ZrQTZhSFh2OTJkNFRoaFBYN3NQNFNhSkswbGtpUlc?oc=5) (Tue, 23 Jun 2026 16:39:28 GMT)
- [Global Payments: How Stablecoins Are Reshaping Payments - FinTech Magazine](https://news.google.com/rss/articles/CBMikAFBVV95cUxOWld4WFNmRnA4NTJzbmZvVWtWZ3YzdkFlVHVVbnJOWThrcXhkNjdzYldpblFuSXJVVTdJZXBsdGlRR25EUzgtWTJCS3Fyclk5UjRsN05iZkRreUlwN2hSczA0bWtOQmh5dmJiaE55QUFEbVdKSkVCT3V4UDV0cV9NTkxGM1RzR3Fybks4eng0aW4?oc=5) (Tue, 23 Jun 2026 16:22:35 GMT)

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
