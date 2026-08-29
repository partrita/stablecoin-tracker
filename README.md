# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-29 04:56:10 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,102,012,015** | 🟢 +0.21% | 🟢 +0.41% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [OCC Sends Final Stablecoin Rules For White House Sign-Off - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTE82WkdLNjVDSXdOWG5qTjRUUUZndkhpano2MHBXV21BendudWUtUHhFdWNQdFQ3WWFmUXI1TXlUWXhzUW1qc0RBcmlGTHcwNGlnU3lhVzdR0gFWQVVfeXFMTzZaR0s2NUNJd05YbmpONFRRRmd2SGlqejYwcFdXbUF6d251ZS1QeEV1Y1B0VDdZYWZRcjVNeVRZeHNRbWpzREFyaUZMdzA0aWdTeWFXN1E?oc=5) (Fri, 28 Aug 2026 23:47:00 GMT)
- [BIS General Manager Says Tokenized Deposits Beat Stablecoins for Digital Payments - PYMNTS.com](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcUFaNkw5YXlYaWxROUJjMEdtODBTcGdGZTVfVnBnUnVsYlJ1bU43VkdNd2RRRzJiOWkwdjJBeE9TT3ktbFFzV2hPNkJBdTJPQk5ZOWRsUElLQnNrc1lJZWRHOUNhZldmOG9nQ2JBSVVzWFdjcS1tLUVoeXRzTTUyMXJ5ZERKVXFiaE5HVjR5X2NSWlJLNVRCU2NYeU1pZzFVdFZWdzM1SmpSSk9ZTXpzVWp2bTd2S1c5dFhGOGVUTm4?oc=5) (Fri, 28 Aug 2026 21:05:49 GMT)
- [This Week in Stablecoins: Interoperability vs Competing Interests - PYMNTS.com](https://news.google.com/rss/articles/CBMirAFBVV95cUxOOUZfdWxUMWZxbWlrTmpSUnpJRmNGV2R1ZzladnpKSmFLa05pR1JBTXpZTk1VQTlKMG5xWGhGVVRTb005QlhxTWNMd3ktUDdpX2hySDZoUnp1blNCYzE1ekl0UERRcTVVX01zZnYxR1FEakZ6LTBCUU9LZjQ4c3FrTVp5OHN1QU1DMkZxZDE4UUM2X0hnT2pfWWQwbW1QSFNzdmdUY1JDMThRYUh2?oc=5) (Fri, 28 Aug 2026 20:50:48 GMT)
- [Twelve Major Banks Are Building a Stablecoin on Public Chains. That Changes the Competitive Calculus. - forkast.news](https://news.google.com/rss/articles/CBMivgFBVV95cUxOS0gzdEJ0UTQ0ZEhHUmMtOTM0aFpUdGRaZXlSWVMxU0lmUURFRkpFUHdjOUJGYlhheUk4elFvTnk1ZnVtTHhZS3lybW5USUtHYlpjaDNqYWxidFlIUE85bktMemMtU3dHWmFSZkYwemktVFFoejVCZUN6YV9mUzZkZFdOMUozb3VhLVBUX0dRd0tkWDRmZkhvcG12Rjh4R2k4UzhzZVRNNGd6QnFHQ0ZmSlBCaW5jZ3otY1hTamtR?oc=5) (Fri, 28 Aug 2026 20:11:56 GMT)
- [The Digital Euro Race Is Taking Shape, With Stablecoins Leading The Way - Forbes](https://news.google.com/rss/articles/CBMixAFBVV95cUxOeEJpMlpSc0t0OWY0aGVLTkhpWk1sR2N4VTctRzdsWVVwbHNEa3hhd3BOaVRYSHFuNE1RNnlhWHNwOHpGSlpoM0F3N2dQUEFwR21tTXlLZnc5c1U2Q2g3Y2UybEJFTUVjYUc5QXljVTBmUGVwTU9hWXZHMFVJY1RnWVVwNUI2aERXc1JSTjQxd2YxTDRoMkU0eUxuZ1V0UWJZSjNEY0hnN1JpRVBYeWdCRS1fV0tLSVdIdEFiZGdpdUZYX1c3?oc=5) (Fri, 28 Aug 2026 18:55:51 GMT)

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
