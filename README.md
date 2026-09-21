# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-21 02:33:30 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,977,836,097** | 🟢 +0.03% | 🟢 +0.01% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [dtcpay Completes $25M Series A As SBI Group Joins Stablecoin Payments Push - TradingView](https://news.google.com/rss/articles/CBMiywFBVV95cUxNbDFZUmY1LUJxejNKbm9fd1ZjNm9OY0dabnVXRGhHVmZIVXpGalZtdnFaRGlvaWxxR1ZCRTFRdDZJRWhvZ3ktNVhLVUZ1ZmdUV3FtMDZqSnc0Q19kcDJnRDFnUlkwQ1VOSTdnMGtqZ3pxeWROU2dyM3d1bkFBeHRuRjV0QmN1dG05OXlTSW10SlhUZjQyZWRZWFN6aU9FTHIyeGVoWEQzWjhheEdJOXU5Uzh6MXVjbE1vMkZxemNhOVJoVlFucWZtcHlSTQ?oc=5) (Mon, 21 Sep 2026 00:30:00 GMT)
- [OCC Opens Three Bank Doors to Stablecoins and AI Agents - PYMNTS.com](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPLWJwOGZVUDVlc0pBT2RPVE9DYjdtYWZtUDJ3UTEwQ2NwN0RhR01QNWZnQVpvdGRxRWwzejBjVmFpN2RyNC1XZlZOZ3FtWWk2OS0yQjFIZ0ZyS0FKcjZIQ29kZ190aXJOejlTaVdJcUNNSUlHcnB3TTV2MkxnMWNISXRyUzlGNTJNZEdKbnNCWGkwd0I5dVhWaEhfRHg4TTJVTWZ5RjBuNUM4UQ?oc=5) (Mon, 21 Sep 2026 00:22:19 GMT)
- [Stablecoin salaries can leave workers paying to access their wages - CryptoSlate](https://news.google.com/rss/articles/CBMilgFBVV95cUxNeWFGVi1ZUm9vZzR5amgyaXpBXzlaT2hERllNZERyQWxzejQxVk5OQ0NaZFVsd244NE9tT0RYaTRJS0VPNVJmTllJckNvVzRyd0NmNElHRGU1dzVqX3R3ajl5Q1B0Wjg5LVhPX1VBc2p2UjIySDJaSXBSWU1kTWMxbUVqRDBObG1PcThkZzJzck9FS2pVa0E?oc=5) (Sun, 20 Sep 2026 12:05:36 GMT)
- [Nubank Launches US Banking With A Stablecoin Account Before Its Charter Clears - Startup Fortune](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOMjJtS0RaMWVjQnM0X2k0V2JqOElfbXIxaWRmWWJ6elNLWUZka3A1Y295TnN5QzRiZmQwY2xXUXp1ZGZWS21TN2JCc1l0TTl4TjN1WDk4YzRUcVk3US1jai1VN3BjUkNwbVpaTXpIZGJNT2kyQzBCcDh1Ni1oRms3cm05VEpXOS1WTVZJdVY5THczYTBMdEpIcjdlQ25wZDFqMmFGNHhkckNJZw?oc=5) (Sun, 20 Sep 2026 05:30:25 GMT)
- [Treasury Drew the Line Between Stablecoin Issuers and Everyone Else. The Stakes Are Not Equal. - CryptoRank](https://news.google.com/rss/articles/CBMiygFBVV95cUxPbWk0bms1SmFROTU4Z3JLUHZTaDZscy12OF80TEdLbTBsalNETEF2dm93c3hPRWhxSFc4YmN5MG1hcUczZlR4SG02a1R1ZHp0TllpdVZOZVEtQXNQR2hGOVIwOW5RODZRay1FY0lZVjBsU2MzWFo5ZFQyR2REUWRsaW9YU25QNF93QUd0WFBKNThrZTlXR0VYalpsQzU0c1ZNT0RFQkczWlZqTDZmZzJTYUpzdzF0dGxJbEM1TXBvWWtuaDlEaDFoMGFB?oc=5) (Sun, 20 Sep 2026 01:05:24 GMT)

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
