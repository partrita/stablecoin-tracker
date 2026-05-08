# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-08 02:12:41 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$301,495,963,888** | 🔴 -0.03% | 🔴 -49.70% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Coinbax wins $20,000 PitchFest prize at Consensus Miami for stablecoin compliance - CoinDesk](https://news.google.com/rss/articles/CBMixwFBVV95cUxNd1owU21HWGZJamFubU15Y09CUzJmOWRsQ1pMSmdUUmtySEpvVVYzd3h3S3E0V2w3S2pVOUZSR2o0bjMwWm56V05jTFdvNjFwQnJqMG1EZGc5M1YxSlFfNE5jTnBfbkROR2M2SzFGTGJydFRPcDM0Zk53V2FUYzBSYmM0aUZDenRKTVZ4amFkdTc4NDFpNm1CM2xDT0N1WWNxY3hQcFJCcnR0Qi1wLWl1aDJGdi1sWFBRTXRwYWE0allzN203bnF3?oc=5) (Thu, 07 May 2026 21:50:38 GMT)
- [AI agents and large corporates will lead the next stablecoin boom, executives say - CoinDesk](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQU1JlN3dXVFlwR1AtNm5qb0hBTUxfWHJNOV8zQnlVMXpKMlZRRngxQ0JET2RUeV9PUW9tR2xuWnNnWnh0MGZCSDhFZDdGUS1UTDVPUy1IOWNKTzNSVE5TLU02dGotSjAzLUZRYVd1dlRDMWFfQVZyVVdHWjZiUzJUUEkyTURDYWNlNU85SXVsaTNFVl9DR05DOFY2WXIybEhybDdPM0ZVMEFUYTUybDRLekRiY3ZVX0s0Uk5wNFFwM0p3MEE?oc=5) (Thu, 07 May 2026 21:13:22 GMT)
- [The stablecoin queue: 20 banks and tech giants are waiting to issue tokens with Anchorage Digital - CoinDesk](https://news.google.com/rss/articles/CBMixwFBVV95cUxOSWFIVnBCdnJuVGpBdGNOdUhXb2lrOEU3RUZKSmg1RlFEVkdlV2x3cGp6M3VaTEdJdk1VUm80UUFaQkE4b1lFa05qTU80bUNuankzRFItS0R1MlRuSUVKOGxob0FXbDNfb09aUGVmTGJoWDZIbTRGenBCVGZpZHJ3Tm05SzJNdDB4eHBBTjh5Q2J0MTZpN3N1NVpOZHZxU3hPWFNQa0VKR1UyUG5GeXl5RlpKaV9rUXVLdTJ2QThqVVRtSTJYOU40?oc=5) (Thu, 07 May 2026 16:36:58 GMT)
- [Kraken parent Payward to buy stablecoin payments firm Reap for $600m - ledgerinsights.com](https://news.google.com/rss/articles/CBMioAFBVV95cUxQT292bVVqTVIweGdsVlphTHNod25Sc1pjX19xTEg4TDd2M1hhZTVXd1pBcjg3R1A5N190ellEai0xaVF3RG1sX2lXUEliUlIzaUd0aGRwSEE3cmV4RlhpLWc4Ukw5alhtcHoyNUprMk5hQVMxdmRld3JVYnEzY0tCUzlkV2xBRHcwQnhzcXR3ZTVfY1BuNk5TczhFbE56T3Zu?oc=5) (Thu, 07 May 2026 15:13:46 GMT)
- [Here’s Why Mastercard Is Betting Big on BVNK — and Stablecoin - Global Finance Magazine](https://news.google.com/rss/articles/CBMid0FVX3lxTE1ESUZNYTdCejJJaFdkRUJ1anZqTzN3OENBaXJJVkQ1UTlkODc0RjZUdVNDM2dKWWZJSXZFckdOS0ZjQ05Ha2pyNmlnWFBFYUNkVVpHQ0R4NXI5a1l3cjFFcmZxbFFDcXRwekxvTG9nSzhnOGd1VW93?oc=5) (Thu, 07 May 2026 14:57:01 GMT)

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
