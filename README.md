# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-02 01:19:40 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,076,160,613** | 🔴 -0.01% | 🟢 +0.27% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [The 'stablecoin sandwich' is dead: Why the next phase of crypto payments is all about the user relationship - CoinDesk](https://news.google.com/rss/articles/CBMinwFBVV95cUxNczBfMXBsNkp0RXp1a0NSTUlyT3d6OXlZaGx0b2x2Zy14cXE1Qkd6YXZJZWNpTkMySl9BUDl1WnN0QUJvZ3BuNXNXYmE4TlhvWHRRY2JHNFBNTUpxa3EtZ1F6M3J4eWlSdS13WktESkdyN1NaTE9vcW5rUi0xUHA3NFN4UV8tRTRRbTBOV28wLVpXV0JGMjVrMDc2VzBleEU?oc=5) (Sat, 28 Feb 2026 18:03:04 GMT)
- [Visa, Mastercard Aren't The Real Casualties In Citrini's AI-Stablecoin Scenario - Yahoo Finance](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNdzI1ZmdZN2lmWFpWVnExSXN3ejdMRG1saGh4SFV6am9xbmhsTTlmNXFvZXNjRjliTVNGYjJ4MjRJQk9mZ1B6Y0dFVXQyYjBjbXNWMC1TNHJxZjZaSmZEaTdqZ21pSnZXXzBaRnlCaFM4Wks4SDFVdDh0TGhYQ0I5d3Nvb0FHRXRwV0E4?oc=5) (Sat, 28 Feb 2026 13:31:13 GMT)
- [Stablecoin Disintermediation - Federal Reserve Bank of New York](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5kZC1PZFN4MW9FTzlwa0hkUkNVZzlWS1cxcGhnTUVURWROR1M0VW1Ub1FDeVpPWW1JY0xlWnNYSzZVYmw3WEVwOEFVLWhPTFVackNwb2Z0M2Y3SDNoYU5YTFhoN3BSNlk?oc=5) (Sat, 28 Feb 2026 12:00:42 GMT)
- [OCC Proposes Stablecoin Issuer Regulation, Finalizes Rule on National Trust Banks Authority - Davis Wright Tremaine](https://news.google.com/rss/articles/CBMisgFBVV95cUxOMHBaRDFfeG5qYzJCdE1WZjVtSmFJU1dyNmVpT0FlQng5aXZCd2o0bWlabDNMdTdxM1ZUM01CUVFIQTBfSkY3S1IwYXVqQlgzSy02U3Bzdl9mYW0tNVZMbWRTdERsMG90Wnl0c3NNWEZtWVo2SkFLUEkyQ0tub2twYUtQSmNhR0F6ai1tM1UxY2tqRVZaMlRvUlhPbHlHVGEzcUNxdmE3cEthdGZnY0RObThn?oc=5) (Sat, 28 Feb 2026 09:44:09 GMT)
- [Tether says it has frozen $4.2 billion of its stablecoin over crime links - The Mighty 790 KFGO](https://news.google.com/rss/articles/CBMiowFBVV95cUxPOXNTeWc0Unl6NS1SRHpzOExaYkd0WGdmYnBUa3lySGU5dTlGQUNRYXpzaExuUWRpTF85UWNSaDY3VjlBZEFZUEVZVERrbm9Hd0FOVVd5NG43THNsVGhOUnh6QXl3UUQ0YXFnMXp0Ynh4bXFhMWJJRFlhaFJQcWdrTE53MkpuZnZMRC1rNTBHR3Y1Uzl4U1NMSG9jcFNQSXQ5TTA0?oc=5) (Sat, 28 Feb 2026 07:38:39 GMT)

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
