# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-24 07:44:11 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$271,650,355,208** | 🟢 +0.23% | 🔴 -1.11% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Korean banks set to lead stablecoin issuance under proposed digital asset rules - Korea JoongAng Daily](https://news.google.com/rss/articles/CBMizAFBVV95cUxNUWc0SlJPVGp0b3BBNk5nYlJRTjRQMU1KdE1rdWpPR2Eyd1NDU204NGIzaDNhanFKNjNPNE1uS3hFR2p1X2VuRFF0MVNxVXFfczk0REVZZHJsOXRDU0hsYlp0OEhwQTJCUzF1TjBpamtFdWxZaTJsY21oYmNaVElPNjl5ajRXRjJsaWxraFRYZzJROERDY3ltNnA4YWhIRXBkQmVxRGFLSWNsSFo5eXdGVUcxOHppbzE3WXhadVFUYkNWLVpJa1hVd1pxa24?oc=5) (Tue, 24 Nov 2026 07:18:45 GMT)
- [BlackRock taps Hong Kong stablecoins for new money market fund - South China Morning Post](https://news.google.com/rss/articles/CBMivAFBVV95cUxNMzl6ekJwNy0zUVBrekEwVWZIRkl6Q3lBTmQ5S2tkLUZ6NHdSS0ZnQjVqb0pvdG5xV1F4WGFoRzJGeTJ3b2JKR21VbWF2ZnQ1VTB2aDhBMEJLSFhWcGlibm0xaDlUaG1hdnBiUGZCM2gxcnNvVG5LV1JrZDMxbmlrNmRiVXJsQzZGbzNTRmdEZU9tSGRTYWpMQW1FTVpQWW1ERkp6TGtVNElHTF9tbU1LSmhDbVU5OC1jMFpJRw?oc=5) (Tue, 24 Nov 2026 06:07:29 GMT)
- [TOK27: Tokenisation, Stablecoins and the Future of Global Markets - Mayer Brown](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPUXlXekVIamNYM2txMXlrMWlpenJYcGtYNVd2OTZFcUR2Mko4NkxTVGxUdUp4VGRvUF9lY2lFTW9TcFBHVXV0UEM3N0RCei1ZQ2R5czFKWm5Wem9aSDRQN0JiRTVkYTJrcExVY3FacVpRN3cwWUhqSFk5NFlyNG9vYndyYnpGSVFtX0QyRnVpcTUzZldpZThXV1VlNXhYV1BCNFRxSkxncDBhdHhXMHBnT3BzVzg1MWg2?oc=5) (Tue, 24 Nov 2026 02:06:20 GMT)
- [BlackRock Opens Hong Kong Fund to Stablecoin Payments - The Defiant](https://news.google.com/rss/articles/CBMipgFBVV95cUxOTjd5M3lmbHJDcnVJN1N2UmZqbEdUeWNtRHdIOHl6RHhCZHVrYm5lSXItNEZZQWVIS0hWVXZzRmxmLVhsc3JWelVFSmxkcWZfdXo1UWh3NS0xeko3ME01Vnl4dHp3T21KblVQU2NoTUstdWNBblBqTGJTczlrb2JMdm80aUtGMEJReHlOZDlXWTJDbEJHQmhlSzBkWE1pMDZPUkZCRll3?oc=5) (Tue, 24 Nov 2026 00:35:39 GMT)
- [Payoneer Gets OCC Green Light For Stablecoin Trust Bank - Law360](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNQk9YNklBc213OEoyVGRPX2czTjR3anJIZzZlb095M0NTUWZCWUhtLXQ5QVpjY0szUVM1dFJtR2prTTRHZVhYSDJCaWx6TkFlVXEtZGRwWUw0NjJvZVZGNGIydE9fb3E5TGtNanZqUGlXdmxUOExCUkpyRUl3Y1JnTlQ3MjVVQ0hwcm1lYkxVUWFNWTl1TWZsM3Q3ZlB3SFZKc0pvcmg3NnAwSG1JaldGa0pCb2VLNUM3R1F5Wmw0SGLSAVZBVV95cUxOaTVhWjVKUXlIU1NyWHo2X0I4dFZCUXRScndNeElXVkpmZzZwTHBFLXhBT3h5S2JDb2Y2U2xmby1NM1pacWhiUG9najJmWklOYnRtMWxqQQ?oc=5) (Mon, 23 Nov 2026 23:31:50 GMT)

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
