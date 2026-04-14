# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-14 01:51:01 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$298,591,233,857** | 🔴 -49.97% | 🟢 +0.48% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [White House Study Minimizes Stablecoin Risk, ABA Says - Law360](https://news.google.com/rss/articles/CBMilwFBVV95cUxORVJCMC1VUUpJc18yemJfUVhaV1VzbDVNUkkxc28weHNXV1RoQ1p0blFabGVpSUdzYXZDR3NFczRSYV9US2R6TFdLRFpCVXJfTndJSnhLb1ZGM1NLMGpyZzJ5bTZiQXJ2X3dIVGVUcDE2OTRWUk05STZMRTNCMEVUQS1VSVYwbDZRaGxSbmVLUzRKdWRzMjhz0gFWQVVfeXFMUGlsRkFtZGhWT0lKX0I0TVNGQW84UTlTcTFBeU1kV040WXBDQlhIbnNEeFlvQjh0ZlJMcmVIY2w3V296UlBoUDhHd0pjTENDX2tZR1k3TXc?oc=5) (Tue, 14 Apr 2026 01:07:00 GMT)
- [FDIC proposes GENIUS Act rule establishing framework for FDIC-supervised payment stablecoin issuers - JD Supra](https://news.google.com/rss/articles/CBMifEFVX3lxTE54c3FVZmlhUnZkaW9fQTdPXzZZbndBbTN2YWNuaHExaU9BcUtPSFVpSjFpQ2VYeFZSd2xnV3JYNmttRURhcTZnOU9vUnJ0VFhhUm5YM3BTcHU0SGdQRi1xajAtQXhFNnhNcHJXc2cyT3hZRUZXR1otV0NfQ2g?oc=5) (Mon, 13 Apr 2026 18:52:52 GMT)
- [Circle CEO Defends Company’s Response to Stablecoin Hacks - PYMNTS.com](https://news.google.com/rss/articles/CBMiogFBVV95cUxQWWp0U01laWZiLXZfQjRZYnRDSHphbllnUFI2bnFNNTM0ZFZmcVNrQkNvSEJKUG5nUU5wRlBaZDllaV8xY0pDeGtKTUtWMXBFaE02VGdvdXVCOTZMcG0wX3hGVEk3REpJRFc2cG9GYU9oaEYxNUJqN0JRbnpBalQ3OUs3MzdBT0FoQnlKZTRTaWNQYlk3WmNUelNMRG1HMTBremc?oc=5) (Mon, 13 Apr 2026 18:22:51 GMT)
- [ABA Warns NCUA Against Finalizing Stablecoin Application Rule Too Soon - CU Today](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQY2tpT2dVWENQTWJYN3lvYjNQT0FhNWJOdkNqZUdlckhFWW1NZzJRYU4yY3BKcWRmQ3BEaE9NdWtJRlJmdE15djBHSjhDb0hZczdUSThNcXJhS2o5dHhfUFUwa0N6NG5paHZ2R05XTlZPaUlValUzUnJnTDl5MWszYm50ajJPSUtRMDN3OW5fREZ4UkxqTnE5SHVwLXkyNVFpMVdoN0ZBbnRGc2s?oc=5) (Mon, 13 Apr 2026 18:13:27 GMT)
- [The Numbers Are In. The Banks&#x27; Case for a Yield Ban Just Fell Apart. - FinTech Weekly](https://news.google.com/rss/articles/CBMipAFBVV95cUxOWDVvdDRjWERpY0pTTWtfeXBzRlRlVnlBVkpSZVdHT0VKb0wyRm92NFNhcHlncnk1NHRWODBTZV9HVmgzcm5hNmVYekRuVGsyLUhBb25BRDh3eWVGbTNsQm5KQkRqVWpKWEhCc1RMLU5jdWFiV3NHTTY0TkxTZ3p6TGRUdEI2ZWYyR19HMGhZWnRfOEtFaW9VRkhqcEQ5U1dqQl9VRA?oc=5) (Mon, 13 Apr 2026 17:31:00 GMT)

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
