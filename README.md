# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-13 04:44:23 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$290,899,018,874** | 🔴 -0.07% | 🔴 -0.64% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Xash’s Kevin Huynh Pitches Stablecoin Issuers on Gold Rewards Instead of Passive Yield - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxPempCVGJWYWtPOVJfbElpZEhRclZwQmZ6NHNKZWFkUnNHSWVEQnZjS2QzX0RtaG1hdFpTMEw0Vm1acVBoTHpQdXIzeWxOdEFqVlc1YnhCS2pZdElrY20teXg1d2N2V2pzQW9SbUJGVzZUU01ZVmc5SWY5NkFBbzNxX3N4MkhBM2NibjAzUkFVTEphQ1BWbjZZNF9XbkFocXpBS3c?oc=5) (Tue, 13 Oct 2026 01:57:00 GMT)
- [The stablecoin conversation is missing the everyday user - Asian Banking &amp; Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxPS0J4dE1jcFpKTmVoN3ZVS2NXek5mT2hubUg3aGJyZldhMVAzXzFDOW9vR043TzY2SUo0OF9mYkpnM19naTNPNmFkMjN5Vmp6SlNNdDBzQTE4azN6M1pPYzN0Z1BXemEyQWNfTnFlTHlFSm9OT2FwdFVnTG03Zzh5OGxiTHNfYXYxQlc1UkwxeWFwbmZJclE?oc=5) (Tue, 13 Oct 2026 01:00:00 GMT)
- [Global watchdog warns the $300 billion stablecoin market could face bank runs even with full reserves - CryptoRank](https://news.google.com/rss/articles/CBMi1AFBVV95cUxPVkR5ZVdqcS1laFBoeGFHVU5ST0V6MlJqQ1hhb1Nzb0M1b2V2em9JSDlpOURwb1pPWVpvZllfVXBpUU1PRVd1WFRrVkJGdm9ueTIzenM0aDhnaVJNeVM4R0FoeC1vWUxnNjY4cHhfNVpNcUlndkh0bWgtQmJqaFEzMm5PdE1LdE9jc2lfS3RLaGZPeDZ1TmJPMGRTLWtwV2Nfb2ZOT0tKQVJ6UUQ5aW43dHBCbVpMbElqcUxTaXdtV184WGd6eW1QMGk2aUNhaFZocjF2Vg?oc=5) (Mon, 12 Oct 2026 23:02:03 GMT)
- [Global watchdog warns the $300 billion stablecoin market could face bank runs even with full reserves - CryptoSlate](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQdk4zZEw3c0d5VGstVzJFQ3c1VEd0T1F5ZmN0OWZwM1plNXk2dXpNaWpHYXhfbERGdjY3b1ZwYWI5dm5UWjYyMGVUWVBIU2dQQm9EaUg2VXF1akJDRjgyQzFjS09MVmowMlI1ZVdjVXZVWE9UaDVtaGRxLVp0Ry1vT3ZmcGlNWDVzNkNnTGRpTE4xdDJHUmNULUxyMG05azAxbjNpa0I5bFRkOFozWTFFXzZMTDR6bEdzLWJIRHp0RF91RFU?oc=5) (Mon, 12 Oct 2026 22:10:30 GMT)
- [Stablecoins Have a $10 Million Problem: All That Money Is Going Back to the Bank - PYMNTS.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxNT2xjcnM2MTJEcDhfQTd2Y2tCSmhmOFlndWlKZmZKWC1udVo0LU41VWdKcWlxaGN2SGlKWnoyYkpBZlBOVF9wT1Zmb3NmUUVUNnRWU2Z5SkJwcUprRVQ1cmU0endxNFZOa1FLVlhhaDVUZnJHcXIxV2RmVVpHNDRFRlBXYXFva0pCOTlxVG9ISm5sZWI1TTBoQm5ERFlOZ2VUS0hGOA?oc=5) (Mon, 12 Oct 2026 21:48:35 GMT)

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
