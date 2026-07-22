# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-22 01:51:50 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,252,291,839** | 🔴 -0.05% | 🔴 -0.06% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Britain Wrote The World’s Most Cautious Stablecoin Rules, Three Years Late - Forbes](https://news.google.com/rss/articles/CBMixAFBVV95cUxQSGEzRnRCVmpvcThYTW40bmppZm1VazhJenpfOVJ2SU9EVU8tOXp4bUhFLXlVRzZ5aUlhMVFHaDVSUjBrN25femp1dEtDWTJILV9jMk5rdmJ5WDFWZG5yU0F3TUtfSU9fdzduZExUclBVbFVuY1hhVmxkX0dzc3dsN3BISmxGUi1uWTZ5anpadHB1UmdkOGpubFpwa3Q2elBtWkpXUG1GNzRxQlAtaVIyZkVXSDNkMHJUY3FVemZCVDlieURk?oc=5) (Tue, 21 Jul 2026 21:57:00 GMT)
- [Ramp Opens Stablecoin Accounts and Payments to Customers - CPA Practice Advisor](https://news.google.com/rss/articles/CBMirwFBVV95cUxNNUpxVkdZY3d3SDlQWGhvNDVNeU9GQ2FyZk5WYTJJUlkzQV82b09CV1UyRm9UMzUyblFncEdscDRqMXc5ZmY0Y3FYV2dmNXZ0NVZYRi1vRGVUX3lBcHQwcF9pVzh3V25NSTZ0TzVaTHg2SmxOZzZJcURaTjgtMVRTS1hqdzFLa3NuT1p3NHNMYTJ1cUpkNExkVTA4NFBrSnlXZUNmNDl3OVFpUmNfb2dj?oc=5) (Tue, 21 Jul 2026 20:38:47 GMT)
- [Stablecoin Is the Wrong Weapon in US-China Fight - Bloomberg.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxNRmNNWVdCOUVhUFJjcGZKNEJhd21HN1YxOGxLS21DaGJGTzhhb3pwcFUtcW9xNFU1WG5sWGhPSmhSeHdaR3ZVMjcxSGM2TGNQRUNoV3dPMG9WdTRfVEFMdVhraVBnNjlJN3R6TnROYlRDT01UMEk3b0hxZV9hLWwwcGpaNFVhNkRiSDdhbmhveGZoSG5xb1pkanp3UVl1el95V1o3Yg?oc=5) (Tue, 21 Jul 2026 20:00:20 GMT)
- [Relay Scales Onchain Payments with Less Idle Capital on Circle Gateway - Circle Internet Financial](https://news.google.com/rss/articles/CBMinwFBVV95cUxOOUZwZVhXUkJMOURaNnUtLWhwWlBzdHRTd3RuMDZBb2dCLXRIaUUwLTJTM2M5dk5wVTVYSTNKQ3JjU3JNTENhUk5ERDM0aXZiTVduZHpfdTdQRkFtbjZzelM4a1lEcGM1OTJLSU5IeGhjbklsR1hhQzFLRmJndy1oUmo1eTNjekp6dFhEMW5kSjNPajR4RlNIUDNreTc4VTQ?oc=5) (Tue, 21 Jul 2026 19:45:33 GMT)
- [Zelle Starts Minting New Stablecoin, Eyeing Global Expansion - news.bloombergtax.com](https://news.google.com/rss/articles/CBMivAFBVV95cUxPV0dUaXBBOWhwYlVYaXJJM0RHb0hEZ0kzd0tlU0Jfd1pFTnFWdGZ3dmEzaS16LUZ1akNZZXQ3R21qZkJQM21HTGY5UVd5WUVsVUd2LUYzVXpCVC12VXZtVFREU2gweVRXaTBQUzZlekhCRTdXM3d5YmFNMWJ3ZDFRQ2xXQlJIWnNDdHV1SF9FOTBwbk1DUkF6QndTMnBRRU5PUklBMUNPbUQzR2VHZ2s0c2V6WERqWDRCdks4aA?oc=5) (Tue, 21 Jul 2026 19:40:00 GMT)

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
