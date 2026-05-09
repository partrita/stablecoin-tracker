# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-09 02:06:30 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,196,901,542** | 🔴 -0.43% | 🟢 +0.08% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Yield-Bearing Stablecoins Can Destroy Deposits - Bank Policy Institute](https://news.google.com/rss/articles/CBMicEFVX3lxTFB0TTZ1bTVsS0ZuYzNWVkFDcnlYLURuTkVYc3Fkc1dkN1NYVmZUa2c4dHlndmxUZUVtQ2NDV2UwM2RCb241S3NXNVNaVnZLc190OGNmYlIwOElwS1hLZzN6eG1pME1kdFlOZ2h0dTRZbkg?oc=5) (Fri, 08 May 2026 21:06:00 GMT)
- [Vault: Banks plead for stronger stablecoin restrictions - Punchbowl News](https://news.google.com/rss/articles/CBMigwFBVV95cUxPeWk3dUlmSDAxeFAybkhwRHBId2xDZkRTbm5VUDZDRmJ0Mmd2YTJPYi1lMml3MzMycGNHdDdvNERqekRFZWt6bVE2akdqRG1CS0ZReWdid1Q5eF9VV3YzQXhjWFZ1UTBHMU8tWnJKbWFUYkRCTjV5aGppcVVhckVxQy1kSQ?oc=5) (Fri, 08 May 2026 21:03:30 GMT)
- [Stablecoin Regulatory Clarity: Can Disruptors Be Disrupted? - Seeking Alpha](https://news.google.com/rss/articles/CBMinwFBVV95cUxOZHFla3JYbnVnUjZFa0tNcEFFOFV2QkZzS0tPQlVtYmlmUEo4VTVUOXowM2ZOYmlzVlVJYlFaVUs3eGRyMmRJX2lrYVlPejNKZjlPSlV5c0FhSXA0a1B5MlVQLVZVN25qTl9BUmdxWk5fU1JEYS14cFM1aldVRHJSdnZQRzR2eFdZY1hlT2o3b3dBVFNwQ3lUNXJsYUVFelU?oc=5) (Fri, 08 May 2026 21:03:29 GMT)
- [Banking Trade Groups Urge Senate Banking Leaders to Strengthen Stablecoin Yield Guardrails to Prevent Deposit Flight - Bank Policy Institute](https://news.google.com/rss/articles/CBMizgFBVV95cUxQRzYybTl0dHVDOG53X2FMRWFPMnVxM1VkdkFia2VXYnR5dWlIY2hMbGxldjlYODN2MWZ3anZObnZZZFRyYURfMnhLZmdLMUZiekY1T1VLVmlsTWJMdm1Ranc5ekVJVGNlX2p6RkotZ0NmbHduOEhla202d0lVOHh5R2Fzd3JUbXVaNzdUVnp0LUpJa1UyTUN0MS1QdmtEU1dsRTV4blRZdlJEd3BGRTZwTUVtVnV2anJ5S1dEQU05SWYyVk9UVFJjOXhxVTZ4QQ?oc=5) (Fri, 08 May 2026 20:29:28 GMT)
- [&#x27;Shifted the vibes:&#x27; Stablecoin deal revives crypto bill despite lingering ethics disputes - The Block](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNVmZNb01mTVNSRGFvRjZqUzZVSm91NklyeXlHNURtdC16TFVwWWZjQ3JrM2VsYlM5MHotMDdZMVR4VkNDMlZacFN2REZuQl9RLW5RZGltVHI0cE1DcExCRGZwNV9wcWpweHBrZXJ3Y2k4ZkQxakRBSFhIZUktazRRWVFkT0NGQ1pkT2RyenF3M1lfUm1BUFg3ekRhVUZkXzdIcS1RdUxNQkxHRlBMbXl0ZEJOLUxxRUF1bFhN?oc=5) (Fri, 08 May 2026 20:20:38 GMT)

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
