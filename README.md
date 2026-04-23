# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-23 01:54:36 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,169,085,062** | 🔴 -49.93% | 🟢 +0.30% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [CME Seeks License to Become Stablecoin Issuer - Markets Media](https://news.google.com/rss/articles/CBMigAFBVV95cUxPVENjTlQyMXNfSmVYYWhINHFRNlpFV3NrbXBHem5MMmtXUlNpMUNmN1lndUpvaUtiR0J0a0hmZzR2S25zd0J6Vkxvd000YUZWcTJheUxyb21DOWpBTlNXMWE5ZGFiby1XVElhcVhLQ2xUNXI2SjFRdnRjX0F3QXR3Qg?oc=5) (Wed, 22 Apr 2026 21:39:22 GMT)
- [Tether, Rain, MoneyGram expand stablecoin game - American Banker](https://news.google.com/rss/articles/CBMilAFBVV95cUxNRVNFYnpYZ0xiMFNjM0ZFc0FHRC1KQTV5d2ViS1FIRG84WlJoWXhHRDRPYng1Zm9sWkk5eElDbDdfWXAzcnI4MlpVN2VUM0I4Y21TTmVjbTF1UmxKbGVycU8zTl9zQmRHZnNuVHVJMGhIdElYRlJZSjFaMnFqOTBQQ3dMdmQ1T0hiT3MzZjhaTDYzdGpU?oc=5) (Wed, 22 Apr 2026 19:06:00 GMT)
- [DoorDash to Offer Gig Workers Stablecoin Payouts - PaymentsJournal](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOSkRIeXo1YXUySDh1dVg0V1lVT1lsbWxxSTZKcDRFelhZNGF3MDlwR19ia3V3dW40ZF9manQ5NU52TTdOZkJsQmM0bE1aYWQtaUNZbV9kNWtSZkJoRTdlSG5HbjFiSDYyZnoydGdaQVJ5NTBmRUtNOERucmxnWVNSdUtqd1Q1Zzd10gGOAUFVX3lxTE9qWllxMzNhdFRHS3lvd0kzTVVPQUdFNFdJT3B6MHFBRFpzV3Y3QThfMk0tblU4R2N3bzhDTGs3VHZKMHI5T2szNEhRcDZ4VnNBeUIwbjNVSHRlcWVZb250TW1XcHl0aGJhVHF6ZXMtVlh3cjlZS1lST0dkN1BfSGF0Q2xmVjl4SUxqUWk3b1E?oc=5) (Wed, 22 Apr 2026 19:00:00 GMT)
- [Covering Crypto: Are stablecoins changing crypto? - Fidelity](https://news.google.com/rss/articles/CBMiowFBVV95cUxQU3NHZUppVmVzdm5IVmhNS2ZYbkJfS0JNQmFfalJiSzJRWUZKN215YlVDV0NvdmFoU2w3a1BURFBOQmswN2NJMWgyamFtdkpyX1htNHpqeE05UmVQX01IaDhiTGhLNmpveTZLczh2WTZra2tMQlpETXZyN0RnYVpNV0lfMUwyX0VJdTk4SUFGNW9FWHdJUHUxNk5uNG00d3hvVGh3?oc=5) (Wed, 22 Apr 2026 18:38:36 GMT)
- [Coinbase Lists First GBP Stablecoin as UK Push Accelerates - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxONUtlZEhKU3NQZW5aSkdTbXJvWTN5cVhGRzlIcWx6U28tNjhDOUlpNzMxVURyeGkyeWxwMnpyb3poR3p5am9yV1NVYzlOdjVwWFdYTFhTaU5scmh4ZlBSSnhpc1RBRW9ud3pUSUxTakRoN3ZIVUs3OGVFalFUS0N1X3VVWWZxWUtpMVhWeEhxZUFsRWh4c3Ffck5VWGxnRWhBb1E?oc=5) (Wed, 22 Apr 2026 18:15:15 GMT)

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
