# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-29 14:13:54 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$299,623,920,230** | 🔴 -50.09% | 🔴 -50.02% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Solana Ventures leads $18 million round in Squads to scale its stablecoin platform Altitude - The Block](https://news.google.com/rss/articles/CBMijwFBVV95cUxNeFFKTlk0bkxiZ2F6RkhLcDM1Ykx0VUpRNzNLZE91UlhOWXo4SU1taWU3a0NhNm9GUFRCV3FucC1kYnlnZTNTT2Q5emhfVjlmcXV6dl9LR1c4RVhweW1RQWZZMnlKU2JkaXZCYm9PdUFEM3RsUlphajZadUJyWlhCZ25VOG5LZk85VVVrNzVwSQ?oc=5) (Wed, 29 Apr 2026 13:55:02 GMT)
- [Ripple (XRP) News: OKX’s RLUSD Listing Just Made the Stablecoin Institutional Collateral - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxOVG5Sd2c0TGxabGx2VnQtZnpiMnl3NWhoZ1R3ZkNzWHRiUnhXalBqd2NkRTR1YzNnczBGcUk4bGxNU2NGMGdBWmhrVzNrQU51eldkTHU3U3daRFRVTkVWdHJ5OVcwQ19QR0VfbHp3UklYNDhOUUZtUTRwd2Q4S2xPX2ZjLTJEM3BGS21DVHZEWnI2bFJO?oc=5) (Wed, 29 Apr 2026 13:48:59 GMT)
- [WeFi collaborates with Visa on stablecoin payment use cases - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPSkdXY0RiaGdMZlFJSENYVlNMMHN3WWJVXzZYUUpLcndoaHlndWdiNHROQkJhNm1xQkFCRlI0WWtuTVlTX3VLZzk1c2JTdDdDQV9EQUdsdWZXenFEX05wX0J1U1p6MVM5Nzhfem9kQ0dUX1plbHU3SnU3MXNkQ0JuR0dMVFFSY3lqZmNnbHE2WG9uSnNGLW5RSmt6MVkwQ3FJTjl1WWVpQXZOUQ?oc=5) (Wed, 29 Apr 2026 12:04:08 GMT)
- [WeFi collaborates with Visa on stablecoin payment use cases - Electronic Payments International](https://news.google.com/rss/articles/CBMioAFBVV95cUxNZ1RTN3ZXaTlXN3N0c1VXdjdobXh2dTQ2clNyYS1Lb2ZBdURwbWxDdHNJR2VuUGlRbC1uamxSUWZHNEtGUEJ3SUczY2lvdVh1Ui0xYVhmemR3UnhEcXFqdjVZcW9lQzl6eTlOcmZlRkRfcWpDU2h2a0dLdHQteldWSkptN1VJNDIwTFM0TEp4ZkU5Y1BwSHdEWkJ3SFBIakll?oc=5) (Wed, 29 Apr 2026 11:18:33 GMT)
- [Tether leads Belo&#x27;s $14 million raise to expand stablecoin payments across Latin America - CoinDesk](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNazE5c2RJQzZyZXRSUzVaWjNYbExkRi0wc2VZMWg5YUllRHkzSldqbmZJV2xpRTlvSEk5WGh1QmhueHBSLWIyUVAtZjJuTU5mSnI4ejVPUnJ0YTM2T3MyS0MwQW8xQ2VKUG5PVHdpa3d6WHVaTVhBazNaMkJNMjBTaEx1QTFZdUd4ZFc3bndSNlhMaF9jWDhUMEIzR1ZxbWJjbDBnbVpHRHpJaG1QSlBjbXNtV1ZtVUY1S3BZR2pic3Yxb2xBT3FJRTFDaFVtZHU5?oc=5) (Wed, 29 Apr 2026 11:14:01 GMT)

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
