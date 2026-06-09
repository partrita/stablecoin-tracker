# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-09 02:25:58 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$295,312,640,923** | 🟢 +0.05% | 🔴 -0.75% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Why Banks Should Pay Attention to a Visa–Mastercard–Stripe–Coinbase Stablecoin Alliance - Finovate](https://news.google.com/rss/articles/CBMirgFBVV95cUxPR3ZRckM1S2hVOS1BMndGZ055Z25nb2h3YldBSnRodGhSbFI3YWJiaXNUanZGX3FhVVBNQW5HNG93MTRIdFpub2dBenNwYzRQbFdtaFZUdFhtMDh4RFdRSk1PMl9Rb3JJejV1Sk12VWhGWnFYOEhWbVQxcDZuWldzVzR3UWNlY0piTkx1RHZqMjZpdVYxWXJVeDAySkhydlRkSVFzemtvY29pd3VsY0E?oc=5) (Mon, 08 Jun 2026 21:57:14 GMT)
- [NYDFS and European Banking Authority agree to share stablecoin supervisory information - JD Supra](https://news.google.com/rss/articles/CBMihgFBVV95cUxNWlVvV29sX1hkQjhDSEE3UGRuZzNNdXpMMy1xSkJPZTk1MTRFVS1pd3BNOElrY1VuWVlsU3lPV29Gd2VaN3U1TEVUVWFJSldWVVkyUmlRb0FsMlROOXJ6eE1GVFp5bHFEWC1OTVN1UVNIaUQ1MlJvNGUtdF9Hak9ZYnpuemhIdw?oc=5) (Mon, 08 Jun 2026 20:31:32 GMT)
- [FDIC proposes BSA/AML and sanctions compliance standards for stablecoin issuers under the GENIUS Act - JD Supra](https://news.google.com/rss/articles/CBMihAFBVV95cUxOSFRvREhfNGpCcG1vQkFjdldDd2s3V3JWYWhoSWdxYlN5cEp4S0FmUGhmaTF3SFBwUVQydnBTa05xMkFEQVZSeloxSWpmaVdmZ0FuSDJrT2hqT3VtdDJVMExZQ185cjN1YXhyYk5RQVRxbFRQc2VKZ3lVWjVnWTlmb2VqSlQ?oc=5) (Mon, 08 Jun 2026 20:06:32 GMT)
- [Stablecoin Rulemaking Comments Expose Payments Industry Fault Lines - PYMNTS.com](https://news.google.com/rss/articles/CBMisAFBVV95cUxOZC1oenRrNmxmZHBqSndIYU55VHBJN3p2cU9RTVJheTlWdUQ3NHpVMjBmaGpfbG9MNlFwUzBlX09RWWxoWmdSRDlrOFJQOHZyWUk1a2RJZDlockRwYjctYWxzM3VLLTJIQ2xrZzFIY3VmVUxSLTZyUDBHM0JDTkd1eWc4bS1KcldIc0RZRUR2OFNYN0Z3RWlLN1NqUXFlY1hITzFudUJ5UExYNWpGOFgwRw?oc=5) (Mon, 08 Jun 2026 19:57:21 GMT)
- [Zebec Network scales real-time stablecoin payroll and payouts with USDC and EURC - Circle Internet Financial](https://news.google.com/rss/articles/CBMiXkFVX3lxTFB4T3ktOVhGaTVUbjluZ09jUTA4Z1lpRXRyeXN4Q1JCMHo2emxxTVoyaXRwQW1yNEtqeldxUjEtMzZNMGxucG5zN3N0VUNiRktkakdLcXp2MC1lVVpVZlE?oc=5) (Mon, 08 Jun 2026 19:38:59 GMT)

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
