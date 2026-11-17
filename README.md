# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-17 05:51:50 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$274,693,647,529** | 🔴 -0.14% | 🔴 -1.30% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Visa And Mastercard Stocks Face A Stablecoin Test Investors Should Watch - Yahoo Finance](https://news.google.com/rss/articles/CBMipgFBVV95cUxQMEJVX1dsT3Q5ZVRDZTA3S0xES1V5VGIyc25ZdEJ5ajV2UGliZ3ZxeXdRUi1ORHdxTWRJNWI5c2l5M3RxMFBSc3VBUzVSVVVmVFVKcUt4eXExOG9JRDJlazlHUnZKaEhrSWVmUTFCVTRZcnBtWDB3RE9zNk1CRTFrcnU2RGtqekxLRHRTRkpabjd0Rlp1MTdjdEw2azVvb28yQnM1OXpB?oc=5) (Mon, 16 Nov 2026 02:09:00 GMT)
- [Stripe Focuses On Tempo Blockchain And Stablecoin Enabled Initiatives - Crowdfund Insider](https://news.google.com/rss/articles/CBMiugFBVV95cUxNU05lMWVJY2F1bm9ydXp6b0xqcGVXbDcySDNzUnRpY1N5MUlqbjZkYlRucFZHanRCQkZZR2o2MFpHZjlBNE9oT3J3MVZ0YWkzcjVQa2ptdFh2VXJNVGlQXy01c1c1OE4yMkp4aVNkWnFtbE44cGtNRGlDbEJ1LUJ1NkhzMmRQTE1TNnNpbWJVV0FNaE1kelRyTmRRdTZrdGZvaDItTi12S29WTFgxWFhGejFWX1JIQmNkQkE?oc=5) (Sun, 15 Nov 2026 22:13:25 GMT)
- [Stablecoin Supply Shrinkage Raises a Bigger Question About Crypto Liquidity - TradingView](https://news.google.com/rss/articles/CBMizgFBVV95cUxQeEQ4aG16bUpCWWVmM0F1aGxJWXdIZm5QZDJ3VUFjWm5nUVhnazY5X1JZVGdva0VGMTZzMnRXeVRHMnBDdFdvNnhURmJoZnVRUlU1bW4wcTdYMEotMHhOaTBGWm5tbnRkZTJVUTZfQllNdHhXMkVodjlneDhya3N5cXNTamFVSjJJdjRQa2JoSzREbmNxMTlRZEgzRG5xNW5pY2prckpMWW1MU0o3N1loZ2ZRNUZMQ3lrT1VoY0pqdU5YZTExblZ6aHpXSURTUQ?oc=5) (Sun, 15 Nov 2026 20:00:00 GMT)
- [Arbitrum Draws $91.8M in Stablecoins as ARB Token Sinks 20% in a Week - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTFBLZm1sVHE2S2JlRC1RR2hSa1JfNjZ0WjBIWnpIN1o0VGNzeGl0LVpXS2gtZXZ0b0RYS0ExSWRBUFNCdm1rMFo5enk2dmlSSmV1THQzRFl0Qlh2RWxqQWExU09FVHRoTUNwamNfMTd2VWZXUkhmUEE?oc=5) (Sun, 15 Nov 2026 18:35:00 GMT)
- [21 Financial Institutions Plan to Launch a New Dollar Stablecoin in 2027. Who Will Be the Biggest Winners and Losers? - The Globe and Mail](https://news.google.com/rss/articles/CBMipAJBVV95cUxPLUJTNzdQaWZ2dkVnbDktdU85d1FYSmNDRU53TkYxRC1oMjNsMEFFdjVLY1p0QktiMUlFSW5kOW5Dc0VtdTB1aHp4V0wwdXJVbThoOThOQVV3Q3Q3a1kxRU9vOFM3cVlGa2R4MDNUREZpcWRhdWFtUUEyYW1HdXlNUEQ3X0FDOEpydGM3MHFzUkxJWE41Ym1wbTJsRUV6V2hZU2tCTzd5ZndXdlJZeFdPRDhsYUdoSmRHZGMwaUx0bEpqYWdTSmtTcHd3ZHdCT1dwNVQ2T2tadEFFN3JnOW9PVkVGQnRCTURadlhKY3Nxb2loSlQtM1FfUTFiSDVkX0V0Nnk3eDdLS1V4SmQwdXdNN0YzaFdNdmdZQzUtSEdMcXB0bHlD?oc=5) (Sun, 15 Nov 2026 15:40:12 GMT)

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
