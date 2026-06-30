# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-30 02:36:05 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,882,622,426** | 🔴 -0.56% | 🔴 -0.89% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [MGUSD, Explained: How MoneyGram Built a Stablecoin Around Distribution - The Defiant](https://news.google.com/rss/articles/CBMiogFBVV95cUxNWGxZdG1halNnRHVNWmVPVGlKd0Y5cE9xbnhjSmVhNW9NSlBGQzQzd202OWEydmt5dWNsUHFlekhTOUZsaWRzbXZuc3FSZWV6aFh3NXJyQy1HV3cyMnZsYkFoRDZYaDVLOXFyazlnTndIOTI4cFdzQUpGXzhSX3UzV1lPZW10SjNoZFRkaVcwMmtMZ1N2aDBic01oQXMwbFZlQkE?oc=5) (Tue, 30 Jun 2026 00:56:50 GMT)
- [Ethereum Built Stablecoins. Its Price Drop Reveals Their Biggest Shift Yet - PYMNTS.com](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPY0xsRXBQdXlac1ltMXBhYjdIYl9JMWh1di1nTzBSYnNISS1yNTd0cW82VXQydEZqRF9qbTJ6Z0lsQVNrQTJCY1ZPMEp0RXRuQ0pUMldTaHdUX3pCVmpzUEpZaTIxcG8wRXMwQzZaTG5wdFhDVzZ6ZUk0cVoyZFVqN1JqdGxqVFNxUTlxTlZHUFdvdUt2NHBIRnRmNkhHMFpTRkVBVEFfLTYzamZqUV9lZnlyOEp4ZVps?oc=5) (Mon, 29 Jun 2026 23:14:03 GMT)
- [UK dilutes stablecoin capital requirement in final crypto rulebook - Reuters](https://news.google.com/rss/articles/CBMitwFBVV95cUxQUHRNOVJFb2lhNGdTdlV6am1nVHVodkNlSkswdERRSi1BN3pieDNIOHo1UnRsZm51WlljeWpoQnc4eEZoZ0taQ1lhWGVVUTZ5RmhMc3ZKVW5WTVVTSnFrSU9UZXExQ0VGUGpDU08tbm1XdGVYMHhVRnNGcWE4RUxVQ2YtRGE0UGNWaEhMTFpLMnFRaldPUU1GZGxsLUZQS3pkUG5mYjc4VlhRNDkxS3dwVmdJTDh6R2M?oc=5) (Mon, 29 Jun 2026 23:09:18 GMT)
- [UK Regulator Vows to Simplify Stablecoin Capital Requirements - Bloomberg.com](https://news.google.com/rss/articles/CBMisgFBVV95cUxOV20zd1cwRTBacHI0ekRTR192SDBPMHQ3T3dCWnVhSXhyX2dwN2MyWW5adjRSTVc2NGhTSjdXQkFsN2pMeGQyX2E1WURfd29hNUxMRmg1aGdPbmZYbzJmTlNmS0lHZW15U2doTU9HdHJqVm5IX1Mza2hMNXhDTTdJMjduVDRDNW1OM0ZhVURqS1dhYkU4bjFGN3FtcVlFSGNUYnhiM3I4YVVFTm1YUzRyVGFR?oc=5) (Mon, 29 Jun 2026 23:01:00 GMT)
- [JPMorgan urges strong safeguards as congress weighs crypto market structure rules - CoinDesk](https://news.google.com/rss/articles/CBMiygFBVV95cUxNR1hQNFBsQjZVemlfNFVhUlZwcHBMUHlXbXF5Z2Jwdzh2WHZXeGFfcFpOVnBsYnA4NnAwTXdlYV9SOURJc0tmYnVmSURsd2Nma0VBVXEySGU1MEhiaGJXclRPdlI1eTBKZjhicDRRZFFSY2lhakFLaDZmMjlVaFBUWXl4c1l0Y2FaaGVxQW1uZTRxSXRDZVZGdnZxS1pEZVVCeUlEeWJWQ0NkMkR4WDczM3kydTQzSkhlNExwdzZBUkhXdHpNZVpHMm9R?oc=5) (Mon, 29 Jun 2026 21:00:00 GMT)

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
