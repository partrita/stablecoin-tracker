# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-09 00:20:27 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,636,672,605** | 🟢 +0.11% | 🔴 -66.57% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [FinCEN, OFAC Propose AML Rules For Stablecoin Issuers - Law360](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBvcFlnanFjYmI4WEFRSmkwanNmSW13OUQySkhXeHk1RFNqMTJlSi1hb0pBZGxiSXpFc3VpOVFuajR6Wkp1SFRUTW5aT0RIejRf0gFYQVVfeXFMTVo1cEwya2tpZmN1VElNd2VMbVRpcWxuU0xkMGt4dzZXZmVwUHpqMVFlTFBEUFZjTVctcXczazhkTmJNc3duRWFrcWw0akloeHhFV0lWMmo5Tg?oc=5) (Thu, 09 Apr 2026 00:01:00 GMT)
- [Paysafe’s MoonPay Deal Brings Stablecoin Rails to a Payments Platform That Handled $167B Last Year - Yahoo Finance](https://news.google.com/rss/articles/CBMipgFBVV95cUxPOHBDUkZpcGZtdlQzTDF4dlRnZ2NGelhjTGRmUl85dkp4VDlqNXRIeHE5bzVwb0MwRERVWXR3cFN4d0dzeEVMcTlFcjB1bV9OQmNlMDlwRWV1X3hHOUU3RlVnQmtiOHNOMFp2WFNEdnlRbjVVbXNYU2RMeVVLdjYzOWQ1SnI5REk5OUstaEVPNzhIOEl4Zk9xbGllOVFZVFVIb0hyemFn?oc=5) (Wed, 08 Apr 2026 23:27:00 GMT)
- [Georgia lawmakers pass state-level stablecoin license - State Affairs](https://news.google.com/rss/articles/CBMibEFVX3lxTE5vbndQZXFxTXVRelpEWXFzbUo2RGtCbi04aFNYMG8wTW1BWUdnei1oNkFKT1VaZEFHdXNFZTlINzVVWFgxTXphMmtwbmtxbTZ1ODZLQVdZb3VfcTdYTV9ocXpUNndmdjVJM2hGeQ?oc=5) (Wed, 08 Apr 2026 23:03:45 GMT)
- [The integration brings TRM’s blockchain intelligence directly into Stablecore’s infrastructure, enabling banks and credit unions to confidently bring digital asset products to their customers - TRM Labs](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNVTdPb2RpUlJHeGpGMk9aRWxINGQwUTItUmoxTm04QndCLXZpbDdnLWxDbmpwc3VfZlJ6aUdxS0NvSFFRWlpRbFZxZGIwZlpZbDU4bm1qSFFxaThJUXdHNUJ4ZkhUbW1zUnIzUThUenZVbG0taWx5RTd5UUg0NE1EVUdnblNycGw1aG9malJWOS1zSnh2QTBmcEZZTU9OYm1lNnVMRl9YQmZxQ1RZdnc1YUhDV2FsLWJPNkphRGVVMU51ZGpkQ3ZiVW1DVHQzbk8wNng4Z1lUWDFpbmtyV211N042MA?oc=5) (Wed, 08 Apr 2026 22:54:15 GMT)
- [Circle Launches Managed Payments for Stablecoin Settlement - PYMNTS.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxNZy1QbWpBUkhuVVZOZ3dLd0syQkNOQUpOLUZqRjFEaEF5elRZRW1TN3hQdEE5VXpCTnRWOXIteWwxMjc3S1dNdXljQWM3TFdzVUhYbkxzZnFoVkJ3WjJSVmt5Vk0ybVpLYzZGejdsbTdOM2Z5eUZwTzNwQ3Y3TFFObUVfTkdwYVJjUlhkaVFONkFRcHFkMHg0emlES2RVR21wOHpoUA?oc=5) (Wed, 08 Apr 2026 22:29:48 GMT)

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
