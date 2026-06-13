# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-13 02:37:25 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,421,567,055** | 🔴 -0.04% | 🔴 -0.80% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Wall Street&#x27;s biggest stablecoin IPO, makes a sudden $4.4 billion move - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMijAFBVV95cUxQZ1ROZ1NNTXVocDdhRkE0c1VUVkluNVNmazdzSFhqdG0xNXVXVVVOSlpNaE9uVWJFRk5FV1lHaGxKTjFNamRZMWY3RHVzbXR1NnZxekhiaXc5aXVxM0hLMTFjVHdtSGhVVkdoOVpwcVF3N0t2ZE9YeHlYRFc5OEhlNlc3UTlJdl9WTUhCag?oc=5) (Fri, 12 Jun 2026 17:58:33 GMT)
- [Wall Street&#x27;s biggest stablecoin IPO, makes a sudden $4.4 billion move - thestreet.com](https://news.google.com/rss/articles/CBMihwFBVV95cUxQc3Y2T1pOWU1PNGhkdzc3Sm5FRUh4RnByaFprUThpbnNrUjE1UUptZkQ3XzF1U09WRzJkd3RUanNnMkZzYXYtX0Nja1U4RGZEQU9sY3FpcGRTaE9hTWRIRktrcGZBc3ZrMGI3dWxjdTZjV3BCTnFsbG1aLTBYbHdtRGdhcmNhY0k?oc=5) (Fri, 12 Jun 2026 17:19:10 GMT)
- [Bankers association urges consistency between FDIC, OCC stablecoin rules - ledgerinsights.com](https://news.google.com/rss/articles/CBMipgFBVV95cUxPcmJCdHFiU3JTTWRqcjM5RWFTYkVBTGM3azc2bE05M3VELXhtRVY0VmNyYUV2bHIzM0o3NkhFUFBDNWNvdGUwSi1uUjFTWmNOcVNvcWhpbkgxY0ZUaEFlOXZfLXhmSDZ1TkpqTXBLd3ZaV0RXMWxHM01nOU55d2VDdlk1LVo3MlBkbU8wa2daaGxLZEViMjJtZ2ZJTnZDYmFUMmVVdkN3?oc=5) (Fri, 12 Jun 2026 16:18:14 GMT)
- [Zelle heads to India; preps stablecoin for global expansion - Finextra Research](https://news.google.com/rss/articles/CBMiowFBVV95cUxOWHZVeFp2b19YaGFDdXZUMHlCQ3hMdGRKczVYUUNMS18xUDFLRHU5VEE5aGF2ZkllNGJVczR4alB3eFBLd0tmVDlFMVpxYWhKS1F5QWF5S0dBTE4tTVZjUkJwQWRVNjcyelVicGltNndKWFBpTUdzUU1iaUtUQXFmZmU2OEFCVm5FZ1RlVDNKTnM0SXU2QmJLd0pqeUNMQ0tRRGhB?oc=5) (Fri, 12 Jun 2026 15:12:00 GMT)
- [SIFMA makes recommendations for FinCEN on AML proposal for stablecoin issuers - Financial Regulation News -](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQTHJnNWdpSlFOX1RZd0ZlRlZSdnVaZmszWVNLcF9IenhRRUo5MVhOSFFKejc0Vzd0eUxjM2M2LXlqaE00STZ3RWFOejlob1VfNkJaMTFsSDJfSW1FVGw1cUZucjlaOEpQRlkydTJuSVY4YmJ5a1Z5UXdTajR1OUZpWnduZ1RLTXQ0Y3I2Zzhyb3VDUTlMMWxjMU9kdTU0Z2hCenZybzE2d0N0ZG8?oc=5) (Fri, 12 Jun 2026 14:55:24 GMT)

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
