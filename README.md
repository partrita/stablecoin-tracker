# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-30 02:14:58 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,906,504,637** | 🔴 -0.48% | 🔴 -0.90% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Cash App enables USDC for P2P - eMarketer](https://news.google.com/rss/articles/CBMigAFBVV95cUxQRlhqSGJjU1B5OUhCeVlQZmJMRFpvY3VsUllDYVpFbko1S0ppZzgzTXdlVFlkZDFVNE9SN0ZQM055TWFlTWxzQ1FkdmlmbFY1TVJhMk9nT1dIY1RPZnhseEo0c2Q4QmJiTjZ0dWR0Wm1pVWwxRWlwOEJEOWd6MWlraw?oc=5) (Fri, 29 May 2026 20:46:12 GMT)
- [‘The banks will not accept it’: Dimon escalates battle over stablecoin rewards in CLARITY Act debate - CoinDesk](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQeTFCMU8xem1iU2FmRVE0ckJyUXFFU2RZNU9qZnhmLTBGX3VCSTl4V2dod0JSWlpaLWFwaG4xNFNtcENudG1Zb3ZnSWRnSkpDWW5DUE00QmFkTTFkN3dUQ0o4cUFCY1dxQ1ZHbkxyR1c5TjRNT1ZJNEU0X3RFMmJoMnJrVVhraEhKSThpWE9aQVpKMTZDNktKQ2xsRUtPRVJDWnpJWW9mRGJwNkRqVWJ2LWtkSmR4cVR4aWE5ZFc1Z3g4QVRNQ2p2Z3hCclI5dXdfTTZRbkdDUQ?oc=5) (Fri, 29 May 2026 20:05:07 GMT)
- [Crypto Brief - Lowenstein Crypto Newsletter - May 28, 2026 - JD Supra](https://news.google.com/rss/articles/CBMifkFVX3lxTFBRdXFfa0R4OVpqWlM1LXZVVTdQaW4xZGNiVDFlS2JQMUVGN3Zob2UxQXR4X09PYkVCc2VyQmxGNFB5aGQ2Uk5qU0o4RU5GdHhTdTdtWGpJc294Q1pzd0Y0azZhZDlBazBPVTg5bHZvZm13WXotb19Nem1DLWNMQQ?oc=5) (Fri, 29 May 2026 19:26:28 GMT)
- [Stablecoin Settlement Is Here, but Seamless Off-Chain Money Movement Is Not - PYMNTS.com](https://news.google.com/rss/articles/CBMiugFBVV95cUxNQWpGNmRBR0hKeHdnTFl1cVlraWtlQm5yazNDZElCb3NlaEIwX2JtbFA0ZEk3WDVYLVVxMTZCTS1nSHgyV1Y2RTNvVVFmdmZKR1hKcnhhV3NGS09iOVplMzJwbUhhQXBVN3lTei1lcEZ0am5DbF9ka1N5RjR5YW52UmxSTmctUng3czhxdU5TVFM3NV9aNnlFQWNpWkREWnQtLVVmNFd2WlUxX1ItaE5LNUUzcmNrWnNseUE?oc=5) (Fri, 29 May 2026 17:54:02 GMT)
- [Payments Stocks in the Stablecoin Era: 3 to Buy and 1 to Avoid - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxPT0h0Z0FfNG5KZzhoT0p1WkgycmZNcjhRaFFLZEgzaGN6aXR4STIxS2JucXlMV25QblVJTGt4RGtIYk1IQnR2UEIzalFqVVNnYlpVLUFZdzQ3UWdtcEh2UzlHb083MlVITWdRd1VodURsT2kzdnlJSDY5aVBMa0s0M1FLamh3Z2hfLURFRW9GYmIzYzhVdUd5b2pwbUFpZw?oc=5) (Fri, 29 May 2026 17:40:00 GMT)

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
