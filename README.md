# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-29 02:08:41 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,101,698,810** | 🔴 -50.01% | 🔴 -49.94% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Financial trade group creates stablecoin certification for treasury - CFO.com](https://news.google.com/rss/articles/CBMipgFBVV95cUxNeFdaQm1CaTZXX19YeDUyRk5TaXozMk8tQkEyd1BjN1U4dDdETk8yUkxNYmFTQ1EzRVB2NjdzV3M0bkl6TUwtWUpJcXA1MHNmSmp0bnVRaFpXcjBLazl5WWN0RUpIM3JjVnFNYkRPVU5QazgtOHp4LTY4Y3loWm9OSkFUZmJVczBSc2FZaE5WcERabHFPeFlRUURSQ2NpRGFaZGxCQ3Vn?oc=5) (Tue, 28 Apr 2026 20:07:01 GMT)
- [US regulatory clarity brings stablecoins into the payments mainstream - Finextra Research](https://news.google.com/rss/articles/CBMisgFBVV95cUxQTU1JMXA1SE1iMHo3WUptRlM3RkZTTVVHeC14S1BIZ08tNi01WFYtVUZNelR1NHJmY2QtbUdqY2JkenpNbnhsc3BHN0NoMnRvOExiTDRQeFhhX3dGenFtckx2d1VDSTluZXlyOEJ1dHVYS2c4OGoyMWFiOTZGRXoybFpEOGxtUjBZeXpFaW9JNm5fMkFRZlVGZEF5WWozVWdxQ3JMZFFhSGRRVGFVMzBQR293?oc=5) (Tue, 28 Apr 2026 20:00:00 GMT)
- [Western Union Stablecoin Launch Tests Valuation Gap And Earnings Outlook - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxOSkJRNVU5M1NmQjVDMDVGQ1dlUEJOS3dRUWVSU3JXYXhrRVNSOHcwV0ZLYU5TWlRJZ0RBb0ZlZzhQeEFQUklNWDBlZVlqUUZ2dUxmN3ExaUlXU19WVWRGX3FtaFBvYnZ2d2pURmItTTFGZHVZYlI2X28tVmZoLTZNMEwwMktsY1pyUUxCZ210RW82WGszWlRoN08zRmkzTEcwM094OQ?oc=5) (Tue, 28 Apr 2026 19:03:05 GMT)
- [Stablecoin Giant Tether Reveals Plans for Modular Bitcoin Mining Hardware - Decrypt](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPM3huSm1pbFBpR28yMFk4dVlXS01ERmlyVEp0cVp4RzBuOFEwV3RBVWlCOFUyY0xYWkpodDFFaHp3RkJqZ2dBZWt2QWtUQnZRV1lDd1dwbjU0eUpidENvMVgzMnBlQkd5bFNVSGpsQW5GNkZ3MUo5Q0psM2NjbEZ3bkhqYUliMWNN0gGQAUFVX3lxTFBZV05LNUdOeG02eExtZkN5SlVIZGt0N0d3VmRyNDlZM1NCX0pNdnBhZVFOTDdhMjYtUTQ4QmJUSkpxOF9tTFZmQ1JtQUpUazlUY0o1RktQbzVHdFdQSklTSGEwSVRQNnVGUk5fcjBZUWhvU3dobzhTVm5aLTBYR3NHcjUtcGhmNHExMHA2MHZIdg?oc=5) (Tue, 28 Apr 2026 16:50:38 GMT)
- [Stablecoin Giant Tether Reveals Plans for Modular Bitcoin Mining Hardware - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxQTHZVNkJNWTVIUjFCd2lra2JuTlhEV2pFZnRnb3NjcGFuVzVUM0lFMWZ2RjRnNkluTzI2VVpwbWRxVU15UjhZeXFtV2lyeENyN29ra29VWlFlT1J2ZUJ2N1ExRjh6S0VXaFJ6Rk81Zkd6a2JNdWlZTVozZFRZaDViakp6UTgyTlg2cHNNMzc1bmVleEFDclVEdkhzb1hkN0RqVHEzTA?oc=5) (Tue, 28 Apr 2026 16:50:38 GMT)

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
