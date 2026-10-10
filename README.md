# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-10 03:33:58 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,058,491,816** | 🔴 -0.13% | 🔴 -0.39% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Circle Stock And 3 Plays On Regulated Stablecoin Payments - Simply Wall Street](https://news.google.com/rss/articles/CBMi1AFBVV95cUxNNnJhYTdzcUx4emRlUUJqNGtaQmY5TkN2aWdMdzlrUlNyYXVZQVQ3MHl6cHV6TTQxclFRaGRiM2E5NnU5MEJWVGZsTTlNQkR5VXRVQ1U4ajc0ZWg0Vlp0SEt2WTNEdENaUkpQSlpvalZYcjE2emdxc0c3dnpOWHBpMUdpSHBEbG1rRWs1dmV2bGhEZnI1RFY2Y1ZHcGJXWWpOX0xBVEN0Z2FDX0lRR0VSNzNmeldEcXg0N1JaMTRQYmc2TVhRYmJrUVVWY01XRS05SHVWa9IB2gFBVV95cUxQelBmbnI1R0VWeUE3dmFkdVJxb0E0MllmekdEUzJsdlF1QkZ5NnlqZnIzcm1DM0o1VXpMQW0xNzljSk5RbjZMLU1VU1M0ek1hUXBDZElUUTVuQ2hxcFdZVy1oc2ttVENiQnhYeV9hYUZ0LXF2TjVJb2luanVsdWYzV1N1Tk5vZjdQbDlvSVg5b3RDbkdQNGZpRUc0SnN4cUJCQmNLM05wSHhQcUlDNFVxUFJ5aVMyN1BWR25IaW52QzM5YXZWeEtCWU00U2k1U1NNakloYTJBWWtvUQ?oc=5) (Fri, 09 Oct 2026 21:52:32 GMT)
- [7 Things Credit Unions Need to Know About NCUA&#x27;s New Stablecoin Reporting Proposal - CUTimes](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNUFNIaklzZ3RvLWFtN2RPWm9acWNhRzltQ011RTMxY1Foa0M4ZDlfNVZCd1k4TUw5ZUtTdmlFbXpiSmkzeGZ6cXlLeGhqV0lySnU3SFhMeHIybU1RNENQLTJPLXNRc0VTeFF4RHVRVEhGRE5zOHZvMU9oRkROczZJaU5kVy1wWldrS1h1YnRBVjJMYWFwSFUxSW91UnAzcDJOekFSQlhDYkhxNDZDSXFEZkNMbFBRNi1y?oc=5) (Fri, 09 Oct 2026 20:56:10 GMT)
- [Stablecoins meet the back office - Axios](https://news.google.com/rss/articles/CBMijwFBVV95cUxPSW5Nb3dLXzhjeWZTbUZiWVhtX1BZNDRXVHRNWkp6X3RaNXhDYmZRUUkxVWtJVkhqaVpsNnN5alNEdmYwdlQycm1wTnNxbGppZHg4WWJwdmVvT1hrRmdBRWxmWlg5R05mWjJMa2dQLTNlRDRQZ2NTSUZrVW1yTnZ4b3ctX29oSGFtcmxVaFdOaw?oc=5) (Fri, 09 Oct 2026 19:55:15 GMT)
- [NCUA Proposes 26 Stablecoin Account Codes, Extending GENIUS Act Reporting to Credit Unions - Forkast News](https://news.google.com/rss/articles/CBMisAFBVV95cUxNMzUwSnFnQnI0U0F5YXlrOGpmWXFTMjJkTzJWU2hzM0JrbVZlVzJBeHhoRXJrSG03Um1KSy1OSFlxQk9wRW9ucnFRV2lnRkZ2ZmdQR0MyU0RKUTRPcUc5bHJqSy1lN2xXY3Z0OEdoQmxucDlVVnhraDFZSHdpVC1sWnR1blZFdjNfU3dkd3VKWTBydWZtQ3BHTl9wbkc0MjE0NWg3X2JuT3ZxcHN2OEktNw?oc=5) (Fri, 09 Oct 2026 19:17:50 GMT)
- [NCUA Proposes 26 Stablecoin Account Codes, Extending GENIUS Act Reporting to Credit Unions - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxQdVJ4VXdHeTczcmlSU210V1VxbGcwaDNscXFCZ3A1TGUtRTRUaE40TE1VU2tPNEVVbnRuT3Q2RXZMd3BIYW5MN05ibXlUdmRtR1lXX2phUnZyRDJnbGR2QUlXUTZadW9ZeFhQWHc0RkhKZk9hUkFpRlVzaVNkWWVvVmkzd2dwWjB1RFBEa01iZ29XQ3JIc1JQY0NCZ09jMEE0cWc?oc=5) (Fri, 09 Oct 2026 19:17:50 GMT)

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
