# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-06 04:25:05 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$280,143,156,652** | 🔴 -0.46% | 🔴 -1.58% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Takenos Raises $7 Million to Build Stablecoin Financial Network in Latin America - bloomingbit](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5kaWt6Z3BIeHhfTzJYOHAxZWZxenVKbHBaSjE0ZE1UT2xvTmM1emVIbjAzRWRxaDBxcXRhZTRJZk1hSVRTMUI1WGpLWmlIQXk4UzhEbA?oc=5) (Fri, 06 Nov 2026 02:51:15 GMT)
- [Anchorpoint Completes Pilot of Open Wallet Verification Framework for HKDAP Stablecoin - Hubbis](https://news.google.com/rss/articles/CBMitAFBVV95cUxPSk9KTUZJei1XZUpRbHRZeHdKMUN4YjFtajZkZWJEbWhGZmdHeUhISnVaRGQ0X08yVmxBVHVITjVoazFxNEp1S0ZNNTBvTGFBaURyaVZYMlVNQUxiSW5Za28xN3JoSERpcVdmaVRXdEt4RWI0WF9LQW9CYUtWa1VmU2FQcGZ1M3owZl9lcFd4aThjeFRWZ2JydUlicEM2ckxCOFRMQy0zOU1YckNIVFZNR0p2M04?oc=5) (Thu, 05 Nov 2026 23:26:11 GMT)
- [XRP Ledger Welcomes New Euro Stablecoin - Cryptonews.net](https://news.google.com/rss/articles/CBMiWkFVX3lxTE42MEVDVm1sZmNvQ0dPRXZwdUUwTGt1VFBNRGhpbjA4c3Z1WGczb19XOGpZdVUtUVdxczlNUWdBZzVfNmNDOXpQS0N1T2NaNmtYWjFWV1JQSy1oQQ?oc=5) (Thu, 05 Nov 2026 22:52:04 GMT)
- [Solana: Samsung Wallet adds USDC through its Stablecoin Account - 05 Nov 2026 - TradingView](https://news.google.com/rss/articles/CBMi1AFBVV95cUxPRjBXc3ZOYVRCa1d2Z2c1a3RIQWRJcnZoNHdBR3ZVelYtY0xGQmxCRmNUOGRlVExhRVRBZUppdVc3dmxKOEdjSjgzU2dqMzRWM09XZS15d1hsMmZsMVpoa3NLVjNtM1YyVXA4bll2ck14NmZiRVY5WXR6ZWc5NDdVYThBd29DUkZJaDlOaXhkR09kX09wdHY4MVk5WmhYNXhDQW44UVRoVUEwNEJPV3pydE14U3ZjZnZzVHlTdU16LVh0RWRYVFF3RU96UHc5VThRTWk4OQ?oc=5) (Thu, 05 Nov 2026 21:21:56 GMT)
- [World Liberty&#x27;s WLFI Buyback Could Draw on Stablecoin Reserve Income - BeInCrypto](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFA4dlBXMm4wSnp2MjJKLUFNTUkydHhsTkJvUktkNm56S291OUlvc0RnVld3TnZOblVFS0k4a0Vra3pFY3EyeGxmLXc0aTNFeU9KMHFqbjBPWlBDZy1YMnVMVDhmTmQtRGM?oc=5) (Thu, 05 Nov 2026 20:30:44 GMT)

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
