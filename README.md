# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-18 01:23:58 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,491,675,397** | 🔴 -0.09% | 🔴 -0.14% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Credit Unions Gain Path Into Stablecoins — But Not Without Costs, Risks and Strategic Choices - CU Today](https://news.google.com/rss/articles/CBMixgFBVV95cUxOR3lKM0NhWUxMOWtQd0tDbjVheEpSZEJiWV9laHVoMVQteFBRR0JTejRsRll5N3dIdUs2QkhTV3BsWjlzaV90N3dfdzQtVnozb2laSkdFSzloOEYtSXhxX2lYYTNzclZ5NGROQWhrY2h1OVZDbjdxeXhDblJSN0VmVTFSNV9acUE2dXJtVUhwbTJXMHZTNmdHY1JTSEN0dmw4NlhSVE5MSWVjZkRlU2NJQTZsVFpGQlpTU29wZ2p2V2R1WGViZGc?oc=5) (Tue, 17 Feb 2026 23:17:27 GMT)
- [Stripe-Owned Bridge Gains National Bank Trust Charter to Boost Stablecoin Offerings - Yahoo Finance](https://news.google.com/rss/articles/CBMihwFBVV95cUxQczl0RGNreng0Ym5TZHE0RlludXp4ZzA5WTFrQm01bVlKMTliajNfRTV0NG91RzRmLUVSejMxMThDUTJlTFRFMndna2RxRl9kRkZQb05DRzlWREdHUU91aXVjN1kzblAyYUs4MElib0RNMXc1TG81OEtZV1dYbHNUMjU5aExzTVE?oc=5) (Tue, 17 Feb 2026 22:13:49 GMT)
- [Stripe-owned stablecoin platform Bridge wins conditional OCC approval for national bank charter - The Block](https://news.google.com/rss/articles/CBMisgFBVV95cUxPWEI0d2dVb3RGR0ZOWmxRTDRPQVhVX3BjeGNEd3lvSy1LczIzaXR6ajc1TXV1R3VCSFVqTE12T3Y5aWxXSVJIWlBqc1IyYm5Razh5NUx6LWowajNYT2h3RlVvWEZpUG1BUkNDWFBYd1h4dG5EcDlEdVNCNFNyTTZ5NzVuS0VualJyZVFGa1BpX3N4bXdfby1hc0c4UW5DcHFFQU9mdWF1aUZRRkNVY2xKTjZB?oc=5) (Tue, 17 Feb 2026 21:13:10 GMT)
- [Stripe's stablecoin firm Bridge wins initial approval of national bank trust charter - CoinDesk](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQUXpQWjNMTWxEb0hKUDVKeWRkdGlILXZfSTZySm1Fa2NLNWJHTjJkTU9sYnhBRklDbV9nYzhfc0VFRmdhRjVyYnRxSFNPX1FNZTBhaWY2NUNVQmhRMFJtajlzMGgwd3RJYlNwMDU3OEU1SjNHYnZ6QmNXYWlXeGtwN09Qd29vaE5xNWVLcUlrTEV1WmV3cVRnMEwzU2hnSkVTT251YzdxR0lvUlQzWDlnZTR5VXVJTjN5LTN2MWIzSnJTNXBnRW9LWQ?oc=5) (Tue, 17 Feb 2026 20:12:06 GMT)
- [Malaysia starts sandbox pilots incl tokenized deposits, Stanchart stablecoin - ledgerinsights.com](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQVHBuZzkwbjF1SUNZV2ZCZXpacUlJbHN1OXhxQm5KbE5GSUxIUHozdEk5U0xkMzczSTJkUWFUUFNzMlRMTzZMXzJ2WlNIZEJ6Q3llWk4zWFVOVTFIV2hBSmxRR0wzUjNGeERuWUoyVDUxSlQyQm1JZm1qekdLbkJrWmZrSmstZHdCekI3cy1nRXBjMGZaYXpKWks4ZVpNMW5LUXNHRlRzdndZQ1U?oc=5) (Tue, 17 Feb 2026 18:04:51 GMT)

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
