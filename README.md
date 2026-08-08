# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-08 00:59:27 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$287,315,810,396** | 🟢 +0.14% | 🟢 +0.27% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [5 charts: How crypto cards are driving stablecoin spend - a16zcrypto.com](https://news.google.com/rss/articles/CBMifkFVX3lxTE11S2VYLVNfT0xYWUxXM1ZPWmpsRlV2WEh1cHhlVTJ0MFAyZHVETThuRjlxU3B5Tm50cUlsZWgtV2JidGhDemtIZmp1SVZZZHZEUXh4Z1FaUklyTWFRbUsxZlVVS1B1UXVYMHFrcDVvLUNWd0NjNjdNMFJyQ1B5Zw?oc=5) (Fri, 07 Aug 2026 19:57:47 GMT)
- [FCA framework departs from traditional stablecoin model - OMFIF](https://news.google.com/rss/articles/CBMijwFBVV95cUxQZGJFZTl2aXQwY29YdGp1UW5tTnlzd2pMSEJiSDl5UjAtVjdUNkRXN2N1OS1ZZGxWdXM1a01QbEFBNXJLOTBSZVF5UEFTaHhYRHNYVUh5YVd3WUxORzVxdGVzNWdGMzRjOTdLSDJ6ZUFFSkV3R0hxeGhKNjV1cFJfeEJhWFFGMXJBckd4eXFkUQ?oc=5) (Fri, 07 Aug 2026 19:51:56 GMT)
- [KuCoin Brings Stablecoin Prepaid Cards to Businesses - PaymentsJournal](https://news.google.com/rss/articles/CBMijgFBVV95cUxNUElTMkI0eHNhSUNHZkUtVnJpanpvNXN2ak5DeE9JeXVhcTlhLWhzRW1aUHZxems4bk5FdGU3WkdHT01XSzNMOFYxX2Y1aTZSUEhnMkpVQnpYQ1psbjlNalhsWGZ4cEZuVjZIZ3duQmZicGNLSzhTSk4xUUEtQzBGSFVuTm5SWkFGQkM4RGln0gGTAUFVX3lxTFBESkg0c0l1TExmanlDMFdURnFQSE1QbVMwUXJKRE40WVcyQllXTERQUUlIZHBYSG9zWmt1Y2tsaXR0RnBXN1U0NDUyaXB0b0p5c0RCdmxGV2FWWVdjQ3Nkb2N0RkNOQXpwMEM4dXA2YjJlRUoydzJCcl9ybW9JeElLaXdVQ3pVX1RvVHhMUk9ONVlZZw?oc=5) (Fri, 07 Aug 2026 18:00:00 GMT)
- [Mastercard Tests Crypto Credential as a Trust Layer for Stablecoin Payments - Startup Fortune](https://news.google.com/rss/articles/CBMipgFBVV95cUxOUVVGWEhYTzJjY0JYRlhyU2h5bjJrLW9ybDJCT2FaUFJXX2dpbW5UdTBxVTdMTHVheFAzOGdWcEJsUGNFQnV2UTJBRkpwN19fVzhpMmo4Q0JYeWs2a1h2cWhrajRGRmZFcncyRnMyYW1hVXQxWkZDc0RIQTh6a3ZiTEMtS1ExVjhQLWY0djZ0Q3QwNEpSY2h6UlRJZ1pRS1dSWHU4Tm5B?oc=5) (Fri, 07 Aug 2026 17:05:15 GMT)
- [Africa: PayPal Expands PYUSD Stablecoin to 27 Additional Markets - Glenbrook Partners](https://news.google.com/rss/articles/CBMiogFBVV95cUxPWlBIeFNxYW8tNksydHhRdlVmSEdhQVRfbG9KaVliM3ZWVjdFZ2picmt4TGtMN0NrZFZiVHZoRFNDWFkyV0VSdk00c2lVNFR5a0xtSUtsY1AybXpfcUdHQWhJZ1FnczRna1drdjFNTkJ1a2RCUmI5ZHJnNWhaYXNLd2haSWpFYjJQaWhsbEhfeXpPSTlLUndQc1BFMi16SEQ2bmc?oc=5) (Fri, 07 Aug 2026 16:12:53 GMT)

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
