# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-03 02:00:17 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,439,221,576** | 🔴 -0.06% | 🔴 -0.52% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [From stablecoins to sovereignty: The rise of trust-based digital dollar systems - asianbusinessreview.com](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOUnF1UlNNZjRYNkNLZkZWOXd3ajBrNFRVamRKZGRlbzFVeG5NZVh5U1VOXzFkNVJiclY4LTJURWN2d3U2OXNEXzA1LVZreHIxOEpENmJFakdUYnMyOWFxb2oyek9YRGRXd0xpZklET2hvWHdKaWloeFdUZG8yNk95ZVk1NlFsWXFNY3p4MjJ1OVVVT3lVZ2R1R1ZmRnp3WER0VmVRQ2lSZjRXQQ?oc=5) (Mon, 03 Aug 2026 01:00:00 GMT)
- [Onafriq Partners With Privy to Advance Stablecoin Infrastructure Across Africa - The Fast Mode](https://news.google.com/rss/articles/CBMizgFBVV95cUxNNTFOMXQ2djN5WUhFaS1OcHItaVJqS1J1c2pxV1o4ZVpfYlltemZ1WktZdkc1cnpSWnlwQ09MR1ZKUTNXZFVheHNYWHB4RERDbFgxQzV3Ql9pNnI1Rm9ScTExeFBnYVFtZnNzMHM3aWlnX0dHX1dRcHJhNjd0VVl5STRva1RwMHp5d2dXVU5aZ083aTJCNVJ4TFo1UjE1eTNoblVaZlR6TURRa0tjSGJmN1NFeU5vbkhPOWU2SlR5aEVZVzVWSmg1ZVQxODJJdw?oc=5) (Sun, 02 Aug 2026 23:42:24 GMT)
- [A massive stablecoin fragmentation war is brewing between tech giants and a startup is aiming to capitalize on it - CoinDesk](https://news.google.com/rss/articles/CBMiygFBVV95cUxOZGdKSHJCTVBsazdIV3pENG1hYjlEYUZHYmhLbXpWbVBBa0FlakdKT2NfWlNweFpRalZoNEk5SENId0pkbmRlUHB0endfODE0TUw3ZUxPRjd5UHZWdW5yUnpnbUp3WFJjYVJvSFN0WDZ5RU9oYTFLOW1IamFDRjhjbjRRQ1V3RFBocFNkUUwtM2xiaGVBYXNEbUY5UEw2aGwxVEdSZlZ1bEQzNnNDMW1MZ2FDUGpQNG5vUFRxeUhkS1VsRTRBZlAxZTJ3?oc=5) (Sun, 02 Aug 2026 19:47:40 GMT)
- [AX Coin Stablecoin Receives Sharia Certification in Bahrain - CairoScene](https://news.google.com/rss/articles/CBMilgFBVV95cUxPRy1HSWl2bHZNeDE2ZTQ2T2lhMVNXXzJZY2RIUEl0aHA4M21QaGZpUlNkbVVBbkIzZjRLZldSbGpxdXdwMEVDOUxuZFlWN1V1QkpiTjduWUtuRW9ySUl0WFExV3pEV1Fadlo0c1BjTkgxZkJVY0MtWnNDaHR5X3BiUnVwNG5MeVMtbGI3N1diT2dLNy1HVGc?oc=5) (Sun, 02 Aug 2026 09:04:39 GMT)
- [South Korean stablecoin outflows hit 18 months - Crypto News](https://news.google.com/rss/articles/CBMidkFVX3lxTE1SMEJRdzZTQ1M0bEFSdVRobGlSeVJUT2VhdUoxZjdPSlUwVktkQjRvNnR5MlN6aEFWV1RnZlFnQnl6QU9hUXNxeldtTTVYUzFnU3V0VC1VXzZLZzV0eUVuZlg5OTNxdUdhU0xKTWV0dGRkQVNjVFE?oc=5) (Sun, 02 Aug 2026 07:34:25 GMT)

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
