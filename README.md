# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-20 05:00:28 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$271,905,417,442** | 🔴 -0.59% | 🔴 -1.38% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [MoonPay Applies for National Trust Bank Charter to Offer Stablecoin and Custody Services - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxNYVdtYXB3bGxQTEFkTS1DaGFVRGNNM2hTanFXY0hwV0lNMDZFbW5DakRlWHlTZHlaOFRYd0RaOTg4U0stSlJ4Z3JLS09ReC1CR05DV20tTGE1b1BPVW1zQVcySm9pc1hISTJvT0UyQThfWWZsX2t3eUYxY1pteXVtVUp6ejY4SGp3QzJJZ0dQN2VNeFpYZG9fZTVpUV92Ym9ta3c?oc=5) (Fri, 20 Nov 2026 03:06:00 GMT)
- [Bitcoin Slides Toward $62,000 as Stablecoin Liquidity Shrinks - Businesskorea](https://news.google.com/rss/articles/CBMidEFVX3lxTE9zbGVLRHdUQkJkMlpDVjlZOHd1VDlFREFnVzF2ajNhMDZDcVlrTUJxSU1RLUpGMlBhMzRWMDlaWTUyaW1GelZxS3pZZmlsOG84ZWdFMXJFTGdNUnNzWE5YbnVXNGtNNEZzcnlEMElnYllBcEdi?oc=5) (Fri, 20 Nov 2026 00:30:17 GMT)
- [MoonPay Files With OCC to Create MoonPay National Trust Bank for Stablecoins: 6 outlets compared - NewsCord](https://news.google.com/rss/articles/CBMi5AFBVV95cUxQTy11RVRZNXpLZUZWd1JXVkFlVFZMUlo3eVlNdF9udGJKNUllMHNPMEV3aVdsOGlJdjJ4bEVzc2FJS09RVmt0aTVReHZ6WGpmVEFLWU9rcjlIbzhJc1lmQXVWRnZseFFaUEUyYXBJR3R5SzZwbFR4X0hpR1ZhdlBqX0pjYlJuM2VPTDY1NzMzaUlMNV85NTVkVEY3TEswYVAtNDUtMlJHQkZ1QVBTMTVpMjF0WjhycWRJeDNmYUg4THhNcFpyZVViLVFONjJoU2U5S3kwaHVLdEhKRnNlLVNnOHRCdjM?oc=5) (Thu, 19 Nov 2026 23:24:19 GMT)
- [Tether Takes Stake in Swiss Stablecoin Firm SCRYPT to Build Out Cross-Border Payments - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE44eW9RbTVsWXpCRjFoa3Y3ekZ6QWc0Y05DMmNzY09CWWJJNzh0QllhczhhbVFXeTFsN1IzYUJiUmxaanQtaTV4bWlMS3BmRUV5dHBaUHhhN19UTkhPNk9WSmVDel9rdnpxal9DSnVPcGVPQVJYbkE?oc=5) (Thu, 19 Nov 2026 23:05:00 GMT)
- [MoonPay Files for National Trust Bank Charter to House Stablecoin Reserves - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE9Sb1dkSGdFX09WeF9OaENsVHE5aGpJclhHZkx4bWZxSGNrTlgtWFhaSzgwMjh5bUVJNEFiUTNjdXNBU2QyRVB2Q0w0NXNjZ1RiVzVETlM4SmJ1QnZvR3hSYlM0azJna0FUdURLQzR5eGt6QU9Id0E?oc=5) (Thu, 19 Nov 2026 22:25:00 GMT)

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
