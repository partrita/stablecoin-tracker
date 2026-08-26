# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-26 00:47:01 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,159,255,278** | 🟢 +0.01% | 🟢 +0.84% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Visa joins MAS-led project to pilot stablecoin settlement - Finextra Research](https://news.google.com/rss/articles/CBMiogFBVV95cUxOdGNCaWJaMEROWldKMFQwVFl1UDh4RzVuekVzeDVNOTQ0MHJXWWtXanl5VnBtU3pJREY3Vm1RajhGbFRJaW05VDJJX1V3aDFyMnd5ME1STlBRVFFHaUlnb09xU0RZb0tpVlh5dDhVODR2QUU4aVVSRHZnVm5Sa1BDamdwaWxERDRQcEozZElBdzZoLXFjemd4d0lMY2FJdmJ5VXc?oc=5) (Tue, 25 Aug 2026 23:24:52 GMT)
- [World Liberty’s USD1 becomes Canton’s largest native stablecoin - ledgerinsights.com](https://news.google.com/rss/articles/CBMimAFBVV95cUxNSUE2ZVBpWHJmZDM3anVaWGIzN2JFMXowN3Z5NTFjZ0UwczNmelF0cFpZS2I2OVlreWU2T0E0VE1KRXRPUnpUS2pzbk5TLTVKdFFsZWkyUU5QTlh6OEpjRVpaZlJ1N0FTVFdyQklpTlk3TjJ6OUxZSWFSclFObDdhbkd1THJxOVI4VXRZbWxzV3YwX3JBZ2FQZQ?oc=5) (Tue, 25 Aug 2026 22:10:55 GMT)
- [DCUC Pushes Stablecoin Rules, Servicemember Education Protections - CUTimes](https://news.google.com/rss/articles/CBMiogFBVV95cUxNNWdlN2ZURG4zc2lJbXJsMHN4MmZnR2FfRzQxTjUxZnZTVURZVG9FMy1acDg2TUotaV94RWtCajY4bDBxTVpxb2Y1SFZoaU5abUNGa0p5djBRb3FnYXpIYlJ2NFVNSEhMZ2RodTJXM2RyMzJqSEhkU1BGYlRiV3NhY2VFVHc5UTA0NzZ0bUNvc0s1c3JGdTZQQjhNS0xad3h4R3c?oc=5) (Tue, 25 Aug 2026 20:52:17 GMT)
- [Stablecoin Exec Rebuts Conflict-of-Interest Claims - Briefs Finance](https://news.google.com/rss/articles/CBMikgFBVV95cUxOSDdyYTQ4a2I0X3U4Rm56U3NZT2pTdDItZHNyd2IzMUV2QjBZR3BjUFpJblNvQjJFZjlkRTdlYm9OSHRyVDVFeWpTMHRUNnlRSWZTY2dsU3JYMHFwOHhRVDdfSkI2SGRMRUdicEtON1lScEZSZzZhNG1KQVhZSDlmaHd2TnBEYjFVMFJveEJLMkpxdw?oc=5) (Tue, 25 Aug 2026 19:38:31 GMT)
- [New GENIUS Act Stablecoin Rules Are Coming By November. Here&#x27;s What It Could Mean for the Crypto Market. - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPdnpEMzBPb01IT3RDNk03b05DT0VVNzNKdnRjb0lwQzJ0NG5xVVk0UUVIUGVxcnE3YkhyX2lXUWtiVHZsMVhad1pINlVPckdkMmF0LVJfTGZVYUxzTmh6b3ZCTXVwcF8wLWI4Y0lnRjczN05BbVZ2LXh4YnJiRFRxM0tPWVFDU0k4RmUtX2tnUTM0cWNyS0s1dA?oc=5) (Tue, 25 Aug 2026 18:55:00 GMT)

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
