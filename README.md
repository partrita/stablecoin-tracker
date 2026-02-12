# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-12 01:22:54 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,590,845,614** | 🔴 -0.11% | 🟢 +0.56% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Same Stablecoin, Different Bill: Why Africa's Cash-Out Costs Climb to Nearly 20% - Finance Magnates](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNOUpRdzE2NEFaUWlEZWFLV2xnczR4QklxVG10Q2VFLXBlQnlGVkxhTUpzeXlkVDVOMUJ6c3NFcWtZZWI2MkpJT3N2dXRoZEJBV1hSbm9Jc25HTnJzamlYTWF0dDQ5ZS1GQjFPQkVfaUNjMk5oREV0Qm9ZLVR0dWthR1NWbW11SXdRT19HS21mX1RnLV9pYmNTTm1SSGx0X1BKTzhQVlVXSzZiY3ZITmoxVEtHS0lXVlM3WHRkX2lSS1NMdw?oc=5) (Wed, 11 Feb 2026 21:26:42 GMT)
- [Zerohash adds Monad support to expand USDC stablecoin payments - The Block](https://news.google.com/rss/articles/CBMigAFBVV95cUxQNWMtUFBlM09NemNveU40a0tyZ2VFSkJqNjhuS0xhMklaQkhueHEwUUdwOGc4SEhrVndEUkxRaE9oQ1hEdUFUZmNneWR2ajExZWxmdUJqQnp6T3Q5TVhNbFREWGRLR0NDUlBIRVh5eWxOV29wYUpQTk54YnBtaW1FaA?oc=5) (Wed, 11 Feb 2026 21:21:35 GMT)
- [NCUA Proposes Framework for Credit Union-Backed Stablecoin Issuers - Credit Union Times](https://news.google.com/rss/articles/CBMipAFBVV95cUxNSHZuRDRsWWVZa3hTQk1TZXo4a2U1cS1GOWhSbTNYcXpUMWVMSDlYYmZlNWJSNWVqd2RWOFZpclhSdmNxS0ZMeVdJVnRUNE94cjk1c2NselNMaC1jODVaMzRsYlJXVERXN2F0ck12NUNHZ0lQSWhCUXhKcVRRVzRzVFFfcENmU2c1S3dINGtaYUE4alh1X2d6d19QcXBEU0pnVUhHc9IBqgFBVV95cUxPQi1Tejd6MWZJYnQ4eVZfRFpiS1NLLUE1eFE4X3JSdFJBWF9CM09OM2xYVTdOeEduOFo0WFAzeUQxNHl2bXRxa3VyMmFnelRhSHVPZThSOVFtYk5RUXNacTR0MW16MENIdE1TNlppeW5ibUFoMWh3Q0czYmRLMWNYZEE1aDhvdWxRQlU3OTIzUFc0dFlhVzdNVzIyT191MlRZaVFmbWNBQnVEdw?oc=5) (Wed, 11 Feb 2026 20:16:09 GMT)
- [Key facts: Citigroup forecasts growth; shares dip after Fed changes; banks propose stablecoin ban - TradingView](https://news.google.com/rss/articles/CBMi7AFBVV95cUxOdUJPVmNtZHVjTjNEYWZXQkJHY04yTDFTVGE3MWhOTGFmU3NYOENuNGhOcTVzZy00SmVISVJBbWp5MnJaSE1na0ZmSGw4RlJXbXlxek1yWlgxbUJjSjZlWVcybE1oN05qaUdwVzIxOVZEejMtSTVFVVVBa2I4OHdXOTJDYkhnWFFGQXhRdWJsS21OajM0eW96Vjc4UU10bEJ5ZnI0dmtVWE9tLWZlMVc4NjJxdS1WOVJCdlV6eTdZMWxvV2ZXd2tKWm1pbC0yZXhBOWJLdG13VUtkdzNoSXRtLUhOSXNiSkM5YnExTA?oc=5) (Wed, 11 Feb 2026 20:03:58 GMT)
- [Tether could become 'top 10 T-bill buyer' this year, USAT CEO Bo Hines says - The Block](https://news.google.com/rss/articles/CBMihAFBVV95cUxPQ1BLQUJUQVU4X1R3aVdma1NZSlBGYmtuaDh6cUxtU25LWkdoQTI5eGs0OG9xc1Nmd1BCTFdpSDZod3JXUUhnQ1oyTDlocFV3QjhCbm5KSWZLUXJEU3pldVNTQnVVZjhfR2lwbFpmNHo2UUE1ci0wNTBMQXhiMkdhZHo4Rnk?oc=5) (Wed, 11 Feb 2026 19:21:05 GMT)

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
