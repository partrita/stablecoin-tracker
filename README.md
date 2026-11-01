# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-01 03:30:06 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$284,272,974,717** | 🔴 -0.02% | 🔴 -1.18% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Bitcoin Vs. Stablecoins Vs. CBDCs: The Fight Over Digital Money - Forbes](https://news.google.com/rss/articles/CBMitwFBVV95cUxNOFNKTjFGMXV4UTFBZVk2SkRyNElTbVJRY0R3R3BPYUE4MmpQa0RIOUZZQ2l1LXVZVFp1R01XekVIa2puckhvWnlqTS1xS005WTZ4NjRtaUxJdW1rUmtGWVdRUUl6bnVtZEd1NlFhMzdCWVNhQzNlU1JGZVNRZm0tYXpVSmNmcHF0MTZtZHRUdmhjUWpnWXJSWnU1bHFwQkhKSnZsaGgwNDNUcE50bENucEVnUXY0bk0?oc=5) (Sat, 31 Oct 2026 21:27:28 GMT)
- [Shopify’s Base USDC Checkout Puts Stablecoins Into Mainstream E-Commerce - TradingView](https://news.google.com/rss/articles/CBMiygFBVV95cUxQckRwTm5iVERhZU5CUzJIdkNUdlQ3Q1ZFTzhKVEc1T3V3ZFZRMUR3OTlTaE9OZ1BUaWVkQV9DUlZxNDQtenhQWEFoTDJqLTlJdXJzaF9vWkliVFdpUVNEdmNRMkt3VjdGMkNFWklHNlZrRnRFTDZtMk05RUJESmxRQlJ5TzM1UmdQTThJU19nWW9Da1M0ekpwTXB4TzJOaW9VcXR0WjJMNEZwNDZ6cjBQbWZGTDMzV0ctQ0stanlzaExFOERpY2xsWk5R?oc=5) (Sat, 31 Oct 2026 21:00:00 GMT)
- [Polygon Extends Open Money Stack to Solana for Stablecoin Payment Flows - TradingView](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQaHV2RnNmTTFlYi1HWWx4VHRiUE12bllUSkNvc3phWkZIdkZkcFlXMG9KTlpqajl5UmtvMHJWUG5YODFNVS1DRGxhUUpibVVxM3RCdzByR3I3QUlQbWd2YUhjN1VPYmN4QTRKTFl3N3otRElYaXdNTXhoOHEwOUo4T3p2dGxSQU1VOVFnSGRTbHduUWdNVE9feEpyNF82XzlPdXlvTE11TE1MVUlWY2YtdWI5SUJGYndsUjhZVTlQeC1sYjZOWEtfNA?oc=5) (Sat, 31 Oct 2026 17:00:00 GMT)
- [GENIUS Act: What New Financial Standards Must Stablecoin Issuers Meet in 2027? - Coinpedia](https://news.google.com/rss/articles/CBMitgFBVV95cUxPZFViWDlidWQ0aE50eURHaGM0bGhzLWx6SFFoYXlnekM0amcwLXIxSWw0OE9JMVRGQlhsVG1iN3N1aHpBSVhoNE5Hb0FsbDlOLThPTFVFVU4yM0tlVXQtUWR5OVlFZXpDaG1nZFpwSnNDcmlrbDZubEZBbjNpUFlRTTctdjBEMi1vY0NZZF9IOG9abkhTQllpTnBQaHVsRTY5OE1kamZxdXhCNjVhd0lUQkRpcjdFdw?oc=5) (Sat, 31 Oct 2026 14:09:55 GMT)
- [STABLECOINS &#124; World’s Largest Stablecoin Reports $1.5 Billion in Q3 2026 Operating Profit - BitKE](https://news.google.com/rss/articles/CBMicEFVX3lxTFA1NVVyc3hhNmROREVjRUdhbmQ2Z1k2cXVJMTlBb2ZEYmE5R29zUmFkZE9vYnphSEJjOUxqRkdGWFM3VWJPTlBVOW1zazl4ZlpISkZHaTQycnlYdDdVV3FHX3pYTDFuRE9tRU43QlZTYks?oc=5) (Sat, 31 Oct 2026 04:00:35 GMT)

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
