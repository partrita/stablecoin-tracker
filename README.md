# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-01 01:51:28 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$296,614,491,960** | 🔴 -66.69% | 🔴 -0.47% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Tether Announces USAT Stablecoin Expansion to Celo Network - Yahoo Finance](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPTVk4WVYxWVhUTVp6dE5mal93N05YcGdXRXJxNWRwdUlMODllbEFMVWhHUVYyQzhQU1lNQUJiRDdfTE1SY3prWjk0UV9VWDRVb0lndkludUhLS0wzdXlZa2lmekZxVC1mZjVnQldqMlVDUnV2MGFrSktkTHEwRThnWnJPQ1Fsb2tjeEhNQWpJNDZ5VS1HbWZ2Rm1LMEFUOXBuNjRmYlN3cENadVk?oc=5) (Tue, 31 Mar 2026 23:09:36 GMT)
- [Fed&#x27;s Barr invokes &#x27;long and painful history&#x27; while encouraging strong stablecoin oversight - The Block](https://news.google.com/rss/articles/CBMitAFBVV95cUxQcnJaR1JqWVRDWWRpSTE5SnVkX2Y0TUJ1VXRkZmdjUW84dUVCNV9zcFRQdGVJVHhmbWhnMmk3Q2ppVDFIOWRUQl9lU2pxTTF1YWVTejJGcHlXck12dFo4ajg5R0kxWS16LTZNSzBkQVprRHpIVGJzRk1obUZBQjB0ZDB4X3FXY05RNE9SdlFLZTJfMFBDbHk0UjhoNGxrLTE1RmpsRU5yX1oxeDliSHZBVE9NZ3Q?oc=5) (Tue, 31 Mar 2026 21:21:37 GMT)
- [Ripple Backs Convera To Enabled Cross Border Stablecoin Payments - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxOOUNnX3pTNVJ0RC1XQzlaMlVDZ1Zpc1NlTC0tTlNlbk9OVkFySy03YW9obHNWUlV0RU1mY2hiN2lIQ1BtVnhraXNMNFFFTWJEbFZzVnhBLXdWS1BJNHMwOTJ4dENYU3NEMm80SEt1SFZjc1hvelB5eE1Cd0F2RHUyZlFuSWJ4eFcyT3p6SjgxSG50NklDcklGYVJGcEFqVXhG?oc=5) (Tue, 31 Mar 2026 20:41:00 GMT)
- [Circle Mints $750 Million Of USDC Stablecoin On Solana Network - Yahoo Finance](https://news.google.com/rss/articles/CBMimgFBVV95cUxPLU9fdDhqdFFCNDV4a1h6dkJSQ0RkcWFrQmR0SkdydlhBNDl1OUFCLUpydDNwOEVwZ3VnRXUwYkllM3RsQmItLWtjbnpubDB6NTY1SWhJMGRLaTZTcF9IOUI2VFk3WFpCREZ6dWN5al9CZ2xZUk53dnJkdkg1X0RCT1hzVWs1VEZURUJScC1GZmRiVVBNd19uZjVB?oc=5) (Tue, 31 Mar 2026 20:39:00 GMT)
- [Big 4 auditor confirms Ripple&#x27;s stablecoin supply fully backed with reserves - thestreet.com](https://news.google.com/rss/articles/CBMitwFBVV95cUxOakRib1N6anFxaHBPTmk2dGJlU05sSFBBQkxUZUhkR3lQRFBHbDRLdXA1Z01BQTBqbGZQdmpFZGdEZmYyc09MVmR4VXV5X0UtMk5PaFVtaEdvSEJ5TDQtWno2WlJ0VGxrb3pab2pBbWRlSG5tNEFqYWYtMlVXY2ZPSjJTZ3pjZDBDM2c1c1M2bmZCdG9hV0FWZ0hMZUNDNkU5amlFM3VYZjVWT3NRVW9mU2IwQjN1blk?oc=5) (Tue, 31 Mar 2026 20:28:04 GMT)

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
