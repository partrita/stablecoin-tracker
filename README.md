# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-31 02:00:13 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,994,982,515** | 🔴 -0.06% | 🔴 -0.62% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Florida Enacts Stablecoin Licensing Framework and Government Payment Pilot - The National Law Review](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOb092dm9GR0l6S2NvMW5Yd0Y2WDVYSk1OOHo2aUFnX0U3TVc1U3BfNktOd0xFV0Vua25DNXpoczU4TWpMRkZDLWwteGZDX0VhQ2sySkU5VkxybjNVTzMzdG54dFg1ckJhNkRkX0pIanloWW82cU56SUJma3VPSmJZMXBRakMwZUR0WkVNVkJFU1BKVGVyM1RKR3FBNGtNVXh4S2NwLTFiQmF4Y3fSAbABQVVfeXFMT1BvcEl5clJHbTRINzZReFZoZ0I2Nm0zUUl0d09BdGV1Mm1RdEtDVVo4TzBLZDVIOGR0RVNKeXhEVE0xWWNZbHQyZHFTLTJwV21URmJNRHpBZ2tvSVN6Szh5ZnhEdmtwVFV0dDJIVHlpV0FtTFNmQWF4Rnk3UjA1RUNGeXpNMFRVZ05RcTZYQ3k5VTI2WEFmSVRzVWJsblltdnNLeGdYaldlOUpuQkltcTc?oc=5) (Thu, 30 Jul 2026 23:54:38 GMT)
- [FINANCIAL TECHNOLOGY—Banking... - VitalLaw.com](https://news.google.com/rss/articles/CBMiigJBVV95cUxNUEh5enVHMkNZLXB4OHhRX1JLUEtUWklNYjkybGMwUGVXSl9CVEYyMWI1bFdRclhIYWdzSWJ4SldlWVktNUxxRmdfZkJLV2QyNGRVWEVlSnEwNFhpUER4dlAwZXJOOFZtWXVLUjY5LXZINnBNRVgzaVlxeXFJUU9NZDRXWC0yYVFPU2JjYkdQUzd1dE5XeEFjOU9BTEVxZmlIN2NXMG54QXlhYzNseG9EREpjT0hTZVNxVEFyZzB3UC1KVUhpU2FBZWVlVU54ZnI1WlZpZEh6TWlIV1d5Mmt1NldYVnlOeUhxenpMNlRTdzJOUzE1TWF0UGtyWmhnRTRVV3duMHVRcTJPUQ?oc=5) (Thu, 30 Jul 2026 21:27:00 GMT)
- [Stripe Helps Data Firm Dune Accept Stablecoin Payments - PYMNTS.com](https://news.google.com/rss/articles/CBMimgFBVV95cUxNOG1xcHJmU0VMTWdETEZ5WkpPRjdNWThwa1lETHlvUW11bVVGT0t4bHBMbVFIT21VekU0dDEyVERuQl94X1ZhYVYzRGQ3WDZRZ0ZZRm9XODN1b1JqV1hsS1I2SHozT2FITmNSSHprYVBLc0pUU2hYdlZ0TnNwS3pUOEFFX3BpMDc4OVp3QVFPbmlKTFhuZEhCOGVn?oc=5) (Thu, 30 Jul 2026 18:07:35 GMT)
- [Credit Unions Urged To Weigh In On Stablecoin ID Rules Before Deadline - CU Today](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQQnhHWWZoMHVoZEQwaFMxUTE0ZkE0TTRqWmlhaTFqdGg3eTVrRDE0dUF6NmxnX3pwUERqRi13QVlsaTJCM0hfWnhMTTM1a2hOXzktOGF0WHlWX1FIb1luaEI3UjdWdnBXMTR6R2RNUm41MTA3Q3Jvd1FHdTdTZURDVG1CVXU4aUQ3M3dGYV9OWnVrMzM5Wm5PcHRtaGZxOWduM1Vhc2U3UHF4MFk?oc=5) (Thu, 30 Jul 2026 17:46:11 GMT)
- [Stablecoins complement dollar: Fed - Payments Dive](https://news.google.com/rss/articles/CBMigAFBVV95cUxQZi1sYW5vZnNUaDlKSk0zM1gwYlVmTTB4bHZ2NmRpdTV6WnZzNmpUbXR3YVM1ZWdnWWIxelZYV0pSdm4wcWhlLW1oSl90eVRuWWx3ci1CZnNtN1FSaWFmdXRaVEo1a1NYTWRZSTRJMmlXSHoxZENiMXNNb0t2UTczZw?oc=5) (Thu, 30 Jul 2026 15:15:33 GMT)

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
