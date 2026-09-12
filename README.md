# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-12 02:20:56 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,894,219,224** | 🟢 +0.03% | 🟢 +0.04% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Circle-Tazapay deal aims to accelerate USDC adoption in cross-border B2B payments - Digital Commerce 360](https://news.google.com/rss/articles/CBMimAFBVV95cUxNQTZHcXlwbUxSYWJubXktNjRsWlZzU0hQQnpGOFZXVWR0VU5HMVBSQTc0NGpLSzBSQzFna01kVHF0YWFYbUdKLWZTMnJNVEdDNjd6RDN6bTBKcU1NV1hHMUpueDJlVE5jdFk3eGNyd25LZF9fY3VXdWF5UG0zMkRQaEdOYWZreE1lcHZWNWFvaW9BaXI1dFFzTNIBmAFBVV95cUxNQTZHcXlwbUxSYWJubXktNjRsWlZzU0hQQnpGOFZXVWR0VU5HMVBSQTc0NGpLSzBSQzFna01kVHF0YWFYbUdKLWZTMnJNVEdDNjd6RDN6bTBKcU1NV1hHMUpueDJlVE5jdFk3eGNyd25LZF9fY3VXdWF5UG0zMkRQaEdOYWZreE1lcHZWNWFvaW9BaXI1dFFzTA?oc=5) (Fri, 11 Sep 2026 22:42:06 GMT)
- [BVNK and Marqeta dangle a payments lure for stablecoins - American Banker](https://news.google.com/rss/articles/CBMingFBVV95cUxPeXdaNjNNYkNWckxva1R2czlDNGp4SW11YUdRV0JzRkQzWmNGQXVJMFdSWVVEc2pZNm1mRlZxbHllQWlHWlQ3OGlQVzI4UDlpYnBFajJlNGd4bnBYcUl6LWdpMXBjWUIyR1pVQl9xSTVyUDQxSnB0YWk1Wmg4cG1BRVROZHJHMl9tM1FiRFpnbFdtWDhzUVJtSDRDZEpZdw?oc=5) (Fri, 11 Sep 2026 19:51:00 GMT)
- [GENIUS Act Pushes Stablecoin Compliance Into Banks’ Back Offices - PYMNTS.com](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQbXlrTlJoaUo1dnRyWDF5aVNISEpFOXkwT19GZFdPSWJCOWo0X0ZfQUV6Y2prU0Z4S2pXTlhCQ09QemU0TmVaMWhOWklwTFR6dGRJMjRfZGlwSXdncWM4WXcza3gyTlpiSWJDRVdVenlvTEp0dTk3WWZaMzdIVV96Tk9uX2tteGxreVFGTjdFZXNsVkVoNmNUU2pscGxXaHpZTGh5RzMzVmRzOUk?oc=5) (Fri, 11 Sep 2026 18:13:34 GMT)
- [Beyond stablecoins: The tokenisation story - RBC Wealth Management](https://news.google.com/rss/articles/CBMilwFBVV95cUxNaUU0TVJfUkhyZ19YSnluQ2FDa3Y4eUFMOWtmVmZVLURyV1dXdktpMl9lVWVFTHBUOHo2UlV3MTA5UnVrZjJqaFRtb3hhcjF6Y19LdGp5VmdDZC1MSkVzeTVna1p3WkZjQVhWNHgzUmxLZG9uMG1GczlVbGdfNks3MEFXV3c0VHMxMEtWX0Q0QlgxcFNNNEhB?oc=5) (Fri, 11 Sep 2026 17:30:55 GMT)
- [House Panel Weighs Growth, Stablecoins and Financial Regulation - Legis1](https://news.google.com/rss/articles/CBMickFVX3lxTE9TNkRDaEtDVXI3N29Nekp5SjVONkFBcmZDeFpSU3hxeXM4VG9GTzNVSDhEQzJyb0t2ekRJMV8xUWxfQXVJTEFMNTBHVlZyaTFia29kMUkzOWRMQzhJWTZ2TC0zTUlzUkV0UUlfQVYyMXFadw?oc=5) (Fri, 11 Sep 2026 17:07:13 GMT)

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
