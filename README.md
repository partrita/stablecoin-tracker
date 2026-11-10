# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-10 05:24:44 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$278,307,525,378** | 🔴 -0.12% | 🔴 -1.43% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Bitso Business Says Stablecoin Payment Volume Now Runs Above $150B Annualized - TradingView](https://news.google.com/rss/articles/CBMizwFBVV95cUxNWE9LQTFkV0RUUUpBM1Y5eVBQcWMxdzZlbEtnT1p5bDlOMXFQWGU1WEI5YXRuNTgwM1l6YXN0bXdXYUgxdlFBd2FxeUFXdVEzQkRkUmtMY0xySGxpRXhfaDZkaW9RbFpEZ3k4UkpUOVd5QVJOckdKQjYxbTJDYkdQeHBqUVFZcEZySFFZNDR3YVlHR1pnbENlSlcyOVhGM19oNkx6Z0RrWU1RMnFqaW1uWm1TbGRrb0FxaFh1OUtaVDZ1MzJROW1XNlo3dTdfaUU?oc=5) (Tue, 10 Nov 2026 04:00:00 GMT)
- [&#91;WDAF 2026&#93; Tether eyes USDT as bridge between Korea, global consumers - The Korea Herald](https://news.google.com/rss/articles/CBMiV0FVX3lxTE84ZU45dDM1aVhDdG00UmpTdWZwMWN3aTV2VGRSWG5SR196RElWUVVLWkpjenAzV0xFeXNfWWEyWTY4OFZVdjkxd3VydE5ES1V1ajNYYXZhOA?oc=5) (Tue, 10 Nov 2026 02:51:58 GMT)
- [NHN Ramps Up Stablecoin, AI Payments Business With Groupwide Push - bloomingbit](https://news.google.com/rss/articles/CBMiVEFVX3lxTFBPYUJBbXVkMlpsaTd1MUFpTElOVWZ5QS1UbE5iblU4UUxpd0FPY08zcENNdVg2NktGVm4wUGF0a1ZKWTNXeUNTVmxybXl6WkE3OXZ1OA?oc=5) (Tue, 10 Nov 2026 01:32:20 GMT)
- [Canada opens bank stablecoin access, but strips deposit guarantees - CryptoSlate](https://news.google.com/rss/articles/CBMilAFBVV95cUxNT21nQWRoRVkxVWs3LTNyeVpHcm43OW50XzJJRHJnc2dMYVREU0RUY1ZFMHR6YlJwYXpieHgxdnZ2UWJqbzY0MmN5VG5ta3ZUTE5vU3B4RFJYYnloYjd2cjM4OE9leUJQLU5uRDZTRWJPQm1HMUNvdm5ieW85TzJOcEdCb3ZuUHZ0YXh1cjJESFJhOVV1?oc=5) (Tue, 10 Nov 2026 00:40:00 GMT)
- [PNC launches stablecoin payments for corporate clients - Finextra Research](https://news.google.com/rss/articles/CBMingFBVV95cUxNUU9FaEZoRWV4b01sTmg0UG5GTlN6V1R1VUpfLWE1YVNtb01mcDVJLTFrTnRpSmd0dnJKc3RjVjdVUEZCSWYtRVlveFl5MDg3QVRTRHgzZl9oZlM3VzJJaEhpdjlESXpEVmx2OWZaXzFrbFd4MlNPZy1RYVFKeGRMNlFjTllUZ2RRYkMwQjJXYm03Vmg1NXhvNUJvLU5nQQ?oc=5) (Tue, 10 Nov 2026 00:01:00 GMT)

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
