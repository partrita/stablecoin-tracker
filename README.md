# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-17 02:19:02 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,683,357,306** | 🔴 -0.11% | 🔴 -0.47% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Marqeta and Coinbase Take Stablecoin Spending Mainstream - PYMNTS.com](https://news.google.com/rss/articles/CBMinAFBVV95cUxPZGV0eDEtSHFQV19mdnNLZDU1bjhSUk55QW5NN014bUdaaFBQRWdTWUFYN1ZPVDB1MllLQmRUZEFVV045SWMwa0F6akh4bXJvU2cxNzVpSDR2cGczemI1VmlkSnRIcVB5bmw4emhOOXRtM1cwc1VncDBwc09oZkw3M0RzTEdJclJDbksyMGg3ekpJa1FFbzYyb0txUU4?oc=5) (Fri, 16 Oct 2026 22:40:02 GMT)
- [Japan’s three big banks complete joint stablecoin trial for cross-border payments - Trade Finance Global](https://news.google.com/rss/articles/CBMivwFBVV95cUxQTHktR2lPaDc0LXU0Z3dSMkRkVmxCaXhudC1BVHV0S0JINVEzQkdxYThfX2VmMWQwNXFjOEJhR1hVLUpxS2ppb0VZa2ZwakVvR0xxdlRWUlhGN0xiQmZUaWk2OVhVYURiZThmQzI0RkxLbWM4NkphNEpYWk1MdTNmNFJuU2JBTUlaaDVINGRWRlBaUWRDeHo3VEdBczRjMjVmSzF2dUFUR1AtT0tqTVpFMThVaUFkQndMRXhQNVRNMA?oc=5) (Fri, 16 Oct 2026 20:12:01 GMT)
- [Visa (V) Could Be 64% Overvalued As Stablecoin Rollout Tests Valuation - Simply Wall Street](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPNkhVSnRKYlYxV3RhZ3FtaWtQaWo3cWFpSTZaTDRnTkxPN1JoaEVpWlF0NzZZcEMzLV93Yjg4RkxCZXJEMHI4NnBpdnpkYzUzeUlxYTdXWDlFWHVQR25uV2xvenppRlRxdUZ4QXBTVk1GUm85QnAyLTNmMW9Xa2xZTzViMHphbVlUTVYtcGk0WVdxcXVRWk1Xd1ZGSnJwd25MaEJvalVXMUdVMGJZcHZyX1hJZEVjYXFCUTlabGVWaWV5dG5NMDE5SFZBWWJXS2g4UXfSAdIBQVVfeXFMTzZIVUp0SmJWMVd0YWdxbWlrUGlqN3FhaUk2Wkw0Z05MTzdSaGhFaVpRdDc2WXBDMy1fd2I4OEZMQmVyRDByODZwaXZ6ZGM1M3lJcWE3V1g5RVh1UEdubldsb3p6aUZUcXVGeEFwU1ZNRlJvOUJwMi0zZjFvV2tsWU81YjB6YW1ZVE1WLXBpNFlXcXF1UVpNV3dWRkpycHduTGhCb2pVVzFHVTBiWXB2cl9YSWRFY2FxQlE5WmxlVmlleXRuTTAxOUhWQVliV0toOFF3?oc=5) (Fri, 16 Oct 2026 19:39:09 GMT)
- [Stablecoins Take Aim at Cash Locked in Prefunding - PYMNTS.com](https://news.google.com/rss/articles/CBMikAFBVV95cUxOUDZUT3BvTVRfLWN1RDdqSk0weU96NXRWcm5SYkprUERnVjJEQ1BEMWctSHlWSlA2a2xjNVI1OG91TF9jTVhPU3dkbjJqLWJrTTBBVEh0QXNmOGNrc1ZoV1E4NzRiSXN6UXQ3ZVF0SU1QMTF6MnZvR2Mtbk43WnI4cjNCSlM4bGVJbEgxQTB0OUY?oc=5) (Fri, 16 Oct 2026 19:29:31 GMT)
- [Stablecoin Rails Go Mainstream: Ripple, Kora, FSB Oct 2026 - FinanceX Magazine](https://news.google.com/rss/articles/CBMirgFBVV95cUxOTXhCbHctQkNtS0dmYXh4OGhDMTBKSldZdi0xaDJTZnRGTnJYUUV1VnN6UF9sTkV3cW8ydGZtVlZKdDJMRGpjckpMNVlnaUdLWTZRQ1NOVUgwZ1dKOVFZMl9XZ2kxTFJvb2FnanZmYXFCY1JsRThmMndiZzJCTmdqeEFYTzFIS3VobTI4MFFMQWdRbHdYVkUwbTk5SUFBZGdlcS01N2xMT29kdnc5V0E?oc=5) (Fri, 16 Oct 2026 19:03:40 GMT)

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
