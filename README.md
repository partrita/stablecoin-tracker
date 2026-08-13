# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-13 01:13:38 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,826,187,009** | 🔴 -0.02% | 🔴 -0.01% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Standard Chartered’s Anchorpoint launches beta version of HKDAP stablecoin - ledgerinsights.com](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPVVpSd0FRR040VGhpcjRNWllHaWV1VUJqQmw0ME1SNlhtYzE4dE1HZ2NrMzBhdVVhR1RJUE5zWmliUVBVeWdiUmxfSlJLZXgwU3VEVk5jX1ZxbWJRZGcwNkE0Z1QwX2dZRG10WlpVcGdtaWZtdE4wQ1NiV3lYUDNmYU1xX2l3VlBNem1pYWFjMzY1bUJFZ1MzSWRxaFpLRDhtYVgxamxkcTg?oc=5) (Wed, 12 Aug 2026 23:20:26 GMT)
- [Anchorpoint names HashKey as distributor for Hong Kong dollar stablecoin HKDAP - Crypto News](https://news.google.com/rss/articles/CBMie0FVX3lxTE53a3NMOEFuTGVTUDNjOWVaY2dIaGptbzdTaUZjcHNQWktUU24yMFJESHBwemJIQnRPZWVpNEVRdTJqRG1fN3R4SnlYYWVtdVhROVBoajN0b0ExLU5hQ1JpejNoVURGVHUxRUVhdlZLNkpKSjhrSFAtR3N6UQ?oc=5) (Wed, 12 Aug 2026 21:46:51 GMT)
- [Banks Challenge OCC’s Weekly Stablecoin Reporting Burden - PYMNTS.com](https://news.google.com/rss/articles/CBMinwFBVV95cUxPX0xZbklkLVc2Uy1YM3ZEWUtOUjFLR0RGMVg5SmpPbHIwUzNRM1M5YlZQX3d5OWFDTm9Zc185OFJOVXg3UTV6RVRyTnJTN1VlYkswa3NEc1BPcGgtZ0hoMDhua1Q4Y0V3QjNNXzNWTEx0Vy1DamdLUmgwdlB3eWp4SkVnNU4zZ1MyUml6bVJUOGVYZkxQaHJxT0llSEN3VTQ?oc=5) (Wed, 12 Aug 2026 20:56:57 GMT)
- [Bank of England Lab Targets $2.5 Trillion Trade Gap With Stablecoin-CBDC Test - Tech Times](https://news.google.com/rss/articles/CBMivwFBVV95cUxPSEFZa2xPd2owaGp1OHpQSGw4NFNZM0RTNWUya2U3dWpJSk5rUEVTc1FLSTduQ1lmN3dXSFFEWWJ2NlM4VFdNTmNVOTNFYjNObzctOVVvanFIQW9YUFB5X0s3YThvREUxY1E2bGV2eDNFQWxhX1ZaakI4Y2NBYXJUZng1SmRTSEktZ3dBUzFHVXBSaFF5Rl9DRExHUEROSUw0X0M4SUd0VnRhM0VhSUduOUdHTWlqRTVRX2M4Y0JUOA?oc=5) (Wed, 12 Aug 2026 20:46:05 GMT)
- [Anchorpoint Rolls Out HKDAP Hong Kong Dollar Stablecoin With Institutional Beta Access: 10 outlets compared - NewsCord](https://news.google.com/rss/articles/CBMi6AFBVV95cUxPN0RXbU90R2x4Z28yRjNyVGdzamVjLWpvVmJSQWpCZjBQWGJtNElBazlaQ2dYSWpCTE5URU9BU1lacTludnBVZmVOTnZLVXN3NFMweTNGbEctbm9zUWtMOHZaaTN1ZlF0blY1NXUwV3RoYkFHYk83eFRpMjQwcFBrMWpQeFQtSVZPZTkxRHVaSWt2ZFRINGpkLVJpT3hIcElkWDUzS0RGZ1Z4Z2laTTk4YVVvS2hfMU1ZVWl4d1g4QkJCNHpmYS1UOVQ5SXREZU1idFZsa25Jb1k2V0loMl9nRlQ3TlBVaGFo?oc=5) (Wed, 12 Aug 2026 19:46:53 GMT)

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
