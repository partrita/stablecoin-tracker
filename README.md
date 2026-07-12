# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-12 01:55:53 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,785,690,538** | 🟢 +0.03% | 🟢 +0.46% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Digital Dollar Banned Until 2031 With Stablecoin Rulemaking One Week Away - InsuranceNewsNet](https://news.google.com/rss/articles/CBMisAFBVV95cUxNWHpGY2psdk9EbTk4TXA3Umx0NTlnUkx2cEM2MDI2dVpHMUxNQlk3RW1EczVhQ3V0WWdFUEItd0tPS2F6Zk5CZTZuWW9nSHNLTkVHUnlMR2cyYTNMNlJEU2pXNVFWRHlOMmt1ZTA1ZV91TkFPczB1bWZKMURNdUxreVVuRTVhd001YmhfSTU5TnB6RUpJZ0dTODdoWUhOY0ZoU2RlU2R1TU5sNmdHN3FyYQ?oc=5) (Sat, 11 Jul 2026 20:07:48 GMT)
- [Ripple&#x27;s stablecoin is fading away on popular chain, XRP crashes - thestreet.com](https://news.google.com/rss/articles/CBMiigFBVV95cUxQSGxsR1lwR2I5SWVDZ1RBZlF4OXc4elBCRXlIdjVBc2Y0SzBSSWIyOTNNX1daaE9leXZDWXBiN1NrWkt2N2NLMkczSEo5blhZTEQtaGJjdVVZVW9PbEt4RTZWX0NSdnhGZm5tdVBoWk1KQjVGc0xfV2VKVG1PXy1rbkJ3UVo2M0g4amc?oc=5) (Sat, 11 Jul 2026 17:58:54 GMT)
- [Circle Just Became The Only Licensed Stablecoin Bank. Here&#x27;s Why That Matters (NYSE:CRCL) - Seeking Alpha](https://news.google.com/rss/articles/CBMiywFBVV95cUxNbTRwQXRHS3E4WWFwWmY1b3lYY1dpQWQxbXRvV0h2dl93LUNJTGtZUlpSMm1nYUdTdF8wREhXOFZxbWNJRW5vR3dvcHNPNUdmb1o2VGNadVdoU1NSTGVWUS1xZ3l4T3lfc2NYMldGeUpBODg5NkwtbFRVYndzbkNqRE9lUEJqanZadHlWeEpDQzMtMkhMSktpdGdmNWN4Um1pRjh4MHdXMHdOek1pSG1UYnFMbW1uckVEY3h6aUhCcl9rZkljM3J2UUZobw?oc=5) (Sat, 11 Jul 2026 12:13:25 GMT)
- [Internet Economy Stablecoins - Trend Hunter](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA5ejlYU1RNRU1rV1VfTEhHckZoZlVVSi1FMkJFblFTQ2E4SkZSSmc5YUV4aTluQmcxNUplc0FNY19tb25oMHBWU2VYTTJERzlvaUc1RWprYThIcmfSAVtBVV95cUxQOXo5WFNUTUVNa1dVX0xIR3JGaGZVVUotRTJCRW5RU0NhOEpGUkpnOWFFeGk5bkJnMTVKZXNBTWNfbW9uaDBwVlNlWE0yREc5b2lHNUVqa2E4SHJn?oc=5) (Sat, 11 Jul 2026 12:08:09 GMT)
- [MILESTONE &#124; TRON Dominates Issuance, Settlement of World’s Largest Stablecoin in H1 2026 - BitKE](https://news.google.com/rss/articles/CBMie0FVX3lxTE9td2EzUHR2MGpCemtaTGR6MWx3cDdYX2FJUUZ5T0JXQ0NRX015OV9Rajd1c1lHd1lrVzR3V19jaHBMY2h5ZXNKR0JxLUhyUmpqTzQ5Sk15SnlPQ3FmdHJvTU92dmxOMUY2ZFdPYnF5NnRMNWg3SjlON1hOVQ?oc=5) (Sat, 11 Jul 2026 06:00:24 GMT)

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
