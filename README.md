# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-01 02:50:21 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,396,808,115** | 🔴 -0.10% | 🔴 -1.00% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Rising stablecoin use could cement dollar dominance, ECB&#x27;s Schnabel says - Yahoo! Finance Canada](https://news.google.com/rss/articles/CBMijwFBVV95cUxOM01lSlVobkxlVDY5b0FFbzNPUmI0NGFobmFmR1Q3cWlYV0VPZEdaSHNucEFFa0NvSXpEMGk1eU1NMVFzNTJ5LVRPVXJCbWQ1eW95SC1JcW9aYmVjOUhPNkVLaENTOXRTQU5iWTNxZ2VFem1IeEdwa1QyR1Vha0tOTUNEQ3FqelVhRkJ6a2d0Zw?oc=5) (Mon, 01 Jun 2026 00:15:00 GMT)
- [From money market funds to stablecoins: lessons for central banks - European Central Bank](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOYWpBLUxCb0JzalYyTXNRSTB1MTlreEVoaDhxTnJtWHgyNmxUTU9odWVLUHlIMlpybFlfNkpvZzBIOFlobjVqdTZPckptcDV1QXIyR3ZvMmhkX25OeG95dk5fWEpKdlEtcm52a3dpcFh2UDJpUXNKTUY0R1hjNHVtT05GY1VMdHRmQlFj?oc=5) (Mon, 01 Jun 2026 00:10:32 GMT)
- [Stablecoin demand may soon fade, BoE&#x27;s Greene says - Reuters](https://news.google.com/rss/articles/CBMiowFBVV95cUxOX2RKY1lIZEwtYzlBSXN2Mkx2RU9YYXVqZmlFaWZ5V2piVTRyWWtud0E4UXByUzh2RU94WGZ2R3RVallTTmhkakFVQ21scXI4X3hMOThkT3BxSHp3UzBjaV8tLUFvcEUzbUpRX1JMNkMtTmpyeEZvWFFjQmR5R2ZXc21MejVHZGV5cFVyZVpUclRudkdOWkhQV1hoODdnZ2tNTHF3?oc=5) (Sun, 31 May 2026 15:30:09 GMT)
- [Stablecoin demand may soon fade, BoE&#x27;s Greene says - Yahoo! Finance Canada](https://news.google.com/rss/articles/CBMihwFBVV95cUxPU1gxUE9iMXo5TXBEUENFbWtiVjZPYzZzT2VCTWQxRDNvakxONTdvYXRQeWhDVXdSOXc5Zkhjd2ltbHVsYmxFVGNkVGttSGd2LS1WdUpheERGdXhwa0k2ME5FSlc5NnBxRXRuTDFoT2p2ZGlzVXBZVnAyaHZxWC1xdFRaN3FxNFk?oc=5) (Sun, 31 May 2026 15:29:56 GMT)
- [Fed’s Waller Says Stablecoins to Broaden Reach of US Policy - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxOekgzVVJDc3lqSGJlNmhha0pPWXhqbzAtMVNCZHNzdVN6SDRPWEM5dnJicURReTZ4bnJNYVIwTzdDWjRjemNPeWxjMDI3Y1hjWC1aM3IwTEc1SUpXTTdERHBIMUEwZ3NIVy1ybmtnZW9yWkRhT2ZaX2tlVHd3Y0NCaFRtMGZBYVFqNllpZnVOY1lmX3V6X2VKbVdWdU83bTRfV0E?oc=5) (Sun, 31 May 2026 13:59:47 GMT)

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
