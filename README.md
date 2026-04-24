# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-24 00:00:22 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,317,556,471** | 🔴 -49.98% | 🔴 -49.93% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [FASB Wants Companies to Reveal Stablecoin Holdings - PYMNTS.com](https://news.google.com/rss/articles/CBMimgFBVV95cUxOeEVfTHR5SVZFTUVGaV9nSkt5cjJsTXAxSWdrUEZmQmZhTk9qWmhSM2Uwa2M1T3BmZ3pZeTFnRDgyZXNZUXhIbXh4aXZJVXNOeHF2VFUtRDNTeHdQa0YwSDZiMC1zcVBKQVhpcmZrb1Z5bUJHakRsX1NIeUhFdzRKcWxReDQwQ2RvVjNPSkpMWFU0c3NWNUpMX0Zn?oc=5) (Thu, 23 Apr 2026 20:47:34 GMT)
- [DoorDash Tests Stablecoin Payouts To Reshape Gig Worker Economics - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQTXVsaHQ0d3QweW9jbDFrdDJLeXY3M0FvTF9vM2dLQW1KeHp6YXRtUXNWdVh4MmpiMUhFeS0xRnZKY3Fsb2tSRXpOZFlCdmNrYUg3Yi1OYXZPSmpQWDV4U1NWRlJCSHlhYnFwcGRwal9GOHc3TGNUR296YVMxRG9qN1pXNGdJalhhMDkyZkdJTHZUYzh0cHB3MFFpWnpqZ3QyQ2Q4NDA3eGdIUQ?oc=5) (Thu, 23 Apr 2026 19:03:43 GMT)
- [BaaS provider Coastal Bank partners Tempo for cross border stablecoin payments - ledgerinsights.com](https://news.google.com/rss/articles/CBMirwFBVV95cUxQR3JmMjM4anZxVVJQV2g3eEVKa2t4ZTc0b1lGaV9YVHByTFNjNzBNSXMzNnMyb1otS3QzUXNncWpLVnZJTzFNTjNfbEZXc2FEVE9vRDZGbWdEZnhnR1Z2Nkdjbl9oZUhnV25qQ2IxRVZaTFJsZ2Q4TDVnNFQ5UU9CdUZUM1gwNUZDektrdVYwNTZ3RVI1N1lPeXp2aEZpVG1sU1piWTkwVV84SlMySGpZ?oc=5) (Thu, 23 Apr 2026 17:43:13 GMT)
- [Scott Melker dives into the stablecoin takeover - Yahoo Finance](https://news.google.com/rss/articles/CBMimgFBVV95cUxNOUc3dWxDcEQyZzk2SHZBQV9uR0VGNGd2UzlqUVZ4NVF6Vk9xMTVONm0wSkxOSU9KSngzMzdQWGVhWDZ1QWhjdnA1TGNmRlEyWDVub1lvU3VsZlpHVVU4UDFfQTEtX1g4UE1UMmdrcHdrZ2xMYXZPeERVTENTNWxNbnppRVcwU1VQckZQU1p4Q1oyem1QYjZlMWNB?oc=5) (Thu, 23 Apr 2026 17:39:21 GMT)
- [Stablecoin takeover: Why banks are fighting the GENIUS Act - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxPNnhIRmhET1N1Vzh5V3JyTmxKX0YtaG9KZ1liNE1hMDNvNU9taHQtWDVTVmg1TF9pVlNxNHNkeEtmcHB3M3J3NWtraG5yUTNfYm9HTFZtUVh4alU2U20xV2gwT0UwZThwMkgxbFJZNE9GM0ZRNl9jNVk2VnRhVWQ1OVRtNEtid2tKUDNKZ2NJcERORC1JaVJnMDJnWThsRzJTa3FxNWtXcw?oc=5) (Thu, 23 Apr 2026 16:44:57 GMT)

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
