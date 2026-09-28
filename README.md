# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-28 02:46:48 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,694,937,621** | 🔴 -0.03% | 🟢 +0.59% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Fed proposed stablecoin rule could trigger a 48-hour liquidation run - CryptoSlate](https://news.google.com/rss/articles/CBMimAFBVV95cUxPZ21FSHEtenYzMlZ3NnNCb3d0TlU0YTB4ZjVuNGZoZkZFUDRPbHdpN2RTeU1tUmNvRjUzZGxPS0Izb1ZFcC16V1owNW8zbm5tYzU0WUo5dDI0Y3M2LXhLMWI4QWhRTmpuY01Hc1BXdG5EcUNBZ1BsSVhwQUpvcUVIa091SEdhUUxjdmoybjItMjQ1dDJWWlFwVg?oc=5) (Sat, 26 Sep 2026 17:55:58 GMT)
- [From dual currencies to crypto. Is Argentina a blueprint for the stablecoin future? - Buenos Aires Herald](https://news.google.com/rss/articles/CBMivAFBVV95cUxNNlNfZ1VMSnpaRG43Vzl6Y2V5a1IycF9mQ1pOLUZXb2wxSDQtNTcxOWFVbk5kWkROc2VrSVZsblp2MEFQRjR6ckxHWHltUmVqWTNHbEl2UmVIeVRldmFvR0x6X2E4b3NjSlZLNlNKdkJkaG1McFlyZkhFckpLeHNlZHg5ZXVESktQWnpvREZneEw4VUkyZHlPWTlieVFJS0ppaXY4VVROR2xwYjgxeFJrZ21ZMGNQbFJkeGYtTQ?oc=5) (Sat, 26 Sep 2026 17:49:55 GMT)
- [Is SoFi Technologies (SOFI) Cheap On Its Stablecoin Rollout And Growth Push? - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxOUXlkUjQ3Vmp1cXlFVl95NUZweXgweGlvR1pZWkFndTdNQTRmYVFQRDhXXzBWMFdVMkZnUzg0NU83RFNTZ0pRNzJUeHNjT2NWUnFxdGNfRkZXelctb096WjY5MTRoSUNqOFIyT2NVLWFrZEZldDJKelZ5ZVI1UENkS0o5bHU3bHlUNkQ4N09UdG53SDRpd0VGZnZ0QXFHeE9xVC1LYXpjUQ?oc=5) (Sat, 26 Sep 2026 17:10:19 GMT)
- [SoFi Is Bypassing the Banking Bottleneck With Stablecoin Settlement - MarketBeat](https://news.google.com/rss/articles/CBMipwFBVV95cUxOUWJ2UlZld1g0aURRNVliR09MWWlBS2lHa2c0LThyYW9ZakpMbG83THpkaWtNQzVBTVFCOERpb21UamFFcng4RTVDTGFickxaWlVTSHQ2OFJiTmNLYW5BdUJwU3ozLUdaaUtOeXI2VURzX01Vb1VRUjNqTl9zcTh2MG1aNHNYRzBjZ2ZQUTZaOUFEa0t5dkhmWXg2YUlFX2gyMkFSN085cw?oc=5) (Sat, 26 Sep 2026 15:42:05 GMT)
- [SoFi Is Bypassing the Banking Bottleneck With Stablecoin Settlement - Yahoo Finance](https://news.google.com/rss/articles/CBMirgFBVV95cUxPRXh0LWswc1FOeFdWcUtfUDBCYkg1ZW9aeTNQaDVYMnRGcmk3dVNvdlVwbDZMMXFTLVFmUjJxQzlXbUFkcDNvaWI5VW0tQmsta2pGXzNRSWJid1BUWTAxQVBrS1RZV1AwMFZzaG02XzV2MFpfVW1rZ3M4WnN2dVo4QkZSWlc0czdtNGNzdEhhRjEzMXNXRmhRaTlTVE51TmhUUWdmeU9kTTdtR3FVTmc?oc=5) (Sat, 26 Sep 2026 15:40:00 GMT)

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
