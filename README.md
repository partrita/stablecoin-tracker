# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-13 01:55:51 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$298,455,047,757** | 🟢 +0.00% | 🔴 -49.80% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Tether Hires JPMorgan Executive for U.S. Stablecoin Expansion - The Information](https://news.google.com/rss/articles/CBMingFBVV95cUxPSkdSdHEydk1yb0tsdkxqUXE0bHoteEdKX0FJbC1WemVkSjZrNFlMZFdDbkZaUm5xWmJ6OGxGeUlIV25uLWNwb2VmN0pfT0w4ZFpXRFBPdXl6MnhJS2lhT3ptT1RoNThrM0RlNE45cWVQVExhQWFpZnpuemJPcmdyNVp0Y0NURlJ5M3RwQXNSTV9QSEpQYjJOOXRidy14QQ?oc=5) (Mon, 13 Apr 2026 13:04:00 GMT)
- [2 Stablecoin-Related Investments That Could Soar in Value in 2026 - The Globe and Mail](https://news.google.com/rss/articles/CBMi5AFBVV95cUxOS3Q4R01rRFQxX3htNWROekFPWk5SYUJaZkpXTWxzdmRkNWVfUXFYcHVzeEZ6clQxbUdyelVxWHRBUDJtN2ViTlFOc1d5cy1yYWNvTFNUSnNXMzdvSGxTLVAyLUM5UlRMX1J5TVhLVy1UZTJ4dU1kRElQcHU3Ym5jMjZGaVB5Zm9pMWdUbVluVVNlUkE3eldKREpJRFhxa2xxTjI2R0FxNWVPd3NZc2JEaHZ0cXR2TjhqZkNGT0VrMmgyMmxYVUhLX0dtT01CazF3NHRYd0hNQVV6OS14d1dkdzBpU3E?oc=5) (Mon, 13 Apr 2026 10:21:48 GMT)
- [2 Stablecoin-Related Investments That Could Soar in Value in 2026 - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxNWFZQNGg1dUZZVWpVbzVyRnFtd2lhN1B6QTExZThKODgzVk5GNURHcDhvTGVjS2pLa2hQSnBIYzBDVWhWSlZNVTFMRUtZME5FYXd5UGg0MUFSNkowa29nQWZadzdtakVldWZ2ZzNmOERmeGxyS1MxZUFMZEctZ1BYV3pVZG5wSGVoMS1qYUY2RzlXUXRXdDlPUg?oc=5) (Mon, 13 Apr 2026 10:18:34 GMT)
- [Hong Kong Grants Stablecoin Issuer Licences - Wealth Briefing](https://news.google.com/rss/articles/CBMilwFBVV95cUxNbVRVRjFzMlBQdE51SkZoZTJNRTlCb29LWmZzckJLb3lsMXRZeTBTZ3N1bHdWV1JfazRFa0NPNEVpdG9tLUE3YzNWUi1Hd3ljZGJZYWMxY3FmN2JKaXpUclBfMGV6VmxaSmowRVVmN2pXQXVUSlktbDdfc0lzNFBZVm1pZ0pqT0otZkRoOHo0bHRZTVZCN1NV?oc=5) (Sun, 12 Apr 2026 20:46:08 GMT)
- [Stablecoin Forecasts Stretch Higher as Bessent Presses for U.S. Crypto Clarity - Yahoo Finance](https://news.google.com/rss/articles/CBMirAFBVV95cUxOR0l5c0g4amhWNndSZ0EtYU5EMHhsQW5XQnRMaGp6U2MxaGFkY25zRi1TbmRBc21CSW9mSllFUTAwaXZ4NmQwcTRFVFZGb21tMm04SW4zR0RJRDczb1VOODRoTVhKZEktN1VReklHVDVqSEY1ZjhuZTViTFM3bnd4QlplN0dHVlBxb0tYenptcEJFMWlETFhad1dlTjhTOWZwRWR0U1NYMXR4ZXFF?oc=5) (Sun, 12 Apr 2026 18:38:00 GMT)

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
