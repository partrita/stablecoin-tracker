# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-11 01:26:35 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$298,393,679,889** | 🔴 -49.94% | 🟢 +0.35% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [The US Operationalized Stablecoins This Week, But Who’s Using Them? - PYMNTS.com](https://news.google.com/rss/articles/CBMipwFBVV95cUxQU3A0ZnhHblVidWJ2S3lYVDFmU3ZXYWlEdXJRYmE4RzZ4azJFTjdMcTJtNlQ1UTZZSFN1QjZYWnR6d2pXZ0dLWDN0aUduZ1FaTWpzOTlfdFVISXVjRll1aGpGOGtoYlBPWTFBak9EUmRvTy0wWWlOZEtJNGF1ekd4VVlmLTFPSHZtQ1NjbUhRM2JrMFYxSl93MTA5VXQ0bmpqZVJLSlp3UQ?oc=5) (Fri, 10 Apr 2026 22:45:22 GMT)
- [What Are Stablecoins Used for Today? Estimating the Distribution of Stablecoins - kansascityfed.org](https://news.google.com/rss/articles/CBMi6AFBVV95cUxOaHcybkF3VkNrZTkyQ25DbkdtSmlMZjFQdTVjUHBCakJkZjJiSy1WemFlWDVtUTF0U1FfTnpOSG45UmZldFJ0MjhRRkc1YWpwQkZKMzlrdGVLT3ZEMXBjbnJXZERzT3VpWC1rWGJHa0hnX0RsT0ZrOHVBeVd6UHZDRGlwVlF3Y1hpU2lmZ1l0T1lpSEdYTW56MUNHb2JqNnI3V2dBQ19kYjdPTXFTeXpMRjBWamd2bjVxQktIUFFTeGlGamxobGxZX0M1Y2xmbHJORjJITWZWTURPQXRTODV6c3Q3VDlnUXps?oc=5) (Fri, 10 Apr 2026 22:29:13 GMT)
- [FDIC moves to regulate stablecoin issuers under the GENIUS Act - MSN](https://news.google.com/rss/articles/CBMitAFBVV95cUxQVnllYndYTkxfcVFsM2hxV0todWhzZWJGTlg0Y0tKRlhUb01DNGd1QnpDRm1VNUxGWG0xYjRHYzhER0s4WmhvSGdnWjJaOGZLMGVFWUF1dnMtVDRfa3FpMWY3cmNTcUlYRDhkNndjWUZhZ3MwLVU0bnozdVA3eVBKc3pUc2FTSnBKb0x1ZFV4SHktcjJpWXJjUFlrT0t5YTFrVzdkZmc4YmtIZmZDZmpCTW1JTmY?oc=5) (Fri, 10 Apr 2026 19:49:36 GMT)
- [The Stack - Grayscale](https://news.google.com/rss/articles/CBMijAFBVV95cUxQQnpRRGZ0LWJxaHp1U2pxRlFaNmtLWlRJR0U2aE5wdzhrZmxsWUdHTWE1Y3QyMDdUcG9sbHp4bFhtLXR2V0pLZGgzR0F0Y3NMdVV3MEtBbjNfRld0aVYzQnFiQUs5NXFQbnF3Sk1aM3kxODlfa3Vua0UzV0F5MndyOW41M1VxOGFnbVpJNA?oc=5) (Fri, 10 Apr 2026 15:09:31 GMT)
- [Can Visa&#x27;s OwlTing Partnership Accelerate Stablecoin Adoption? - Zacks Investment Research](https://news.google.com/rss/articles/CBMiowFBVV95cUxObEtMY3YxeHZpNzdtd24yTV9QVDlTZFI0aEpGSGYyNUFJb0Z3M1NOeVVyS0dFSU1uYkc2QTJKdmNDeUFqb21CQjFtaGZRbWtqd1YtclZla3lDeWlWaXI1dXgwRzZOZC1maG8xVnViOC1QZWg0TU54UTZ5aWNQVTZkVmZMUlljQm54Yzc5bGhkZzJMaTZLZ1RSWU0yMW5TNlBIVk80?oc=5) (Fri, 10 Apr 2026 15:05:21 GMT)

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
