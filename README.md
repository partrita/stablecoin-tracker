# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-24 13:54:06 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,303,013,539** | 🔴 -49.98% | 🔴 -49.93% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [9 charts on what stablecoins are becoming - a16z crypto](https://news.google.com/rss/articles/CBMia0FVX3lxTFA0Q2VlYnRiYUdlVEM0cVBBczNXeExKWlJ4Rmp1TWRFMlFueDlzUjM1eS10SFNmbG9DczUzOFRsOWQyM0szOXFLMi1DMXUwMExaUUFLd3JVcFhieHJYNWhRemctMGhFb3BVYUpj?oc=5) (Fri, 24 Apr 2026 13:29:26 GMT)
- [Morgan Stanley Becomes Stablecoin Reserve Manager - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNdy1ibktKbjRENEhXR0RrNTBGY2tyTU5mQ3RUMUVpeF9XTzZGTVVtYndRLUx6VExRTlNBOWR4NzFhMHY1OFFueEpFRnZhN0Q2MUhUekZHSUZMRllpanI5eS1ZV01rMWR2a25LZ1lJVGJWTzIxUzBLbHpaRDU0ekxwZnVBRVUwdUQ4SEN5b19rNDlHbzA3VXhDN0pLZ3JrRHNHLUVoLTZyZ2c4QQ?oc=5) (Fri, 24 Apr 2026 13:07:00 GMT)
- [Morgan Stanley is latest to launch MMF targeting stablecoin issuers - ledgerinsights.com](https://news.google.com/rss/articles/CBMioAFBVV95cUxPbmtOWFB6SHZnT2JYWkRKVFZpSnRndjhaOFFzOUthTG5Xc05VQU9vcEpaRFVONkpUS2JHcXdQSVQ5cnhiVzNidVZqbjNZaHBGZFRLaThoNnZhT1dQc2p1TjJ0a3dCZHQ0aHFyb2xpSXFnbFB5Q3k0Z1NiOHlrRDB3Z2g4YWtHT3o5dE5Ma2tLNkNGVVh1eXlMTEhlZFdNb0gt?oc=5) (Fri, 24 Apr 2026 12:32:37 GMT)
- [Morgan Stanley launches stablecoin reserves fund aligned with GENIUS Act requirements - The Block](https://news.google.com/rss/articles/CBMivgFBVV95cUxPdnQweHRGZWE2S3BpS1JpZWtIeVFzbW85ekVXQlQxSGh3Y3ItSWt5X1B6MWlKbHZlNUZhcnRxUXlFZ0pfUGdmNWVfZ3V2TE5kejFhNGZJUExLM0FuNkk2MnUySHZ2SjNKZFpXQ3hyeU5LZ1ZOYnRGUlJIX29GZ1E3QzFOTHdjT2JSeUtXQXRxWXh2QjNyTU1FXzZELXZKS0NRWG9ZOER3TjdweTBkcDhobUZaOVdxWjlxeGdoLVBR?oc=5) (Fri, 24 Apr 2026 12:24:54 GMT)
- [Morgan Stanley launches Stablecoin Reserves Portfolio. Here&#x27;s what it means - CoinDesk](https://news.google.com/rss/articles/CBMiywFBVV95cUxNbl80SU0xLWFaR2RmaTNrdVRWRElLYmlFcE4xU3A0ZWZyWnZyZ1V1QjJHM3diczRDbDRCTk5CM21UWFF6ZnVLY2V1b1lrNERRMVRuYTlzRnp3Q1g4NHZTODQwdVZBNTY3ZHZtT3NMZV81dnlRbHh2WWlrMWZHVkdLTlJrMHlaRk9kLXVCeC1oVnpjc21ieVVpblNTREh6UmMwd21rTWtNZG5wUHhCeHV1NjFxdFpEQndnWkxnMlVLWmktSnUyT1RWRnN3SQ?oc=5) (Fri, 24 Apr 2026 06:42:02 GMT)

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
