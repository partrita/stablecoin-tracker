# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-22 02:38:25 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$288,875,779,328** | 🟢 +0.13% | 🔴 -0.56% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [FINANCIAL TECHNOLOGY—OCC finalizes GENIUS Act payment stablecoin rule for 2027 (Oct 21, 2026) - VitalLaw.com](https://news.google.com/rss/articles/CBMi3wFBVV95cUxQTFhmbkpOblZjNjVLcmgzN25tY1ZMM2JfZVl6SkstbWFpMzhaRkgwcUVfYlJCMW1LZEhtb0pLdDZUaEFWY19TVWMxN3pxQVp1YkkzVWx4ZUR2dGFCMjBBay1fTTlQUFhIUURWRVhzUGxqZXZKWjBXRDdHeE5yVjllS0szMWkzUk0zaGt5UGRXNkthVWszYTJ5ZGRpcjltcUtqQ3dUcjFvLUpZbUVYVWszY2c4SU83TTEyaFQzaWZpb0cybTA2SC03WEFORFM2alk1ME5UNkdYWU5PMVpTZlJj?oc=5) (Wed, 21 Oct 2026 20:57:55 GMT)
- [NEWS: Tether claims 94% drop in Iran-linked stablecoin transactons amid sanctions probe - AML Intelligence](https://news.google.com/rss/articles/CBMixAFBVV95cUxOYU1GclZITWlUc1VZX3hDVzJ0S0V2emFpbGN6ZkpqcDNWODFBQms0c1JpaEYwNUd0WThieDJyNDRwcno2Z1hQZ2xud2hmR25COE9qc3MtNXJZQ0VNTkxscWwzR0o3dUJYSmtRdmhNcjZlOEJocnpSWHJBdk1iVkZjeHJCcG9yTHJaOUFBZG9FLTY0b2dTRFgtUnpuSm5lZlBmdFd4WE5GQWZZbjBFclQ4VFkxX1ZRWFZHVjdGano3Y18yVU1n?oc=5) (Wed, 21 Oct 2026 20:19:58 GMT)
- [OCC issues final rule on stablecoin framework - Banking Dive](https://news.google.com/rss/articles/CBMinwFBVV95cUxOSlg5bkhITk5JUktEZUFYVWNJb1Z2dFFlLTdfTWQtVXJzSmViUEdNbEVkek8zejF2aVhrRmltOGZ6Q0dnQUdWR3JVNTlFUkNIUkw0enpGem5nZGpQcmdFY2FZU0hHeTdlWVNxY1JUaU00bnNieHUwdm11TWxfRXgtWm1LYmwwTlN6MmtFa1BwXzhqenlfa0Mzdk12X0NGS1k?oc=5) (Wed, 21 Oct 2026 19:09:31 GMT)
- [OCC issues final rule on stablecoin framework - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxPSWVqYi05NXdaMDNvN0FwX05qbEZfWjUwUC1Yd0RuOHRHaVljR0ZvQTFKZUJfN1V1UmZ5QzBtVDJlZ3RWZ3JWQTZXcGdNV3NnZGlZTzFGdGJMSHBSV011cG5FajF0eVlCU25UbEpPeE9DdUZ2MC1YMU1FLXZ0aVBiUk1RN2RnWFA2enhISjA2Y1l4QXM4d1B3Q1gwMkVFQQ?oc=5) (Wed, 21 Oct 2026 19:05:00 GMT)
- [Stablecoin transfers hit $891 billion — a 4x jump since 2023 - Yahoo Finance](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQbkcxdHpSLXRRTFdMOEUwOE02bjdKZEM4OGtwU1JhckJJNWpQWGhqYVFsTkNGM1hlakdoY3BZVThtQ2pHSzJmeTFMVDBlY01DSE5ua19sa1BoUmV4Ml8wR1FwdENNOUNXOXhyV2daWDlRZ0gzaU16WWoxQkctNGJ1V0w3Z0x2Ymo5UGVB?oc=5) (Wed, 21 Oct 2026 19:00:00 GMT)

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
