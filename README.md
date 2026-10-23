# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-23 02:42:57 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$288,239,414,969** | 🔴 -0.22% | 🔴 -0.61% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [HSBC RedCoin stablecoin launches for 3.3 million PayMe users in Hong Kong - South China Morning Post](https://news.google.com/rss/articles/CBMixAFBVV95cUxQSXU3dDdnb1dNLUNITkNUX1NCUlVPUnVzZXNlQ0RDWUJ1Y18tQnZpX1FNampjVXRIelIyLWtmQjE4dHMtWkZ3OGRRdmZVcnJnUUdoUnlxS3NGUzUwdzZ0ZVVGRm1zSWVyQVlrVkRzZTFTbk85Y2RTTkJOVjFvM2o1djdYVklhOURDTzZpSTNScjd4WEM0MWhWZ2xXMjlTWmpldl9Fd3llazl5bVJ3SE5VM2h4aVdMNFI4aGRjSFNsd1djUWQz?oc=5) (Thu, 22 Oct 2026 23:00:09 GMT)
- [Mastercard (MA) Introduced A Stablecoin Security API - Yahoo Finance](https://news.google.com/rss/articles/CBMirgFBVV95cUxQUVlsQ1Jvb2oyVEhwN1NKRjBfZVlITzRWUlpIcE1VMXRTRDNNem51dFpuSGl5UFRTc1lUMFBuclY1S09MZEk2LWp1WjRRNDY3VkdFMzFoR0RyWWJpT3pRQnJoSk8zRzVOQkdHVm8xOG52YmVwemU0d3RKTnYycXR0QjJlZEZFemd5blZlWjRNeVM3eHFRcUhpZXVrbTc2elY2cHJpZzljNzQ5UGlPRWc?oc=5) (Thu, 22 Oct 2026 21:13:03 GMT)
- [Crypto for Advisors: Stablecoins are ready for prime time - CoinDesk](https://news.google.com/rss/articles/CBMirgFBVV95cUxQdmlxc2lzSDEwUGxEZXdzeFk0Q3ZMTXY0bjhieUx2a2xGQllrNXZSUXZaSU93emlaSkFNcnlFMjQyeTlOZWpOemlKeEYtWUpFdHhTZVZNRUpkdTA5QWs4NVZuZXBGcGZEMmlDa0Z2eHNGUklEaXl5eWNvbC1KWXpuYVpibHZXOUpWaVNfT0gxQzVPTVpyQlNHVC1YMXdCSmVRekNGSng4LUQ0dWVuM3c?oc=5) (Thu, 22 Oct 2026 20:00:28 GMT)
- [OCC’s Rules Leave Door Open to Stablecoin Yield - PaymentsJournal](https://news.google.com/rss/articles/CBMihgFBVV95cUxPVldudHVSS09sT1QxU1U3d0U3MTZrTHFfRnFuclpBbWswZ3hTV0lJeFNIeGJfUTlXYS1PNGpkbXowNFNMZlRad3dXTkhZa3lyVElnQWg1eWlPQ1IzN1BsY3NmLV9vSEN3Yi0zR1A2T3Zid19DSnRpSi04NS1RQnR0T0JqRm1nZ9IBiwFBVV95cUxNUmJoZkZwWUtPNmJhZWMwQUdZNV9OeUJLQU1iVjE2b2RBeGdMbnk0aElhMVBsSFh3d3dMYTB2dDRnRlZrTUZZMU9VX1JxRS1fSVl0MVVSYkFYOFZyMDdnVzc4dUEzRFRVVk1IVThZYkt6SnUxeGJSendjY3ZHWkM0T3pmRHJNMnJTOFpJ?oc=5) (Thu, 22 Oct 2026 18:00:00 GMT)
- [The OCC’s Stablecoin Rule: The Limits of Regulatory Clarity - The American Action Forum](https://news.google.com/rss/articles/CBMirAFBVV95cUxOLXlRWk4xUTVwZHdielJveFY2Y2VmNjJDWG9GSWp0QjZaeV84ZWVrdVh1NWQ3WmVYX0VHR09VeGMtQWdabTMwSXIzY21zeWVkRHI4OFJOcndFWlJYX3duQjJrVVBBYnFtMWYyNnQxMWJGQXVCTXAwRGZ1QWdvRHJ6M21FdUliTXhxTkhlOEh5Tk0yVmZ3bW02VTRUUUpZbzhaUXVTcUNocmVmYkJs?oc=5) (Thu, 22 Oct 2026 14:51:52 GMT)

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
