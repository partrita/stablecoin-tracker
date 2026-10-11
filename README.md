# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-11 03:06:57 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,076,742,573** | 🟢 +0.01% | 🔴 -0.42% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Trump-linked stablecoin USD1 adds $427 million in a single week - Startup Fortune](https://news.google.com/rss/articles/CBMilAFBVV95cUxNM2RHVVJoMTBkOHItWWV4V1dULWNpa0RYZHAtYjJLUS1NalJ0WUZlLVZPR1VkNF90cmZsZ2RTMWNicmFGRXRqWkprSkFNaGU4UXdwbTc3MjFWWk1yVlBmMUdyZk9kQmZKWi1rT29EMC1xRXJoT1pSQ0Zzdm9XaFN4MDVoaFZYREY1azVVTG1TM05JZnJO?oc=5) (Sat, 10 Oct 2026 18:18:38 GMT)
- [French Committee Backs Stablecoin Swap Tax and Crypto Exit Tax, Then Rejects the Budget - Decrypt News](https://news.google.com/rss/articles/CBMickFVX3lxTFA1RzI3YnlwajlIQlkya0ltcVFsSV9sajVzX2VlZE43OUt1WlZWWDFOTXJXMFpPbUlZZVl6d1FSXy1yRjVZVzktUUdoS2U4dE1SQVFwRmFBdUt3eE9xUkRTTVAtZGRCR2YwUWNKN0lfbEltUQ?oc=5) (Sat, 10 Oct 2026 13:01:03 GMT)
- [Polkadot launched its own stablecoin and traders dumped DOT anyway - Startup Fortune](https://news.google.com/rss/articles/CBMimgFBVV95cUxQa3dYT19kUGlsVkdpeVFzczliV2hURW93bUhLUTFNcjI4X080MVVWWlFzS1dHQTgxYTRLdlA1UzlhM3h5OEFzOUlsS1YwUHlveFRaOGVacndiRDE1X2lWemQ3R3p0ckJBZTFRQkVhM0wxWXBva3ZrM2RWbDBVVEU0M3JfUTJJaEV5c0NvN1NUb1FpYlAta0dQZ1dn?oc=5) (Sat, 10 Oct 2026 09:24:23 GMT)
- [Coinbase and Gennius Plan ONED Stablecoin Access Through Latin American Banks - The Defiant](https://news.google.com/rss/articles/CBMixgFBVV95cUxOdEF6M2drMFdMbzZYSTZYV2hyN3JNelp2NENWQVNkdEZjUEl4TEdwekJ0bjlMWGQtWGJXN25FZDd1NURxMFJiQlEyQWVUWHlUc1FUempZbkl1TTZ5UktLUFFvZXNFZ1p3d1ZwNHRTbENjeDR3bTNSSVJENUg1Q3NPRUNBQmVDSG5PTlFfeHlPOXFNZ2FXOENyRXNtQnJXQmNsWG9sejhkS0xhSEtzc1g0S1lrODBSRTdLR3FwN2tINUVIYTdWaWc?oc=5) (Sat, 10 Oct 2026 09:07:55 GMT)
- [BTQ Technologies Will Shield MoonPay Korea’s Stablecoins From Quantum Attacks - Quantum Zeitgeist](https://news.google.com/rss/articles/CBMigwFBVV95cUxQUXJELW5QMkR2WWJWYTR6V0FROTM4UlhPek96MnZFVExMRUFrUVhGaVRRYV9ZSTNlcThaRV8tSG1IUExoMFM0RUdDam5lVlg1MExSczhhSkRjaEdncjNTMEJnVHZMTFFnSEczVmNPc0JCNXczc0Y1QUFRTHJqMjBvdFNVQQ?oc=5) (Sat, 10 Oct 2026 08:32:17 GMT)

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
