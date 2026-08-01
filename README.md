# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-01 02:01:27 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,549,140,665** | 🔴 -0.16% | 🔴 -0.62% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [The roadmap for a baht-backed stablecoin - Bangkok Post](https://news.google.com/rss/articles/CBMilwFBVV95cUxQajZTNnVUWHJ5TzU1NFpTNnBfUWFwRmJNQXd2eWxELW5UUjNxdnRaSVJ6VUZ2eXpsRlN5a1B1LUx5QTZ0R3V3NTYwaS02c1lETF9jcy14ZW10ZUhDMWN4QUgwd05rRmhEMGRCdzlrZWoxaGZQMlJseHpLSUQ1dXlQOWRCZVpSMEJpa0dWaXNrMFVlcVY2YlhZ?oc=5) (Fri, 31 Jul 2026 21:54:00 GMT)
- [Brale Debuts ION Interoperability Protocol to Unlock Global Stablecoin Liquidity - ffnews.com](https://news.google.com/rss/articles/CBMipwFBVV95cUxNaHVDYXNNQmhPVlN4VUdvdV9lUzctRUZXdmlIV0lSM21qNU1HVm4xNi1DVmUtVnVNZ3BUUTY0YmstR291NmJpRHQzckFUamdtMFBEY2FxQW41eHhBZkNtRlVXUHJTRUZhOE50c0NWb05WRFFSd1VNMFNJQkdULXB3cjJ5QXI2X1VhMTdjeUlvNFRoOGRZWnJZZTh2R0hUZGlBWVE1OWZ1RQ?oc=5) (Fri, 31 Jul 2026 21:45:12 GMT)
- [Bank of Italy finds no consistent cost advantage for stablecoin remittances - TradingView](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNVEZuWXdLbVpocG5XWGFNbzZUU0Y3RG9lbkFJMVdjdVFyTUZFcDYtMkd5Tmc2WURKVi1EeGpZUkhfcWFreWFmQXZ4MWFJTnFJSGdMa1BpM3FuWEpOTzVmczYwZTJ6THdMNGNheG5jS0dGcno1ZFNhQWprSllGTlh4X2pXWkNWRFRmbnNURUNKdUpjT3k0ckRPYVB1aWlBZGc3ZW8zam11dGs0anV5WENSZzl3MTdzUnZKUUFoa244ZmNFVjZ1T2FwTVVkMGV2dEUzSGRmeXRn?oc=5) (Fri, 31 Jul 2026 20:10:21 GMT)
- [Circle’s NYDFS Trust Charter Completes a Regulatory Depth Moat No Other Stablecoin Issuer Can Match - forkast.news](https://news.google.com/rss/articles/CBMivAFBVV95cUxPQVRZMWoxRWRia2Z6eWx6dElUQjVlLVlyYWc3WnBiQXBVUUFZeFFQdmVPbzVvRm13NHQ5WndZNkRHX2ZMX2VkeHRFWWxLTkNsUTc5Q3RvdHNROUx5MDRGZ2Vvd1pJTGFfVWlQSkdBMXdiNHV2cWhNc1dZNXBtZ1NNOFZXQmxHOFJTUm9STlRzbGNJVHR0Q3FISFdxX29VWldWalF3ODJMcnNYem5vamJMMUFxLUgweERUQmVuSA?oc=5) (Fri, 31 Jul 2026 19:57:53 GMT)
- [Florida Enacts Stablecoin Licensing Framework and Government Payment Pilot - JD Supra](https://news.google.com/rss/articles/CBMihAFBVV95cUxPZW9EeWtWendfdHV2NFBMNFQtTzJoUERIbDVEOEZUdGpJcF81RG1aSmNiSHExZDlKSTM2T1FxRHFXMGc5ang2T3ZvdjY1YjN2NlVrellDUy0wdTZXWGpXZVBFMi13dTFPSXVTdDBxVHpvWG1ucndxTjYyeGNDcEd1OE9Bbnc?oc=5) (Fri, 31 Jul 2026 18:49:14 GMT)

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
