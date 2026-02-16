# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-16 01:22:05 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,650,756,713** | 🟢 +0.01% | 🟢 +0.05% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Cardano Sets February Target for USDCx Stablecoin Launch to Boost Liquidity - Yahoo Finance](https://news.google.com/rss/articles/CBMihwFBVV95cUxNaWJvNWk1WHlJdG9kSUlnby1EN1lndjhMbGs2UGk4X0Eyd09PNmdoR2d6dkhDeU1semFtVWdmNnhtUnV5Rld1aFlFMnZ2MXI4OFJmZ3hxdVltT0VVT01JVThFTHQ3ZzhlU0FyM3BDOVg5SDB3ckp2X3RBRU5uRW9vUzVPRzBfdG8?oc=5) (Sun, 15 Feb 2026 18:30:43 GMT)
- [Coinbase CEO: Stablecoin Rewards Ban Would Be 'More Profitable' for the Exchange - Bitcoin.com News](https://news.google.com/rss/articles/CBMipgFBVV95cUxNME5iaGM4RDNSVGhkVDM2STZWREQzOU1veTgzYXZWY2xOeVVGU0tmY0puUU9yQm9iTXFDWFZUekhSenJDM2RUamxRMFlMM1FzT0VFOV9fWjA4M0lHNHB4QlcxT056bnFJUnJ5VmcyZnBPNUJ6TzM1aWkzUm0wc0xBN2VjUE5EM3pqaTg4di1qdGc0Ql9JZmhpdzlacm5xX2NxSUdMTGNB?oc=5) (Sun, 15 Feb 2026 18:00:33 GMT)
- [AlloyX-Bahrain FinTech Bay pact targets next-gen regulated stablecoins - Stock Titan](https://news.google.com/rss/articles/CBMivAFBVV95cUxOLW9PX0dnbVFTRkRvNUpIWXJKUGJRaHAyTUJhSTZkSlU3Ql9RSVdkZzh5eExBTnVaemhEM0xVanJZVHdjV3pBSUxLVUkwd2lqUUk0dTlKbDc0V2VDRWplaVZ6eTZabFNnZGxrSHJxcV9Da3AyV1hfM3lEdnVlRkp5cVppRzhPQlFmN1hNNEc5RVQyMmxrUDRoSFFKUGEwNEZlNWRDeGxtYnptYlVWdW9nM3RzcjJUVG5DZk1fMQ?oc=5) (Sun, 15 Feb 2026 12:00:00 GMT)
- [Stablecoin Market Rebounds Fast—Nearly 90% of Recent Growth Packed Into One Week - Bitcoin.com News](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQQmFfZlI5dFY4UTcwQWZFU3h1NlBLT1dzUEZrNlh3NGowb1J6MEVCcHluTGgtN1FGdUx0RkRFc0NKbFJjLTZDZnU4YjU3dk1xM2lEeVZaVWJZOFh3QmhaZ3RfMjlSWkpnaENvZ0JLQ2NoUUx0anMzUUxPekVoN1o3Q3p4ZHVaZ0RsekUxaUdfaFBVbUpNemVaYlhneE84cFBsX1IyTTRGUjU?oc=5) (Sun, 15 Feb 2026 02:32:00 GMT)
- [OKX Ventures backs RWA stablecoin with Securitize, Hamilton Lane - MSN](https://news.google.com/rss/articles/CBMiswFBVV95cUxNNkRtZy1QUmNJbllxTlBtUEpDN2dpZmdpeDY2Vi1fbnNRRHU2RkxwdWxnR042c0s0Q3ZYXzVkQi03NU1XdlYwWDdGUlVRTHk4MzNQVS14OGhEYmdWdUpGUWZqb0NmVC1ocWlrTElYSzBuRUtGRFBxR0lDRFg4ODFWR3YxQjlSd1lVV205SmJhRWJZUF9rY3J3T0FRbktOWlN0RHpyX3FaeEVSZDgyVkt3QmRTSQ?oc=5) (Sun, 15 Feb 2026 00:52:30 GMT)

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
