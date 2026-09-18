# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-18 02:26:05 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,280,187,093** | 🟢 +0.04% | 🔴 -0.18% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [dtcpay closes $25M Series A as SBI Group joins stablecoin payments push - Dealroom](https://news.google.com/rss/articles/CBMipwFBVV95cUxPQWwzNEk4V0cxa1ZHMlJUeWl1UU9VOXNxbmdieU9RZy1hdmJXQXd3RDNNellkdTFjMXRMUmw1czZsdUtfa3dnRURTbUJzQU5iZHVGUWNZcFJxMHVLbkYyVDAza21kbmN5WDNyRGROT0ppdGJ4cmVjVkgxRDJTLWdoYnE5V1lnVHlvWkhuaGRIYlNhZlZySmVwZWNxSmhRMlN2V09ETTJtRQ?oc=5) (Fri, 18 Sep 2026 01:36:26 GMT)
- [Stablecoin Weekly: Digital Dollars Become the Only Game in Town - pymnts.com](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNZ2FuUm5VR0Eza29MQnA3dlMwY3NtcTFoQUxQcEdzemVMTUlqcno4dHR4RlVJOWc0ODBCSVRWZjJFU2c1VTZDekxUcFdfWTIyMlRaUEd3cjlUdm5XS0RZRVdRcTFtQnJpR3NRZzB4Mzk0ZHpRbDh1ZDRNZktIMkl0TUNQdDM5bENXSXoteG9fbTNZbzBrOEhDNHdDb0RUOVJodFN5UF8yVldaUQ?oc=5) (Thu, 17 Sep 2026 20:52:13 GMT)
- [MoneyGram Just Launched Its First Stablecoin-Backed Visa Card. Here&#x27;s What Crypto Investors Need to Know. - Yahoo Finance](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNa3BxOGZ0eVpHWXJEMHd4dmRlVkpLRzF2MXZtc3pTYkRtM1FYZkxaTmk2a01vTTlPN0FVQ09PZTFpNThhaVFBaTFwVjBmVHlBTlhmeUxPYUR5OGQ3NkFGcmRpWUVxMnpNTWsteTI3WG8xd0VDVTJkYXNOWDQtU3NYd0xWTDk5dWlVMW85RjhjZ0d5OHdGQ2JBUUE3c3B2VUJtWlVKZ0U2MzA?oc=5) (Thu, 17 Sep 2026 20:43:00 GMT)
- [What Hyundai learned from its stablecoin test drive - American Banker](https://news.google.com/rss/articles/CBMinAFBVV95cUxOTGVqSnhRWTBCWmVCMmxaNnU0dUxvVGs4RmFwMTdTSG02SFFrRnk2OEZDd2k5a0pybjVBX3dyQ0cxUG9rMVFZREFOdTBueU5jSHlTVzhqUDA3T0N1ZUlqaGxYWGU4NHlwMVRSc2VPU1VRZ0xEZjRsbVQzRkpLOEExN1IzLVJ5NGpyRnlQZFllMW1RbzREZnpNU1FQelA?oc=5) (Thu, 17 Sep 2026 20:29:00 GMT)
- [WisdomTree Partners With MoonPay to Expand U.S. Access to WTGXX Tokenized Treasury Fund - NewsCord](https://news.google.com/rss/articles/CBMi6gFBVV95cUxOZ0JDR0E5bmdGWlVGVzd3aHoxSmhvZ0RiWEY2LXBEMlJsTk5kNlc4SHZIcnVJc3k5YzZRazNlOFJ5R2M3dXE2cTNERkhHSWxWT2R3MnlRYXpJNlo4MmY3dTJwYVJVNHpGa01yQzhKTTRqVWpUbGk0VWNWTURNSFJ5MnZLNVZKSV8zeUtRaHZVSW5qXzh0Sk1yaFhPbi1MTDVVaVR2eC1kZG1oTzhUb1lVQzVSMmRQR3U0Wms4U0ZEdk52MXFvVlRpbGE3cjNUdWl1MUNUcDU4eGdoeGJLV0dRNWdOdG9wU0Jsa0E?oc=5) (Thu, 17 Sep 2026 20:25:06 GMT)

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
