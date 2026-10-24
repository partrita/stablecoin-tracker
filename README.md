# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-24 02:40:20 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$287,804,756,931** | 🔴 -0.15% | 🔴 -0.65% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Money 20/20, AI agents, agentic commerce and stablecoins - Mastercard](https://news.google.com/rss/articles/CBMipgFBVV95cUxNWXpFVmpqSW9aempHNm1fdDV6RjhmT05kMERralFjVkJtN04wLU5jZTlydGxjdS1reE40SC1CWUhjMmF6dU9wZkk0bjZYTWZaai1qQWI1Umh1dXhGTFBxRFIzcEM3U1JtUG9vWVhaUGFHOWpoUjhkQTRDaTRrXzhGWV9aRDVTUFY2TC03UEluTGViRTJScmpPajIweEtnV1NwT3I1UUdR?oc=5) (Sat, 24 Oct 2026 00:08:56 GMT)
- [HSBC Launches Hong Kong Dollar Stablecoin for Everyday Payments - PYMNTS.com](https://news.google.com/rss/articles/CBMipgFBVV95cUxOckFRb0tPUkFndjBMN1dtQ3I5dzBmWkJHaTU5amVtWTdLWlVKbDkyTnprejhNLW1yU2hFSXE3RmpTdFM5MDlGdEQ5MGR2VnVLZm9pZGh3WVRINFVpM1dDaVpfVU1xdFRJM0FNb3lsQk1FX1JSMERWbXI4WlVsM0VpVzlQRmlpZlNJZFNHd0x6MWRfQ0MxTDdHTlMtWGMycklQTFZiT0pn?oc=5) (Fri, 23 Oct 2026 19:56:58 GMT)
- [OCC Finalizes Stablecoin Rules That Supervise Issuers Like Banks - Forbes](https://news.google.com/rss/articles/CBMitwFBVV95cUxOUDAxV25tY2Eta0JSRGhBNHctMjBRVzJRWTFVcmhwY2hoeGExZXNuMzM0RG9vUi1UR0RORjdzcXFJeXdUVThYQUJpOWdXcGczNGlEdVJXd0NIaEtFUGxTM1NSdUo0OVNaRHdrX3hCZ09YdWxkQkJFN28wM0VDMkdsci1NZnNxWmZWOHNUVVB2Y0o4Tl9RdE5mSGVoZi13aGQ1RHZZQ2llNlk2eTI0NXgzTEJpRlVPcm8?oc=5) (Fri, 23 Oct 2026 18:25:57 GMT)
- [Coinbase to drop this Japanese yen stablecoin years after its price crash sparked investor lawsuits - CryptoSlate](https://news.google.com/rss/articles/CBMiwgFBVV95cUxOOTdpaGRHTzkyaUJSdk5WaGZWckhNdk1KWkR3dUNULTdFOUdmYWZQZ1lXVmxSMlJqRGlqOVF0WFotM2FnRkRDa0k5MkpGeDVoazBiT2FWSU02SG9UZS1yM0QxSUxsd3huQVJvbm9HVXBkbTFPck15NGQ4WllwY3FVZlNjSk1IVjBmX0tZQkE1Q0E2eVVLeGRWckJHSzhpSFBOWnhBSjdyUHNYbTdqZzRzODRxcTZJY1Vqanpjb2dnRlBoZw?oc=5) (Fri, 23 Oct 2026 17:10:05 GMT)
- [Solidgate Wins MiCA CASP Licence for Its Own Stablecoin Rails - FinanceX Magazine](https://news.google.com/rss/articles/CBMioAFBVV95cUxOYjZheW1WLURvdXp1NmFWRlF0WF9icHpXZTE4YWRScnNnYmlvQjBHVGo4WWlXMzVjSnJsSXhIQkdFRjQwM0tFYjA2R3ZrSWlxOEFESVFoUW5fd2hWV2hqdzRPaUdFZXlYRjB0OHE1TFU0MS1KRlB5ZlpCNXVCVnUzSEE1dncxSk1JMi1LWDh2NERGb19fVzVvY3g1bEdhdFpn?oc=5) (Fri, 23 Oct 2026 17:04:57 GMT)

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
