# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-02 03:38:41 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$283,796,786,453** | 🔴 -0.17% | 🔴 -1.29% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoins and the macroeconomy: Bank disintermediation versus fiscal space - CEPR](https://news.google.com/rss/articles/CBMipAFBVV95cUxPakNTOXdLeWgyMFd5NWRSclpvcW8xMGJnanU5MFFUYWJfZUU4UGkySTFiRktUX1hvVmJFT3dpc2dzZnd6bzd6ODdrbnpFSW51d01OaTBHOFJzY2EyWEQxcUtSdW9OOUZ3NWQ3RjYyVkJuNGZfTExKd1NDQ2tkcUZBS2U5OUtRS2VuSWhGR2xoeGlRcXQ2d0ZHcUR6bHk3bnVEeDJEMw?oc=5) (Mon, 02 Nov 2026 00:45:00 GMT)
- [What Is RLUSD? Ripple’s Stablecoin Backing and Redemption Explained - The Defiant](https://news.google.com/rss/articles/CBMitwFBVV95cUxQUUdSTHJUMmQ4MXN1TW9nUEpLRi1BLW9uX0pVNXp0T09ObVlud2c2WnNDSk1hR0ZjcUgtRXhrYzFSNllvQnMwSDJXdGFOWTJRVG9Fak1DTUdUQXktNFpYZ3dCZGotV0pWWkVXNjJUQ19SbGFEaTVYb0FuM1dnZjc5dUVhLXNUV0xIN2Q4bjZMYUppNzFHbW9DTEt6M1Y2MlZPdEY2enlpN3JfV2ZJWF9CNmZidDJteFk?oc=5) (Sun, 01 Nov 2026 22:39:10 GMT)
- [XRP Ledger Stablecoin Transfer Value Reached $14.09 Billion in Q3 2026 - www.tokenpost.com](https://news.google.com/rss/articles/CBMiWkFVX3lxTFAtcnBwN3BZR2NvT25neGEzT3RKQVZyVnN4aTdqMVlNVm1kZGg3VUtsQ2tHS3hLTW5GZzhHb1NHTHZyY0wzQ19xb2RvU21zS1RYNlNhRUFVZzBlUQ?oc=5) (Sun, 01 Nov 2026 20:51:00 GMT)
- [XRPL Stablecoin Supply Tops $1B as RLUSD Captures 98% of Market - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE0tdC0tVlhYckIxd0hYSG5sX201OU9JYnFHNEFYN3JZNzZOcEdTSWJaeXNsaXl6b1BLci1jb2s5VXlfclFKUWJDYkl3TWc2Uk9RRENuMGJ3aW03VHlhYUxDLTI5cEEyWGZxNEhxSEJ1cUNpWmFrc1E?oc=5) (Sun, 01 Nov 2026 19:55:00 GMT)
- [Standard Chartered Predicts the Stablecoin Market Will Hit $2 Trillion by 2030. These Are the 3 Stablecoins Investors Need to Know. - AOL.com](https://news.google.com/rss/articles/CBMikwFBVV95cUxOZE5UclcySGl6MHhVV2p1TXJTU016M3I1alNUN0ZZMk9IZUFaVDYxSWdkSHhZdGNjNl9iN0ZoYlVlblJ2enNET1M2dDd1TXhfd1dlNW9oNWVNTHdldXUwYmx2Q09GeXlVVWhQeTNYdXdpcWxkOXFnTG1mQThpYUt4OVIxWXc5M3NJTml1OHAzVEdiYm8?oc=5) (Sun, 01 Nov 2026 13:55:00 GMT)

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
