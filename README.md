# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-15 02:39:48 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,310,105,658** | 🟢 +0.12% | 🟢 +0.14% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Mastercard CFO Outlines Growth Strategy Driven by Stablecoins and Value-Added Services - PYMNTS.com](https://news.google.com/rss/articles/CBMixAFBVV95cUxNbFBPbnNTMGlINWlveHZDU0lYMC03UlIyRmgyWmx2cW9RcVNYYjktS2lYMWtIU0xTbC1YWHBsN25MS2I4QndBRm9rN2lCUEp4Nzl0QjRSdm1lWVdZVUVmRGRpRk9KRTRNV0tfNEVVUkhUbVpweXA5Nmg4LWVNaW8xekVTNm9QQVJnbENpdmYxWVc3dW1TTjZFZ2g2ZTBrYllVb2NHZTNWbHJmem5FRUdveS1reWlkUGdSTHlLY2dsbWRlcGNZ?oc=5) (Tue, 15 Sep 2026 00:01:45 GMT)
- [Banks Want More: Trade Groups Demand Stricter Stablecoin Limits in Clarity Act - Decrypt](https://news.google.com/rss/articles/CBMiggFBVV95cUxNUVRpWERXX3RaN2IwUjA3M0RmcFdCUEUwcTdmWHFiNFozVHJfN1dpWkVlNVFucHJxLWpSblg3c0k5NmhvUjZVYkh4WnEwdGVxTlJ3aFpodjNzSm1PMEFIT0IxVUhRclVha25McWI0VktyUkkwVHdhZXd4cFFwcGRJM2t30gGKAUFVX3lxTE5WQUE2TEttWlh3OUtCTEpta1hQNHQ0WW16QjM0Vm82c0oyUFFDN0IxV0NwVzV0SGFwRDljVE05QUthM3VzMjNyYThvU0RYaVhiU0pPeHp2V3pKU0JWcXpibEExZHlHTUZRZW1nSXNOQndnM3ZFVmpxcDR6NUZhLW1JN2k2NWVqaDFQdw?oc=5) (Mon, 14 Sep 2026 21:46:04 GMT)
- [The Treasury’s New Stablecoin ‘Panic Button’ Lacks a Manual - forkast.news](https://news.google.com/rss/articles/CBMihAFBVV95cUxPaGdZSVlCNFdXMU5wa0Q0MmVkTmdZTG5YRzNHWm9Ya2hEYWpoU0VJVlFoQW9XQXN0VmpWVlBYSWVfLWJ3c0RNUHQxbEdEa1p1dUoyaGZBLU9IS05DV2E3VWxJaDlBd2h6OHZfdF8zc21nTmNRNFVoYmpXZDBkLTkzdXY3Yk0?oc=5) (Mon, 14 Sep 2026 19:17:18 GMT)
- [Stablecoins and World Trade - World Trade Organization](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNZUMyREx0bW42NXAwU2RXOUJ0ZmpXRTJYYjgzejZmX2g3MFVNWXVTblM2dHBPM3U1Zk1mVXhMeTZnM2k2cE11MVBrMjVUY0dyOFFybEIwY0MzMDA5eGcyUFhEaV9XMmhJTTdTR0lyWlBUbU5NM0ctMnI5QW9mOW10blFhVFdtcEw4?oc=5) (Mon, 14 Sep 2026 18:05:50 GMT)
- [Banks escalate stablecoin rewards fight as Senate prepares for a Clarity Act vote - CoinDesk](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPbUJ0SjFTTVEyV05lZUdGSmxUM1NfbFlyZEF0dmFKM25ldFVSdlNZMTVxdHVrTzU4WUtoaE9SSFNBeUJNWFZTOWxoU29CZDB4ZHdQVVpGMXhJR3pMdGptZjB2UHlxdFpMRXF1RENUd1lJZWdyemRqc2lINmlmU3lIczRvZUZWOXdhbXNuZXRmV0ZDS3NJSDZ4aHM1dGQtU1VhNFhHWlR1V1VkVk14bGx0ZUxHYXE3UFlyUnRwTFZsZEljdw?oc=5) (Mon, 14 Sep 2026 18:03:27 GMT)

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
