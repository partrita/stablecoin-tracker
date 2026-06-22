# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-22 02:55:26 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,559,416,041** | 🔴 -0.01% | 🟢 +0.06% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoin regulation converts issuers into psuedo-banks while adding a barrier to entry for smaller players - CryptoRank](https://news.google.com/rss/articles/CBMigAFBVV95cUxQOHByVmJJUjdSN2pBcUhUUDZ4Q29FTUJVb2Fzak5QelBuMWJTZjZVRzdLMU1zdXZ0bGZDZVJ2S3MxVUF1N0JjcmdEdkxIQkVMWjZCeDlIaVRsTzd3ZU4xelVHeUMtU3VWR3hGWC1DV1VBV3I5RlY1cGphbzdHYVFQRA?oc=5) (Sun, 21 Jun 2026 18:35:20 GMT)
- [Federal Regulators Want Stablecoins to Keep Working Without ID Checks - Gizmodo](https://news.google.com/rss/articles/CBMiogFBVV95cUxNZGNnMkpIN2xZbWUxS25rNG02ZGhhRktURzBxWDFLcThxYkNRbTB5SmJjRUJGcDc5YmJCazdRaTZuSVJGcFYzdUFvWmtxRWRuaW5EX016WXQtZ191aTNJWk1WTEdaeEVfTkE4Q2l3aW5oLVRKMUt3UHRVUkFPdG9hWEJ2bXQ4Y1V3RTh4X3ZrQktiejFwYS1fN044MEU2M1hJQVE?oc=5) (Sun, 21 Jun 2026 17:12:32 GMT)
- [Stablecoin regulation converts issuers into psuedo-banks while adding a barrier to entry for smaller players - CryptoSlate](https://news.google.com/rss/articles/CBMib0FVX3lxTE1zekE0empGYk9wcmEwZXRuLWwzeWsyOHV6VXZ6R0hjNHVfSjlaTTREejN1emVGTnBPQ05GYVB1dmZDSzZkb1dxNTNEd1RnV195bkYxWVJidUd0RUtYRllPeklRUE5FZ2RxWDZGV1dlRQ?oc=5) (Sun, 21 Jun 2026 13:10:09 GMT)
- [Stablecoin Regulation Is Becoming a Major Theme - Moomoo](https://news.google.com/rss/articles/CBMiogFBVV95cUxNSmM2bGFUNE5Oc3FHNUxJTnpEMy1tVnB0bUtTYmZVVDFtd3hJaHlzeU5RUXQwSzFUaG13aXd5YzRiNEVCQm5sMUhZOUtkNGduVExEWHFyM3J4aWZ2YWlIT2Vmd09OVE1xTXBET2VMSy1lMmlSSmZUSWpfUURhMW1sZWRfTVplb0M5ejdtdGxxU1phTnd3UURtajhBTk15TC1tLXc?oc=5) (Sun, 21 Jun 2026 12:18:13 GMT)
- [A single vendor termination just wiped 88% off a stablecoin that called itself institutional-grade - Startup Fortune](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPaThhTkdwSjZkU2ZhQUYxMURZR3ZLb1dzMm84bkRsVFhXM0hwSDZTN21SZXNia2Z2OG9tbnR1eG9Db2xLQk1KSl9uX2gyYTY4eDRtaGtGZ1llQmRYNXdUY0tmbzZ3NHZ2UkFmTWxISFp5WVRHYlF3d2t2ZUUwSnZVcTVwOXA4SUlHV2t6TlRZM1Q3aGU0Q0RYem1laTlQYkEwY3J5bjczeHZYZ1M3a2VTRGpPdnlfUmJVSzhQc0NmNTBDaUk?oc=5) (Sun, 21 Jun 2026 05:48:53 GMT)

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
