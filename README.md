# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-16 01:55:21 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$299,283,018,648** | 🔴 -66.67% | 🔴 -66.49% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Visa’s Tempo Validator Move Brings Stablecoin Infrastructure Into Investor Focus - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxPaFZfWkxCTFFpRnJBRTB1N1h3T21KTC11ZDRiQVFXNXl0R1dQWlN3emNCeHZRckhvOHE5dzF4YzdKM2c2TEdkSHVPWTl5U2FvSEJEOHEwWVB5UTZLcUpjamJnRkxnN0JiS3hwZmZSZXhqdFd5YW90Y2ZSM2V2Mmk4eUozSUk4NHVZZlRCSEdONFNwRWFMbEw5N1dnTUNhZw?oc=5) (Thu, 16 Apr 2026 01:08:00 GMT)
- [Banks Won&#x27;t Like This: White House Analysis Says Banning Stablecoin Yield Barely Boosts Lending - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxQbDJaVklnVGk5emw3VS1xZnhZWERUcENsUUg1LUJPdTFJMjlzU0FCNktxN1hTLVNULWU4U1d2dUw3Mnl2bGNJNGRPQjdTSXMxc042Wm5tNnhyWmFQRXRZVnl5bTRBX1JHZ0traUlDZEJhY0NleGhaTWtIUVpaVzNPckdvWnNDaU1YNWpHSHJPRm5nLVp0c3NIN0pza0g?oc=5) (Wed, 15 Apr 2026 23:01:03 GMT)
- [Ethereum absorbs $8.4B – But stablecoin activity is moving elsewhere - AMBCrypto](https://news.google.com/rss/articles/CBMiRkFVX3lxTE9ZeFBHVFZUdnlUV2xSdVVjZzk1T0V4RGtNY3dYWThlbUpLaENLbDJxRDlWaXNsYy02eWdSZXRaYWNmLWQ2ZnfSAZcBQVVfeXFMTS1tNXgxX1JuY0xpSV9kVEtnZlA5NHdVOFJGSkc3Vm5FNWhMU0dwakZjcmZTcHNQbFMtMlZJRlZhZUxOTDFUNGlpZ0xzbDMtZGJnbnMyZWwwSkRyd0JJaWZUb01nOTV4QXFUUDBUVFlXZkpJQmIzNzdKVC10TnNMX1pzdWg5SmVnMVBTMkRCR3dlQXBFMjJPMA?oc=5) (Wed, 15 Apr 2026 23:00:28 GMT)
- [Companies Would Need to Disclose Stablecoin Holdings Under FASB Proposal - WSJ](https://news.google.com/rss/articles/CBMiswFBVV95cUxNby1iTEY0R1owLTNQYlY1T3o5UU9nWlVlX3BHeGw1clZLNU1PUmRqa0ZDWGlieVBVbTdlSkQ4Y2pXLXQxeFQtTlBYdXNlYjNpZjVFNzBEdzRlRENtNklkOUxRaEZLeW5GT3VLQjk3akhhTnN1bngzTXo0dnZNdlFsbnVHeWhxQkttOUZRbEFhMUJCdnc3NVcyZDgxUUduQVJnQXVuekt4ZmFIRHhMdEl3QV9SSQ?oc=5) (Wed, 15 Apr 2026 21:08:00 GMT)
- [Treasury Proposes Framework for State Stablecoin Laws—Should You Issue Under a State Regime? - The National Law Review](https://news.google.com/rss/articles/CBMisAFBVV95cUxNR2MwVml5cDI0Y2RmZUstRDhSVVFrZjBVSU02MDhTWEc0aGswQ0lDdi10WVJrcDFGT0xJcXhkVm01eFVWWUJJZXp6QVZtRmkzN09DeWU5blROeFZzYzI0bm1hZV9qcU40djZFM3p1N3ljdlJoTlp5SDZzQ3dGb05TQ2xLbWl2NjRnSEFNNktBcUlSRmxYVEF0YzZRUktJRDh0RzF1Vm9jYmxoQy1lQ3V0MNIBtgFBVV95cUxQV2pVZWVqNWZEOV9RbkFMRUFBQ0MtbGh5aWNvYWhWd2JBUzZOSk16WnhOYk43TmdCRzdQOXJMb2d5YUtGUUhDN0htN09POW1UbWZPMVNUQWNzU3pKdVEzZVVGbEVlS2EtVFQ1a0RTMVJxOFcycE5UZWhDc2h1SG1FR25nNEdoeDRDYU9wRFdiMV85QV9hOHBvLXIxMV9SQ2Q4WkF5NlRQRzJCZWcyNkpsbi1PZ0xJZw?oc=5) (Wed, 15 Apr 2026 20:30:49 GMT)

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
