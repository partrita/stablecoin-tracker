# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-14 01:17:47 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$298,490,854,792** | 🟢 +0.18% | 🟢 +0.80% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [The Practical Implications Of New FDIC Stablecoin Measures - Law360](https://news.google.com/rss/articles/CBMixAFBVV95cUxQVDFlU1RZMlk0LTN5RzZhTW5LWVN3MlBPbnR1bFYyN3Z2S1c1MHZzVzdQSmNZZFRiZ2lHdTc5THhFNUNtUWlVbzFpREdSTTZURmJFZ05MeTN4T1o5V2xhU3Q5bkNZR3dNWndUeE9TLUpMREtEZ3B0YWQ0QjVYNkpMVjJVZS0weF9mbnJsWEJDUUFxb0tzLVpDWW4zajZvTXF1NFJpb2F3VjZwMTVFT1drYzlPeTF2ZVM3MWpwLUZLU0c3ZlZQ0gFWQVVfeXFMTkZyNDZyZUM1TXZ0dy1KWGg3LTcwVjctN1JPRDB3aU9iUWVLYm84MDNkeWdkVUItaHRRcXQ3OVRXOW1DbEFTR3E3Zk5XZnNpVGtNeG9Hb2c?oc=5) (Fri, 13 Mar 2026 20:30:00 GMT)
- [The Practical Implications Of New FDIC Stablecoin Measures - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5GcjQ2cmVDNU12dHctSlhoNy03MFY3LTdST0Qwd2lPYlFlS2JvODAzZHlnZFVCLWh0UXF0NzlUVzltQ2xBU0dxN2ZOV2ZzaVRrTXhvR29n0gFWQVVfeXFMTkZyNDZyZUM1TXZ0dy1KWGg3LTcwVjctN1JPRDB3aU9iUWVLYm84MDNkeWdkVUItaHRRcXQ3OVRXOW1DbEFTR3E3Zk5XZnNpVGtNeG9Hb2c?oc=5) (Fri, 13 Mar 2026 20:30:00 GMT)
- [Can SoFi (SOFI) Leverage Its Mastercard Stablecoin Tie-Up To Redefine Its Fintech Identity? - Yahoo Finance](https://news.google.com/rss/articles/CBMijwFBVV95cUxPOGhJTmM3NmJCSldndDNUYU40b1QwT05ETW9TSmFyMmpRSldHcDJ5ZXljSmg0VlgyNW9XNG55dGQxTEQtdjVwVnZNM0U2UVZzTEc2ZDhYZmc1bmtWQ0JVY1JVcGdodFJ2WUN2THlSM2s3U25rX1h5WnRrUmNnRDBqd05mWFV1azd6ellYME4xZw?oc=5) (Fri, 13 Mar 2026 19:09:38 GMT)
- [Sky slashes buybacks 87% to boost stablecoin reserves ahead of ‘massive oil shock’ - dlnews.com](https://news.google.com/rss/articles/CBMimwFBVV95cUxPWmVpTlE5cEdDdWwtS2h3NXQ1WUlsN1NaTW5PaFl4X0ZseDNEN2xRbXlIYjNKZFNxLWpCTFJwZHJsTE5SOFJDaXBjSEw0c3BGc2p0akxaUnA4TGtrcXZFS2JiVE02MUpsYy1pN3JRMTFQQ2JVZUNnZHJYRmFrSUJKbGhnVnRNQV9DMVY1c2tURHY4S1BmalJPTFVncw?oc=5) (Fri, 13 Mar 2026 11:34:23 GMT)
- [HSBC and StanChart to be first Hong Kong stablecoin issuers; European stocks fall as Middle East war puts oil above $100 - TheBanker.com](https://news.google.com/rss/articles/CBMiekFVX3lxTFBBT3RxLXhuemN3VEU0eTZvRFd6bzlOLUlERTZWMHlMcDZYV3Y1VzQ5Uk15ekxIdkstLTE2V0prZ1BTeE1zdThyaTZBdUxvekNRR1h0RDBpM0R0R3VSU2RWaXdIaXYtTVFEMHg5bHpxRWxaOUROMjhNeWRn?oc=5) (Fri, 13 Mar 2026 11:17:27 GMT)

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
