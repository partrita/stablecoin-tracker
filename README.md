# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-06 02:03:41 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$301,093,684,663** | 🟢 +0.10% | 🔴 -49.84% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Delaware Makes Its Stablecoin Land Grab - PYMNTS.com](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNUVVBY3Q4RjhJMkVwSjFfNm4xRFV6SGFJYlRWTUphbHJzRGJwZ1AzWVA2UGlOYUJ0ZF9lYlNZeXFmblprWmxPVXN1MDByODVBYnJiMFkyVzhoSnJQSG0wY1hQTFRUTE54WkEyWkgwd1RueldQYkZLNnhwUVJyelA3c2ZFcnVVNTBSNTEw?oc=5) (Wed, 06 May 2026 00:06:03 GMT)
- [Banks Say Stablecoin Yield Fix For Crypto Bill &#x27;Falls Short&#x27; - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTFA5bk9TNlNsVXJYT21yeVFCWTZJZEFaMHVMYTVxVTE2b1ZXNXhDVGV5dE9ySDhwZF96UXpmWjJBWmVobGRzVllOaHJ4YXNEQWMwYzNsQlRB0gFWQVVfeXFMUDluT1M2U2xVclhPbXJ5UUJZNklkQVowdUxhNXFVMTZvVlc1eENUZXl0T3JIOHBkX3pRemZaMkFaZWhsZHNWWU5ocnhhc0RBYzBjM2xCVEE?oc=5) (Tue, 05 May 2026 21:45:00 GMT)
- [SoFi to launch its stablecoin on Solana, citing speed and cost - The Block](https://news.google.com/rss/articles/CBMingFBVV95cUxQRXJfRUpXNnNlUWdyREJYQVFvdVplRTI2S1N0SF83a1dhV3NYTEY2VHRGM0l4bnBZQmZXMF9zeWloNUdJNW52MDZzRkhjWFNZVGw4dHJ6b1g2Qm9qcEd0X19rS1NUeXlHaXVTLTF2UWhXbzNFSlN3czc5dkdyazRmX1FETG1md3g1STg1bmhCbnJSZ05kcVI3M1FBbnQ0dw?oc=5) (Tue, 05 May 2026 19:15:55 GMT)
- [AICPA wants regulators to use its stablecoin guidance - Accounting Today](https://news.google.com/rss/articles/CBMilAFBVV95cUxNUFJQZzdCMzdhMWVRRUdIVEloYXBFOGs5TU5MbDlDNHBIdVdhNDZUejByNy1YdHdtdHdhUklBNlNCRnQwWUYyZ2lVSjhZcTNqWHc0cThmcThvZXprMlRYRmNRR185UzRxWTkzbWVib3NBc19VRW05cDAtYnhQQjVnRFo3WGdLR0dwTzduT2RWSWFlMTcy?oc=5) (Tue, 05 May 2026 17:53:00 GMT)
- [A Model Built to Mislead: Why the CEA&#x27;s Stablecoin Analysis was Rigged - Americans for Financial Reform](https://news.google.com/rss/articles/CBMid0FVX3lxTE1wZFcyMWxKeS0xSVhqM01oaWkyN2tJQTVYMUVMTHlzMlpnczdkem5qdUZtSXF3eXdad0hOSm5KLVFVR3RxalpaMXBOaWdrR0Z4TGYtdTFkcTI0eUJwRG9Zdld1ak9XQzV3QWxHRUJnQ0V2SUJIWWNz?oc=5) (Tue, 05 May 2026 17:52:55 GMT)

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
