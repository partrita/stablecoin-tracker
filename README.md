# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-23 02:30:37 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,482,824,919** | 🔴 -0.03% | 🔴 -0.07% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [British pound stablecoins capped to $53B ceiling as Bank of England sets out stablecoin rules - CryptoSlate](https://news.google.com/rss/articles/CBMiSEFVX3lxTE5lbFp2OUt1MndiVk1sdzV2VVpmUVJSV3J6dnExNG1MbkNRTlZibzBfTlZxaFJMVkp5SXQwbmJtazFIbDVnenE3ZA?oc=5) (Tue, 23 Jun 2026 01:25:28 GMT)
- [OCC Pitches Anti-Illicit Finance Rules For Stablecoin Issuers - Law360](https://news.google.com/rss/articles/CBMiowFBVV95cUxNTXdqN0RuQ2Jhak1ReEpIdC1IRXZ5MFhmdnVzNno2SDZmb0h4eURSSmMtS3VlWmxGWWtNRDVuV2NMMndPaXMzc0NubTlCZWgzUzAtZC03YnE1dk9EZGZaVFVmUkM2eTc5SHE0b2Q3bUt2NllQLTlRRm5vekdUeC1ZZ3hZc282ZldIUVhSMENfMzcwNko5NlBlWWdnUXN6eXBrV2Jn0gFWQVVfeXFMUEsxbWlqWTFsdmRWazh4Y2xFMkdIM21BUmxnYVZsM01INmdHQzhQV1RTdmNreDJHcHRUVVF6VVFyb0o3SGVGby13eVROb0o4OVpDczhjN2c?oc=5) (Tue, 23 Jun 2026 00:08:00 GMT)
- [U.K. proposes systemic stablecoin rules - Investment Executive](https://news.google.com/rss/articles/CBMilgFBVV95cUxPM0dsTm9WVXFpX3hwRGV2Vmx1MG5jTXJWVzdEd21iQjMtbEhmRVRaMF9VamxQb1Y3NnhGWFZydEM1OGcxdGNCM2ViRDZEc3dqa0pUU0tDRy1EaGJWVjg5V3pGSExVOUxpUTNfU0stUm1EZnFJbG56YlFnYTNqdkdyUmtDRUVOMkNGWGlLUWcybEE5cXVLY1E?oc=5) (Mon, 22 Jun 2026 21:21:03 GMT)
- [Regulators Propose Customer-ID Rules for Stablecoin Issuers - Law.com](https://news.google.com/rss/articles/CBMirwFBVV95cUxPMlJYWGZJTEo0MzE2QjRicFRyX2MxMEZFbEVKVm14OHhVaDdablhiWDBIRExCc21tb0FTaE40Z2ZTdGNrWGlIc09DMGxPY1h6UDF0c043Snk0b2dwS3lhQUhHNjhHNjJjbWZOMWZuZDJ2bko3Y2hVY251WmFwV3B1cURvRVFHa3hIWTZYaGJCLTNFc0ZUNUlBUURUd0NraEpKaER1dGZXNTFtckdsVG5N?oc=5) (Mon, 22 Jun 2026 21:03:00 GMT)
- [OCC Applying Bank Secrecy Act to Stablecoin Issuers - PYMNTS.com](https://news.google.com/rss/articles/CBMimwFBVV95cUxNUXY2YzdtRHNkQTF2eTdXNVNfZU1QZW9JMkhvVDhZU3RudHBZR2Nvbl9KNlUzUV9rZUtNbWNBY0VrVDdlRUpiaGpteUVSZUVlU09kRlJZSW9QZi1pWENidFEyQVMyS3dEOFVieWZHdDJlanppY0xTNU5LSDVmcmlQclZvNnFDLWxEVFZQN3Btb05PZ0c1TzgzWjAtOA?oc=5) (Mon, 22 Jun 2026 20:04:28 GMT)

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
