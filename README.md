# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-04 01:45:44 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,640,859,534** | 🟢 +0.07% | 🔴 -0.41% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Fintech Dakota Seeks OCC Trust Charter For Stablecoin Biz - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTE9fWUk1VlgyUmdqX1otNS1aUHBXMjU1bGp1bTZ5Ql9Pd2o5X0FHaUU5eHRjVVNKUUVCS0lGclhlV3g5U1RXUW8xbGFMNklNa2RfR3pGZ25R0gFWQVVfeXFMT19ZSTVWWDJSZ2pfWi01LVpQcFcyNTVsanVtNnlCX093ajlfQUdpRTl4dGNVU0pRRUJLSUZyWGVXeDlTVFdRbzFsYUw2SU1rZF9HekZnblE?oc=5) (Mon, 03 Aug 2026 22:52:00 GMT)
- [Yellow Card CEO on Funding, Stablecoin’s Global Foothold - bloomberg.com](https://news.google.com/rss/articles/CBMisgFBVV95cUxPY2pReHFUZ08tYWxGVEI1N0tUUHRYdVR1ZDZHUDNhaV9tcU80dHotMDRmbnMzNmRienpOd3dTd2FBcEwxaFFmd2d4d25oeDFWYjdoTEZkc2V4MXR6b0h6VmhYLUlxelY3Q1JDUUpKb0RYeHBhdjFPY1ZTOURpUDlSWDFla1g2X0Y0MW42SER5ZWdmZ2VwblNMVkVkWlhoZ2tqcEp2U3UzdFpMOUVQZzctRFh3?oc=5) (Mon, 03 Aug 2026 21:27:44 GMT)
- [BlackRock Targets Stablecoin Issuers and Institutions in Latest Tokenized Funds - Coinpedia](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQSWo2OU82NzhQbGktVU1GSnVaSnVBOU8tUWs5SEhoWEVkV1JmSGwzeEZFT0c2Y0IwQ25IaFdQalJEUS05aXc2V1FRWjB3LWE3WFByQWwzZHV5emw4bTN2N2ZETVFwREdWWFk4aUZpdGE0bktEck5xYVNnMmowZ21UZDNzck9BS0NDdEJvN0kxQURObnlLbFpPNzFjQXVBc1IxbjctelRWTmN5OW_SAbABQVVfeXFMTjBIRVZjWEdvWHl4cHBRYkNvWGo5S2VHcWFNbUdheDZJbS1SNW9tMGFXVF9HRzdackdCMzVVZnBvMkF1akhSME9CNGtlYkM4c2NmZmI0RjZDczhTdl96Z0VkQTVJa19hWnQ4U2ptdDVDMjJtc3A0cjhrblpQVGVIRm1tNWU2UzhneHZoem1nUGtLLXFTWV9ycFlQX0hrM0tKQ1BoMjR3LVBUbi15cnc1SGY?oc=5) (Mon, 03 Aug 2026 20:49:46 GMT)
- [Research Exchange: July 2026 - Bank Policy Institute](https://news.google.com/rss/articles/CBMiV0FVX3lxTE5TcTNUaTg3UDZuYk9KM0NkVnFvM0FUMXhvSlBxaEl1NllfS0ZHd2RJZU9LS3d1dGFwZ1Rockk0UFhBMGo3Yk9hMXd1R3MzSFlTX2poZkNzUQ?oc=5) (Mon, 03 Aug 2026 20:46:05 GMT)
- [What Happens to Correspondent Banking If Every Country Has Its Own Stablecoin? - Financial IT](https://news.google.com/rss/articles/CBMitgFBVV95cUxPQ1Y0U0hwZUt5a0ZPdmRQVUlHcmxmU1ZIZnhRZWQxQ0tKbjBPbElPTGN0T0hKcEhfMWV5NFRKTXI0RWRNUUh4RUhrb0tJRTRFYXVlTXFHMzM2SGIwbHNlc0oxV3JncF9IZmdzeWJtRnhsN1RtUjlFX2ctaHF0R1ZfX08waTI2WDVPS0tZcGN2LWdZV2VWd2Exd2lQeUNQdi1VQjFzTk9EU0t0Wl9zWkprU3lOTFdEdw?oc=5) (Mon, 03 Aug 2026 20:38:59 GMT)

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
