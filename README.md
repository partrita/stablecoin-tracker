# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-03 02:55:52 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,324,631,269** | 🔴 -0.07% | 🔴 -0.97% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Rigid stablecoin reserve rules can increase default risk, BIS paper finds - ledgerinsights.com](https://news.google.com/rss/articles/CBMipwFBVV95cUxQVFFrd1dEd2JyUU1RbVVKNmVLMUZtWXV1bml3aFFEWldfNUp4QkdfREdaWlhoaGpsdDJwd2FBRDB1NkhIYWI1WmRZTUptd3FoRVlCS2EyVFhhTGd0MXZYU1VLX1Bpcy1ObWd6RmViN1F3eUxPNkxEdlNodlFhclN0OXp3bEtfN0RFamZvNXBWMHVaOVBDOUpuMTJacHZSZ2thZksyaUNKaw?oc=5) (Wed, 03 Jun 2026 00:31:20 GMT)
- [Lords committee urges looser UK stablecoin regime - TheBanker.com](https://news.google.com/rss/articles/CBMiekFVX3lxTE94ZUpZR0JudTEwZTZBMG9GZzJ3aklUQ2psZDU4WkFYazE1XzY5LXNSSjdabXlCYi04ZkxjMUwwSnNzbXBiOHJ3aTFzRnV5OVEtQ2RIQzFFVFdpMXlWU0VfSEtiS2gzYVFBbmd1NExrRkdCbVJZdm5jeGlB?oc=5) (Wed, 03 Jun 2026 00:09:23 GMT)
- [Bank of England faces calls from UK lawmakers to ease stablecoin plans - Reuters](https://news.google.com/rss/articles/CBMisgFBVV95cUxQYW50VU96bkRsQWRkS1gtdnBySjB0SkhaYi1MdUowQ1VneW5GS010elNfQ00zYmNuNjcwOXlnZEdTU1YxUHNjdmU4Sl85T0tYQWptTS02eXhxMW9Kelc3T2VCamVFTC1LLTZpbUVxcGhrQ08wOEROZkFBSlFwa1VsZGowRGVJMWtySks0U2ZvVHZFNTQ0OUVTM0lqb2NhczI2UEdGVkR6dFJEekN3Vk1RcDNB?oc=5) (Tue, 02 Jun 2026 23:12:12 GMT)
- [Financial Services Regulation Committee publishes report on regulation of stablecoins - UK Parliament](https://news.google.com/rss/articles/CBMikwJBVV95cUxNXzgzeVVveS16Y2ktZHFnUXJnZ0x0VXJkSjZaN0pUS2lUUzBIZ0ZDNUJ4WlFtZFlVUWFrc3pvTVZFaDFZYm5tenlhZVBvY05jYnVNWFp4SnlsTGI1MTBqTTJXMER5aXBId18tdWRIMUZvSDFyeUlKZW9xQ09aNFdGNTlwZ2c3TTM0ZF9rVF96YXlTQmZ6WU9BZmFkUmlSMFlwTTg1RE0zLUR2eGZlSG9fYzdVOFdaM0puR0VDc2d0cFlURU9EeTBiWHg4VkFBVmZ0SEVibk01RHFtdUdVUm5sN2lLTk96Y0sxTHh4VVRuUy1TYmpwa2VZVzVlc3JuNjU3UUlKTnBFWkRheTMzQVdmTG9BVQ?oc=5) (Tue, 02 Jun 2026 23:08:48 GMT)
- [UK House of Lords committee calls on Bank of England to reconsider proposed stablecoin restrictions - CoinDesk](https://news.google.com/rss/articles/CBMi2gFBVV95cUxOc3hEVTBZaWlSSkpRaHJjbS0tT1pteXNrXzA2TmpPNUNsOHJKVDhJdXRQYjliZGVKTE4wTi1vWHFiVHdqeXVpbGRxNE5hREJ4T211YmVzelBsMklxSjFBZFowUkZYQ2E0ZDh2VDlGbTVYTEpvSkY3aDNCRDFQWGF3YWE5RlU0eDFqMm0wcWE0cGo1WnZ6bUdYWEJkTlh2ZjZweEZFbzV3LVc0dzNfUU9XOFhGZVBQWWVtUGJIbS0waVVQVTBKX3FpWlEwUG5Pc0R1c2hERlpvVVFfZw?oc=5) (Tue, 02 Jun 2026 23:03:08 GMT)

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
