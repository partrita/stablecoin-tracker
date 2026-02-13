# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-13 01:25:59 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,209,767,543** | 🔴 -0.13% | 🟢 +0.54% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [INTERVIEW: Mitsubishi UFJ Trust to Issue Stablecoin in FY 2026 - nippon.com](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5VcExsNjhsOUdLQmw2RU5QNF9kS1pUQVdDaUdYSTF0M3BITDNYVG1EU1RPeHVtRkcwWTFMZV9YQlltZTMyT1RNbFhaZ0pTX3JkQkk2d2tZVEMxNGdT?oc=5) (Fri, 13 Feb 2026 00:00:00 GMT)
- [CFOs Eye Stablecoins as Capital Tool, Not a Crypto Bet - PYMNTS.com](https://news.google.com/rss/articles/CBMingFBVV95cUxOOGo1S3B5SGFaTXBfdU94WEJTSEVWaktTU3JUT3A1Z2JzbVR2OG00QVlXNk4yYjRxVU5jQU9ZbEpWc290YTlQVThXcmVsZkwtX21oYXR3SVl2UjBLTjhZMUZrUGVQRnlqMF9zcjRjQ1FNVUhneHMtT19ybmNVcmRLY3ZnMUg2Rk5BYVBsYmdpbWFfR0NtMzJnQ3hWNzY4dw?oc=5) (Thu, 12 Feb 2026 23:21:15 GMT)
- [Agant registers with U.K. FCA ahead of British pound stablecoin debut - CoinDesk](https://news.google.com/rss/articles/CBMisAFBVV95cUxOVElXR0RpM3VZMS1PeVdBN1hKTE1YeGg2ZnJyVFdvQ2NwSzlpQlp4b1dVSkxBVkNRUEowUmhiTExpYmhGb0l6T09Tc0lBLUNGdVVNMUZqODA3QUxvc1J1WUl4aW9kelEwYURRMDVlWlA3VHkyZ0ZIbFRxMEZaNTI5NEdJXzZGVFRXSmcwRldfME5Ea0VMZEZXNF9QYzlQY2Y0SUF2eHdsbHpqMmlna2JzeA?oc=5) (Thu, 12 Feb 2026 20:56:24 GMT)
- [FDIC extends comment period on proposed requirements for banks seeking to issue stablecoins under GENIUS Act - JD Supra](https://news.google.com/rss/articles/CBMiigFBVV95cUxNckFVVU84Yl9YR0NCcE9LYUhwQ04xVWwxamlUSDV4WTRiMHE0bFhIRy0zWVJXaGNVQnk2V1NXbFBnMWFabERzUXBtWlZwOXNINmo0QjF4MTVpd3JUTDJmenJvaVp2TWRvVEwxTERnZDFVRjZtdVVsdWZQMWFVbndKZ2gzeWpiNkQzTUE?oc=5) (Thu, 12 Feb 2026 20:45:11 GMT)
- [US GENIUS Act: NCUA publishes draft rules for stablecoin issuers - FXStreet](https://news.google.com/rss/articles/CBMi8AFBVV95cUxQRnBFMkR4bmdqQ1pTd2JKLWFHaFAtN3pQZTRVbDlES0FlWFBYMVBtUnNWS0FhaFktZi00dm5rdG9ZbXc3NXFSbXd5RUU1ZkFWOHhVZ1pHNE4wTkQ2ZnFWaklmZHBoYkd4UU5sRHBNRUZuMkVYLUhBTlVTSVlRVWEwSmNoQUlTbVB4eWJQVnFkWDBXNDZYV3QzRmtBaUdsU01CTmNkc1VKZlNVZjhsdjM1NVk1T2xDaVc5U0JlN2xNTzlpSDNzbzJSQkJMOGdHV3dzOFBNa1hzWmk2M0JwSU5VVjVsUEdYMkNXem00bjVYMGXSAfYBQVVfeXFMTVg0bFhDSzEtN3g4Vm5SY0pieUpJWUZDSU5VNXl1SUNrMmpPX3djN3p1WEZRWW5BWXZCLTdpNHhnUkRoLXVwNlBzZTBkNTdSYWREd0Fwejg1V0JUSnpVMk40YmpUYlZ2NkdUODRjYThyMlNDT2FXRTlDMTZaMkJRQXlORHllY29VaTlqMkVUNGt2R1FlQS1Ka05UX1RNWUQtN0JtWUVuaXRpTEtMLVNwU05kSFl3NzJGdWEwUnBRNEZkdVgtYmoyMXhUQ2kzV19CbE55QkxKS3VHR3A1bEdLa3AwOHNfXzdkMWpMcW9GS0s3SGRfR3dn?oc=5) (Thu, 12 Feb 2026 16:22:39 GMT)

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
