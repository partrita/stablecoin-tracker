# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-25 02:33:12 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,709,881,636** | 🔴 -0.15% | 🔴 -0.19% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecore launches stablecoin and digital asset programme for credit unions - Finextra Research](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQMkdaZml2VkYzaFFtRlpOQXF6X0FXY2hQODZja2FvY2xROFA4eWdSb0N5TlZlb1RGWFNTZWtKU2ZUbDg2OHE3dlR6SzRyU3J3dVFmZUFUYm5TQ2FJSlBpY2VuYXpPQl9KYm5nTHV0VjVFb2h0T29zazc2amk2a19FUHRlNTdmMGtNOVJNN3RQQllfTHRablRXRTNrcldaTDhhQ3ZFMkRJMl9rYU00N0dlNzdwTjI3d3hneHl3?oc=5) (Thu, 25 Jun 2026 00:01:00 GMT)
- [The real cowboys of crypto: Wyoming ropes a $1 stablecoin - Pittsburgh Post-Gazette](https://news.google.com/rss/articles/CBMitAFBVV95cUxPY2wwclRYeVIySVdldTdsaVFubXFmRUxicUkzSkFLdjV3d1ZYRE5YcFdNVTFDNVFnOGh2aDlOVFFQZzVibUNPVGZqVnR4dW5lZmsxbzloWmpIY0VLM05aWGZPSVBEVm9zaXV4ZmZmMDdkdnRhSHVhZ3NTT2FBUGpTNmxGMjJLWVJxcVVVY1hJUVlmNzZ1ZTl5a2x1UGJLMnVnWTNUdzN0VU01bFhWbjhtRGFwVHo?oc=5) (Wed, 24 Jun 2026 21:58:51 GMT)
- [XRP Is Down 50%, and a $785 Million Stablecoin May Be Part of the Problem - Yahoo Finance](https://news.google.com/rss/articles/CBMikgFBVV95cUxOWDJlckdFNkxZcDA0LTBGanZTcUN4bUM4dXhWbG4wVW5PVV92Q1RFWmM5VHBpcnVjNElhb29pNkt5LU1pdWJYcXFnMXBrYnFpVDk4M1FpcGFCakVsbi1ramJ0WlBVMXBwUm9nZFFsRktKS1ZwT3lxdjdxM1VLeDFOaFQxWHliZmM5a1BwdFJLTG5Rdw?oc=5) (Wed, 24 Jun 2026 20:00:00 GMT)
- [Stablecore, Circuit launch digital asset and stablecoin program for credit unions - ledgerinsights.com](https://news.google.com/rss/articles/CBMisgFBVV95cUxQcVhHLVNvUzd1YTIzNnZyemxpZ2dkclZrQXVxUnBqX0J4SjF1MFlfdkZtZGxhM1FiVUpWLVRPbm9hbHlVWFVWcnpfOWd3M1d6NUh6N1ZWQTBsSm5EbDl3Skc1Z3RGOV9YVEo2a21RZFlOM1lxQ1hveFFoT0R6Nk1naXdWa3JFNlZhRVJWVFhldF9mQkNUR1cwTWdpeVlGUS01Qng5TF90eHF3MEdQamxhWERB?oc=5) (Wed, 24 Jun 2026 18:26:11 GMT)
- [Bank Of England Publishes Stablecoin Rules - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxOeGRYd2JtNHFCQ1JYNy1HT09IUEYwOXU4OERxMjRkS1VjU2dMcmF5aGNudUw0bUwtT1hfcmI2RDN0Ym5paFdabXlJQWpWNGs1RVctZk9BNWQzSEZ1ZFdaRGs5WE1SbVZsdHpZclVpUmd4bFh5Q0VDdTVnS1VYNFBFYlcwN0NRQTY3REhHeG0tTUVZblo2VmgzblZ2RjNJc0poX0I1b1k3SQ?oc=5) (Wed, 24 Jun 2026 16:23:00 GMT)

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
