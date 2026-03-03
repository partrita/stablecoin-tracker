# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-03 01:22:27 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,885,714,715** | 🟢 +0.28% | 🟢 +0.56% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [What the OCC’s 2026 Rulemaking Means for Stablecoin Issuers - Finovate](https://news.google.com/rss/articles/CBMihwFBVV95cUxPZkZnRDdVLUpEUXRGVGNFYzVDNV95Wm5lNWVLZXZudWxfQ0kyQ2c4WE1BaFFPa0NmdTQzOFpKXzZ2azh0M0EtQzRWRmVJY0RhRmZGbUJtV1ZkWGdyRXhKcndpbEI4ZmpkQllHWGRXVEVlSWdEYWZ5S28zMWZRTkhhc201TWVWZ2c?oc=5) (Mon, 02 Mar 2026 21:20:13 GMT)
- [Stablecoin Explainer 2026 - eMarketer](https://news.google.com/rss/articles/CBMia0FVX3lxTFBTQVcxLUw0OTJTQTl3N09jRXJLX1FrUVZrTjhSOG1HOURlQ0EtVlIyLWRzajlyMXlnNmJydE4tcks1Q0tLdGpaeGN0UTdZR1pibzVQa0hZcHd1MXhoMmZ1cm1vQm9sMWdTOGpV?oc=5) (Mon, 02 Mar 2026 18:08:45 GMT)
- [Institutional Crypto Plans Stall In 2025 Even As Stablecoin Volumes Climb - CU Today](https://news.google.com/rss/articles/CBMirwFBVV95cUxNUUdrZmY0V1l4MGl5R0dNUUtPRFhkY0FTblFRZHJrTEpwci1Va1ZZTTVJYkJpUzlMUEQ0Q2dYSkhrV2ZxNDk4dkJaVWJ6NEJpTk1JdVVWZTdyYnRCOXNQaGYwSmtIcDBiVExGcU5Hc3BwRkhLN2o4MDBVT1hHeVJLLXJOc24ydGxhMDUxRmpXTWd4S19JSFhpSUY2THlWNkNCRnZHbXRIZ0VKaG9UdHpB?oc=5) (Mon, 02 Mar 2026 16:51:12 GMT)
- [Crypto world faces growing pressure to relent on stablecoin rewards to win bigger prize - CoinDesk](https://news.google.com/rss/articles/CBMi0wFBVV95cUxOWEwtSWt6ZG80Z2ZmdkNiUkFnaUhLWjFIT0NpTmJ4cDhpaVE1YUxIS3g2SmxhSUVRbGJJQkpwRHZwZlBSLWxVLTBXVHNyNHlfbHJlSkJ6WU5OLWNtU2V2TnJ5M0ctc0VrVkV5UWkwT0NoZWlSVkFKY1Vnc0FEeFlPcGpqOElMUEJfSFRYSWY3bmgtTHQ5Yl9FaC15a0NyZ0dNS1pCN1phMFJ2VWJEQ21vN0ptdlVPbk5oQTcwUG83Qmx0X2NrOFVVb1gtU3ZMMFYwM3Zj?oc=5) (Mon, 02 Mar 2026 16:50:01 GMT)
- [European bank consortium targets 2026 launch for euro-backed stablecoin: report - The Block](https://news.google.com/rss/articles/CBMitAFBVV95cUxPbTNJWElFdVBNSGd3LXhWZmhBVUljb2FuQWltcGdUcTkwV21TX3ZTdDc3TG1kOGpxLUxNMUpsbUdLRF9jTEpWQ3hkTDAwMnN0QzloTnRfaXAwdmxWRnZhWTdVNWFITDZ1TG91SXVJZjYyVk5DeGhvWkMzUUFXMmlXWlNBT1p3bU9wWS1tQTRSMHQ1QVNFZGd6bktOdVNuUXJ3MnVRY1NTVm1tbkY5eTNwdGFqS3g?oc=5) (Mon, 02 Mar 2026 16:13:46 GMT)

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
