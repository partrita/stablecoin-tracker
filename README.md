# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-28 02:41:13 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,620,561,880** | 🔴 -0.00% | 🔴 -0.33% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Gov. DeSantis signs stablecoin framework, new crypto kiosk fraud rules into law - Florida Politics](https://news.google.com/rss/articles/CBMiogFBVV95cUxQOTQybFdOX2hZemRLTl9IdlRKODhyQjFBRk9yY25FN0xFdDdkZ0hkY1JQY0pKaHRlYUFkTFRySUktS0VNM0RqMzFxWW9mWW9nZDZnVXA3NWJyWG13dGt0VFk0VW9TZUhuTm1lVGw0NVVQcDRPZFhDeGJDdmJRME9jWFpyVTBjNHdManFsc1hBS2l5ZHd6TkZlTndzRVR6Q3pzQ2c?oc=5) (Sat, 27 Jun 2026 20:06:43 GMT)
- [The UK softened stablecoin rules, but may still be capping its own market - CryptoSlate](https://news.google.com/rss/articles/CBMingFBVV95cUxQLUZ4SkhJbi1sUlJmM1BDVDFtaVBGTmNDblBpdzV1ekJkemNFRlJra1Z5LTMxcHhWT1VyYTdOWVhwNlRCS0JKODMzTk9ET0VrNVo1V3ZEbnBPaHRDb0JjcUJzYUhhRi1kMVd2SUhvTlhNQkROMWhkS2ZRUWJRcXVieHlBOGlCdnhpU3R4S2xfYUs4Wkk3X29nMFlxMWRRQQ?oc=5) (Sat, 27 Jun 2026 18:25:33 GMT)
- [The Stablecoin Founder Map Doesn&#x27;t Match the Stablecoin Volume Map - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxQQjBPNk9ENXI1QUVNX3A0QkZTUE5rbElkTThCUW9RaHRkbl94WUJZUldJMDlqUGRSSDRrcXQyOTFsQ05aeXFXMHRfUlNleHY2cXpnR1BBcVQ0RjhHOF9uMzVjV3JxdVBUZ1A0dno2M3NKZjRVNjNBVmpfbDlURldlM0VyeFFXX1owUlBDc25TLTBpNFhoUkVzbFNNNVJHejhrVnc?oc=5) (Sat, 27 Jun 2026 17:01:04 GMT)
- [The Stablecoin Founder Map Doesn&#x27;t Match the Stablecoin Volume Map - Decrypt](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNRnNlbGhESXZMdXVlQzV6Q0lOSnh0SlRLQ2h4b01Xd2NvSGkxcTNqS2NSTW0zSTA5c3hmMFBCcndWa2hCLUx4bHRkeWtQLTduTkF2ZUY3U1NHcXRxRHh0a0FGV0w3OEJIWkxxT0N0Q1Yzc0JYc01sTFBfUnRJVEhiRG5OcjdFdHV2X1BJ0gGTAUFVX3lxTE9HQTBhTzZVSm1KNWdkMTdrTXpUemNDdUpKbmU4Vk9mbFV5Z3oxREFwX1BCLVJ1UVIyOW1PM0ZBNEw5QXpfd1djNldCSV91YUtuaVRjRTM2RHZMZVkxX1piMHlLMjVkWThqM3NBekFyU19uZk9UZFRpRWZSeW9jdW1NV3VOLU5EQ0pNdEgwakozUVNVYw?oc=5) (Sat, 27 Jun 2026 17:01:04 GMT)
- [Standard Chartered Says XRP Hits $28 by 2030 but Ripple’s Own Stablecoin May Have Other Plans - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxOdlRRT19WVVB0ZmhuMHJIZmY2ckhEMGZBV3Z2Y0VVMjEzSXVXNy14Vi1nNnZvOUlsLWpObDRXcjJ4bFhPWEowWGdIRFRwYVFNSmY2SDlLYW1wTnE1Q2tkLUg2aEg3b3BOVmEzR1BBUEoxSWc2Q2xYcG1qVjN1Vk04MHdRODlteVZuVE42aWtCdkY4SGZ3T3RKZVpmRDNIdw?oc=5) (Sat, 27 Jun 2026 16:56:01 GMT)

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
