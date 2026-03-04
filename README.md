# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-04 01:17:40 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,992,776,080** | 🟢 +0.04% | 🟢 +0.52% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoins Face Tax-Time Reckoning as GENIUS Act Sets Compliance Bar - PYMNTS.com](https://news.google.com/rss/articles/CBMirgFBVV95cUxOMWVpRUlMeTUwemp1VUk4ckNaa0MwakVqWmJPYjltdUlFR3dkLUp2NWtRQzVJRHpSNEMyOWVNQl80WHBjbVBPb2E4Uno0VklnU29uWms1eGZyY2VSb1owYnJSSjNvRkdWSFdnLXhZSUZKT29ndUtJYlY5SmNDWEwwRzZjajI4ZzBZcldWbVljUm5RMlhEUXREdHdSVS1iOThTbzk4MHM0TGFsMF95d2c?oc=5) (Wed, 04 Mar 2026 00:11:59 GMT)
- [Office of the Comptroller of the Currency Proposes GENIUS Act Implementing Rules for Payment Stablecoins - Pillsbury Winthrop Shaw Pittman](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPU09OLXdvRlNsanU1M3Y2M1lCNTEwSk1KVThDa0phemc2ajVaaEJROTBvQXlpWVgtVXJNZGNwOTZCanNKTHdTa0dCR2Rhc0VmUE42cVhzWHpWRWxNNjdnNFd0ZTdtVFg0UHA5cFpINXo4MUNCTzZtYXFpOWVHMFFZZjliS2dkSnR5VW9BSXhfNWx1T05GTXI4Z01fUmdjdWdoWXZ5SmEzZDl4em43dTd6VzZQN1VkWE90VEpJ?oc=5) (Tue, 03 Mar 2026 21:56:55 GMT)
- [French Hill urges Senate to take up House crypto bill amid stablecoin yield fight - The Block](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPaUV3ZHcybEUtOG5IWXlSZ2hTUll3T0trMDFFY1FUbVc0cEZNSlA3YXh4TkEybFljVHhUbWFaOGR5Vm04ZlU5cGthanJObFkwUDhsdDBvQXZ6UDFfOW95WXVEdTlsbU80REthQklIdC1obzJfcGNzM19UcjJTeWp6U1BCWjMwU3dicWFIbGNaVE5rbFRwcTdMRDNoOUNJZWtwQ29TQ1NHWGkxZw?oc=5) (Tue, 03 Mar 2026 21:43:06 GMT)
- [JP Morgan CEO Jamie Dimon says stablecoin issuers paying interest should be regulated as banks - CoinDesk](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQYUJvSVVTa09VMng3cDR4TWVVTVl3UlBWcTNibmhSZVZleWdWNUk3Q3JkT1gyamx0REdrc01iUzlLX0RUTXJoY1JYbzkxZkhmTklMUjVGTmVaVmVNSE56QUVSbFpxNllkMWw4NGxzX2cyeHgyNTJXbmNNY1ZHcE92X1ZNQW5OUGpSQ1BFZWdScGZoOFhmVlduOVBCMjBXZHBkWGl0VW1heVNVLXVnQUxfdG9Ha1Y0WU0wMUFWT0pIaXkyZm1xVm56NjlZTVpRRjRmcUNZ?oc=5) (Tue, 03 Mar 2026 21:10:04 GMT)
- [Mastercard, Visa make deals to jolt stablecoins - American Banker](https://news.google.com/rss/articles/CBMilgFBVV95cUxNNEdVbFN5N0V2aDhtNThfMEdManU4UDNaaFJOYmlYcDBQVEZEWUx4blR0YWx4elJnQmJ4RTNUVG1xSGRMU2VfOHJ0dFpBdVd4Ym1PTktqMkVsaElQVWtTb0ROT2xpaV9rclZjQ0Z0R0gtY3Z1b1FDYlM2ZVE5bWc4QjFucTlmbVh1MlpZWV9CZDZlWFFObmc?oc=5) (Tue, 03 Mar 2026 20:45:00 GMT)

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
