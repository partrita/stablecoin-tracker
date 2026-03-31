# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-31 14:24:09 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$296,845,987,082** | 🔴 -0.02% | 🔴 -0.43% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Investing in The Better Money Company - a16z crypto](https://news.google.com/rss/articles/CBMib0FVX3lxTE13SFJNdzZvaC1ITnRVRkZYSm1GbkQwQ3Buby05a2NUdnNBZmNzTHY0Q3k2ZFJ6MEVSNzVzMjFhMVVEYm1KX2JTTlk4ZUI1MGJTa04wdTNaNEt3N2V6UHItTks0LW1fdGdPXzd1Z0o3RQ?oc=5) (Tue, 31 Mar 2026 13:01:26 GMT)
- [Exclusive: Former a16z crypto investor raises $10 million to launch stablecoin clearinghouse Better Money - Fortune](https://news.google.com/rss/articles/CBMipwFBVV95cUxORmdFSVhxbzIxUFpiRGx6RGJtUTZ1QVpCTDd1RWJ0RExVOE5lYW9HSVREd21sOXE4RzRDcENheDZtVHNQOWZOZkI1MFRDbktVWTgzb1JTS0J3bFpmaGt6NEtQNThmajAydlF2enRWcXhBX19rSERDRDBaQ0ljTW9xR0lQamVtWlp4VW9qbmZXdHVqR3JMVHV6ejNUSlYzb0s0eUF5bDZRbw?oc=5) (Tue, 31 Mar 2026 12:30:00 GMT)
- [In the world of Stripe: Acquisitions, agentic AI, and stablecoins - Tearsheet](https://news.google.com/rss/articles/CBMimAFBVV95cUxQa0FmUEZtQnY3WDcwQkRRSnRUS1hlbG5fWG9jbi1YYmtjWU8xb2pfS2d1NENzLTcxeVFUVDhnUm1iSXNYOEdsaWNoWUpwRWdPaFNSRDdYZHhrYUdRWjJTVTh0el9BRkFzS0o2enhVYU5kbHlXM2s5WDQwSkt3M0c3YWFIc1ZhNVpIcHBHMUZmQkhncmZxekVGeQ?oc=5) (Tue, 31 Mar 2026 11:47:32 GMT)
- [Forex startup OpenFX raises $94 million to expand stablecoin-powered cross-border payments - CoinDesk](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPNDZKMTdPZnZfTnBCcFVFd3lrekRaV0xJZWpUd18yM2VTWjlQZmtsSWpxWlNPZVQxWGwzLXBCU0sxWmVodGhKSnU0LW5GWWJzX2JncWhPSjZuSnAySlU0c3pfUENMbEE2NFdBU0dlY1ZsYW8wa3cwRjlyTVc0d3hvT2w3ZEdkQnRKN2JGaVFtWGh0eVN4WnVycHgzTkZBeVlfc2IzYjdfRTd0SVUtWWN6Q0h3LVlIWWN0LWt3bGpWc19XMVN4bWs5WmNsekE2X19sTjVV?oc=5) (Tue, 31 Mar 2026 11:41:27 GMT)
- [&#x27;Unstable velocity&#x27;: Standard Chartered says stablecoin usage rising faster than expected as new use cases emerge - The Block](https://news.google.com/rss/articles/CBMi3wFBVV95cUxQTkY5dVV2VGRPdDhLUzQxejJ4dWg1XzRpZnRaSGYyMHdTVnRkbGdXNEJzWF9hdzJGLWhkeXAtSVE1ZmRQNEFLWktiNkFqU0VxMWZMTktIOHo4VHJaUlU0MFZTdWZxLU0yd0syVkkwUUpWV1J1c3VzUWxGVDVlOC00WUUyWEtTZ25Hb1o3b21WUGFkTDVWclQwNXBfTC1qcE04N1A0VTVjSnFsSmk1UFJLNHZ2dUV1cFFld2VBUUJIYUw3UnRfWXhBYk9WbnlLTmhCUDJnYjJDYkVkTEk5X2ZB?oc=5) (Tue, 31 Mar 2026 10:14:25 GMT)

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
