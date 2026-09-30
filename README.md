# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-30 03:12:49 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,074,669,289** | 🔴 -0.03% | 🔴 -0.07% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [FINANCIAL TECHNOLOGY—Treasury issues Stablecoin Certification Review Committee interim final rule - vitallaw.com](https://news.google.com/rss/articles/CBMi-AFBVV95cUxQRmpndkFscHZscHoteThHRGdTRHRuc2JYTG52VHd1SlhfZWxjVE03Rl81QmlCektwR0FSUklTVThUeUgwd0dVM2kwdTI3cDJQTlJucllmN3dMMjVfazViZ0Z0U1RiaUg1b0JEaEtIUXdNSFJhTlhreHpNY2E0blVTNFpEQ2pDaVZiSk9zbU1PSDQyak9UZlNsU1ZQRTJoV1FyeHZwWWNUOXRPMEtlVGotQVlKb0VleXBlN3dvOTRNbnV3blFOa3JKYU9TTHhaWmVETmhWQVpPa29hRnBLN3VkajRIODZKeTU3dTQ3TzlZcjEzWGJ5NUNyQw?oc=5) (Tue, 29 Sep 2026 22:19:14 GMT)
- [Aztec Labs Relaunches zk.money Privacy Wallet On Ethereum With DAI Stablecoin Deposits: how 11 outlets framed it - NewsCord](https://news.google.com/rss/articles/CBMi6gFBVV95cUxQeEVsOV9IVUc0ZG5NYkxQSWktc1gtcHBWTkF2dFc5YWtENFNfYVdvZ0xwVHVuNlZ6T0NicHJBbXpDNXhReVRvUjUwczhOcnd4TTgzRDdKcENTc3BYLXEtVjNCdEJKTFVWa0Z4dGFVdDBhOHBZUm5PVTdCcy1kbkxXWWZqMVY3QmdKaU02R1lEMFVrOWRIMXg0dERuY1JEb1o4ek5hbm1ZRHB2dDNkR1NRM01NZlJwdW9aVzZGU1VReUlVUVpISll2bkdCSjRNWHBqcDR4bjQ1RFROR0tpUkxTQkhwSVpubDVMZ3c?oc=5) (Tue, 29 Sep 2026 22:02:26 GMT)
- [Polygon Passes $3 Trillion in Stablecoin Transfer Volume - Polygon Labs](https://news.google.com/rss/articles/CBMigwFBVV95cUxNcGc4SnNLb3g3aEVrNVVENUZ4ZXV5OEZKU2x0YTJYZ185OHMtQWNwMzAydmZPb0gwOGtVT09OTGlJRjhjLUNyUDBjalM4OTE3NDZ0VmZaY25xWVppS3lfODZrX29pc0x0SWNsMzJMdWFIWHhjRFZieGxKZ2g2c2ZZX2hzTQ?oc=5) (Tue, 29 Sep 2026 19:58:45 GMT)
- [Fed guarantees 2-day stablecoin payouts, but $76B remains blocked - CryptoSlate](https://news.google.com/rss/articles/CBMikgFBVV95cUxQdHhWVmM2emJKSUg2WUVFR2JxUGtjYjdKOXlPUnNHZ0tTTGdLTWtUWG84UW1ZaE0zZ212aEIxaURiQV9FRUxsQ2h5QXJmczF3SERqWDdNMnQ0dHRpbFhWb3BUWWs1cmcybGh2amhQS1duTXdDQVRsNEt3N1pIenNWLS1STEZfWG8wQ2hDZXRLNmt6UQ?oc=5) (Tue, 29 Sep 2026 19:50:36 GMT)
- [Private Stablecoin Payments Are Back on Ethereum – But Is the Software Legal? - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUF9NbUVpeDJJSXJDY3BzMVQ4b1NSQnphZzZacnNlLTh6TTJwXzZBSHpnRWNoWFZIc0hiRVlXUlJmR2xXX29RbnVHb0ExMGRKcTREWEJ4ZkZlOTEtb0did2pFS0FrNUx2VDUzSTZHcVpTR2xhMWpNOEVBQ2FnTUU1Mng3V1kySExHS1VBNnlraHcwY0dYckxnczBNVUZ1MTFNWTNRTG1HQ3hYdw?oc=5) (Tue, 29 Sep 2026 18:47:19 GMT)

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
