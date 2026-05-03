# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-03 02:04:51 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,255,970,016** | 🟢 +0.10% | 🔴 -0.04% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Coinbase Expands Stablecoin Credit And Payments Role As Valuation Questions Linger - simplywall.st](https://news.google.com/rss/articles/CBMi4gFBVV95cUxNLXVRUnR0N1ZyTGd0ZWtDTGdMTE04dHQ0UzBnVEhmS213NTdoR2JQQlF4TUZNTUl6VnVwaHp6N3NCcER2WTFQOFRqeE9BNWhQMHNKWk9vUHh3cVNYa0o1amJzTXRqcXd5aWRpamJFZUNyY0VaYWs4azN6OC12T3lTX2FhVVVmSXl1M29SVUtWQkN0dmJ5NlBwY0pNRWRqQ29GZFhONnJkWnBPbENZaVloclpuVXFkdEV0N2dORUJEMHlhSzNVV3FXY2ZzOVFpQU85ZWxuZk1EUlFMT0h5cmRfekZ30gHnAUFVX3lxTE5kaUEtcUtHaFQ2aC1uY2VYWms4bERkTWVrMUY2SldBd3R2WFJ4Rk1CdDFxMnVIb2ZvTDZsMl9XUk5hZHVlUlZoS0pRNmdlcmRjeVZ1R2d0YXEyelJUS2hXVTRFYWhJc2RYT1E4OHlEdVBkX29JQWFBYWY2NlQ4c0lYQlVSel85RXJqX1dNLVVCRHlZb3E5ZlJqSUZzMjZZcVFXN1RvcENXVHRNZVprRTZydDdQREltZ0s3WmxCWWRScjVWV2hVRUZKb0xzUDlkYzg1dUdqVk1UelRvOEtpMlJITDQwa255cw?oc=5) (Sat, 02 May 2026 22:00:44 GMT)
- [Stablecoin Yield Deal Removes Obstacle to Crypto Bill. What It Means For Coinbase. - Barron&#x27;s](https://news.google.com/rss/articles/CBMirwFBVV95cUxQRl82QmMtd2ozMnN1b3Izdjl4bG9XQU14QS1yQ0tteTlaa0JXSzUzeVpGQ3RlY2hKeTdFX08zdlRmSm1NYXhSQnFEdVo3aFpzbGxQSzk0OERZMXJlWXZ4aEdNZ1FhclVPNVkwVUEwQ1JhTlllTzlzQS1JdDBnXzllc1NMYnVIYTlZMjR6Mm81d0pNVmdzcTk4NXFBaHZEQTJDMXV0eXh6QUctRXBlZUJj?oc=5) (Sat, 02 May 2026 20:04:00 GMT)
- [Coinbase Says Key Stablecoin Bill Deal Reached - Bitbo](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9vSWp5Z2gxbEVpdWFtSXVraDBZWjItYmpVcmNVVzVCYkpGRFBzZmtXaEhlSG1KODRYMmh0d0lXekF1YnFMdm9rbHloYUxfdzNzdWRCSUVYMVJETzhpcGhhUnVB?oc=5) (Sat, 02 May 2026 19:25:00 GMT)
- [Brazil&#x27;s central bank bans stablecoin and crypto settlement in cross-border payments - CoinDesk](https://news.google.com/rss/articles/CBMixgFBVV95cUxNVmpQWGlHNDlnQ2N1QjVvMjhqWEN2bzl1b3FRMjM0QzhPSF8yaHNFMTV2OVliNDM3OU00V0hJUUVlQzgzQ1NKal9XdXBoeHVJaFpBQW9NQXVSR0wxRnRfclE1eGl4RV8yVC0yUVBuUmVmOURFRU13bFNnekNOZ0Fyc1FsY2Y2c1Z2V0pBVDk3bml5WVM5WkM5bGhqYXlQaW45T25qeFkxZFZmX0RfNWNRa2xzNGZMbnlGUGlzYmpScWstLTNzNUE?oc=5) (Sat, 02 May 2026 16:58:19 GMT)
- [JPMorgan casts doubt on stablecoin market cap growth - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMikAFBVV95cUxNX2xxNndiUVFUa3ZTbUFUM3A4bFJkS2tYZkR5X1V2VlUtVV9EYTlWQXo5Tmg0eDMwNVN4WUIzd1FDUUFIeENub1VJVkJGVjJweTMtQlJTcGpTSUlvNXZLWk4wbldQSHNCclpJall4VEVIaGZPVUJDNWF0aEtyVDNvbEV4eWc4bGtIRkpsLU0zZFo?oc=5) (Sat, 02 May 2026 16:30:00 GMT)

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
