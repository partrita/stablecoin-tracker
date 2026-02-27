# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-27 01:17:11 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,019,931,878** | 🔴 -0.00% | 🟢 +0.40% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Federal Bank Regulator Moves to Restrict US Stablecoin Rewards - Bloomberg.com](https://news.google.com/rss/articles/CBMiswFBVV95cUxNY0g3UF9HSXdlTjM3SG9MVlk2UXBJc213Y1RhdkJ6ZUg3REpmcG5IRl8ydTdqZ0dxTDhGZkhfUUdyem5aVUlmdC1NTC1oNkhLazRLbHZxYmVkVW5CeTlDX0V1UWVGV29kSnJpbm9HSW9GVmZRS1FQbkFjM1hGT3dBYS1qZXJIaHEtYzltXzNTTkI0UkZPNV9HY2MyaTVKcHVfZmdQWWhyRm56OEtseVZfWllCcw?oc=5) (Thu, 26 Feb 2026 22:46:30 GMT)
- [U.S. regulator's GENIUS pitch puts dark cloud over crypto sector's stablecoin model - CoinDesk](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNSFpXbUpxX0JEc3pId1ZEMFczNmZ3d2I1SWVkSVpqLURiTXlfam5LWGd1Qzc2cm1kU2o3OEVPNXgwWV9mSHRfT3ZlV3g0QXdjSVJUSTdMdGZ3ckM3RzdhTUZDcEJjem0zSEYzZjR1bUF4Z2pOVVBkU3daeGk0NGJkS09Id2xOelA5VEljU3gwblZEeXBGSGFhV1cwbTJWUGU1SEVfczI1cFViY0QtemlGUU5NVXV5eHE1ZTgySW55bURyblE?oc=5) (Thu, 26 Feb 2026 22:03:19 GMT)
- [OCC Issues Proposed Rules for Stablecoin Activity Under the GENIUS Act - PYMNTS.com](https://news.google.com/rss/articles/CBMipwFBVV95cUxNTEwzOTJ4d0RyS0VBMjNKdU0tSkppUnlsam91OTJqa2F2QkJwakNNZHdMTHdVU2dwOHNxU3h1Nm9NTEd5MVpQZ3d5RTJCcXBCbXIxcGROclNPcnlxSVUxQThBQnhJcDhsVklRNk0wTURHeF9zdWxweHV6WTdOX0szUTNSc1BMN3FqSS1jRXdLZ1l4LURxVUNBV3V5VmFUZmFlZmFPMFpQbw?oc=5) (Thu, 26 Feb 2026 20:44:08 GMT)
- [US lawmakers revisit stablecoin yields amid deposit flight concerns - The Block](https://news.google.com/rss/articles/CBMinwFBVV95cUxQNnZfZl9tUGowdDhqNmlrN1dUbjJpU0tibUNwaGF4RGR2RGhLMkQwOW9nRklsQ1NELTI5RFJUcHdiNzVTaThHVWZNS281X1RWSENVbTZnbjFZSUV1TGJqQWs1VWUybEFnaS1ZS3Z0WGZjUC1tT2J5a1E0WGIzREV2cXBFNi1zNm1JcENYM0VvbjNKWlRrdmJ0by14cE1OeHc?oc=5) (Thu, 26 Feb 2026 20:18:28 GMT)
- [OCC proposes comprehensive stablecoin framework - American Banker](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPeDRaUmFobGEySkhfSFlCaVVIVzVTNnpKV09sbDRvRzV6YjZUS3k3SXJRZW1WS21ScTdvUXlVTEdMSVFObm9DSE92elZlSFlCUjZoLXhNWUx4bElJZk1PckhKbkJnT1ltMVpsZS1JUi1ad3hMYXdOQVBkcWtPMldEQVlqNzhMZFp0aHRv?oc=5) (Thu, 26 Feb 2026 20:00:00 GMT)

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
