# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-14 01:18:16 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,536,405,519** | 🟢 +0.11% | 🔴 -0.19% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [White House crypto adviser says banks shouldn't fear stablecoin yield - TradingView](https://news.google.com/rss/articles/CBMizgFBVV95cUxNWmlQdFgxZlhxUE1SY0RrTk80eXRNU3lnbG4wc3Z0d09xMjRkTUF5clBiMkkxSXpacXF5NFpaWVBSTXFiUEFkWXZQSVUyaW9jXzlUdGo0MEctSVdSclZsenNUQ3MwNDZkTVlKdGtrZnc1ZmVud1BfWHZtdDd4SGNTaUhpQ1dPN0FjSGdPQXlfXzFNUHllTEJmZ3l6YWNJaHNtSng1YmxxbHRKdHhMVW40V1UtZ0k2a3hzY3VoWVc0VFN2em1tbjRRUjVjTmhrdw?oc=5) (Fri, 13 Feb 2026 21:54:56 GMT)
- [Stablecoins Explained: Bridging Digital Assets and Traditional Finance - Knowledge at Wharton](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOMHJKZENkWmx6Z0w2VVE4ejBBcFFXNEZnMk92eHlXYThCR2p3M2JKUGlvUGItRGVPZGNMNHJmTWFoc25LcWNHVF9aSTZTU2w1U3F0bTN5Q0NTLWx6YkdpeGZ0TEZhTHNwc083TGxNTTZVZlhRWW80LUdkeURYc05MN1V4VVZHOE5RX3B2UFZFd1RvakNCWHB4SGtEQ3RrNEtiSGJoYW1RMUtvVEZJS3JFZVAxXy13RWhjVExybHp2Zmd4WGlrZmVoX3ZJU2hhdEMydVE?oc=5) (Fri, 13 Feb 2026 20:21:54 GMT)
- [Crypto group counters Wall Street bankers with its own stablecoin principles for bill - CoinDesk](https://news.google.com/rss/articles/CBMixwFBVV95cUxNNDFOV3Zkd3poWHhiVXM2V3dTY3pySGh2RVY4OUJWWkZ6cUZmTk01Qm1oTmVSaXFsN3F4a0FOeTgyZi10NTFjbVVwSEV0TlQ2dGc0d3RUQnVyby1LeGEwdmN2dEFLd0ZmcWxoSlZWODFRWTY2SFpSWlZ4NmZMYnhtTl9RUGFGSlZVdUp3S0s4OXp1VnJzRTJWcUVOTENuYmxhYzcwTmxJMlEySVA5UkNYVzdUeFpMZ1FCc01xNE9PX0o2TzRSOTlV?oc=5) (Fri, 13 Feb 2026 19:26:38 GMT)
- [This Week in Stablecoins: The Market Starts to Splinter - PYMNTS.com](https://news.google.com/rss/articles/CBMimgFBVV95cUxQVEgyeXM0SmlWbm40Y1VTRzJWaHA4X3Q4bDYwbGVzWVFjWEwtWXJZNEZHdF9qTWxDS3hzTDJ6Y2tWcW0wWUFKVjBhYlN4VzBVNkhNWmg5ZlRWRHJEV1hvNXU0aFU3dXFnVkJ6NjNHQ3V4aGdzZG9mSmF6ci1sOXVaZlV6TGlFLXF1aGlWWlN0R3NaUnlpeWV5bXlR?oc=5) (Fri, 13 Feb 2026 18:51:19 GMT)
- [Nomura, Daiwa, Japan’s big 3 banks to test stablecoin securities settlement - ledgerinsights.com](https://news.google.com/rss/articles/CBMipwFBVV95cUxOVzVaMGZicVBMWGg4TFczcjZEbEZVX3I4eGU3VVlEdEdFX1JxNjlMQzhoamp6OW5WU2ZmUDZCMW16TUpCZXFkazdTTlhHekVkdkFOT3ZPZEZ6bncybmkxUVplM3BEVkpyaElPS1Z5QjFOM09ROXp6UWY4Qm9yVmh6eTRSUFl2VVpBNkNZQmVuTkVPdWQtdDZUeFFXQWMwRm84OTlwMVE2bw?oc=5) (Fri, 13 Feb 2026 17:10:37 GMT)

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
