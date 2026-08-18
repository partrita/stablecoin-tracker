# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-18 00:43:50 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,697,331,643** | 🟢 +0.00% | 🔴 -0.11% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoin Remittances Face Reality Check in Banca d’Italia Study - Global Finance Magazine](https://news.google.com/rss/articles/CBMikgFBVV95cUxOYWN6QldjTEJIYngxRmVuMHBpNXRHV2kyVFZ3aFd4TlNkT3lWencwQWJ6eUwzM0FmMlRxMGdxR1dhdWxPaFc1N0x6X19zd1hWbHZZbUFvTzFudnhLcUNzejVPdnZ0OXJDQUx4MmFVVG5TX0M1YXhFb25nejhlREJpclE4RVNrQlhoa2ZacjYyZGROQQ?oc=5) (Tue, 18 Aug 2026 06:00:00 GMT)
- [Treasury Plan Would Map Boundaries Of US Stablecoin Market - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1fQmdQWmJIdzBZSU5mbVV1ZFFwNTZBV3hDSW5fdHJnakRfQ2lCeWt6bWdCUlp5ajdiX2VBQ05TdWZrZ2NNQ09lcUlwR3RzVXRqT0tDa0NB0gFWQVVfeXFMTV9CZ1BaYkh3MFlJTmZtVXVkUXA1NkFXeENJbl90cmdqRF9DaUJ5a3ptZ0JSWnlqN2JfZUFDTlN1ZmtnY01DT2VxSXBHdHNVdGpPS0NrQ0E?oc=5) (Tue, 18 Aug 2026 03:18:00 GMT)
- [Stablecoins expose gaps in Asia’s financial defences - East Asia Forum](https://news.google.com/rss/articles/CBMikwFBVV95cUxQOUpvUml4Zm85bkRRX2FHVENhTVlNeE1GbzZ5SkFFdGZXUTZNNTNlclZQR0MyZDZ0dVAyZGZZLUFubVpWczd6endhNTVGZEp4N3NwWU9mU2k5RjNUSVRNcHhTRGFTVHVlM1lNRkUyc3JmOXZGTng2ZHVpdmZEcG9HTHhsU3d3Y0tES3BYeThqQllkQzQ?oc=5) (Tue, 18 Aug 2026 00:00:00 GMT)
- [U.S. Treasury Proposes GENIUS Act Rules Limiting Stablecoin Issuance And Sales: how 11 outlets framed it - NewsCord](https://news.google.com/rss/articles/CBMi5AFBVV95cUxPMEpMb0IySjBLQ3pEWE9HWEstaUZJTkRHMDlFYmhjVVZEbFFaZ25GVmJlYkpVXzdaM2IxLW10bVBJck5HdThRcURiRC1FeFk2M25zYkZ2VUtGTUZ2RzNSM1IyUzRwTmEyaHg1YlFuUGVwX2d6NEp0dVNPS2ZfU1dLVWJ3VS16SF9uVEptdUVVcFNaZW1rNHZPV2J1d01DN2xCbWNGWUNLWmlWS2J2ZXN6YWtPQ1c2Zk1LamYxNmpuTDlQclN1QjV3SXQ4UWp4YkRMTDZkVlI0QmNwYlVGWU5jcXlLNF8?oc=5) (Mon, 17 Aug 2026 23:49:22 GMT)
- [FINANCIAL TECHNOLOGY—Treasury seeks comment on GENIUS Act rules for stablecoins (Aug 17, 2026) - VitalLaw.com](https://news.google.com/rss/articles/CBMi4AFBVV95cUxPemczNU9IOThta0RrS1I3R2F5ZUtxbVpJWmtZMktIdFJpaEduNzU2N0Q4dkU4ZUxoVjZzeGppT25fRTl5bHRuM210YnBQeXNSZ3RpcDlyTHpqU1pzc09OT2hpQ2dGa0lkWmJxSmZ0TG9YRWhrWUNKSXpXYTFHbWJabC03ekItclVsbFFXNmpndm5nSWl5OEg2SGNwaTBGQXpGY3Zzb1ZyTUtxU2hZVVFWX1NxYTlYNkRrMENyZFVBeTFfWm9iLUJ0V29jQ0tjSXAtaGhJSG80VFBwVFBfOE5PQw?oc=5) (Mon, 17 Aug 2026 22:42:02 GMT)

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
