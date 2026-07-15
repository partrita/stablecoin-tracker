# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-15 01:41:08 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,435,156,914** | 🟢 +0.08% | 🔴 -0.61% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [US banking groups urge changes to stablecoin rewards in Clarity Act, again - ledgerinsights.com](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQUmgtOWt2cW4zRXl5cHJhUGhFSEZ4UXM0ZzNTSkdKaFNyWU85QnZqVW5aZ19XcWVfSGxXQUVyNi02bEc2UVVYUjk1UW15TXdVYWlHUWNPbVZRWjhWSUNoU2tta29FNlRMN3hkUkpsU29xZGhKaUxuRG1RaE9lOEJaZnRGOWJfSFdVUHJFUFB6c1UyNjY0ejdMRFozN0VodXZCWG1tVXVRejI?oc=5) (Wed, 15 Jul 2026 00:27:19 GMT)
- [Coinbase CEO Brian Armstrong Warns UK Stablecoin Limits Could Compromise London’s Financial Competitiveness - NewsCord](https://news.google.com/rss/articles/CBMi6gFBVV95cUxQT3V2TlVUcG8zRmZUWWJpdEtaWUVTeFhLV2NxMG01RkFwM0J4MzFSOFN4YVhOdmFNbjM2LTdVeFJWa0h3WEhrNXRfbUpVdldPdHBscmhRQUI0X2Ric2tBZmhaREw0blRza05DdEpJVUJ5NHpOSEY2MjFGYXNjSDJzWU5zRUNGUmpVNHB1RXZVMHRPcGZiLUZpQnVMTlRyQUVPM3N2MFZUUkdYNWNxSjBya2tfdm9SRFpxVjJQdW1ZdDNTclE5anJVVGJVMlVGUmZZZkZZcEhzNXI5WFdxVTJJT25lU3BUZGx3a2c?oc=5) (Tue, 14 Jul 2026 22:49:34 GMT)
- [Velocity Raises $38 Million as Stablecoins Reshape Mainstream Business Finance - PYMNTS.com](https://news.google.com/rss/articles/CBMixAFBVV95cUxPVjY5dTEtci1oblZiS0x5cXR1SjlUV25RWThiTGpiNV9ocFN0VVkyWHBTdGtoZ3pzWG1mTmZUa2FrREdxTnMtMUdwZndUNTdrVGRoOU1zeEZZV25fOVFTcWdFV0tDS25CM1pkcVNyTkpCTkswdG9iZmROTnoycmNaS2prazBXbFZhRGdTUElUS21MRmpubVhyVlhWV1M2QVZIcUUxVVgzNG1aNFNGS2JUZHE2U1VWTWlxd0lVcGs2QTZkQVZD?oc=5) (Tue, 14 Jul 2026 22:04:03 GMT)
- [Banks Unveil Blockchain Network as Stablecoin Payments Reach $33 Trillion - TradingView](https://news.google.com/rss/articles/CBMizAFBVV95cUxPUEYwNXJ5TG5UMTBlNVNuMGdFNG1xZXc2QldxbGU4bGZQRm1MX3BXd2p0N1BIUmZubmdPSFRrNHI1ckVFSUQ4UTBxVUxaNFE4MElmSkRqR1V2U1BEMzQ5ZnVhYVNWVjNpSDBzZFBncVNZanp5UnlyX1F1dTdxX0xmWnhWOEJQTFdhTTJmMjFNekc4VjZSLXNHMkU5OU9FLVQ3WTlSODJfMF9vNU5PZmY0eWVZYmRyMG4zSWV4UENjblUwVGt0dnh5cC1QaEY?oc=5) (Tue, 14 Jul 2026 21:19:54 GMT)
- [Velocity raises $38M to build stablecoin treasury infrastructure for enterprises - TradingView](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNamExTUVRSm1SNkVxNGk5WHpxcmhXQXBHYWM4NEMtbWVHU2dDUnVYdzloQ1FVQWtrUWFMNUg5bW5uTnlXMGI4Z0F1S0hncjJYdzJySENqNEFtaElDaTBDTVRzaUE4aFdVaEtlTnpVMFM3U3MwOWRrUV8xdmlrMVZmX0ZmdUxIa055eGNyR0pkaXBBbWpXMV9uZEg2MkFnaWJxNklLa1ljTVNQUXNXTHBtMjJGQ21nR0FTMWVNZjJON1Nhd3RaRDdQb1RCcGdaeVQ0aU5rM3pOdWFBaG8?oc=5) (Tue, 14 Jul 2026 20:04:31 GMT)

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
