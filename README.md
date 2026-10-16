# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-16 02:26:34 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,009,164,258** | 🔴 -0.17% | 🔴 -0.49% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Why Liquidity Is the Real Bottleneck in Stablecoin Payments - Fireblocks](https://news.google.com/rss/articles/CBMifEFVX3lxTE8yWVRNX3Jldm8xV3JEbjVsakh4NURabG1DZDhSUEhtZ2VqNkw1dllfV01EV3BZOHI1UGs5aU1Ed2N5V3Y4UTJRMTQ0NlNVRDZObHJjUmN1SWxJNm12aHBMTkpZd1NjeXNCaVlzdmF4NE5FQ0NnS21aNno5dy0?oc=5) (Thu, 15 Oct 2026 21:39:13 GMT)
- [GetPicks Raises $3M to Bring Stablecoin-Powered Payments to Daily Fantasy Sports - markets.businessinsider.com](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQUjFMUlB1RGZVejE5Z2J3WnFGZGZ1UEZOMzNna1hrWFUzdjFhaE9DMkdTaGhrcjVjdnlHZ1VKZ3JVM05uRlM2TXZxTmxNNzFWMlpyUGlYcFlsODZHZlpUb2c0bTgtRXFMOU9VTjNnbE56ank1T3UtbVBoeGNjR0xWdWhRYzVYRktiNUtod1I4MVJUVTVMbjYtNUhKOElqbjlHTnJBbGZjVUtQQlVGZlMycE5TV3FaMWd3YlYzY0V2M1lveExsSFZrbGxnWGU1dGZTMTltSg?oc=5) (Thu, 15 Oct 2026 21:10:09 GMT)
- [Stablecoins Move Into Supermarket Checkouts - Abasto, Food and Beverage Industry News](https://news.google.com/rss/articles/CBMifkFVX3lxTE1SVjlJQ0w0RWYwOGRPdDh6b1ZLNUlkS3ZGYUo3NVhDakh4cmZUTVJaUHRwVVpNeU9naTFUb2dMdDZEUGF5OGd0TENjeC1LQ3ZuSHF1X0Q3X2tvOWsyZEJaNk85R1A0WlR3eWw2cTh4N0JzYUhybzMzX2hZQ08xUQ?oc=5) (Thu, 15 Oct 2026 21:01:29 GMT)
- [Getting Money Back Could Be Stablecoins’ Next Big Selling Point - PYMNTS.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxNSmJ5ZzE3cElxeWlpYVRPNTdxVzUtMk5ITDg5THZuMG5YZVF2RlB0a0YtV1hSQzBiV0xzRW5KSVJhYlU0NmY2M21EdU5jV0p5UUJOWEdrUExnSjU2NjlWeDNNUTIwUy15a1hBY2NwRTRyLWIybWR3UkxMNmx4OG9KR1d4RnRjWHhCZXl4dkphNi0xdEZNWEI1SUhFNFZLUmZVRE9ybg?oc=5) (Thu, 15 Oct 2026 20:59:28 GMT)
- [Stripe Teams With Plasma To Unveil Multi-Currency Stablecoin Cards - PYMNTS.com](https://news.google.com/rss/articles/CBMitwFBVV95cUxQSDNwSTFaTXRXWGw4bGRMc05UbExJXzExcGlpQWo0SzQzYmIxOWd0ODVOaEpVWDB3SjFGLTU0NVJrTndRZUdLY0xvNDdvRFZPMmpzeFQzUkdEcU9pVUJTTms2cWRGc0ZBV0pYLVlpVzNQNlJzSXlpY0Nha1FCSTVhbWEyMmR2TjdRRjcxOW9ERFkxUy03ZlQ3ZHZxMXRPSmlmQ1ZGMDlod1ZfT29OZzlxVGdkdEp0bkU?oc=5) (Thu, 15 Oct 2026 20:14:30 GMT)

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
