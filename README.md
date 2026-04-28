# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-28 09:27:23 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,168,226,706** | 🔴 -50.04% | 🟢 +0.01% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Western Union says stablecoin strategy is moving from testing to rollout - AMBCrypto](https://news.google.com/rss/articles/CBMimwFBVV95cUxPOEl3R1lOcTdMRll6QXJ3VHdqcjM4YkE2cjhEYlJLczBXYTRUMnBBNENvVnhQX0I5RGFERExiODlic0g3S1duMUFLVnZzQmVSdTd0VHotV2cxWUpRQnVYc2hxX1JQUlFyRndhcno1WEo4UGVYbDBNM2dXNVg0WklKREdQY2pMck90a2xhMGotbC1Gc1gxUFcydVlXNNIBoAFBVV95cUxONm9pS3lzTTRYSmpiWUluUmdOYTVXWDNxLWxkbTE0M2RYRl9qTlhDUzNxaDFTTW5Gal9tZnZkRlNoWXNZQVg2UktqUDExVm50eFRhOXgybFJtRWQ4VmJLbTFzNV9vSnBSVzUtTTdsNzNhWkViNjRPS0NXbXNNcnc0NjRRaWlDRUJxVUc4MTJ6ck82M1lrTHpVUUluT3BtUWtm?oc=5) (Mon, 27 Apr 2026 21:57:31 GMT)
- [Why stablecoins are making many banks nervous - marketplace.org](https://news.google.com/rss/articles/CBMilAFBVV95cUxPVXBVcFFDVGgyQW94WnlVVnJXOWxwSUNKTlBvN0pEZG9qbzFYaVhRMWUwWWh4OUtJTGJzQTdoZ3IzNFFTV1A1aVpPVW1Tc0VUbXhyQjRYc3dzd3pHQUVIRTl0STNYWDlVNHFmQjUyVXktcmUwbnR1NVN6ZFZnWnhyMjdYQWZDVkdqZ0UtT0c3ZlNhYVVQ?oc=5) (Mon, 27 Apr 2026 21:20:00 GMT)
- [Paystand Launches USDb: The First Bitcoin-Aligned Stablecoin Purpose-Built for the $100 Trillion B2B Economy - Business Wire](https://news.google.com/rss/articles/CBMi-gFBVV95cUxNTVpkV3BjZTBJZ1FwVU53N290RGtBTDcxRmQ5WGM0ZFlsaEtMeWtwR05LNThlcWlsTTlsaTRHdkY2aFpIc1EtZHdScDh4bzluN3dIeXJRem8xUkwtLThUUU14ajZBbFJneFFVQzFwZHZKX2RQTGZoMjFJWGJRcUM2eEI0SkE4allSNkc3WUhFVUNnYVpiUGdVOENoVTd1SHQ0Yk5MSjEtNXZxbzRtWFdsdDdGazF0Z2FYYjZjVEp2M0NDSnctMDlLSC1fVXlVamNZaFlXd3ZXSGlUNTFrSG5BNTV0Z2h3RUdZZTJubTNVVF9HNUptT3BjWkJn?oc=5) (Mon, 27 Apr 2026 21:00:00 GMT)
- [Western Union eyeing stablecoin launch to settle global transactions without SWIFT, CEO says - CoinDesk](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNT01uR2FiYXFsUW9NLU1CM0psbjhYZnZ2amcxcTlOc2trNW1uX2JETmZXNXVjcld2V0RCb3VBSDM5amhwYUFDak9yVHNPVTJQanY3NXlkdE1GcUZXeFZLVzk0UktGbVB5SVo4MzVtWXN1M05sRlh0Q0F2QU1kbzFFeVJQVUJqLWYway14dEM2YnBaOG5pYkpFZi1JMW9yeEZxM0txY1BkRmwweUFIYkJoT3Ntel9maGJScnlOS1MxVVQzaFVXTXpFRWxYa2lNQUticUE?oc=5) (Mon, 27 Apr 2026 20:40:10 GMT)
- [BLOG: JPMorgan, BNY Mellon roll out deposit tokens, lobby to restrict non-bank stablecoins - thebusinessjournal.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxPSEtlSkpFT2htQmxQMzF5WnFlQkpTLTFybHNZZHJ6RXVNbU9fTHN0dFFQenktR1JJMS1EQ2RBazc5a3V5R1NBbzRueUxMcTNzSkNVXzA3bEFuRm5jOHlBUFluRVVoalJjQ3RlZFUySXNWNlVLU3FFRlMyeTVhVUkwZw?oc=5) (Mon, 27 Apr 2026 20:39:01 GMT)

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
