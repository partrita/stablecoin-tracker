# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-17 02:38:53 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,167,428,556** | 🔴 -0.04% | 🔴 -0.29% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Solana gets the default spot for stablecoins at FDIC-insured bank - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMijgFBVV95cUxPaTlZUV9nbHlyQzkwUlpLcnNNeXB2UF93WV81YXE3d1BWUEh6TC1SWWVPeG53eV91X0x2TlUxem1mVVllTmxIZ19PSUFfOWVOY3lNdjh4REdWU25rWUlHOC1wRFlrZ01sV2pWWjJvaU9aSWIzT2VIbWppTWtLa0FvR3ZIZU5XSVF5T0RhbU1B?oc=5) (Thu, 17 Sep 2026 00:53:00 GMT)
- [UK Tells Crypto Firms Who Needs a License as Treasury Moves to Exempt UK Stablecoin Payments - unchainedcrypto.com](https://news.google.com/rss/articles/CBMivgFBVV95cUxPR0hVdjhXdXJoTkFVMXR5Sktlc2VqdXgzdXhNRUJ0WDhvMU4zRVBZUk1wUVJDZl9YbEVxT1hLQXpHd0s4b1VSNmZrWXhxdDZfVXo3bDZTTlhxR0ZhVXI0ekt0aDVrUVRNWUtsa1Q1dFBLN0RwMlFMWERINS1aMkdiaUZqUm9VQVRkMlJGZk56b2VPZmtGbXF4QnkzNTdtMTRLNW85LUpGdWhrWGwyaXM3dnpscE9nMkUwaTlBMk9n?oc=5) (Thu, 17 Sep 2026 00:42:00 GMT)
- [Stablecoins vs Traditional Banking - The Block](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNWjRUd1lfYkxLUWp5LTFYdFVzY2ZqSFdpSERqeUNmUS1Vd3ZLTHVEMlZodVdkNDNIWGtzYkpKYjBKV21FbW83azZkSjNqR1BjTzc0TW9TNU1Cb3UwbUtUNTV0blFXMGpXZVQ3a2RRM0M0SnY3U1VZeC1tNm9vMkdaWEVOV3VIdDdOZmtv?oc=5) (Wed, 16 Sep 2026 23:26:01 GMT)
- [How Do Stablecoins Maintain Their Peg? - The Block](https://news.google.com/rss/articles/CBMijwFBVV95cUxQQ0lPa0VPVUU5ZE9mbkhhN1lfWFktczcwSncwUFhCb2paTTl5SXF2VHdlOFFldm5IejNqOENHLUl3WHpwSWpaLWV5M2ZYT3MtYjVPZ2psdGFvRzlZVkRUczFrZ2lXT0dtNGh6R0d2ZjFpQ0U2d1B6Y2lwN1lZUTdia1UtX1lTbm1rS2VfMVhBYw?oc=5) (Wed, 16 Sep 2026 23:26:01 GMT)
- [What Is RLUSD? Ripple&#x27;s XRP-Native Stablecoin Explained - The Block](https://news.google.com/rss/articles/CBMib0FVX3lxTE1SVUlBVmhxdVgwbHQycXdXT2xsd3F3azBCbDM1R3lJbTcxS1NnX2NnRFRyNkl3c1UxWmpadzU0LUlzNWw4QkgxdzJwYk9nTWhEOUNnSS1PTnNnOUlMdjY4T0NmQjh6c2dzUXQtNklWaw?oc=5) (Wed, 16 Sep 2026 22:56:59 GMT)

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
