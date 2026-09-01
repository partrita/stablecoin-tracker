# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-01 02:49:00 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,507,547,759** | 🔴 -0.14% | 🟢 +0.13% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [&#91;CONTRIBUTION&#93; How stablecoin infrastructure and won-based systems can advance together - The Korea Times](https://news.google.com/rss/articles/CBMizgFBVV95cUxNV2dBWUxyQ2JUWlVVNkJncEdBdVhhalItdjdEX29aakNSTGI5ckVMUDhnaGhnUWRIeEFjTHBhU09WU0FmWEZmZTJMTG5JLVVrckhGbzBINUltYVFFMTVaZFY3cVVWaHlnM1FjVVI5WGxMbGlmMm51bEJPOXRsRGg1Vk9qMlhYREQzWmlvS2QxUHdSbFVvMjduV0xIVEpHdUtFTzlEUWxUeG5iZmp2elRmVHVXazZrVHhCT1hvbzlxbFQ1cVZsNl9zMWNSSzFCQdIB0wFBVV95cUxQR1FSbG1EQm1GNEh4VHd5MDJnRlRHQ2xhamJzbnZXTUFPQlEtRDV6dTAxMkZKNko3ai1RbTVfU1E0ckFINlVtNHRJYkdSeHI3SjRHN0RsVDlTUVlhbGVxcXlzSXp3YXRiTU1tZnZPeldrWTV5cGgzVnkwUnczLTR5YW9MeF85VlByTlhDalpMbjJtSlB6U1VRWm5zT3JSTHVWYjJyUGR5MXY5cXNkVkFFSW8zeTNkRlpjWU9wS2FYbE1NdTQ0dlhob2Rta0MwSG05MEZF?oc=5) (Tue, 01 Sep 2026 01:26:03 GMT)
- [Hot Topics in International Trade Braumiller Law Group&#x27;s VP Bob Brewer is joined by DC Counsel Jim Holbein to discuss The Genius Act, Stablecoin, and the upcoming regulations.mov - JD Supra](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNVmxFeUs0Vm8ySnNrcUQ2eGsxcU5OZGJ5OU9nZ0tfRUxoeGlCRFJOaTNpWUFIR1poVEFvQ0lPTVFmSms4cWx3NEt4Z3BvWmlyR1J0bFdQTGEya0VrYXVkRlp6Z3lCUXBocWZwZFZmbFhnOUdzekI3S25GbzE5RS1BNTE5TWgtSjRl?oc=5) (Mon, 31 Aug 2026 23:30:14 GMT)
- [Blockchain Association Challenges Stablecoin ‘Deposit Flight’ Warnings - CU Today](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOMnVudGxZVkUzWm0yclZXaTN6WjVpT3V2ZmFaQ1RoM0liZ1o5ZDJ3MGxESlQ3R182Y01sQzNISmhpenEyOGhOLUsxMG5DYno2RWZRWFVzYUxjNk02SHlaai1lR200LW9fem4zVkR3N19fcm1Mdm5WVEQ0OW9oS0tjQmowdkNreDExcjNqWHdyZWFuSlJqaU5vaWs1MTNfaEIzMFQta2VHa1c?oc=5) (Mon, 31 Aug 2026 22:09:39 GMT)
- [The Stablecoin Race Could Make Bank Loans More Expensive - beincrypto.com](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFB3Z01NZWNfenBoeUNFdmFNN19rdXVWSWNXZFN6VldCQUxGTFNXM3dnX2RmWVlXaWZ0djdxeXUwV2hNRjRvYURnQWJ4SllHaGRIVWdZdE5xODNJemkzRDVwYlRlOXpoQVk?oc=5) (Mon, 31 Aug 2026 21:25:00 GMT)
- [Binance’s ERC-20 Stablecoin Reserves Facing an Inflection Point - CryptoQuant](https://news.google.com/rss/articles/CBMidkFVX3lxTFBaMHZZazZ0bzhtWHRHQXFLMkFGRnQ1S3pXTnhreUpvTXlzNzIyZzBBYU9MM3dWZmZKWXA3SHhtUlByRkQzM1I4R0FVVTE4N1R4eVVwSU10aFJTRDBtSUtIWG4zRmEyNHYzeEdweUEzNXBlRDdEWmc?oc=5) (Mon, 31 Aug 2026 19:39:01 GMT)

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
