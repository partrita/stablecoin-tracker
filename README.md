# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-12 02:11:43 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$301,383,554,338** | 🟢 +0.12% | 🟢 +0.20% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [&#x27;We Need Your Help&#x27;: Banks Rallied For Stablecoin Yield Fight - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTE00UHQtbVQ0Uk5uZG9ZTXZBSlNab2laanFsRE02YjM1NHlHako0MS0yNWJLdEVtZVBZNGREa1hVcXNWTGk4Rm9rY2kteG5oajNKNFVVcXJ30gFWQVVfeXFMTTRQdC1tVDRSTm5kb1lNdkFKU1pvaVpqcWxETTZiMzU0eUdqSjQxLTI1Ykt0RW1lUFk0ZERrWFVxc1ZMaThGb2tjaS14bmhqM0o0VVVxcnc?oc=5) (Mon, 11 May 2026 23:31:00 GMT)
- [Anchorage Digital Ends USDG Promotion to Assert Stablecoin Neutrality - PYMNTS.com](https://news.google.com/rss/articles/CBMiswFBVV95cUxPZ1V6M0EyVXduVGoyTkY5clU4UXNvMnRhVmNaY3FoTFF3WVRVakQ5WHpKNENMR1pZU0c1M0diLXdYNG1DWDBmRjBUQW11MEhPVzl1Y3ZvemZ0bXhvelF4U25nQ3prUW95QU9zWUpZeVpCUWlmWWJwVVd1LXdpVlEzRGJKWVhjSkg2TGFlV1BaQ2laRXc0ZU9WY1BqWHQ2NWZzeUxqaUlEd0U1ZjRFSWN4TXBpZw?oc=5) (Mon, 11 May 2026 19:53:12 GMT)
- [How Mastercard’s Stablecoin Remittance Push with Yellow Card Could Reshape the MA Investment Narrative - Yahoo Finance](https://news.google.com/rss/articles/CBMirgFBVV95cUxOUmxadkVWM2VrN3A5RkNKUmpPMmVaTEJoRU9RWmdFSU5MTlNiZU10dGJ5cGItRnk0QU9LMXRiajRldDBfdlcxODl4MnlWSTFWbWpBeUlBR3hwMHZUMDJ5MjhpWFZhUVRCckg4bGk3SDZiS0ExbVlJZ01iMGNQNnNfU0lfZXhIUEo3WmVKVFUwT1VrVTA4bEkxT0dmMlV6MmdNRTNianZUZ1BEdTlONFE?oc=5) (Mon, 11 May 2026 19:13:20 GMT)
- [Corpay Taps BVNK To Offer Customers Stablecoin Settlement - PYMNTS.com](https://news.google.com/rss/articles/CBMingFBVV95cUxOU1Qzell3VjFmWnhFTmJ6b05SNGJxbE9wLUhhcTdtbGNjZC1jR0Rtd3RRQzVDUTBObHgyeUtSbFJyM1UzLWN3UXJoaThWMHd0dGtzMmNRZHBBTThOYnRfbGpfZGU0QXE5VXB4WjBXelJxMm5lYlVnc1EyRkdtTER5UlhBemZmbjNVMGZpQjc4TWl2OFFkRUQzLVVfcDdfQQ?oc=5) (Mon, 11 May 2026 18:35:24 GMT)
- [Stablecoin yield: American Bankers Association urges CEOs to contact Senators - ledgerinsights.com](https://news.google.com/rss/articles/CBMirAFBVV95cUxNOVBEUWRKQThGLU04NjVaaVJjWnprb216MWgzeE91RkdZbVdBeHU2M3ZwSTdqZGgxT2tmempKWGlBQk9mZmZvR2dvbmZ5TzU3MzIwX21VdGNxb19NX1dKVTdJN3E4Wk1FZFc3WVJXWmZ5ci1HUVBYVU1SaDRMMUVaTkVSTlJ5akpjdlo1YWg3UHFsN3BfR2xxOEVtbEg2Um5uQzhEZmZjQVp2dkw4?oc=5) (Mon, 11 May 2026 18:07:54 GMT)

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
