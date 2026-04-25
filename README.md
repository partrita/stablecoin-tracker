# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-25 01:45:36 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,290,569,059** | 🔴 -50.03% | 🔴 -0.12% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoin Growth in the U.S. - Purdue Global Law School](https://news.google.com/rss/articles/CBMic0FVX3lxTE9uWjZ3RTVSTGM4a1VJejZyQ2tFdUNjUmxsOHpMcW9nZlE3b05EQWNaT3dOTUZtai02SDNma04zb3RRQkhSS2JaUDUzTWVJS21IaHhsQjZlclh4S19NVGRPWFdfX3BMYnVHYWJpQUpWZjRyMDA?oc=5) (Fri, 24 Apr 2026 20:57:47 GMT)
- [OCC’s GENIUS Act Proposal: What Prospective Issuers Need to Know - Morgan Lewis](https://news.google.com/rss/articles/CBMipgFBVV95cUxQdGFFNG5LTUJ1aVNHX1ZWSzBPNzJxVWtVNldreWtPQnE4SThTMEpOVFZQS3dQbkNjSGJlR0JtVjZ1TndNd3IyVnBYcjdSdlpUVWJrNWx1TVZrYi1EUk5jNHcxZFlEdGhpV1FoWGNqdnlvOFhVWHVlTlhRdXM3QlRiUXhfRGpkZFB4Mk92OVBqNUpJbTE4RThQWVE5WjNNTzdZYzVabXdB?oc=5) (Fri, 24 Apr 2026 19:43:17 GMT)
- [Morgan Stanley Supports Stablecoin Issuers With New Fund for Reserves - PYMNTS.com](https://news.google.com/rss/articles/CBMirgFBVV95cUxNUS0zb3lXV1drTzc1TVhBN2ZsTWY2ZE80RnRnZDVIRjN4bW1jRjR5X0RZQTl1NDY0cWNkM2luRFVENXc0NjJmMThOVmFQNXRISVYwS2pXcWEyRFJGSXZHMW1zSFc4OU0xM2ljWl9nVnBybEt4NlRhYUNicVl2LV9kajlOYnNMQXFfQlU5aXJ4R1l6UV9VWWpZYmRROE1oQW4xVjQ5bjczZ0tKN25wZHc?oc=5) (Fri, 24 Apr 2026 18:37:44 GMT)
- [The Privacy Problem Institutions Can’t Ignore in Stablecoins - PYMNTS.com](https://news.google.com/rss/articles/CBMipgFBVV95cUxQRkNOSVpMT2ZvbUFFU19OU3dJanZtekRPMHYtTHp3WkwxNUlXSWtEUEhZd1ZHcW41a1R6c3RORE5kcGdGQnFVUnRGbFlEMlVVYks5aVhtbHJWbkNKQ2I3YlA3SDlxT3c5ZXNsc1VlYUMySFNzbC1GLVBwTy1PbExqaDhFOUtRaF9veHpMVXRFVWxid0Vhc0ExZF96YzRMQUdsS1JDRGV3?oc=5) (Fri, 24 Apr 2026 18:31:43 GMT)
- [Why Morgan Stanley&#x27;s stablecoin bet could reshape finance - Yahoo Finance UK](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPc1hmOFdnXzV0OXdUTlA1TEg3a19vclI0cGdrMXd5a1dvWXpqT0NlZ0NkNGEwWC1LRU9rZ1BiSzRtejNnc0ZiOFlwNUpDWVNNVFdqUXdtN25jdDZreEs4emFYNU1OMUwwYVpTeExzUzFjRkRJTzc1dEZyRWFiMVlHNmNWdWlDY1JKM2ZwZy1qVnZIMElmbndNWndSSVVwbHVIUFZzMEs0dWh1QQ?oc=5) (Fri, 24 Apr 2026 17:02:12 GMT)

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
