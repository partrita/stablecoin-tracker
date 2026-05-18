# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-18 02:34:52 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,919,785,090** | 🔴 -0.02% | 🔴 -0.03% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [NCUA’s New Stablecoin Framework Sparks Debate Over CUs’ Best Digital-Dollar Strategy - CU Today](https://news.google.com/rss/articles/CBMivAFBVV95cUxQcEFDbXVISGJKdk5GeDFycWxWMlRkTUpJYUF1ZWs1STlsdnlsb3RTMmRTQ0VOdl9YaVNhcjBiQTJSVUVHMUdfV1VYQURBV3BEb3U1STYxby1aSVpuQ1hCUlY2LTR2a3U0cjFKa3Q0VXdTX0JzeElidXZIUWN4RXNKc1loZV9oeEdOMXBXSzlCM1lydFdLbmJBeFl1RVZRRzlpLUp2cVpTZkRGUzFpbGVtcXdYRXlUX0QxWlBpMQ?oc=5) (Sun, 17 May 2026 13:10:30 GMT)
- [Ruble-pegged stablecoin A7A5 says it has a business even if sanctions end - CoinDesk](https://news.google.com/rss/articles/CBMiywFBVV95cUxONFVXdUxjVEh6WUhzX01WVHR6dURaV0w0amYxd01MZU9HNm5oZEhuaXdQSFpXQWpwSVQ2WDNLeHNfbGRyUXFLZUpLR0FCX3RwZmJGMXdQTE5CS1BXSVpGYzFMOTUtSlZJSW9DaTFHRF9iTlpzdWg1b2ZTNFBtOG1wSy16dlF4clBib3ctb0E1TFhfc1lLaGdQa1pNNUFJNWgxWmpfV29KNmQxUGE3bFNtZXBPcndnaHpKd3h1NTU4cnFIZmJNdmRmeXd1RQ?oc=5) (Sun, 17 May 2026 08:01:22 GMT)
- [The stablecoin talk is loud this earnings season - CFO Brew](https://news.google.com/rss/articles/CBMihwFBVV95cUxPS1JhM3ZKdmdXZ3ZEMU9zei1VM0xKd25EWGgtNkRlcVp6MXp0V3d6VmFObC1rZVhQREM5UXNLZGFFMktRb1JGZVFPQi1Ba1B3cHI0elFHM25MckJXRFZhNU0tU0xrNHY3V1Q5bFFUSHNLRnpfdnZfQm80OGZna2M0bVRIRnZvRTA?oc=5) (Sat, 16 May 2026 16:16:08 GMT)
- [Stablecoin bill moving through the NC House - The North State Journal](https://news.google.com/rss/articles/CBMiigFBVV95cUxQVjVnbEJQNUgxb0xGeUU1QzlzVDlNRU5VWTh1QkNPNzJnRjRPWkdIN094T0xlSkEwUU9tSUJwTTR4aDAwY3pKVU1SWTRXQzJiNWI1cXpYUUNWcG15YnZHMjRYYnFLdGxUVWNoNF9PZHF0UjVEQkxiUmdPcFBhRk1XbmJyb0tUZmJVNFE?oc=5) (Sat, 16 May 2026 11:55:16 GMT)
- [Stablecoin loophole threatens lending by Kansas community banks - Salina Journal](https://news.google.com/rss/articles/CBMiugFBVV95cUxNVHpEOWdsUW1VQndTV1BKMk9TLWphZXB6S3p1MVlPbkRQc1RsQjY2T3AydEFwaThGV3psaWF4ZC1ZUk1fYXBKU3U4NzRuS0tlNlZDaVlwNGxKLU1Sb016T0Y2SzFDR3kxOU5FNWxMU1V3OUNUZzFqY0Y0cU1wdUdXdXFUaHVJal9DdXdDQlpweEVLdzBRLWd0RURYQ2dBQ1EydDNkSXU0SWRyR3dZdUZTekVoLUFWQXRZbWc?oc=5) (Sat, 16 May 2026 09:01:00 GMT)

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
