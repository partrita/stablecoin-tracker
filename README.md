# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-15 02:53:35 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,392,377,456** | 🔴 -0.01% | 🔴 -0.61% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [CPI &#124; Banking Groups Pitch Anti-Money Laundering Rules for Stablecoins - PYMNTS.com](https://news.google.com/rss/articles/CBMinwFBVV95cUxOTUE4X0l0YS0wQm56cG9lZUVfQnYtT1FGMjRjY3AwdjBJSEhqVjFkSl93WFJIalF3NWpuemJQVjFfVjFIMkNjNXpBTmNJdF8tMjdJVXp2NzNPN04tOXA3eTl5bnBGT2M3OWhHbzhhMUNSTjFMTUw1OVlsWFc5NHo3RVdjVFc5a01TakVwRlExVVh2aWdKLUE5T1E3Y0VyOWc?oc=5) (Sun, 14 Jun 2026 17:53:54 GMT)
- [SoFi Stablecoin And AI Coach Put Valuation And Growth In Focus - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxORDdyR3ZBMTlHQnFIbDJ6OGtlVWhJRzI5bjVWNHdVdUIyZy1ReXVQMmQtbEJ2d0hESk5OZVZFeXVJQkhRdnFSemV1RDk3cTcxdDJiSGxlRWhTZENJcGJiVWdnT2t4M283S3c3aHQxdEo4OUJDU2NPSUVOX2lCckRkZERhUUttUnZtam9DaGtVMmNWaXZNN3REbQ?oc=5) (Sun, 14 Jun 2026 16:10:26 GMT)
- [Mitsubishi UFJ Joins Major Banks To Launch Yen Stablecoin By 2027 - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxPU1dkNUl1U1VoSXh3Q0RPb0xoTUV2OE5FVi1laHhHYXVFbzF2QkpkcG1ocjhuVnN5cG1aRkRsTG5temp4aU02OHJBWWVQU3NjcWJ5Yl9aUnk5MXY2Sl9STENYcEZ0dndiQUNPNEdNdG9tbEx2SzZOVFBOZWtvQXpfb1JUckN5dHpPYnhHUS1ELVg5c1N4Nm52RTY5WjR0UQ?oc=5) (Sun, 14 Jun 2026 16:10:11 GMT)
- [Trump-backed World Liberty Financial to fund UFC fighter bonuses in USD1 stablecoin at White House event - The Block](https://news.google.com/rss/articles/CBMi1wFBVV95cUxNaTh4MkIzQnhRUS1Pc0pFVHlMeHR3V195Y2E2OEUtQjBqbTBhSUotRm9nZUtmSHZHaG9YUmZoRUZQRTJEVS04NXV6ZVROckVoT1d4SWxuYmdIekdXMkNNMmJ2T1A4ZmRRWEROTVpqd2FTX3RLQ1pOdk1sWFc5ZU9HWS1QS0YtMGZ6U2pVby1oS0hRNnV4RFllVElYYXBZQU1tU01CQnZOODR1aHpCZlNvTnRQa2FmV0gzT3l4VklNNnlTNnBac1ZtRGtNQVdnTDRQYThMLUJ0MA?oc=5) (Sun, 14 Jun 2026 15:44:41 GMT)
- [UFC to pay White House fighters in crypto issued by Trump company - The Guardian](https://news.google.com/rss/articles/CBMihgFBVV95cUxPVHhCa0diS0hxYk1YUmQ3NHNYTTNnNnRlU0FrZ0pSdGhEWUtYcTg3RHZRWGxEUEx5UEQwVVRVNHFxY0dnbzZiM29xMUduN3FUOGE4VlRSOENaYnBXdFRTZ2FMRkRuZmd3RlRzckJrNW8teWp0X1d3RU15ZFRRVW9aQTBQT1VjUQ?oc=5) (Sun, 14 Jun 2026 12:20:00 GMT)

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
