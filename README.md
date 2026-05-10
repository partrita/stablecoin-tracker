# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-10 02:07:44 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,935,479,273** | 🟢 +0.25% | 🟢 +0.23% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [BoE&#x27;s Bailey warns of looming &#x27;wrestle&#x27; with US over stablecoin rules, flags run risk for UK - The Block](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPRjV3cUFXNmNfNnZ3eU5jYmN6Zkdjb1p1RHFTWDFsbHN3VTB6V3EzTGY1Q2FnR0ZybFFVT1pqWi1DaXFpR0xmQ1dtSFpLVFUwR1lSY0lpTUUtYWxtYUxJQWtZZ25kSVhqQzVsOUdHMmlOOHVBR2RYQ1BmTk5QRHVoUG1sWHVsdVB5VDNWb19xQ1lwRG13OFF0R0JuVTJhRnZUcnJ2M0RUdXk2azB2MnBkd1pXT1RrYnphYVJ1RlV0Ul9NUQ?oc=5) (Sat, 09 May 2026 19:56:36 GMT)
- [BPInsights: May 9, 2026 - Bank Policy Institute](https://news.google.com/rss/articles/CBMiT0FVX3lxTE55d3ByZUljai1QZTFzUTRmODh2Rk8xaHYtM0NwQkFvSmVZRnVTQ3c5bDB3U2NQRWFNX0ZybUpxZ3UxSmNKZkFKX2puc29jYnc?oc=5) (Sat, 09 May 2026 11:00:00 GMT)
- [Hennen: North Dakota leads with Roughrider stablecoin - InForum](https://news.google.com/rss/articles/CBMilwFBVV95cUxQZWd1bktIWXJZUnB2WFkzWndzWVlEaFBvamtsOHE1dWJBT3ZWWTdnd2tGTFZSZGxJTGFFOTM2d3dUVkxzRWtzekREcFhmUV9NT051WEJDNF9mZzRUeTJZZndiU2p1QmRTcWYtRVhlZnp2czhlNUk0VlNKYXpSM0g1eU9BNmdKTUxhTE5tTEJBazdWVnNyWlVB?oc=5) (Sat, 09 May 2026 10:06:43 GMT)
- [Mastercard Stablecoin Push With Yellow Card And What It Means For Valuation - Yahoo Finance](https://news.google.com/rss/articles/CBMipgFBVV95cUxPOXJmQ1laZEVvbTA5dS1WODktNVBFdnBqck9zNXVlNDRZcFd1d0JUTGRtSV8wMjk5QUtxdDZCeTJFSnVNTmVBakxkUmgxUHd4YXE4MjNLcVl5MjRLSzlDMjlNZENkZUkzRkR6cWxvT3hYbHdSLTZNeGdIdG1Ec0dEaExpMFBjRzhnS2RrNkJjb2MyQkpfZ25nbU50dlhWTWJCSlROV0dB?oc=5) (Sat, 09 May 2026 08:22:48 GMT)
- [How HIFI Built Compliance Into Stablecoin Infrastructure From Day Zero - TRM Labs](https://news.google.com/rss/articles/CBMivAFBVV95cUxPUGlCYm9XaVp2SW93V3FpbGZDRFM1dW8zN0g3VllnVTVNNktOVW5FUVRhSDdtdDZKLTQ1VDJ0Yjhma1h4NWx0YlJWNFNZQ29PMWtIR3NOcTFVdWc3cHlvd1RFTFYwcGhDT2F4WHpXeU1mcnhfUkotaDZDMWthWGRTTGw2aDFaNlJBZFFIRkNUTW13TXRkRDg0OWgyM3VYd2RseWlyTnl0Vk50aDFrMDBmbW1MNl9IbGRPWkNfaA?oc=5) (Sat, 09 May 2026 03:20:37 GMT)

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
