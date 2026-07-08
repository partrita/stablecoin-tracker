# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-08 01:54:10 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,217,234,335** | 🟢 +0.08% | 🟢 +0.41% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Open USD pushes Korea to rethink stablecoin model - The Korea Times](https://news.google.com/rss/articles/CBMirwFBVV95cUxPV0V6SzhwOWxDRWF6TWIwa21xTEZXYnZ4WkpYdlRna3Q5Q0pWSWRNVG44YUVlM2hFUFdtZkV5OUVINXBIb3NtTk56UFItUG5GTXdUVWp5Q0NLTEFGejVtbmJKMGZrWEFaQU5yQjduN0plLTdHd1hrWGd2SDBxZkQ2SmwwdHRyWG81NXVlRHI5Yk9JT0JPUkg4Xy0tS3I1VkFzRDQ2a2RvWFl2MmRic0xV0gG0AUFVX3lxTE02amxWOEJUSW9ndjk1U19Wa3U0OE5lRGt0dlUwOV9EMXJjb1B0N0M1SUFKVDNtbG5sSU5KeWlCRGpfWFFVeU03Rmw1T1A3VmxVUHpDWi03ckdKZVVDU2NCVm8ybmI3V2NxV2NMNDVGMzctbFpjYWJJZ3hYWFQtelQ4ZnVKdkYxNW96dHJBYkE3aU0yQmxMYllyRDV4OUNFaTNiUWFfVHdPNjdkX3gyY0R5a0U3TA?oc=5) (Tue, 07 Jul 2026 22:01:00 GMT)
- [Is Visa (V) Undervalued After Its AI Payments Push And Stablecoin Moves? - Yahoo Finance UK](https://news.google.com/rss/articles/CBMihgFBVV95cUxPbXBaM3R4ZFlvNDBVNVl5VWJRZ2FMZzRwbXc3LUhfd1J3UlEyTmFQZGQ5blp0X3FNUjdpR1pSUl91bnM0MjczbDUxdnBqSERUWVhqMkpjc2pVR3d4X0RwU3pyVkhhZnNpUDU2N1Jxa1VsV28tMGhkbEpmOGNvcWZjRm1JcWNSUQ?oc=5) (Tue, 07 Jul 2026 21:18:13 GMT)
- [Stablecoins Turn Into Aid Rails After Venezuela Earthquake - Bloomberg.com](https://news.google.com/rss/articles/CBMisgFBVV95cUxNYzhscVF2N3Y5OEF6Y3VHcG5MXzNqbHI3QzcyWE16cnE4c1kwY0VNWXhIMXk3UDRlYmxMYTU5Qkx2U1puV2lsaXl0WmF1YVFrbVlFNUpXVVdBV002bGNlS05ZM2VsQ1JNaldMMHJxcnFWbDd4YVVtcWl4MlBSbmQ2Y3lYZWlZVkVBMFhJN1BKWjlINWl6NVBOeGFGVEU1MlZOZy1fUkdYM2prQ2E5WV9KS0Fn?oc=5) (Tue, 07 Jul 2026 21:00:01 GMT)
- [Is Coinbase’s Open USD Move a Threat to Circle’s Dominance? - Disruption Banking](https://news.google.com/rss/articles/CBMipAFBVV95cUxQTklDUVBVQ1Yxdk15Q01QUnNzLVV3dUFvQUsyVkhDei0ycDJ4N29HdVF1dWJrZ1d6dFREOVZYQVFoRFhtdUQ3OENkckxUczNwaS16bUZuZW5EMTZ6UkJQcndCdGtyY1dyM2FTVUFTbnZ4LVB0cVpaMGdYREVFSDZqaG1sdFpvMG5SblVoLUlsRnRfUjVoV3BvZTl2TVJtTDRWWVJjSg?oc=5) (Tue, 07 Jul 2026 19:36:32 GMT)
- [Circle&#x27;s USDC now runs 70% of the stablecoin volume - Yahoo Finance](https://news.google.com/rss/articles/CBMie0FVX3lxTE5jcmZjcDFpZ2QzbHJBcWVZcWpheFZlVF83TnZKdEM0YWcxRXdidHd3Z0ctTUoxZ2pmZ0hXcDEtTFAzQ0FtQ0hMaFZwTkJEUTZGVFJxdVBEanZwZmZxZU5qeDl6ajZWTE5nVEZNX20tbkk3MDBpVHJfai1WQQ?oc=5) (Tue, 07 Jul 2026 18:30:00 GMT)

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
