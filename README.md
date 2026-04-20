# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-20 01:56:27 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$299,905,467,904** | 🔴 -50.07% | 🔴 -49.75% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Vault: Banks test limits of their crypto leverage - Punchbowl News](https://news.google.com/rss/articles/CBMia0FVX3lxTE9PVWd5eGtJQ2FrMkMySUFFZEZmZmdZNmE5MHFUUHBkN0ZKU1RmYUR4X2ZlZEpzT2FINER3amQ4Z3FCYTVVX0U4WENmV1lBTGtzODlSRXFqTzVxdmtLRmRNWjJRUm9jSkt6M1dF?oc=5) (Sun, 19 Apr 2026 20:39:33 GMT)
- [CFOs Eye Stablecoins As Payments Tool, Not Crypto Bet - CU Today](https://news.google.com/rss/articles/CBMikwFBVV95cUxOa2VNNlFjTmdET2FkSkdjTVNJbzlMUm53R19kR2ZBRnJua0NScGVSVzhhTEdFQWFENDFSb0FZU3VHYjBuN1pwVlh1d3VSSXlkMXM0TThzel9iMVRISTJORXN1cnM4eGFVVm91ZEV1ekNsZDZBZV9DSDZoU3p5NTNfVEU4SWsxeUE2akIzUzgxY3NUVkU?oc=5) (Sun, 19 Apr 2026 14:33:54 GMT)
- [‘Move on beyond greed!’ White House blasts banks over stablecoin yield opposition - AMBCrypto](https://news.google.com/rss/articles/CBMiRkFVX3lxTE5hVzlnUTdJWTUwcG93dm0tT2pOSzdYLWdueXZRQUE3MXJQN2VWR2NzWEdrSUFjNzNveFpmQTc2UFkzUHV0cEHSAagBQVVfeXFMUERDRDkxcHNxeTJwVWNIdllVdWlPeFlrb2hHbE5aTVAzbVFPUmVKbWlCZHk5V1Vva0VvSUtSTFdRdU5JdDRBVHctbGVZNm9DVU12ZnRaV2NHSDU2aFRFSUxIVVZJeGtkVFNaUlo1TjFYNUh0TFA1d0xyX1J2eEszeWM5QmQ0LW5qLUZvZ29lSUNDYjlrZFBmS0xmWmlOY19CXzRlMGNHbFNr?oc=5) (Sat, 18 Apr 2026 18:00:37 GMT)
- [&#x27;That Is The Wrong Question&#x27;: Bankers Group Reject White House Stablecoin Report - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxPc2QxX29VNTJ4aDB1ZmJmS05tZENXS2hQZUZlaC1XN3JtNk1MUUVvRVVQbWExWXh3WEtBRG1iQ3IzOTRkNEN6d0VsWjVvMEtYRWcwS1QyMGZqaWQ3R19PRlMtYlEwczQ2VlNCb3JRM0lRSEdJVXhyNGhVOEVGVXV6cnJaYmYteThTSHRUX0JITzQ1SDRBRjFxSEU1U1VQQQ?oc=5) (Sat, 18 Apr 2026 13:16:40 GMT)
- [Banks Broaden Lobbying Against Stablecoin Yield in CLARITY Act Talks - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPSmpWZUE2eV9UalQzZ0ZaRXozM2lvbHlCamNsWkRTSERNVm1vLVM4WTBmUTJGYVFFWFR3VEZZNXBkVE1sUnFNZzVCV0k3VlFDX2pUejJVTEs5d3VqS1ZqQzJ5X3cwV2kxWGRnekxpNWtITmpPZDJIdE1LWlVFc3NEVXY4dmpDeWZPcUJfMFZDMVVCeHNHWjRPRVJvRndEN0Z4RWNkZWpMSFItdw?oc=5) (Sat, 18 Apr 2026 10:43:14 GMT)

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
