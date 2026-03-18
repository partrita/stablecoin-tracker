# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-18 01:24:46 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$298,882,559,060** | 🟢 +0.11% | 🟢 +0.42% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Mastercard to acquire stablecoin firm BVNK in up to $1.8B deal - Anadolu Ajansı](https://news.google.com/rss/articles/CBMiowFBVV95cUxPcHJZSkQ4UnZ4X2tWTmNNbmVpMExQNDR5N1lvR0NHOTRYVFlFc0ZVUndINklrVF9ZSEtzaG9YRS1BTGZXaXBNZWxJOTdGcGc2N3QzaVBmRVIyU052VXdFWDRxNC1DM2NXQjlkZ0NmWWNDR3VSbXpobEVWLXJwaHdkUGliS0RXekNMOUtaa0xRaU1KR0JHcTBwZTBkTldEaVEwdjRv?oc=5) (Tue, 17 Mar 2026 22:32:15 GMT)
- [Will PayPal’s (PYPL) Global PYUSD Stablecoin Push Recast Its Role in Digital Commerce? - Yahoo Finance](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPSDI2QW1vMHZELTRocnZER2pMbnpzeHBnVVRHOG5jQmQ4NW1hRlQ2V0NFZlNHY2pCLW1ycnRiSUdQT3JFYkl4cTU1OU90OC1Nb3d1UWxKcGRuU3BVTjJjVVhXSHRmaVJmZ2lFWlRfY2lOZFVvWDd2ZlFtTkxnLXN0VFc0TDZ4czNn?oc=5) (Tue, 17 Mar 2026 21:11:42 GMT)
- [How Visa’s Stablecoin and AI Push Could Reshape the Investment Case for Visa (V) Investors - Yahoo Finance](https://news.google.com/rss/articles/CBMigAFBVV95cUxObUNfaWRIYmh3aUgzNmN1Y1JjQVV2YjNORGdaNVJZaVFOa3V1Qy1LS3RfdTRORVVfejZOUGVmVjVGa20zSGhBOTlDUk1uYzM3c1RDaWpMMEdXVTU3RE54eG1DZTdvT1l1d1czVFB3S3JkNVZGaVNVWXl2cm5tTGR4Vw?oc=5) (Tue, 17 Mar 2026 21:09:28 GMT)
- [Mastercard Acquires Stablecoin Infrastructure BVNK for $1.8 Billion - Finovate](https://news.google.com/rss/articles/CBMikgFBVV95cUxPLU1hODBvSEJ2VU1EcDA3YmswNGFta0RJNmQ4bTBsM2NkUTRMTW8tVFNhWEhVbU9mMkxYSkxGYTF6Q0pkemR6T1BmM3JWWWUydEdUam1jT0NkSFFXSzBFYmg0M2Q0Ym94V2IwVWVKX0lUblBYczZVcVB6OGtiVXNIVzFRUVF6anloNXRPN3RmbU9Edw?oc=5) (Tue, 17 Mar 2026 19:56:43 GMT)
- [PayPal Scales PYUSD Stablecoin to Reach 70 Countries - PYMNTS.com](https://news.google.com/rss/articles/CBMinAFBVV95cUxOOGctUDg5d2F6YlVIY0d5dkotMl9ZQkZhV2UwY2ZLb1BwWWFwZjVyQk9SMzZ2S0o5Y0k0REZkUmF5Qm9jc3BmR21EdWRqSE1NWG1ER1ByOUo3WlRJVnVSc2hQMlVYVlhLaENWQW0wV3BOTnc5QTZYSjFyRURqUG0ycFdZUkF2VmZCX3BxZUlUOXJ2Tkk2R2NHUlM3MHQ?oc=5) (Tue, 17 Mar 2026 19:32:37 GMT)

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
