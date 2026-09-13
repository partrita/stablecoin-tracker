# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-13 02:18:48 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,869,390,930** | 🔴 -0.01% | 🔴 -0.00% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Warren Buffett&#x27;s old favorite bank enters stablecoin business - thestreet.com](https://news.google.com/rss/articles/CBMiowFBVV95cUxOb3pjUnFoM1FDdjN0Ul9QNzlVdWd0X01XajZrb0VpdTNocVFWdVJxRnBaTjMyVHdFRjFsbXJELVp5VXFQSENWV2N2Tmx2YlNtMFdvcWdqUFVFUEJZcEZvVDNqVWhoTGExaE1LNnRPUnRJdU9zanpSR0IwNF9JcHRGYU9HVUJPVlMzYTkzbXZ5Rk42Y1U2M1dYTW9OaFhEbURrelB3?oc=5) (Sun, 13 Sep 2026 00:53:07 GMT)
- [Thailand’s stablecoin proposal would block transfers to other people’s wallets - CryptoSlate](https://news.google.com/rss/articles/CBMiowFBVV95cUxOa1ZuNEJqNnRhRi0zMExSSXcyR3FjdVR4eDh3aFBRTm5OV0VOb2RKYzRBaDNhTzMtNFF5SXpHY2FLMlk1V01aYXZJRGdUb2dzSXlpTXdwNllybWVCWm9jSmRyYTRnVmNLd0d1ZTVFbHkyQm1IWG1hT1FHZk9JeUhNZFZybFV2VWZzS2JXdi1QRVkwcG5Oa2ttcXJNNFNmRWlZOTZR?oc=5) (Sat, 12 Sep 2026 21:25:29 GMT)
- [Ripple eyes $13 trillion corporate treasury opportunity to grow RLUSD stablecoin, executive says - CoinDesk](https://news.google.com/rss/articles/CBMiyAFBVV95cUxOelZQMkloN2g2WWFaSnpCMF9ySm5RYVIydW1xcElTcjBjYVJ1U1RKLURzVUdwZEJ1NmRaeDJ6ZWE0RzJBa2p1S2lLbWp4T2JaWmo3RFg5Vms3azA5R1VKWTBjZmsyOTdoTHcwQlZybllDSWVWcm8zRE5kbzFlcUN2bkVNZ0Q1YlNQM05lNExSd1k3a3NlN0F5VTg4S1NGMkRYM1RCWG9IUHd5bFAtMUJ2UFZPa0tINUUxLVhfMjVxX1pDUkNWRHNvUQ?oc=5) (Sat, 12 Sep 2026 16:00:00 GMT)
- [(Sm)all banks should compete on technology, not fear it - Fortune](https://news.google.com/rss/articles/CBMiggFBVV95cUxQVDRlTmVscEpXZkh6Y2YyZkJ1eWktVWxDYWw5dkwzUHotWDR6ZkRaQnN2aUlKcFhyaUdHV0ZsVUcyaHJvaTAwOU9kWEdtNGdPZnFJa1hZWVktOG5mWHRKa2JFMlp3eDFYWVdGZDFrLUNmQlc3Wm43NkJlY21pYWluRWVn?oc=5) (Sat, 12 Sep 2026 14:38:00 GMT)
- [How Stablecoin Card Partnership At Marqeta (MQ) Has Changed Its Investment Story - simplywall.st](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQa0JrZlZVS0g1WGN6bVNZVnlTZk93bzdxWXFoN0p5aGZZWnFyVEJ0OWNSUUtvMzdRdGU5VzRxaHg2QkpESGp6OFlyZkI4VDRUQWF0d3dZLU1VS0JzOGdOVG5UVzFlb2lZaDlJdlRfQXNWVDZYcjAxRno1bVZzRGFPODVFY3liNXZvei1KZHR6VXluNkIyYWVFQVk4eW1pczE4R3BHbHB2MHl5ZlR2ZVB6VUF5QXJQbUZxVm56VE05MGxhZnBqV0x2WXVJT0hiQlk4VFVPRdIB2gFBVV95cUxOQkgzdjFHaTNlU2I5ZUFiSFpxNDFFZ1c5aVFxN284LXFHblZtX3AwWVJ1SVFHUkQzbjhqb3ZOOG5sNHo3aFU3WWVWWWlrRE9KOE81LXUxWVpWOU96ODlCWTNPYmVzMGVWU2VyS2pEUmdHVlVXWnV0X0JXdWxjNnR0V3BnTXc4VUxWOTQtV1JhZ1R6eW1RZ19vUUFfR1R1RVg5ekUwOGZXSFM1UEZfNE51eTUxUkc4V3V2bVFIZXFEQTZTOFl2aXVLME82bHJwV25NNFBIa2RTelFpZw?oc=5) (Sat, 12 Sep 2026 06:28:54 GMT)

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
