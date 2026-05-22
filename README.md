# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-22 02:36:36 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,247,154,967** | 🟢 +0.11% | 🔴 -0.14% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Deel Adds Stablecoin Salary Payouts - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxPTnBGRE9vZk1SYjZkeDhJUGlnQm5zUlZ3WmJXMjdRNnFrLWdnWWE0SHlBSk52eDBtOGJxdUFvYzd5RFZzY2p3bXl0clJjdjE5WWZ0aTJDbXJRY1BPdjJBMC03X3BWTHd4WHdMTGhyakVzZ05peXF5MTVac0tpTjQ3d2N5MlhueWpOMTR4aDhsLUhwVnBSSFdlZDFRQWFCR0lnVFE?oc=5) (Fri, 22 May 2026 02:13:00 GMT)
- [Deel launches stablecoin salary payouts via Solana - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMikgFBVV95cUxORzc5Mlp6T3FpOWJKbmZ0Q0I3Unp1aDlkbnNEaV9xNmZhcEhoLXNVUVVYeEFtc2NRVXBlNzZpRHdveUZMTWlJSjhJanZGZDd1YkRCZzl2cjFrY0VyeENDTVZ1Um9iRnljaTE1bS1LbzB1eVozRFhycWJhSTh5WWhSc0FJcmRyRnZIclBBdDJxYVdXQQ?oc=5) (Fri, 22 May 2026 00:01:00 GMT)
- [Sui Eliminates Crypto’s Biggest Friction Point with Gasless Stablecoin Transfers - Bitcoin News](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNcWtXU2lZZmhoemZrZV81eHVwRHJmTUhvbjZtTnY4a21QMnFrTnZJMEhWc2E1VVktQ1NkS1Z5a3hwTXZyNGtoemE4cVhtYmhraF96c1NWUlRDYkt3LU1TNHFkOFlMMFd6U2N4UTJfRHgzWk05QTYya09GVnJZMDM4M214WWhtMzg5Y0RsbjdabzF0dkJWRlpMeE1HZVh1d3VYVVFGTTNxTXc?oc=5) (Thu, 21 May 2026 23:05:05 GMT)
- [What the GENIUS Act PPSI Rule Means for Stablecoin Issuers - TRM Labs](https://news.google.com/rss/articles/CBMingFBVV95cUxPblpPOXdDVE4ya2UwaXlJNDRzbGN4VV80ajFUcm4zaklTcVpkZl9Da3Bmbm03WTI4RVc4TkNBNElFNEJmTGdKNzcxd3JDb3FJdDRzRGZKOW1sSWJrY1AtU2RVNjRjWEVsdFlYM1dLR1NTblhZTXRfQmQ5WkpUVTJyQWZwb19DMHJ0d216d3NxVzNzR3Zud0N0WnpuUkFfQQ?oc=5) (Thu, 21 May 2026 20:32:49 GMT)
- [JPMorgan says tokenized money market funds unlikely to grow beyond 15% of stablecoin market - The Block](https://news.google.com/rss/articles/CBMijgFBVV95cUxPNGFYVjFiNHczdnJxOE5FNUl5WGExZ1dCX2FPZVVZeE5wUEo4dVNrd1RGR3JkTmdia3VDdkRmc0lzVVp0RWRJUFAwWFlpNlJyaExldzRCRUZldEowdzBQM1lrQzVXbHNOZjMydnJGUWlycUhLdG1ZaWdwbktyYmZSeGc0bVMzRHZNc1c5c2tn?oc=5) (Thu, 21 May 2026 16:48:08 GMT)

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
