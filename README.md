# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-14 02:52:45 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,133,768,637** | 🟢 +0.08% | 🔴 -0.61% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [MiCA Stablecoin Rules Reshape EU Liquidity, 100 Days On - FinanceX Magazine](https://news.google.com/rss/articles/CBMilwFBVV95cUxOcS1VSU1WaEtQekZNME5qWllKV09NU3FodUtVeFJURHF2aXBKUGFlZUlBa3E1RFFNVE5IblBoalFHQUlTRDVuYUQzMnVrakUzVzF3My1PQkJDS0JJaGNBTjBtbjZtdjU2YVlCc0E2M0V6QzBQV3Rqb0prR3Z0dy1mZ3FHclZONTNvRklpSnR5cGdDd1FXWW9n?oc=5) (Wed, 14 Oct 2026 01:05:27 GMT)
- [Citi’s Fraser Says Enterprises Value Tokenized Deposits Over Stablecoins - PYMNTS.com](https://news.google.com/rss/articles/CBMisgFBVV95cUxNR19wSWZ0VlAwZDcwdXV2b001d0FFSHRaMGZGUGVYRG84M09ublU3Yk5ON0RFNjZlRHdiMVBXR3ZIdzN0MnA0bFV0OER6X1piekVNX2xYZy1MV0dJTVpIOUwxVm0zQTBrdXJaZHQzNG1SZF9iNUJ5VXkwcXlPd1BTX1JPREdxUENDUmlPQWpqcV9lUnE0VHgtblZZaU95UUI2Z0NtY0REOFUtUUF5OGxvTTlR?oc=5) (Tue, 13 Oct 2026 23:16:23 GMT)
- [Stablecore’s Nick Elledge on Making Stablecoins “Feel Like Banking” - Finovate](https://news.google.com/rss/articles/CBMijwFBVV95cUxQMHAzeG1LdFZzTGFWMFdHNGdwXzdWdjRISnJkSzNqYjRSQTFXeG1TODR0TnVDSFB4Y1NHbXRHQjM4QjZrbmwwekpHTHJCWThRZm5BUW54WXlkM3N1clVNSFlpMmpfT2tnR2hmWjNZWTdSTzd1ODFOeDR4RWZfalp1NDRWUXFvb2ZHQlc4Z3JzQQ?oc=5) (Tue, 13 Oct 2026 23:09:23 GMT)
- [SAP and Samsung Shift Stablecoin Battle From Issuance to Distribution - Payments Industry Intelligence](https://news.google.com/rss/articles/CBMilAFBVV95cUxNUzRGb09KU0tKbDBrckVSWEptbUZKX2JfMU5faGxRRWxxUjJONlZmcldMVXhFOWo0TkFzdFFVQlJwS3NYckRQT1k5b2FkanhGMFRQcEcxazFRUVozamJDSDc1UDlLYTNMazM5Y3YyZjM0SkhSNWRZZHNJR3htdzg0dlRCbVozYm9pdWphVXVSLUdFakZU?oc=5) (Tue, 13 Oct 2026 22:07:05 GMT)
- [Stablecoins Have A Weakness, And New Research Finds Banks &amp; CUs Can Exploit It - CU Today](https://news.google.com/rss/articles/CBMisgFBVV95cUxNRVhXa0IwLWdsWEV3T29tbXVmWEFGZnFXaTQ0OWM4a3Rpc1FrWS1TSlhrUnV2TXJWNEpEVEZraExBWkltWUU1anZkRHBKNFRvYzRJQ0hFSGFNVDhMcVRpN2g4Qk5MV2VjV2wxaTdhN2FqYUVKTEdRTGNpY2w5MW9reDVWVm5LVnM4U2FWN2lPbGIxOVR5U0t0bkNXWXhzVS12M2JYdGdIeXFod0g2UUEyM2d3?oc=5) (Tue, 13 Oct 2026 22:02:06 GMT)

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
