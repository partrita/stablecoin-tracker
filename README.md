# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-07 01:15:16 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$296,111,746,955** | 🟢 +0.02% | 🟢 +1.09% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Mastercard Expands SoFiUSD Stablecoin Use As Shares Trade Below Targets - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxOeU1DVjZHbzdfUkctSWxjd01CWlFRQVI0cF9MODhva29fMkVVbTVGejdBUlhhdVFtRUY3SFltOTA3SXpmR0lMVE9kR25Lb2hvSVBWSl81Zm5vbjFlM05RSHZYUklTT2YxZ3EtaUlUQzRQNFBfb1pZa1lvaUJlV1VYTmFaSTMybk9ieWdOMmpLRTlLaGlm?oc=5) (Sat, 07 Mar 2026 00:22:00 GMT)
- [U.S. Office of the Comptroller of the Currency Proposes Comprehensive Supervisory Framework for Payment Stablecoins Under GENIUS Act - Sidley](https://news.google.com/rss/articles/CBMihAJBVV95cUxPNldwRjJUVVdvMXotNmRjOHJKRXRSSDRWZko1M3huSm4wYmxQTjFjZW50MTlkWUo1aGc1amRkemp3M3BwZnFhOHZVZzhSV01oYVlrYjZFcUVUNVFrbmZyMTZ4SXktRldvemF0X0hBdUs4QlNJdHZRNTFsSlNDbjBwUUFoLUNBamJ5N0RVc1NsOW00bzU0X05iTHMydTRlZjZ2dEw0YjNzRVAwX09OMHd4TGZXbC1jUEk3U2FtSDhZY2RtUkY2MG9ZQnd4d0pfdXhuaTJsUXVodVJVY1V4NWV1eTMwWWxoVXV1dFMtSzBxbGd0SEtnV3Rmc1NtSzNGZmYzSmcwYQ?oc=5) (Fri, 06 Mar 2026 21:36:42 GMT)
- [First US state-level stablecoin bill passes in Florida - The Block](https://news.google.com/rss/articles/CBMilAFBVV95cUxNYWdrM3RKclVKMFpId09naF9mOXRIelU3NnBQc3dXaE1RTktRZlBvb1l2VUZSNHhESEJlWVhqSnVHcGZ4cERGNHFYQlAxYzZYRHQtSGdyeXRtMGs1Vkl6Y01tSThvNjI4WGRiYUtlWUNlT1NVMXRBdXBHUVVRRV85X01DcDhwc09aeG4xY3VwNW00eDZ3?oc=5) (Fri, 06 Mar 2026 19:11:40 GMT)
- [FinTech and Big Finance Fight to Own the Stablecoin Stack - PYMNTS.com](https://news.google.com/rss/articles/CBMiowFBVV95cUxPX1Q2dXdNbUpXWFdFRU1OZ0JUdzUyNHJFcl85YUM0WTRzTzRCTXRnZWwwZkJaLXhEaW1FM0VpenhpM24welBpaU1iSmZ5WVJyZlVRRFlaanM5dTIxbVQ2OEFZcWRVUkYzRmpWZ19XT0l4dVNBUHlWNWVyc0o4Q2V5Ml9Ta0pvMWlFQnp2QkxhNFJxTEtSYm5SbzhIZERUVFh6a1M4?oc=5) (Fri, 06 Mar 2026 18:37:33 GMT)
- [Stablecoin is moving into traditional finance in 2026 - Finextra Research](https://news.google.com/rss/articles/CBMingFBVV95cUxPRmN2cS1WWGFZelhyVlY4TkxxRFU1eHg0b3JXeWlGRGlJZUhmdWk2djRYdHpjVURtRW5mQWFnbDY0SFNjeElFLTBtbVE3ZXdvU1pzeTJXVkpNSFhSaXl6LUdGRjZ3Q1JSVlJCVFgwM3JIUFZXOTVtVnlqQWpDYndUbjF5Mk1vYzEwLXpYWTZLc0pnM2x5UUl6WGh0WUN4UQ?oc=5) (Fri, 06 Mar 2026 14:00:00 GMT)

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
