# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-19 02:25:40 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,913,635,060** | 🟢 +0.22% | 🟢 +0.01% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [OCC Approves 3 Trust Charters For Stablecoin Businesses - Law360](https://news.google.com/rss/articles/CBMimwFBVV95cUxQV3dRR3FSNzJET0hzaXgxM0ZCWGlySVYzc1BSQkk5dkRTc21PZzZNQUNyVURIT0F6eGFmM3d6ejhpNUdYMFp2amUxRmliVzBlb1RqWXhqRUI2RkdEcXNFcTlaOUJLT2ZpeFJiZFo4SHlLbHEtWlZBZWZIeFpVUW91V3U1VURnSTFvblRhMmR4WUUwNFRLaHEtZjlWZ9IBVkFVX3lxTE5fUk1lMXZNS0c4RmRCNVR0UEtyQ3d3clA2eTM2dTNZMThzRURUZW5Nc2JEOGhRYTFFdWlDVjV5dkIzTDBJLUUtN2tudjE1SEY4WC1CMlR3?oc=5) (Sat, 19 Sep 2026 00:29:00 GMT)
- [What Is a Stablecoin Reward, and Why Did the CLARITY Act’s Failure Keep It Alive? - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxQeU5EVEd3VDR0N29COUdTSGdUbG54Nl82cUJlZGNzVnpkUG5Uc2dQckE4Z1RHQ1U2N3VSM05CRThZSjJ2TFdiZ1RfOGJ0dFhrQW1fYTJHVmlHc2dsbURjWmFqdjYyTlR5VHVLRjRwQk5nSDJnRFRNR1V5V0lqSmR4QlV3d3A0cWFoUVdacUxvTVNKTjlwSlNqcS1rLXVnLW8?oc=5) (Fri, 18 Sep 2026 23:10:49 GMT)
- [Exclusive &#124; Stablecoin Company for Big Business Gets a Conditional Banking License - WSJ](https://news.google.com/rss/articles/CBMiugFBVV95cUxPakFkbDU3cVdxT3JLMmpmOHlQcm1leGoxaXJkTVZRTTBnRENQQnoyWWJVNXNWaFVPbERUdWZ3cVVjX0UwOV9XdG9feGlBMEdncjhacGt2OHNoSlVwVDZiSEhOc2tPUEV2Q2VvbTdYSVVfQlBfNUl1eTZDZC1zTTh1VGp1Sk1MOXFoSmNQUUJSa3VqbHJDOTl5WU1qZzZiYWItcGhfNGppQ1JQQ19ZUHo3WEtUVDVSVDNnYXc?oc=5) (Fri, 18 Sep 2026 20:05:00 GMT)
- [Visa’s Stablecoin Settlements Grew 15 Times in a Year. Is the Stock Still a Buy Near $370? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiygFBVV95cUxPZnBhYXpyNEZPMkhidmYzdGM1ZWpramlHc3hRbFJGOXFEYnBpa1hhR1VsNGtjd3hFNDR1dXY2SHdqb1BMWGgtcTNGTzV3VTBuSE51S0Uza01SQWtkN0hZTWlsWm02aVloUXF4d3JrOW5ZQU5LNS1kU2hqSlJkUENBY1dSN2hFZGN5QjY4aElmQ2ZaRlBvLUhta0dHUHR4LUFfcmx3VVp1WW9wRmk0b0V4Mnl2T1hfVjVTaE9jOFA3NExBcF9rakZMMHpR?oc=5) (Fri, 18 Sep 2026 19:55:00 GMT)
- [Why SBI just put millions behind a Singapore startup’s stablecoin push - cryptoslate.com](https://news.google.com/rss/articles/CBMimgFBVV95cUxNU2dUMFhicmlrOEwtUXFQT2pqb1ZJaVV3OWhVcS1XdXVJQ0F2MHZNNWFiLXRkZDVsbkptRzNKM1RjNW1vbWh4djNmT1VyMk1mUFBJOFQxTmk3bldvdkxhVDN1Q0w0LUNBZVdSV1hqXzRRLVNYc0tvLTY0Uy1hQjFxWFVfekhMWjkteXJnd3Q2a0Z1b0l1WXVFQkVn?oc=5) (Fri, 18 Sep 2026 19:50:45 GMT)

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
