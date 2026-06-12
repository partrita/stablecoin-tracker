# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-12 02:44:48 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,533,622,025** | 🔴 -0.14% | 🔴 -0.84% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Bank, Crypto Groups Seek Limits In Stablecoin AML Regs - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTFA2LUVTTXRoWE5CUmxMemJkQlFwdHlyVmNyQ2NGWW9YbmhFV2xCQS1sUjllVnJHX3VHcUZmTi10NGUtRUxELWF0aHhyQ2hSVXVaRGRIUlh30gFWQVVfeXFMUDYtRVNNdGhYTkJSbEx6YmRCUXB0eXJWY3JDY0ZZb1huaEVXbEJBLWxSOWVWckdfdUdxRmZOLXQ0ZS1FTEQtYXRoeHJDaFJVdVpEZEhSWHc?oc=5) (Fri, 12 Jun 2026 01:52:00 GMT)
- [FDIC Stablecoin Rulemaking Highlights Fight Over Fees, Deposits and Custody - PYMNTS.com](https://news.google.com/rss/articles/CBMiugFBVV95cUxPRHpsVXhoM3lobl9lSGxwNzI2el9ZTlA4RjlfeGlnWHZWQmhWZkhTOVlVR0pObTBXV01qLVpWU0NXYmE1RTJtOXNZVjVCTEpkX2lpeGVidXVTLVhzZURzTHhfclcxSnQ0X2pwTjFFalk5T3F3S3M1dVhmeW01dVNRckVLTVpmWlVWUHc3UldablE5cVMwaFdFb1BKdGdybllpOFhUZU9EcnRqSXBaZTFPbkdLRERFWWlsalE?oc=5) (Thu, 11 Jun 2026 23:17:12 GMT)
- [Fiserv stablecoin set for July launch - The Business Journals](https://news.google.com/rss/articles/CBMimgFBVV95cUxOUzZZai1qbmtOejJGbUVmd0lOU0pqLU1Idk5HT3puUTB2djIxa2dmTG1ycHZNNU1NNEhDNHpzLWVjN0Nmb3FxSFctUzZpRXh4WkMxdUFYdnRnb0RVZVNLTEhJT3U0aElhZFVxeDU0SGVMeUJwZ2JMZHBtcXExc2F0ajZmNmZvSDdRenU2M0J1SUxZa29zNW5URmNn?oc=5) (Thu, 11 Jun 2026 20:02:00 GMT)
- [Big banks are ditching private blockchains to build tokenized cash networks on public infrastructure - CoinDesk](https://news.google.com/rss/articles/CBMi3gFBVV95cUxNTnBjbV9JYWRTZkhsLXZ1Ym1VdDRBU09RV255RkR3bnR5aG5XTlB5emhUaW9QVU1HNWNCaVJZVUNBZ0IyM2V0eEEwU2hWTDRPaVNkV2ZmSTR6UTZtR3RaRk0yTEpSM1p2SDlFLXJBOFloM2tJTTFNSVpLQUFXUWNxaU9yS1R2OGk2TFhzWTROX2I4TE5kenlVeC1OTmwtZ1BXSUlxaXo0RkhqQUpxdnZFVGsxQU1iazAxcG9hSDdDcWM4akN6ckNCUWZwV19QTGM5d2RubVFTSi00RVA4aHc?oc=5) (Thu, 11 Jun 2026 16:54:54 GMT)
- [Zelle Plans Expansion Into India, with a Stablecoin in Tow - PaymentsJournal](https://news.google.com/rss/articles/CBMilAFBVV95cUxQeURFUG1adE51MVZXZnNKbnhPN0J4M0RSQkxNODlOTlFyNGJWS3BhOHduZzR5VVJPWXdWdmhJQ0JhUEp0alhMY2ZmRGVWZFJXZGI4NlVJVzhoeHVGc1ZBR3ZwYUJhT0dPeWJHalRxVGZrYTBBT3hPNU85WlAyMjdFWklIbmxvdXBaVzJMZWxtSUItVHE10gGaAUFVX3lxTFBqdmhVZlZ4R0wxbHNDRV9zZEV5WEkzYUc5LU5YRDh2NWNPLXpDaWJ3Nm5RRFpXRURSVWJJTXl5YlpHcXJrbE02NXlIWTM3amJZTk53ckFkTzhVQ2s3SHItM1lqOFFOMmJZSnFJaU5ScmpPMkcyYWJVSVU5T053VnpUM3QtbGRQVlpTOTl6UXB4Rk5JVVpSWmg3eXc?oc=5) (Thu, 11 Jun 2026 16:47:22 GMT)

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
