# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-28 05:40:18 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$270,767,318,265** | 🔴 -0.03% | 🔴 -0.07% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [PayPal’s PYUSD stablecoin goes live on Sei with sub-second settlement - Crypto Briefing](https://news.google.com/rss/articles/CBMidkFVX3lxTE1famJlSk1ibGI1Tmp4X1NNd1hJTl9zOVV6dExTZUFoUVd4UThlYnpRRGk5c0taX05adUhwVnZTRW1lV3owQjc3MEtUV04teS0xdkNweGxBTGlwbUtfSmFXVDFPZlJtVDJoeVl1Q093bE9rWGpNNHc?oc=5) (Sat, 28 Nov 2026 01:04:28 GMT)
- [Schuman Financial to Launch MiCA-Compliant Euro Stablecoin EURØP on Celo, the Most Widely Adopted Stablecoin Network - celo-blockchain](https://news.google.com/rss/articles/CBMi2gFBVV95cUxNQmJlenFzOUtKZGplbS0zU19CN3kycDl0VDR1M1NqRHdXQnFucDlHUHlxZUNrdDQ1M1RYRF94QU9nX2hUVGhqSFpHWFhSZzBIWlRraEVoS2FyUDVWTzZIQ0k4NC0yNllSakRyTjJUS1VqcGtZRFAzWHk2UVFuNEk4M1BERUsxLXR3NjdjRnFFbXN0X3U4aXdNNjZrS185cUs4aGc2OTN0QWl2d0hxSGFwZmlnQXE2eE42Uk1kUUg2dV9JREl5Z2duMkRSR1NTMVZTdV9kTXlBcmpYZw?oc=5) (Sat, 28 Nov 2026 00:00:00 GMT)
- [Aon says it settled two stablecoin insurance premiums on Solana - Crypto News](https://news.google.com/rss/articles/CBMibkFVX3lxTFAtYnFiR0FOdVRIenUzVVlOZmxib2RWT1JlOG9LcVpmZW9DLVRPMl9aWFM2a0s1eFJ5eFdkSndYRjUtY1U2T0JqdERib3VYeF9oMXgwSjJJUzF0WFJhckJFTVJVU09zSUNqdlVUZkp3?oc=5) (Fri, 27 Nov 2026 20:30:00 GMT)
- [MiCA for business: stablecoin budget, plan and calendar - Global Advisory Experts](https://news.google.com/rss/articles/CBMikwFBVV95cUxOc0RLT242Yk1hOHhDTGhzNzFfWGFUR0M1czlrUHBwSnZZdGNCdWZoeWVmYVNJUFdNcjhBSDFsbTlwbWtOWW9qWm5CeGRQbkIyVHU3eTljZ2FpaDgxOFBtZ0NZQk9vcE8ycGVDWXd2RDlaWGlGUmxZeXczbk9BUzFxeGVzX1dpTnhlc2xobzZqTlp1Q0U?oc=5) (Fri, 27 Nov 2026 17:29:06 GMT)
- [B3 and banks team up to launch real-backed stablecoin - Valor International](https://news.google.com/rss/articles/CBMivAFBVV95cUxQQ3picUkwYTk4eHp5NVd1bG9nQms0cjEza0dtU2psZU5jaFdfQVZVZXJwUmZqQy0waW95czdnOTdDd1k1SE4taVBRN1hUd2lXcHg0NkNjOVVuTHFHR2c1NFNydE40VmZmd2hSdEJweG9oSUJqWnZUXy1VZ3VYZTJUeEplTnJGUTRFN1VjNzAwdzR5SUhQNHFBSTFnUEEyQU5ReUFZSTYzWGRhQ1NyeU9aX2EzZEVsTWNjLWtDWdIBywFBVV95cUxQODZzZkFNQ0R4c01fM3R6d2pUblBpcjJyVFhlZHpxNXRyOGhrdUdQaG8ybDJyNlRncXl2cDF1dk9yU1pRQllKTEdxbFo3SHVnOF9tZ2NZUEpSMmpTUHh4YWNHUEZZMmFaODNiQTJmMUFRVlN4dlMzaF83ZllLZG5BQ1VnV1NjbzVrUzl1Nzlmb2g2OXJqODRqS1JqXy1GckdJU0hsd3l4RmZjTXhINHlTVUliRmczUnY1Ym1zVzc1M0E3ZWJaYUx4ZEpiUQ?oc=5) (Fri, 27 Nov 2026 17:14:28 GMT)

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
