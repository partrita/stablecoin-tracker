# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-23 01:21:25 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,286,499,110** | 🔴 -0.03% | 🟢 +0.22% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Assessing Shift4 Payments (FOUR) Valuation After Stablecoin Launch And Mixed Analyst And Institutional Activity - simplywall.st](https://news.google.com/rss/articles/CBMi3wFBVV95cUxNcUstd2ZEV2IyV0pRVlVZV1NRSmt0R0p3RjBYM0lxMGRxQ0NsT0Y5WU5vNnFxeGFWNkx6cG5rUVpla2tsRnJGUFN0RzBpcjFaOGkxc1pYM0pGMlA0U19GV3l4TkhhUlpWR3Q1bDRnVUI4cm55M0lLZkpNOUdnaENuQWJzOEhVSHB0WEF2VW9lcUhtQV8wVC04cFRRYk03OGFFMUVGYjVJQW1WbDFObTA2bVk1T2NfM0VyRVZZTGRBU21vZXZoc1ZBR25ndFM4SlhCYTQ3N0dmNmY2RkQxNGJ30gHkAUFVX3lxTE9LTVViQ3RuMWEyNnZUSlBUMy05NnVCTU1iTjVfWVpEMTdjRHdwNTBUY2hpSkVLRnpTU2x0SFJWTkdNZXNHWXY0NUstM21XSTFQM1ZacWRzakRCZmNkOHIySlRVeFpqQy1TVjRnVVNuR0RIdGR2R3V3NVltMU9lXzlMdG5ScXJNeFJNWHB6Vm9OVTFjSW5sbU9WUllwZXg3R0plUDN2blV5bEcwRVNxNDlJMFRfMzVKdTJ2cVdBYkJNUlJHcjRvVXZ3Nm5WNTQ1MFR0Nkx1LXp4elQtZE1LVDhYRFBIOQ?oc=5) (Sun, 22 Feb 2026 23:35:30 GMT)
- [XRP Ledger Sees Société Générale Launch First Euro Stablecoin - Yahoo Finance](https://news.google.com/rss/articles/CBMid0FVX3lxTE1qWEVFelJMbzlUdmJ6Q1pkV1Z2QXM3MkdNTmExMFo1QjI2a1JUTl92VXlTNGZ0M3didlFXNUpEckFRa2Nvb0ZPcW5oRTJlOTdaUzB5R2c5ei01c3ViNl91QUdfVXRZWWN3RTdnTHE1NnluTmd0d2Rn?oc=5) (Sun, 22 Feb 2026 22:30:44 GMT)
- [Wirex Unveils Stablecoin Push-to-Card - Crowdfund Insider](https://news.google.com/rss/articles/CBMijwFBVV95cUxQdXk5elFlckJMbUNLbk5oRHpDNm14VVdnWWRucXY4Qkt0WHZVZlR4SHdyU3Y4bDNfcjd4SExFYmhxR01lRWZTTGJhTS1nTGVycWUxNkhqdE1RWlNzUVZwUzAtZzFXTDNRdVlhQUNlRWFWNVlBZDRsRHNuYzNFZXdfMkFMbmw2OExEOUhVSy1kQQ?oc=5) (Sun, 22 Feb 2026 19:33:14 GMT)
- [ProShares' stablecoin-ready ETF sees $17 billion debut, sparking speculation about Circle - CoinDesk](https://news.google.com/rss/articles/CBMizgFBVV95cUxQaFA4c1NNUGM0d0dNQUVqSmh6U3dOeGpoUklVTVQzZUstOUxXNEZBUl9tZWFIenlKYkg4eElqVE81QUFXSVFsTzUzSVdaYUpaQkRPLUpyTmtZTDVoSU1ISGtJZ3piVHV4TWpKNGZBanE3M09OemY1OFZaRTJVLU9hTU5nS05YU21BN0FOQl9Ec1FQcFBXMWlKV0Q2TjR4WG9hZV9YM0pCMEVvT3owTXJvZGxrVUhQRjlpM3ZFTEsxRXVWNmEtM3o0bzNzRVFIdw?oc=5) (Sun, 22 Feb 2026 15:04:22 GMT)
- [CLARITY Act Showdown: March 1 Red Line on Stablecoin Yield - Disruption Banking](https://news.google.com/rss/articles/CBMipgFBVV95cUxNMzhqNlR2NUs3TWkzV01qa2RwLUhSTFdnb1U4SFRJVFVXNGl0UzhVcmswZHJORUlReXc2ZEltSEFzR2JYaW1pdmkyeFhhLVFKSXk5Tjlsa18xZkI1dFlIdXFHWFUwcWhLaXdhaDlId2U0bkJhSUMzdi15dWxDVGpQMXpDUkxJQkU4c1VtUktSbWZuUmZVTkJNWXNNR2MwWjhvbVlEWEFR?oc=5) (Sat, 21 Feb 2026 16:12:29 GMT)

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
