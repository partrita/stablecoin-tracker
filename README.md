# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-17 02:52:01 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,718,343,846** | 🟢 +0.01% | 🔴 -0.16% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [NYDFS releases new stablecoin regulatory framework - State Affairs](https://news.google.com/rss/articles/CBMie0FVX3lxTE96bXBucGladEdNN3Nsb2dNWDBOdEZHdExxbEdwajQwS2VBUEI2blRWbWRYWjJ5bGhReV9xSzdSZDFIZnJOcnU1TlEyRjdRRUVCdHI4aVFqbXBZU1lHbE9uY1ZaeUJ4NmhCWEZZN3JtREtjaFVyLTRTZ3RuQQ?oc=5) (Wed, 17 Jun 2026 00:17:09 GMT)
- [Visa’s AI Agent and Stablecoin Push Could Be A Game Changer For Visa (V) - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxNMG80N0lhWmVHdG5YSHhybmFqOEZ1VDEwNGFsQlcyOVFfNThpYU4wZ2ZRMVJLUUhhamRJb0hPdmt1ME56NUtfTmQ1Rm9xd3NBM2gybnRZTXdubUhLS0NxV1lTNUlONVNkcUEwTnhwQUZ3ZTc4dkgtYUs0Ti1XeU8zX2x1ZnY1ZjRSMDgwUE1sVlFUQU5CbURySQ?oc=5) (Tue, 16 Jun 2026 22:13:02 GMT)
- [234-year-old bank launches stablecoin fund - thestreet.com](https://news.google.com/rss/articles/CBMiiwFBVV95cUxONGtBbks3UmlsM096Ty1pNTJOYVplSXJNcEcxSlBaUWJYT1REdWt4eGdWU1hlMmRVQmpNVzFXbEJ5QTZCWDRsQ3ZxQ0xzMWVBWFE0THVpWmZjMDRiY1ZLeURYM0czR2tMcXk4VlhSNnY3SmdhNDBic3VDNERvSjRUT0dvM0NLSVplaDI4?oc=5) (Tue, 16 Jun 2026 22:05:45 GMT)
- [U.S. senators urge Treasury not to leave states out of GENIUS Act stablecoin process - CoinDesk](https://news.google.com/rss/articles/CBMixAFBVV95cUxNT1lNM0w2ajlQWUhWLU55ZDB4MEZSZzFlckNWOFBuSVJBTHZYS0ZnMTBkUWxkMnFZbUo3WmY1RHFmeGVXUkduWjloeFVqdmZTU2dLbWFpVURGdUE2RGdzN0F3VHdjanZqeExCT2hWdXdYQl9vSDNHMU9vUnNSQWVuaVY4Tkh2eEdHX3MyUFNQUjNnRjBQbWczV0Fjbm5YcjBvLVQ4OHNtXzlQcFJBVHFKSzA0OGVraVZXN29qakZXTW5iMzcw?oc=5) (Tue, 16 Jun 2026 20:37:22 GMT)
- [Cryptocurrency banking, stablecoins regulation proposed - The Center Square](https://news.google.com/rss/articles/CBMinAFBVV95cUxPbUVJcmxnYUJTbkdFdWxqSDZXRWJDei1sM3pGcG1nei0zcVhCbDFiTmhlcmcyYkFwYmJnSVNuV0oyUjlzMnpBUHB0TmJjb0RiWldlc0ZOTl9NVm9xWjhWaTNyZlZYVnF2aElQWWdFdVFRaUpyU1M1TUl4dkVVNXY3c1BWaG9Wc1ZKbzJVZE41eENDRmZvNnZ1OWxfb3DSAaIBQVVfeXFMUHNUakl5ZVdTaWRac2JMZlZudlZWbUQyWnJkbTVSNzBRQmFUMHVSY1FVOTZTeVVSRzVrb0dlRDhrZFVuQkx0Z3NyT19JaGJpYk1Jd3M4akVKRzFaUE0tUm0tWWRtOERDdmdKalBFTVRtVXpfMzQwQldEVGdzWTlyQWlSNjRLbWZQOTQyU0tUaWJ4OHA5TUJoNFFDVUdyREltenRB?oc=5) (Tue, 16 Jun 2026 19:03:00 GMT)

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
