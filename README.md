# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-20 00:43:47 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,993,855,551** | 🟢 +0.09% | 🟢 +0.06% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [As Crypto Spending Surges, Credit Unions Face New Payments Question - CUToday](https://news.google.com/rss/articles/CBMipgFBVV95cUxPY1dBYXFCb2V1Yy1Kbjc0V3BILWtVOTROMkFxZ3Q2NDJFT2hxV0p0TUZxUk10ZENUM2RYcnN2SEw2R0VGRDUtY09tWXZXLVBQZUZvbWlCdVAzckRwTTQxWnIxLVE5TkgxeE1xR053Y2Vkb2xRODR6ZDFVQ01kOFQ4OHpsTG50enRIWVo3MnN3UDBENlVXdHFmQ0tYN0h4R2tnQlJFcTlR?oc=5) (Wed, 19 Aug 2026 22:41:14 GMT)
- [OCC Advancing Stablecoin Rule At &#x27;Great Speed,&#x27; Gould Says - Law360](https://news.google.com/rss/articles/CBMipgFBVV95cUxOSUhPVmM4d1E5ekJhdnlfb0xIZFdqUG1iUFlaYnZPUTE3VWxmaXBxbzJVTHg2QndlQTgyYjk5MXVfcnppZnhBdTljeGljdHBvenpFeGVwcGhHaGNVQTlrbUhnelFzWks4NHNCVW9FZ2NsUXdJZU82aHBpeFk3bUw5S0QtekVMTjFpZWFIcy1sVDhQc0o2QkEyZmg3d3o1RTh4TllFVkR30gFWQVVfeXFMTXR5dkNIOHpZV0xUZ3Q5NGZsTmRIWmUyckRZbDZQTGJmOUtseXBwYVp3Y3FHb1d2WUlDZmlnY0NKRjJ3bzF5ZzFYX1p3d3Y0dnA3SHRPc1E?oc=5) (Wed, 19 Aug 2026 22:15:00 GMT)
- [Self and USA₮ Launch First Regulated U.S. Stablecoin Distribution to Verified Humans on Celo - FF News](https://news.google.com/rss/articles/CBMiswFBVV95cUxNSXdhRi1QWG5tV1gzd0JqOG5fdk9meW5JTzRSWGYyU0dJS3pTRDI1blU0LTVKbzdtQlhieHJCZ21xTHItZ2ZTbnNrT1FUUjdNbklIaVpuaHV0dDJ1cXBRVGprQjRiTkI0anczNmVBZ3lGeVFEZU1rdy1VOXFLQmxGZVFXX2xhR2xKQTdpSTE5UWFCU3hpT1Zvam50TGg1S0tCLTk3Q2hWUHpBMkVnTzVRbVZhNA?oc=5) (Wed, 19 Aug 2026 21:44:44 GMT)
- [US OCC to adopt stablecoin rule carrying out GENIUS Act by November, Gould says - mlex.com](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBrd3BCMlBVZUFMaGtBRGExQXIyOW9aMFhNWXlhcFNPQ1kzOXNFeGJEeTI4UFFpWTl5VTBFbk5rVS1IYzNSdXhnOWcyUmtkbVd6UEQ1MFU4TUVyd9IBWkFVX3lxTFBrd3BCMlBVZUFMaGtBRGExQXIyOW9aMFhNWXlhcFNPQ1kzOXNFeGJEeTI4UFFpWTl5VTBFbk5rVS1IYzNSdXhnOWcyUmtkbVd6UEQ1MFU4TUVydw?oc=5) (Wed, 19 Aug 2026 21:06:00 GMT)
- [6 Risk Areas Future Fla. Stablecoin Issuers Should Plan For - Law360](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1Ca0p1QVBnNVRYbkg1U2ZWZnhyTEJKX29udFpKbzhQQm9qVXFaOVFiWGR4bHdLellfTEpzeC1RaE9kN1U0cDRYdUxOaDZTWHI1Z2VtNDRn0gFWQVVfeXFMTUJrSnVBUGc1VFhuSDVTZlZmeHJMQkpfb250WkpvOFBCb2pVcVo5UWJYZHhsd0t6WV9MSnN4LVFoT2Q3VTRwNFh1TE5oNlNYcjVnZW00NGc?oc=5) (Wed, 19 Aug 2026 21:00:00 GMT)

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
