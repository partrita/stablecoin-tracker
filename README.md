# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-11 01:30:01 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,903,868,617** | 🟢 +0.05% | 🔴 -74.84% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Better Stablecoin Buy: USD Coin vs. Ripple USD - The Globe and Mail](https://news.google.com/rss/articles/CBMixgFBVV95cUxNdTJPeHNqUWNUX0VKc0VMdG43X0RlM0lvM2Y5dUlVRDBucGlBWklEXzZmLUl5SFZLVF9yb1BEYzN3NEtQMk9fODliZ3pDNloxMWh0aWRlb1JTTHp4cUI0eGJobFo5bVNMVGJqRmJmNldreUFWX0xCVXdIRll6ODRxTjVMaXpOTXRmX1RxOXZMMzBwVFJPaUtmX0gwelhxeTZMNkRyM1ZyX0Voc2VKTEE4Z3ZORU56cHIwZVZfNzRDZHZkUVlHY2c?oc=5) (Tue, 10 Feb 2026 21:28:49 GMT)
- [Avalanche hosts Fosun Wealth’s yield-bearing RWA stablecoin - thestreet.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxNQUJZUWpCdWcxTEJNRTg1ZnVrMTF4a2RYdWhhajVwZ0ZPSEJVRFl0YWpvY19hSm9OTGxFckNWU2IxVEk5UFFDTHl4dFdEQXl4SmpVOWFrc2E5eGltWnNsa0ZqRjVHZlM1Y2p4YWVyM0lyczhJMjZfTTBweDRRMnRzOE1wQmZQcDFWLWdsTWZtTHI0QmZ3Y3JYbUNrNExpcmI0bDBxag?oc=5) (Tue, 10 Feb 2026 20:53:52 GMT)
- [Better Stablecoin Buy: USD Coin vs. Ripple USD - The Motley Fool](https://news.google.com/rss/articles/CBMigAFBVV95cUxNQzN6WDRxTlNaRW1hOUNyMkF5cjNLNk9VbUZTdTFJazNYaUdvVUZHUU5xamVKMlpTc2p0V0lCenRjajVneUk5VmZ6aUNocS1SV3EtczB0dXpJekpHbV9ic0h1ZHdlT2VXbW1kQ250eDhyMHlZWVZkaU1pNms0cEZadg?oc=5) (Tue, 10 Feb 2026 20:43:00 GMT)
- [Protecting Kentucky’s community banks starts with fixing washington’s stablecoin gap - Middlesboro News](https://news.google.com/rss/articles/CBMivgFBVV95cUxNT2lwdWltU1JtSFNtZm91bEtTSVRXLWJPSmw2TzVneTJOeUg0Mm43cFUxNWYtbm9id09Ed2k5eWN5Wm50bnZQMDBzSzdqdWtHYk9Lb3lVRmdOazlEQktUdnktLVZCVjJzMUZ2TEt4dmF4YWlFUWJmZGhCZ3l6WWJvZ3ZkQmp6dWY0WWlJdjhqQ1k0TmFPY0lEU1FDSVhmNV80M1RoTFlqU09uMldDZXdYTVFSbEhhenJQdC0xT1l3?oc=5) (Tue, 10 Feb 2026 18:00:40 GMT)
- [Japan's Nomura, Daiwa team with top banks on stablecoin-based trading - Nikkei Asia](https://news.google.com/rss/articles/CBMirgFBVV95cUxQa0R3ZFJVcmVYQ0x1alNvOUZuQW9BbDlyZmg4dEJGX1VKR3BadjZWNXFRb19RalBOOF81TXp0YmxSUk5vSEphRXZ2VXh0dDZBcnZpc0h0a0JxQS1PUlRURGZqMUNpRlYwNE42bHNOYzY2QmdSajJtOUo0U1Z3V1k4NE03anp5UkU4WG1LMjdKNmY2OWg5WW11Vm5POVR4TE9UZEgzT0c4Z1hlWUFhRXc?oc=5) (Tue, 10 Feb 2026 16:54:00 GMT)

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
