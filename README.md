# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-14 01:44:45 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,197,551,118** | 🔴 -0.52% | 🔴 -0.61% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [IMF paper explores stablecoin impact on currencies with fixed FX rates - ledgerinsights.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxPd290eWFvUTAtUjBwSGFJWTBfSHZuMWxRbGJUOUoxVVlrclZiUkV6eXVMOU5BS0pOTTdFNG5PUzdUNU0zU2hsQXNKWk54OXphU1JLSi1yVVZqY2xNZDB3a3ZrbGtEYkI4VkU3MFgxRTNYdGdZTGlEWUhpbWxLeE1odlRyUHZuTVdhVFNVRk1pQzJybjJSQXdjREtpVWdnM180Q0ZKWg?oc=5) (Tue, 14 Jul 2026 00:47:22 GMT)
- [Credit Unions Can&#x27;t Afford to Ignore Stablecoins: WOCCU White Paper - Credit Union Times](https://news.google.com/rss/articles/CBMiowFBVV95cUxOaUFDQXZraDZrQkhBbHlHcmRhRzZrZDB2OFVtRmhiNTYyX1RPZ0hSY1VNVlBHOVZCRnNZdDhWRDU0S3RnVDJ0R0RnSlVzczdydzdGRmkwN1JHdkVybHZXeUdqVGc1Sk9uWElnZGtxNDZzTmRpYnF4OTBaRkpyNWNVV0NiZktJbDVpVlg3Q2lfckxBMWRMNlZKWUVmYmVROXp6T0Jn?oc=5) (Mon, 13 Jul 2026 21:45:44 GMT)
- [Mizuho Details Rising Redemptions and New Stablecoin Rival Pressuring Circle - PYMNTS.com](https://news.google.com/rss/articles/CBMivAFBVV95cUxQSmJmZW5NSnNxbjZxaFVrczhkaDFxdkJqMjVqNWJzczh0Z2ZsYm1sTWdNSUhBRHRnYUJ6d29yUGRpQW9xTHhITzhVWXdOY1dueEpvQkpIWWN0S2FnVE1GWHBXc2VGYzhiTm1ueEVPZkdaWFZyLTVDNi1CRFhkMDRkdjIyX3ZOZHROS0d6akQ0V3Faa3pmTVh4M0pyMFByV25hSFdITUZ6WFFMV2Y2bDNrRE1YSkt5QXFuN0xQbA?oc=5) (Mon, 13 Jul 2026 20:53:51 GMT)
- [How Kredete uses stablecoins to make remittances faster, cheaper and more accessible - Mastercard](https://news.google.com/rss/articles/CBMipAFBVV95cUxPeHpzS2pkdEwzLUxzbjh5QUZydDI5Mm1MUjVmOHZLLTlWZC13MmNuS0hYaHFWWHRWZk14TnI3TnlFOFdxVThQVmJIaEZFU2VBNmpSdFJnT1FfblJYd1NueHc0VTUyTjZUcHpnSk9EZUNNcHVUdjBtTXJ2M0R1ZGpsSVR1c21MYzRxaFRKZW1aX2tZc0lESXBqeE1nbzZ5bzZpWndqNQ?oc=5) (Mon, 13 Jul 2026 19:05:24 GMT)
- [Bolivia Is Considering Adding Tether&#x27;s USDT Stablecoin to National Payments System: Report - Decrypt](https://news.google.com/rss/articles/CBMimAFBVV95cUxNWGdkdU5IeXhhbmVwaGZNWFF2anNRWTZnaHZINy1TcWtYeW9mel9sMUVpT0thMUFLcTBxZkh1RFdZbXh5RTNvZWVRV0pod0J5ZEtPOWtQQzgtUUY4UEJoZ21aSjA1cnhRNFo1Q1JYTDNCbUxPZ196TkdldkNURzJJa1VOUHk0V01CeTBmdTJHS19VTFFwRE50bdIBoAFBVV95cUxQWU0xRFVJcGk1WjVZMXdjdlowMVUwM0pZNDlBRTA0S1J1ZW5GNHE1QXB1RnNrMVo5LU14dlRLUnJPMjRNOC1CSE5lN1k1Ym1uU1NyRUNVV2FtRXhBVDZXb1d1ejhQRVg0ZEZzbVlvWTJITTBoQUNzTXFBeXhWWkxRaFhKY1ZER3hlRk13Tk1BX1NRYVJjNTdxd0tuZ0RXaF9Z?oc=5) (Mon, 13 Jul 2026 18:57:19 GMT)

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
