# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-19 00:43:52 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,748,688,784** | 🟢 +0.02% | 🔴 -0.05% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [NEXUS Signs MOU With KRWQ on Won Stablecoin Payments - thelec.net](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBBQ3p2eGh2MGQxbXp3bTNyNzVOWXl5MnVNRXdZX0dDeTVCdXNOWXNvQUJlblFBanhmNXdTenNMZmlxWkd6RTBKZEU3M2V4NEUyaGFVWHFvT21uY09HWEFzX3hqSGEwN1U?oc=5) (Tue, 18 Aug 2026 23:25:59 GMT)
- [Visa’s Search for a New Stablecoin Partner Reveals a Strategic Divide - forkast.news](https://news.google.com/rss/articles/CBMilAFBVV95cUxNaWVVTUJGRy14VzVYa28xcHNSdHJmUlRtcjFoVlhmbkZJNnAwMkpySXJyYlUxbkxsR1Zfc2NubjR5RV80V2dESWtlNzZXalRHOEFfSTVxV2VRMEU2ajFZbDdyV2J5RjJ2dHBNOWtOaG8zQ1Jpc20xV1VJaF9ENzRBUEgwLWhZd3B3TVpNRWdHLXBoaC1U?oc=5) (Tue, 18 Aug 2026 22:02:33 GMT)
- [US Treasury seeks public input on GENIUS Act stablecoin rules - Qazinform](https://news.google.com/rss/articles/CBMimwFBVV95cUxQVHRwSVlZMUpGakdQVGhuV01vS0RGOVdjSVJIeUMzZm41eEpYV3VJRkRRc3BNN0ZETlVBTXpJMUVuZXlGRVRfNnVRcHBrYm92Wm43WmhZdjE1dV9QLUNQdUFTeGFUdFg5ZFVjdXd0MGR2U053TTBSSFBpLVptNi1uOWFSUFhRdW9TUENwQVBjMFZFYmM3TDZNM0hhMNIBmwFBVV95cUxQVHRwSVlZMUpGakdQVGhuV01vS0RGOVdjSVJIeUMzZm41eEpYV3VJRkRRc3BNN0ZETlVBTXpJMUVuZXlGRVRfNnVRcHBrYm92Wm43WmhZdjE1dV9QLUNQdUFTeGFUdFg5ZFVjdXd0MGR2U053TTBSSFBpLVptNi1uOWFSUFhRdW9TUENwQVBjMFZFYmM3TDZNM0hhMA?oc=5) (Tue, 18 Aug 2026 20:48:15 GMT)
- [NEWS: Foreign stablecoins face new US compliance hurdle under GENIUS Act proposal - AML Intelligence](https://news.google.com/rss/articles/CBMivgFBVV95cUxOT1pHMHNsRDlWUVo1aloyWnNtVTBZTk1lbk1FNExOUEtZd0N5YmJiendiQU9mSHg4ODhyT05lV2FfRXZLOWVRZDlleG1OOVg3WmEtZTdDYkh6bWd1cXBqdFRVS1Q4LTdMalNNYWxFYUZvOFdfeHFyb1IzNmNjRHdyWnl1dDBiNXRQWW9CR25qaDdjaWlMMzlYc01hSWFJRG10aGRTWHQtNzlfT3pkVHBrSnBOa3hWZEdteERESVZn?oc=5) (Tue, 18 Aug 2026 20:45:59 GMT)
- [White House crypto adviser Patrick Witt says he is &#x27;optimistic and bullish&#x27; on Clarity Act as stablecoin fight resurfaces - The Block](https://news.google.com/rss/articles/CBMi3gFBVV95cUxPSExldWYtd2pva3lfclQ5dk5nWHAtN0ZzaFVjdHZDSDc2QjRua2ZKc19KMjdNWnZ5Uzl0ZDRDdE1CTmM3UjJRdDFleUxwWHRPdW1VV2U0d0RTX2VaSFFIdUc0WXBHNElIRHE3OG5FQWdaQnh3cm45dEZFV1h2TnR6RmJscnlDczF3QlBob3BHUkdPTF80R3pURXNMNFVNMlNZQ054Yk9FQ0YtcTNwdHFvNkZDVE96TWVaS2VWNWtrYTM3bk1GLWs5UUlFMi04bFREUXM1WDkzcDZxV0xBQ2c?oc=5) (Tue, 18 Aug 2026 20:25:35 GMT)

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
