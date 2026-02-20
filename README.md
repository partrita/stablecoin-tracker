# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-20 01:18:54 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,852,279,441** | 🟢 +0.05% | 🟢 +0.22% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Latest White House talks on stablecoin yield make 'progress' with banks, no deal yet - CoinDesk](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNOXZZRVJrbjlqNTRKLWVaeU05SHJuR1FTOVNWajRYTzJlQmJDa1M1ZXpld09vUGdHVDdVYzRMZW5EY05HanU4dzE3aHRfZko3SERWaVlYeE10cWtReU01Tm5oOGJIQ1FuRXVXSEN5MlNTcnFfc2JINGFpS3hLeEFkQXp1bGsweUY4Ri05Q0lLcTdSSVhBSzhrbWhELU5GVFYzZFpqendMdXRGTFlWVWY4ZEdfNlFld3plUS1BNVBzeU54dw?oc=5) (Thu, 19 Feb 2026 23:39:40 GMT)
- [Stripe-owned Bridge acquires trust charter for stablecoins - American Banker](https://news.google.com/rss/articles/CBMimgFBVV95cUxNX2VuUXkxUEZSQ09wRExIaGJsXzBnRUktWXZkT0FRVDVBRGVSYVFoRE5DRjF5aE5RTVF0Q0FkaTNwYUt1OTJ5anZJR2hyZXI1bHl0NnhCa2t0RUhQRk9NOS1LLU5RcFR6amh6ZmFOMTQ3SG1SUGhscU1QUUItSVhLSUFJcUZNSFdscGdvSEdheXVsOUEyU1FoM0x3?oc=5) (Thu, 19 Feb 2026 22:54:00 GMT)
- [Inside the meeting: White House favors some stablecoin rewards, tells banks it's time to move - CoinDesk](https://news.google.com/rss/articles/CBMizwFBVV95cUxPalFZVUdCSTFnNmlDNFVNMjFRenBnTHUxXzRIRFhGTWJCd1Zreno2ZTFlYmMxemhxaXF6NW1nT3UtQS1PZ29ldFg1WlpnNWxzZGlhRDlxb3ZLYmZGbHVGU2VTY2JZYkY3N1NESUdZbHl0RHpKV3JiOEVSRlpGOTFIM3NPOXc3emxfZHFXNkRqOFplUEVjYm9ZRkVtdzBESDhHakx1RGVTZVBOWDVTazg2SXdqQ2FQd0ZwV2gta0V4Mm1rXzlXRVBaSUlpYmh3QTQ?oc=5) (Thu, 19 Feb 2026 22:39:37 GMT)
- [Banks and Stablecoin Wallets Battle for Digital Cash’s Front Door - PYMNTS.com](https://news.google.com/rss/articles/CBMirAFBVV95cUxNdUtsUDdCa0M0REhaclVLcGY1TmpSSnZfUE9zdXIwbFZyNTNWZUJpU1l1Y0xyODUxYlh6RlJSLW5mVXpiWFg0elBhX01kSnFLcDh2TW9PdWVUX3RWV1h4WUw1SjZnS3BkeFhFRURlZldlblFpTmFqZmJNQUtCdnBqOHNkU1JXY05CYlBMWmtQbUtLNkttVVNxUEl6X1JlRFdTTDd5SVVhbXEyaDJn?oc=5) (Thu, 19 Feb 2026 21:46:09 GMT)
- [Hong Kong's stablecoin drive nears quiet climax - Nikkei Asia](https://news.google.com/rss/articles/CBMimAFBVV95cUxPTFlSTDhjakNYRjZ6aDRiRXBHUE50enAyUGFrZDlNOEJiNWVERVVaRm8ySVZUaUM1MUN5TlAxNHFUTlNXZnlmZ1huZmNfaUwzWEdxS1NYSWQ1SWtLVUVqVnpRQkpBaEhZSUZSV2F4cVJlZWdCclBpWktDSy1KeUtyZWl3TzBadk42Mk1pTE1oUXFNSmIzVnpXYw?oc=5) (Thu, 19 Feb 2026 21:00:00 GMT)

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
