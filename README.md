# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-10 23:33:11 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$298,208,450,990** | 🔴 -66.61% | 🟢 +0.43% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [The US Operationalized Stablecoins This Week, But Who’s Using Them? - PYMNTS.com](https://news.google.com/rss/articles/CBMipwFBVV95cUxQU3A0ZnhHblVidWJ2S3lYVDFmU3ZXYWlEdXJRYmE4RzZ4azJFTjdMcTJtNlQ1UTZZSFN1QjZYWnR6d2pXZ0dLWDN0aUduZ1FaTWpzOTlfdFVISXVjRll1aGpGOGtoYlBPWTFBak9EUmRvTy0wWWlOZEtJNGF1ekd4VVlmLTFPSHZtQ1NjbUhRM2JrMFYxSl93MTA5VXQ0bmpqZVJLSlp3UQ?oc=5) (Fri, 10 Apr 2026 22:45:22 GMT)
- [The Stack - Grayscale](https://news.google.com/rss/articles/CBMijAFBVV95cUxQQnpRRGZ0LWJxaHp1U2pxRlFaNmtLWlRJR0U2aE5wdzhrZmxsWUdHTWE1Y3QyMDdUcG9sbHp4bFhtLXR2V0pLZGgzR0F0Y3NMdVV3MEtBbjNfRld0aVYzQnFiQUs5NXFQbnF3Sk1aM3kxODlfa3Vua0UzV0F5MndyOW41M1VxOGFnbVpJNA?oc=5) (Fri, 10 Apr 2026 15:09:31 GMT)
- [Hong Kong grants stablecoin licences to HSBC and Standard Chartered - Electronic Payments International](https://news.google.com/rss/articles/CBMinwFBVV95cUxQR0lpVVNRc2t3a1psQk1rLWttVkhRVE8xMFF0Yi1EbTlRWjNmMWZmYUs5c2lhVVVJQ2M2UHJmWVJPamNXTTNycTI5dThtNDY4SlBoU0NGcGtRX0NwQlJyN3V0MC0zY1l1N19ZcDJPTlVLZElocFpvOGNsUDV2OHJySk5QWThZR09vMnRHX0xnUFBfcWR6b0t6bkU0ZWM0MGM?oc=5) (Fri, 10 Apr 2026 14:04:22 GMT)
- [Stablecoin Trading Volumes To Reach $719 Trillion By 2035: Report - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxOT09ud0hGcTIyblNUdU0tZ0paamx0UVdpWmtRd3p4T2c1YVppVkRuQjU1U1NOSHg1UDdQN1pNc045MnVqVzM1RjBlRGl4UU84cDN6R2d5REdPLXdTNUw1Q0pTaTJxT2hHaEE1SUxrMzFkaVNlSkU3TkFCTGhWaDdHV0w4ZW9TY2VJQlBGdUxlQ2Vwc2M1M0NFTWtoa3RQdHJtV0cw?oc=5) (Fri, 10 Apr 2026 13:00:00 GMT)
- [HSBC Granted First Stablecoin Licence in Hong Kong - Markets Media](https://news.google.com/rss/articles/CBMihwFBVV95cUxPbGhlU0U2MU1OdWJ2dmVlSldRS1dFb3dCTTFkNUh5OXhzcFQyZ3NnckloZXJ1Z0F0c2x1UW15d0tXWEVfbGNmblMzOUtxVXdTazNQSUR4NFhJRHppaWNYaVlkTzItOU5FOWhwUm1VNGZwZEgwV1p4dWFudTVIR2hjWnFTQXBBN2M?oc=5) (Fri, 10 Apr 2026 12:37:22 GMT)

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
