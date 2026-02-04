# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-04 01:17:34 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,915,761,381** | 🟢 +0.12% | 🔴 -0.75% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [CLARITY Act Proposed Ban on Stablecoin Yield Sparks Congressional Debate - Consumer Finance and Fintech Blog](https://news.google.com/rss/articles/CBMixgFBVV95cUxOck9WLUpSU1BOakUtalBHMUZ6SnNYY3ZCY0tGMk1aYWZxV3hIYTB0Q1FzckhXbkxtVi1wZ09UNFlmQTZkTVk0MHc1QjY3ak1CUE5ZVEdjSVBkT3FXdURIVkduVkZOSmdiaU5xM0xqeGdqV2s5aDJwWkhsRGZWejNxYmJBdHJhWmVmTkprV0FfSEl5MGpIQ180SXhQVmFfN2kyclkybTRmN2J0RDN1UERTX0lsUXNZOUdLUHAwS1RZR3U2aFVRWXc?oc=5) (Thu, 29 Jan 2026 21:31:07 GMT)
- [Stablecoin law allows crypto firms to profit from fraud, prosecutors say - cnn.com](https://news.google.com/rss/articles/CBMid0FVX3lxTE1JbGpKbkZGZ2FvaDdzS1pEWlQzU2ZqR1hxVW1zUFdFU2JPeC1CNUVrSWZwZFJheThSLVd4ZW8zb19uMi1ldEZvTkpqQnRwOVlyRXBGLXFoYXk4bEF1SVZUNjk1aFpJMnhzeUp3ZE1EVGlUbFpQRjFz?oc=5) (Mon, 02 Feb 2026 14:00:57 GMT)
- [UAE central bank–sanctioned US dollar stablecoin launches to boost digital-asset settlement - The Block](https://news.google.com/rss/articles/CBMiugFBVV95cUxQZ1QzaUpQNVhfcWdHUnJGOHJ4cjVvZnpYejVUYUVoc193OUZnLTlES3lsZEduc0l6ZjY1WVI3aVFwWkljSXJLZEFWZ1lYX3A2VHBYZ1BvZEs5aG5zY3pwMlByOWRKbzQ3ZzIyeEVRcl9UUGZlcFl0ZmViUDZvQjBfcHA4Um9HdG5OQkdaN3RkeTh3MjY5Q2x6aXBhby0ybEN0eDBVX2l4aEpKc3NYRm1uaHluLVN6VTh3alE?oc=5) (Thu, 29 Jan 2026 06:00:00 GMT)
- [The stablecoin war: Wall Street vs crypto over the future of money - Financial Times](https://news.google.com/rss/articles/CBMicEFVX3lxTE1FeWhNMkxiZi1UcHUxd25EaEdLRHVqS0hWbkYzVGNkUktCcEhNRXFaVDY0QjlCUmRHeTBmU21jODVGQXFVbkxsOWtxNVB4MWJndU5rLXVTS1F1Y1N1VW1ZOGNpMy05Z1AyNFBaSTZ5RzY?oc=5) (Mon, 02 Feb 2026 05:00:33 GMT)
- [Hong Kong regulator targets March for first stablecoin licences - Reuters](https://news.google.com/rss/articles/CBMingFBVV95cUxQWDNfWnU3Y3B2MWlVNG5rVjR6MlAwVUMyNlc2RkV5V0lvOF9BeWMxeFV3VmhUUDRoZGhIMG9UOXk5SmFBblAxZ2NnZ05ZeEszeXg0Vk5sbmxmbldKdnowUEE2UnNLSkt0dDdkVlM3RjlnTGpfLTlxcGt6cy1pUEZNeTRDU0Z2SnNnS3NsMWdiWVRROThiNDh6dEw3dUo0Zw?oc=5) (Mon, 02 Feb 2026 02:31:47 GMT)

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
