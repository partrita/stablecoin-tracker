# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-19 03:32:16 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,546,874,507** | 🟢 +0.09% | 🟢 +0.00% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Bank Regulators Float Joint Stablecoin Customer ID Rule - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5Wb1dPcGpmLXV5R01YQV9xNmhEdW1NZjEycnMycjhHZy1HTmxzc2YyQ1ZPaXpPMEs4RVBST2IxazBpbllLR1NnZDlLVTlqMFV4bW9BYi1B0gFWQVVfeXFMTlZvV09wamYtdXlHTVhBX3E2aER1bU1mMTJyczJyOEdnLUdObHNzZjJDVk9pek8wSzhFUFJPYjFrMGluWUtHU2dkOUtVOWowVXhtb0FiLUE?oc=5) (Fri, 19 Jun 2026 00:24:00 GMT)
- [FINANCIAL TECHNOLOGY—FinCEN, other... - VitalLaw.com](https://news.google.com/rss/articles/CBMihwJBVV95cUxPbEQzYVBGR0hZazZlRHFXNk5LYXZqaWUyUnhLTXZ2LUxSa0hocmVhQ1MwcE1tTUx4bm1MQlV1Nm0wd0hVMi1aSGJTZjgzX2FES3RfQ0NfU19LVmVRTG9HQ25xZlVnbkJiVWxRRlVuNmt2Ti1CcnFNMk1RaFMyYmNFanlvbXpPaGJIcGNYbFRvaVhUVDNJbkVyOWFpaEMwdzM4THZSR2RXLURrTzlzaXFIMFkzS2lWMTc0WTdMYlBJTm52RnY4SnNqMjhrRHRwWFlLVU9KZlpWZXBXbmhDYU1NSlFnbktaWFJQVDBjSklZVWFYb3l5LV9RRWZuaGVseHVadjg4T1hGcw?oc=5) (Fri, 19 Jun 2026 00:19:09 GMT)
- [New stablecoin-powered fintech Sovra raises USD 2 mn in pre-seed funding - EnterpriseAM](https://news.google.com/rss/articles/CBMiswFBVV95cUxQdmFXQWNBbzhudTB5QnlWb3VsQjhDVXlha3JnbV9zek53NVB3bHdqejZWTkU2b0dCZFd2QUlFUzEwaThTaXdkR0k2UE84OTk5ZUhHLXg4aG5HZzZfdzVSVkhycy1NOTVnbmtWNGl5MlBrZWFIbFJ2a2ZoRmY0aWdHa2lzdjhtV1BVaE9YbGtxZ0JZYW9KSmljS05VNGprWDZsREZCU2RneHBOMTU3TWF6TUdnVQ?oc=5) (Fri, 19 Jun 2026 00:00:00 GMT)
- [Trace Finance Raises $32M To Expand Stablecoin Settlement Rails - TradingView](https://news.google.com/rss/articles/CBMivAFBVV95cUxPMlZNeWdRaHNPMXJEclNWWi1wcGtadWNsMkQ0eEtFVlY4aVZ2SG1HYm1fYjZ1bXRoS0lYOEpfYzJZSWo5T2lucGJZc3cwckh3OVBRNC0wTGJOTjhKN1hVMWJCalg3SnUwclRjSjZ5OTM0bnFOdHRUZ21NZHdidFVLamxXenE2QU5Oa21wMkxhaVR3bjlLbENEMkppbjNCSnBxaWlOSjJ2emRFVmt3bklCeHFwbWNHVjUwalJsTQ?oc=5) (Thu, 18 Jun 2026 21:30:36 GMT)
- [Fed seeks tighter stablecoin issuer oversight, proposes bank-style ID requirements - FXStreet](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOaTVpWTB4UjRwX2xfaGxUUkxLbno2Q0p2U0NBNmR2V25qelNyXzl5RmNTM3JmMjBwdjdZZEY4bXk3MmN6Zy03Vms2eTJZWWZndk9TYjdFQmdDOEtiNGdQaUJFTXkzQlRIMzg1Y1dGcDZKd050dnNwbnM5SWxTc3htV2RsZGFMaWZpdlpTUnhrVjVlaHhlQlRTWFJmbnVPQ2poa2kwbmV0R210ZUZ5ZFVMXzc4d3RSQUhsR3lBWmpPZEZuME1COWFIbHFsdE5ZZVlYeVpmTENWOU4?oc=5) (Thu, 18 Jun 2026 21:22:04 GMT)

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
