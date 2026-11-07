# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-07 03:53:13 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$278,627,387,219** | 🔴 -0.54% | 🔴 -2.01% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoin Holders Eye Remittix Earn as USDT and USDC Deposits Meet Live Maple Finance and Fluid Pools - StreetInsider](https://news.google.com/rss/articles/CBMi9AFBVV95cUxPX29JYXN1UTZYdWluWFRUNTkxLUo3aXo4dEV0YXI3X0ZZcXJTZFhKS3V5dGx4TnVqcmpDVkdqZFh4blUyYUpQZG1NeHJmSkhhdUxBUWJkUFhXckR2LUJKT3FGNmZGWTA4ZmhsVkh6YzZSUFh4YUJ1SHpIOUQwWTNOQTd3SGRDRmRlaGgzckxnR3kwRU9HRERfRXFkcDE1eDFidVFtOXQtbUwtLWNhWDg4VVd4anZ1ZHNEbE1JQkhuc1FCeEdKQlFGVkRrdXZQcTVsVHZLdUhqNFo2d2pEWFV4Rk5VcU1fb3BkcFNwUXFEUkNUR2Vl?oc=5) (Sat, 07 Nov 2026 02:02:14 GMT)
- [Figure&#x27;s Karl Samsen on YLDS, a yield-bearing stablecoin built on Stellar - CoinDesk](https://news.google.com/rss/articles/CBMipgFBVV95cUxPMUN1Y2UwSEFuMkZzbXFteEZETG5kUFkxaEVwREFod1dNLWRCRDZrNkIyOEdIQ1ZkRlR1RXFiOWhWa1BhenoybE1YZVVUaFlqYmQ5cGNOY1dLVGVRdUtRMzl3MUJKRlJYZ0s4ZjJBbHlkMWY0OWxMT0tRZWNpSk5fV0V1WlFlOUdDYXJ4dzJ4aVNhS0FBQWlPYVFqc1EtQmpXck1YQ0Fn?oc=5) (Fri, 06 Nov 2026 22:39:09 GMT)
- [Samsung’s 82-Million-Device Bet Shows Stablecoin Wars Moving Beyond Crypto - PYMNTS.com](https://news.google.com/rss/articles/CBMiswFBVV95cUxOUVJORDhHTjJjRmNmRGp6NUc3TTZaNkI4UGo3ZlU0ZVJXbC1zM1hHa3o4Vk50Zm1HSTgwVW1aWHhVemVlbFpvQlhQM0tMeEFIZm5iUnVoeWw2YVN2dFBfdEZ5MHpVdVk4QmNQLTFrTUtuVDV4dnNoMHF4ZllJV05VVXE1cmtySVZwdjlYc3JrQTFCbFdGcVgyel9BSll1bjZxQ0ItYVRjSWNFN0NxREFzb1g1WQ?oc=5) (Fri, 06 Nov 2026 21:55:19 GMT)
- [Study Finds Most Stablecoins Fail GENIUS Act Requirements - PYMNTS.com](https://news.google.com/rss/articles/CBMilgFBVV95cUxPWnYyY1lQVlc1SEtUT3p6U1pwWUFhaTQtXzNVWURkREJFQl9wRWhpdTJxeEU0V1lxTGVGVGduVVZYSklhNU5WVlBGb3dReXlYZDhWS1ZnRi1kQzQ2eG5Xa01CRHJOS1J5S2haNmZIWnFKSzFtQmFud2VLYmd6ay1hWldUUFJhUWM1UUdsYnh5NW55bnp3MWc?oc=5) (Fri, 06 Nov 2026 21:55:19 GMT)
- [Nigeria Erects Strict Stablecoin Wall, Demanding $11M Local Subsidiaries for US Dollar Tokens - Finance Magnates](https://news.google.com/rss/articles/CBMi5AFBVV95cUxOZHA3dTZuZTdteElSVmtUeC1tUy1aN1pJemxzT0ZwRjlFQUJCT3pneEJNMTFtTFZDeXNEZ0dDNEo4bE9KOW1zMnBtUzk1ZldvX0M4T2IzSGpfV2hTcVhRNEpTRFZ5TzVQWWVoVDFWT1N2RXRmMVlFUFBwOEs5MVRwZk0tNlBlSzhnTFRGamFjV2gtbWNwWFpTSjRzQUdpRHluN3BkTjcwaE5wZHNoMTk2aG4wbFBILW9EQ3BWS01jeVBwSmpjSVc2LVNOT3k5TjVDc20yMFNZdFF4SXVXdkJhN3VFNGc?oc=5) (Fri, 06 Nov 2026 21:54:00 GMT)

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
