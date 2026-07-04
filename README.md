# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-04 02:05:07 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,825,100,587** | 🔴 -0.02% | 🔴 -0.96% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [This sanctioned Russian stablecoin claims it processes billions, but blockchain analysts disagree - CoinDesk](https://news.google.com/rss/articles/CBMi2AFBVV95cUxQU0M4cVVSSG1uVWNDeXlpLTE0a21sNnBNWThFeW5kUlZTUUktTzVtUXMwcTZpdGNwb0ttT2Z6VHMyaHk1enpSY3pOM0RjcTRDRUV4X2ZqYVQ3VXJJR3h2MzYzN2tHRGNOVDF1YW9Ha0xZMjhhSnpKbTZ2VkFSUElMbmZreXQxcjlQcHBGUkxuLWNlTGl5WnZOZUZqWTUwaHlLbGgwbXprdmE4LWRxbTJTNlNGWmYybTVwc0ptOHhEZC14RlFnYTlZd2VXcEkzMVdHMDBrUU5ZWXM?oc=5) (Fri, 03 Jul 2026 19:21:56 GMT)
- [Samsung, Dunamu say they were listed as OUSD stablecoin consortium members without official consultation: report - The Block](https://news.google.com/rss/articles/CBMi3wFBVV95cUxOai0xTUZ2aEdUZ2VJRy1yclNuakZZc3FJWEd4cWprSUIxS1k3dXNfa0ctNGtpTVV2N01Ob3lob0RGNmxzTkhhcWFjUzFvSjk0TEJzb190eldOcFp5bFRJNXk5VExtQmFaWk9mcC1LQ3pzTTluSnRHT3UwRXROVVF3TkMtOFdsQS1veHE1MlRhWWxJNVdocmJwZkxQaXVaeWdrZXpTdHZhRFM3TWxHWnBXRHBGQnpZbFlfUHdJbGRJb3VpbjN3dWctVHlpd2oyZ2JJYXhIcHJVZlVNOXhMZ3lN?oc=5) (Fri, 03 Jul 2026 14:32:14 GMT)
- [State Street (STT) Lands Treasury Default ETF Role And Launches Stablecoin Fund - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxQTXZ2SVpNSHM5RWpTOUVsWGJMNUx6MjVpYmtTbWt2NE4wMndJM20ybTNLaTNSeVZKdkozOGRraElxSHJnRUFOREo0eHRuRDF1Skd5c280bFloYlV2S3hwMkVsazNwRGJqZEhOYnQwZlN3OGtXNV9NTzdmTU5ManQ3LTZodHBfU0NBZ3dpWF9feTB4OUhGUm5ycWp2ZW8?oc=5) (Fri, 03 Jul 2026 13:17:06 GMT)
- [The one stablecoin to rule them all? - American Banker](https://news.google.com/rss/articles/CBMie0FVX3lxTFA3WDZlclYyN3gtUGlVWUJleUJOQ2Z2ODRmZnczVTNSTWN6UWd3RGxtWmZSVlEtVlJwcmtKZDM4dkJWa3dvSXRmbFk5SHBMTmhPenJIX1dLRkNEUDk4WjBUcFNfM21QZGktYlVja0JEbkhxanQ0MVBTY1RIZw?oc=5) (Fri, 03 Jul 2026 12:35:00 GMT)
- [What Is USDG? Everything You Need to Know About the Fast-Growing Stablecoin in 2026 - Bitcoin Foundation](https://news.google.com/rss/articles/CBMiswFBVV95cUxOYUcwbnd1M2JlakNZb2JzRnBrRFVHQlcwdGsweFFMRmdZTlZNbFpxUThYX0t4OURQWGlMdTRZNnAxVlE5VHRqX1JPUGlBVUhtTUc4Ml9iSzFoNGdZUXRpTy0tS0tRai0wZjF4a1hkTnJIQ0IxcWdNdFJvWUVrTTdjRGZsOFV6OVpBX08zMl9vQjZNMTZEZm5jM25NR1FUVWE2aTBVak9HREZRNjFEVl9aZThWcw?oc=5) (Fri, 03 Jul 2026 11:02:30 GMT)

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
