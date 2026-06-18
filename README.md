# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-18 02:47:27 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,270,694,722** | 🔴 -0.15% | 🔴 -0.23% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoin development CEO Kazley sells $26,944 in common stock - Investing.com](https://news.google.com/rss/articles/CBMixAFBVV95cUxQUG9aNW5SdGFGSUtuRXFNY203RDRYcnNDQ2RJUndmM09GY2RnQUNHYUZ2YmpnRHdLUWI3WTF4QWF3QTA1VF9nWENNdE9FM291a0ZKbnpYSUhQbWx4dE9hR1hnN3R5RGVRTnBPSElOc0gwNDhhR21kb2hxN0tOMGNfRHRtNnhKYzdfdGZSYTRoVExHZTN3czdUQzJSRDg1bmF1NlVadE5YS3dTd3VxaE5ESWtqMWNzaURyQV9hTE9WTXhicGRf?oc=5) (Thu, 18 Jun 2026 01:00:32 GMT)
- [Stablecoin development CEO Michael Kazley sells $26,944 in stock - Investing.com](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQckhCZUMyVUphUm9RMC1ObllxZWl5TXQ0Q240a0twdUJjU0VoNDFQeFBHbmxxTHdNNUhMblNVcU1tQnVvMHFJNEc4Nm0zRGlxdHpGWHpqSmxlenlKSDlwYWxPQ3MxVnFYN01pQTdOZHh5UXdJMzVwbUJLQzZzUW1nNmRWVjk3ZjNSLWZ6M3NCRUdtSzdmMUhsUTZsS3AyRXRIaVA4cHhUcnRvWnJjRmJNSVMtWnE2YmxfODJsM0FlUXAwaTIzREFybjdkTkhaYy1J?oc=5) (Thu, 18 Jun 2026 00:32:00 GMT)
- [State Street (STT) Is Up 5.7% After Launching GENIUS-Compliant Stablecoin Reserves Fund – Has The Bull Case Changed? - Yahoo Finance](https://news.google.com/rss/articles/CBMijgFBVV95cUxNNWFGc29ZSmgzUWJfZ3pPVnZkSkM3SjFBOEVvOUtRR1F5MnBmRklKZzJOTUdpc21vLXlzX3VjMGJYNkxYN3FzTm1tRUp6ZjZpcVZwOXV0SXJlOERJbFFiYUtPWGZCODR6N2dZcnlKTkNtbXhqcUYwd2hEMndKSWRwTEZZR3lQamttZFZMWUxn?oc=5) (Wed, 17 Jun 2026 23:21:51 GMT)
- [Brazilian stablecoin infrastructure firm Trace Finance raises $32m - Finextra Research](https://news.google.com/rss/articles/CBMirAFBVV95cUxQTDR6SHRuakkyMzZzc2NTSnpONVBHMU90U2UxS0dKcHFFaHc3RUREM3NMSzlvX1F1bEFNZXFjLXlZSnBYSG9YSzFuVEUtYkJ4bDlTeE1XNEl3VzlzdWFzVjZHUWtadENGeTZsN3BnMG53czRjdkdWcXJJeWl3a1pDaWx0bWVVVTVmREwyNnZVWEtoMFZIamZXYXhoYm0xbEpaSFE1d2NzZ1lvc3FI?oc=5) (Wed, 17 Jun 2026 23:02:23 GMT)
- [Fintech Trace Finance Raises $32 Million Series A, Targets Stablecoin Payments - Crowdfund Insider](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQNnljTXA5eTNJNG5wRlNwU2Z6eEhXMDZjX3FpelRLM2poNHZpeUh3OEd2dWNnUDh2UG1iRkJEdE9xSFpVR2xmdElScXA2aTNWOGZRMkJpUWtFRDdPbDI2UGxxdzVIZTY5LURXai1Udm5CeDN4R0Zvc3ZqOXdkOEU1azlVdm40VFBzVTVHQU5jZWRXcURxd1ZoeDMwQTF4eVNJUmZhQTVzaWxZeDRPQVdnWllWLThYN0JUcnF3NU0xQUhiQzA?oc=5) (Wed, 17 Jun 2026 21:32:32 GMT)

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
