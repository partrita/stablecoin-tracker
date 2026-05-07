# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-07 02:06:20 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$301,575,339,119** | 🟢 +0.16% | 🟢 +0.80% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Is Stablecoin Reward Clarity Under The CLARITY Act Altering The Investment Case For Coinbase (COIN)? - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxNbmtuVTRwMWtUMG42c0t4djB3aXFURENUZG4tZWs5Z3J1TGl0LVN1YXVQdVExZnZmQ3R2MHBjT01hVTBVOWpLck9qT1hjNUMtdmdseXhyZS1iaXhBWF9YSHBfSXVXckt5R2RxM2FsQVhxTktJMGdzNmg1bEtJRDQzREJrWVRZVW9oaUhBN3JZUnNDTlV6eU9VZi1rQjJaVXVzaFVocm1kTQ?oc=5) (Wed, 06 May 2026 19:27:09 GMT)
- [Banks, crypto firms battle over stablecoin yield - Banking Dive](https://news.google.com/rss/articles/CBMiswFBVV95cUxPRG1JVmlMa1Y5MG1BMUdSMjEtQmdEcTFJcUVVLVZQTWJqVTlnTjZSbG9ONTg1VDl2U0UzWXBDOWk5eHBrYV9zN2JsYkVUMHpIdDZOdnk4aDZaX2VHeU4zTUZKWXJadWYySVFFajB4czlubmtPOF9LSDU0aVBVdkRudDY5RVpoN01nRzkxdlNxRzc2V3hDNW5qVHBZcG5sVjBteElNOGlSeEZONG85Z3ZtMDdvZw?oc=5) (Wed, 06 May 2026 16:34:09 GMT)
- [&#x27;Clarity Act will pass this summer&#x27;: Coinbase CLO Grewal backs stablecoin compromise, urges banks to accept deal - The Block](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPeHczTGU5SnBjbzFDUV9iOGRjM1pOdkpKcWhKdXlXWVpGY1BsOWNoSlBLU0tIM041NDExYWZsTFBwSXBqZWVDNHNMQlNuNmVGdk1SSzhuazhZRXJXeHY1SzFlY2c0OVMzTlotMlNFaGVzQ0QwNzlVLU12ZDZoR2xDbHhMa0VfOFJzLUdtWjhSdWxLU3VMRk9KYTNzODcxOFgzNlZJTXh0TnQwV0Z0YlBjclNRVFBVRXdWOWlQT0g2VzFxXzY3eXQyYVdtUTNncWhvTXFIejRWNDVkRERI?oc=5) (Wed, 06 May 2026 14:46:59 GMT)
- [Stablecoin yield debate central in GENIUS rule comments; SEC backs Trump&#x27;s idea of allowing semi-annual earnings reports; and more in Bankers&#x27; Hours - LinkedIn](https://news.google.com/rss/articles/CBMimAFBVV95cUxNMzdnRDNIeV80Rnd6cmNGT01aTE5rUW5aUXdSQlowMDdtVkZ2RVNreEhJVkg0VFB5RzNpdVVFcGJyRFdGemtuT1hWb0YxZ3I4cGpZanU1NkFYazFpcXdESzNQY0R1VGh6Qk10b1RBZWxEcFBWMldwN05qMDQ1a2NHOUxlMzJyU0F3Ri1yN0NVaFRiQ2VLdW5XbQ?oc=5) (Wed, 06 May 2026 14:00:16 GMT)
- [OpenTrade raises $17M to expand stablecoin yield infrastructure after topping $200M TVL - The Block](https://news.google.com/rss/articles/CBMivgFBVV95cUxOMUo3d1Q4a3Q1d0tJTmFJaE1WaHp2QlVhWUFrbW5xWTBlWjlWbU5UOXY5bTZPMEg5aTdLdm82ZDFpeTVsQ1FudjlHNUNjTXlzOE5xbEpWX1lsc0lqOE1RRFg1TDVTZTZrWXVFWmJTYkJ4TUVmSzhvYzdENEtOMnZkTnZnWTkxSHpsNFo4SXVIWWFNaF9uOGFESjIzYWszbkRHQm5kaG5oZ3p4SkVuenZ6REtySC1pVWdFMFVEQzJR?oc=5) (Wed, 06 May 2026 13:00:00 GMT)

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
