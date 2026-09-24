# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-24 02:25:18 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,118,882,755** | 🔴 -0.05% | 🟢 +0.67% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Cloudflare Exec Says Ethereum&#x27;s Original Sharding Plan Could Work for Stablecoin Payments - unchainedcrypto.com](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQdzBQb2hjSmQxbGlWWGw5ZUNZQVlzR3hsTURkV0lkQlpCTUZEZWlQSEJ3cXk1MjZMaEQ3LWpPYnhmSWhzLUpxdTRvcTZDUklkX3RUSHd4Q2VOVS1ibjNXOXJIY0pqeFUwb1FyZDJ5R2lJZUVrb1dZaTJ2ODhjSUVLTnVQTWlYMWlINkVzeWtFSWt6Rm5UU2RoLWFpbWJRT3gyLVlOUENESUhFdmhiVzdpQ21Td2JHQnJT?oc=5) (Thu, 24 Sep 2026 00:01:12 GMT)
- [US Weighs Initiative to Promote Dollar-Backed Stablecoin Abroad - Bloomberg.com](https://news.google.com/rss/articles/CBMitAFBVV95cUxQOHFZX0dvRUs2b2Z6d1paWUxNTGN4TWNQQWZXWnNENzV5NHVJRUw1TEdKa0dqaG1tdUZ4UF96YmpMM2VsR0RyZlBEbDQ3UEsxU0Rlc3JwNUtaQW9xYlZFWDZhaEpHS2pzakZ1MzZ0R1oySlBRVFNpb2pfWU5PbmVTbnJUQW9RdldUYUd0MUxCeHlOYzhqTHBYeTZCOEhCTDZ3SkVURnpiT0lOeHNPXzhvR202bmc?oc=5) (Wed, 23 Sep 2026 22:15:54 GMT)
- [US Weighs Initiative to Promote Dollar-Backed Stablecoin Abroad - Yahoo! Finance Canada](https://news.google.com/rss/articles/CBMijAFBVV95cUxOOEtuZ0piOUIzN2d1RGh4SVV4c1BEYWlNTlVXbGxkdW1DbTNPcnc1RXNVM3pETVJvYlotcnpDQWdWUFZqelRWQWxNZEZ5LWdjYjRKMmdrelpXUGMwaDBoV183SVFZa214bVRWWHkxcFFySTF4Z2hUQ2tVT1ZhamtaUUc3Uk1YSWZGYWV1Ug?oc=5) (Wed, 23 Sep 2026 22:15:54 GMT)
- [Is Visa (V) Trading At A Discount As Stablecoin Scale Grows? - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxQWHVNLVJJUE9pTUVSZzZaTVVBRWIyT2UzbjI1bVBUcUxkb1dlaGZmdVBRUUl5WU5raDdsaWFPREFCd05zTjhsdFBxNVhwRm9pZmtCXzhyMTAtRllwcmRUX2VJeDl2Y3p0VEd2SFk1S0tENUt0NzA5MGx6OGl5ZTdOSFZONTRDVElDVXlweGRNUkxUZGhBT1EwWFBudFEyM3Fp?oc=5) (Wed, 23 Sep 2026 22:14:16 GMT)
- [SoFi Bets $25 Billion on Putting Stablecoins Behind the Card Swipe - PYMNTS.com](https://news.google.com/rss/articles/CBMirwFBVV95cUxNdTR1MUV6dXlvZVFpNE5TWUc1bURYUmxUbGxPOVNoODVHX0NWUldoejNaZkE1VTlobEtpZlhGb2dKUWZGbTJPVUpadl8yWDZZNURuYkkwbXNLMGFCRHYwTFdVWDBXTDlUdDZQVDhkelN0RTlqQ0tDMHJ0WTU5ZHBGZHcwRGFfMkxfclBrZDM4WUlLcXNTQkJnbkdFM1NLRjJfdUh5MXZIMjhpbnhGX2VB?oc=5) (Wed, 23 Sep 2026 20:50:48 GMT)

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
