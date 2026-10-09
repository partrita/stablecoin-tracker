# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-09 03:50:27 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,435,122,426** | 🔴 -0.25% | 🔴 -0.17% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [XRPL’s $1.34 billion stablecoin base doesn’t tell us how much XRP users need - CryptoSlate](https://news.google.com/rss/articles/CBMinwFBVV95cUxOU3R2ZXRoS3pwdnE5UlBHbWMzVWNUYktBanFmRGFiSC1ad29GcTZRdndRNW52TFRGbzFqME84Z2p5R0tLeUtUeE9HRS1aR1duV2JWMWh0VTBYdXhZWFhGZzRicVlFNExYT3R6bDZtYWJLNmxvUHlpdl96b0NLUXgxLU9Wd2VyMG5Xbk9SZ1FJbEY1UVRXYW9sTjFuN2tJQ2c?oc=5) (Fri, 09 Oct 2026 01:00:56 GMT)
- [Solana Price Forecast After Samsung Stablecoin Partnership With SOL - Bitget](https://news.google.com/rss/articles/CBMiY0FVX3lxTFBhZS1DYjRNeDBmVFlWbUhMdGswRFlFLTZVNTY5QWlQazlzNjdXUzYtdmlVTWQ0U2x0SC1qS1VSUGc0d3dtTFBmWlgwY000bUlQOUJKczNla0dPaVdjR0FNeTZrONIBY0FVX3lxTFBhZS1DYjRNeDBmVFlWbUhMdGswRFlFLTZVNTY5QWlQazlzNjdXUzYtdmlVTWQ0U2x0SC1qS1VSUGc0d3dtTFBmWlgwY000bUlQOUJKczNla0dPaVdjR0FNeTZrOA?oc=5) (Fri, 09 Oct 2026 00:21:30 GMT)
- [Anyflo emerges from stealth to simplify stablecoin payments for enterprises - Finextra Research](https://news.google.com/rss/articles/CBMiugFBVV95cUxPYUNSM01wRS1fX3MyNWRGZzU3SjBGM0R1aWtTSEItMjZLQWxodXdXR0xCMlJ0ZkphVm9NY0ZZR1dzTjNGMlNOaW41aWhlVnJpUDZyemYtSjk3OUVVbnZZNm9yRXVQazhkSWZ3bTNrODFmWnB0X0Z2cG1FZXdHRzUxRjdoUmQyUnZISGQzOGFROURldG5WMnR1aFN3N3huOUl3TV9MSGxjM28yOHd4S0Q0SkFKaWUyX2lHUmc?oc=5) (Thu, 08 Oct 2026 23:34:12 GMT)
- [JPMorgan Chase (JPM) Puts JLTXX On Ethereum As Stablecoin Reserve Rules Near - Simply Wall Street](https://news.google.com/rss/articles/CBMixgFBVV95cUxOSXo5UTlXVW5HYVhQNVdpT3pWQW44VUZDcUpyT3NJQU9DMmV1MWVzdkM0Q2VXTW5nNTlMQjVlT0t3NjJYcF9nLXZndkxYTXFUUGtnTldya2pzTldQeE9qbmpTOVktcnpLSFlKOWhkcmJydmFWR3pVWWRGNW9BVTlLZ1h1NFZMdDZ0bHFsZGF4ZGdveWw1cFJkc01YcUxkZU5QMjgxZ1RoczFBY3VWX2RYeDhGVzhmMi1GSzZLbXFlNGpFbWV5WnfSAcsBQVVfeXFMUFV6YVA1RVZWSzBmZ3NDTlNHc2NqYWplUmNWU1NYQzVWWGJMRkdXMmNNcF9TMW93dmF4dFpsRDdzQlR0Q1NIeDg0R0J5eFpxcEp1RkNRRlJHOGpvWFlkdXhoaGtkb2ttVnYyckNZbkNaSWVqbDZIaDViYXdjcy1YMUY4VlZGSzNDdWhKZGxyLXZtVC1lOW90RVhYdkxGV0lERm5DcXRsU1ExSDFoajFnOUU4aUU0LTd3cnV5X2d4TmNUeFZ0ancxSlVwdVE?oc=5) (Thu, 08 Oct 2026 22:38:35 GMT)
- [Visa (V) Stock May Be 13% Undervalued On Stablecoin Settlement Push - Yahoo Finance](https://news.google.com/rss/articles/CBMijAFBVV95cUxQeXRrQkNMb0UyZGhZa3U0bUlTTGZuRmJkdmpNb25iTTE1d1ItMy02WHd0ZkpXY3VzaS1ZMXAwYU9RT1BXdkJ5VjNEb2pxU3FWNjdKTmtSVzZHenliVTV4V014LTJ3SmNRUjNfTXZUZURPY0w2anNTUVFjelFnUVllNVdZbnhiMXpOcXJ6Sg?oc=5) (Thu, 08 Oct 2026 22:12:47 GMT)

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
