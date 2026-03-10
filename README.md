# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-10 01:15:14 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,135,228,385** | 🟢 +0.33% | 🟢 +1.11% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Fireblocks Named Stablecoin Payments Market Leader by FXC - Fireblocks](https://news.google.com/rss/articles/CBMingFBVV95cUxPNUZmaTVLTWx3YWxySXB0VTRpaWQwckdUVE5EbnZ6Y1Y4UnBoYk41UExPSUl6S1c2VWF0RG5obGRoTmlyd3pRQzZvZVdCWTV3QXhFOUEyUXRCRUJ1M1lUNW13eDNFUjJtQVlxQUJKTjdRUHlEQmZhNThPTFUzU1Qyd3lDQ2hoX19DWGVicWpZWW9sMExYQ3NkY2cxbU9QZw?oc=5) (Mon, 09 Mar 2026 20:31:33 GMT)
- [The FCA Is Building a Sterling Stablecoin Market. The Rules That Kick In When It Succeeds Could Kill It. - FinTech Weekly](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPd3kyZjhEeVdEZ2FqUzMzN2VxMVMyZVFpOVZNaWs3d3BkQ1BfMlNja3lzSDlHRXBRLXZfSUltNFpCSzRxRnZjNFd2MDhmRndqRkJZYmpDMzRDWDdRV1NiaGhodzZHY1RfQUxod3pOZUdpY1BGNU1Mb1Fwb0xzRDh6cDhkX1dhUVQwM2VkRVlXclVBeDg1Y2dyZmhtUVo5cFZxdmdPdUhFeVBGSmc?oc=5) (Mon, 09 Mar 2026 20:17:00 GMT)
- [Mastercard Tests Bank Issued Stablecoin Rail With SoFiUSD Integration - Yahoo Finance](https://news.google.com/rss/articles/CBMijgFBVV95cUxPdkI0NnhmSkp3WE9NbTEybVR6OC00UGJXOXFEMlBsNXNmd2YtT0gtQ0lPNHZCbmg1cFI0bUtqWlg5ZGNGbGtCSXdjOElXX2laVHR0VDRUQldLSnJlTXExa2pXYllUc0U2S01ERy0tbXNMVGR5Y3llMG5hd1VmYmJSemp5WmVjNWFkbE9TRVhR?oc=5) (Mon, 09 Mar 2026 18:12:37 GMT)
- [Aon Announces Stablecoin Insurance Premium Payment Option - Carrier Management](https://news.google.com/rss/articles/CBMibEFVX3lxTFB4UVMtejBtMnJVdzluMHNFZkJ4UDRQR1haaEsySzNsNENITXN6WUpYdVNEeWJXbnJKT1N0MHI5bFhTOC14MWhrMFBFQjdVOHlWclJINjF5X1BZODFrc0VwR2RGaFhIR2hIcnBXdg?oc=5) (Mon, 09 Mar 2026 16:27:25 GMT)
- [Clarity Act stokes debate on crypto - Payments Dive](https://news.google.com/rss/articles/CBMigwFBVV95cUxQaXU1eG11RHRaS3pDb25GQ2liVVBxUG96TVRBZjBxWUw5UkJQWXNRT2RZbTFXMXRCdFhLZmxsYzdGUmV3UzJBazQwdFByLURyV0R5bkVoai0yQURrRnNWWkMwY3hFWmloeDBXUVdJNTBfa0lqbVZuQ2IxcGtUbXh0dm5jZw?oc=5) (Mon, 09 Mar 2026 15:43:55 GMT)

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
