# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-13 01:57:58 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,714,419,196** | 🔴 -0.02% | 🟢 +0.32% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoin Market Cap Suffers Biggest Decline in 4 Years - PYMNTS.com](https://news.google.com/rss/articles/CBMiogFBVV95cUxOd2w3Q1dvWHZycXF4NUNDTzUyUnZYZDMzZHJyb2h3R09ITy1zT09nR3J1TjN6U1hPSldNU2JnTEV0Z3BKUWxOWnZoWm5JQWF0WmhpamEtSFRMa3A4Z0RSaW1oWFo1N1U3aC1LSjJ2MExPRkFQRHFlSTd1V2kzaVpBSFN6eWJad3RZN2ttSm15STBBNzd6enZRa0h5WGk1ZUV2VGc?oc=5) (Mon, 13 Jul 2026 00:30:13 GMT)
- [Bank of England eases stablecoin rules after political backlash - MSN](https://news.google.com/rss/articles/CBMi-AFBVV95cUxPRUpPNERpSFdVdW9ySTgySUFxQWZWRUQ4TTgxRjdGRldxNl9zUW8zMzBoeVo2cnZWV0NGSG9JaXpsVFJjanJpZUFydlFDQWw2dG95ZkFBeFpJNWJrbGdIUUpKanZ2b3lWSTZ3SmhVcE5ZSkNGOERiNnBhd0MwM0VOOW9nbEJ2WExFdXhONi1Ca1FzdjhPamxobFE4NTdZdXJZZ25BaHdjOURrUURmb29BR0ViNzk0WE1QRFdSZlVZdm05TWVha3dTc2JwYmYxazYwa1pDdVRjMjNPMFI5aGFwV3U5MVI5RGdCQzhLYmRWNkIyOFFvWDUzbg?oc=5) (Sun, 12 Jul 2026 21:54:34 GMT)
- [Stablecoin Market Drops $10 Billion After USDT and USDC Redemptions Reduce Liquidity - NewsCord](https://news.google.com/rss/articles/CBMi6gFBVV95cUxNVmhWdkJmR29UX3NHcDNPTWoyN1A2VFF3ZjNfeU9wcTdHTVN0cVExQjNwU295bjg5Rnh4WmdVQk1OV1Ywd3czaUtNZ1RvRV8tZUZRZ3lvUEZuMDNvWkFxSUZQUTV0TE91Q1NkTXcyTndyRjVlWU5rbE5QbjF6S3VwX084b2k0THVtMmFVemtMeVhTWjE0MEhfVGNValhQbmtBOWpzeU5QczEtYWhmZURLYWhWdkpZWEFSYXZsMzdSM3piZm1EUXluTlFuSlBnVEF1dURVX1NYeFFrenVQRWtvcWR6eTFHbmhlb3c?oc=5) (Sun, 12 Jul 2026 21:50:37 GMT)
- [Plasma Executive Says Stablecoins&#x27; Biggest Opportunity Is Replacing Banks, Not Cards - CUToday](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOT3Z3U3NweVNKSHROenA2QlBNOVQ3cm4zbjl4aG52Ui1VYWotc3YzWTllcFlPZlZURm1vRDFUNVQxdmMzUnlMa1JoSGxPWWpPRTh2dGNKZTBXRWJ3amhxeWRKYl9WZlZOTnB0NktiU190aDVPcTI0T2pSa1RRNm9nZk54NnM0VnBCSlRyLUpJNUxGN1d3aDBNLXU2Z0RPUzRUOHhyTWJSc3JHNnVkWjhoMkQzWTVNRUxIV1BB?oc=5) (Sun, 12 Jul 2026 18:37:09 GMT)
- [Stablecoin market loses $10B as crypto liquidity quietly contracts - Crypto News](https://news.google.com/rss/articles/CBMijwFBVV95cUxPYl9qYnZrS1JIck1udnVTS2hyUVI0TE12a0ltSWwyRjlfNk9oYXZKaUY4d0JiWFhNVkEtWWZxUlNjSm1UVnp1dEtiUTdfVzB4SloxV3RZQXg0ZmZXajlKOXZzd1lPaGk3clhQdTFhWVlKNnYtWDJPalpLaDZoUzdwRnJwMm16WXRIZXlQdlI2OA?oc=5) (Sun, 12 Jul 2026 16:33:28 GMT)

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
