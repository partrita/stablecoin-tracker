# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-14 00:01:54 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,723,308,770** | 🔴 -0.04% | 🔴 -0.07% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoin Issuer Circle Now Runs a Bank (of Sorts). Does That Matter for Circle Stock? - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxOaGN5QlA3d24tbGZydE1RLUhtZ2JDLUNQT0RlRllFVHY1cG1XVFRuY1ZxS29leFZYS0RtTzQzVlF0OGphTHJHMnBZYW5UTDhkOFpvRjJILWtsTllkbzlIdEhKR05MNHdnb19YbV9pdnc5U3FBdHduN2ZOSENEejI3MWtmVjZPWDk0dmN5R0h6SDBURjc0RUVidEhEeURDOUU?oc=5) (Fri, 14 Aug 2026 00:13:00 GMT)
- [Chime Weighs Adding Stablecoin Wallet to Consumer Banking App - PYMNTS.com](https://news.google.com/rss/articles/CBMiowFBVV95cUxOSkg3X01ZRFlwaTRuNXZHWFo5eXZSVTMwb0ttaG8tRUVXc2FuRTU0djY2VTFHTWhjVEVjQ0pBdl9RbFhUcjFBdUlNYmxCdWpuVE5jUnZKbk5uVjBjLW5EQmNSWWxBZWhPeGFpS0UtUW1EbURQay1Ga2hTZDhvbHpsUEVlOENBelp5cERqNDV2eV9Scmk4UXlQMnc3djVwTkJwTXhN?oc=5) (Thu, 13 Aug 2026 23:22:07 GMT)
- [Tether (USDT) says it completed long-promised audit from KPMG, down to counting its gold bars - CoinDesk](https://news.google.com/rss/articles/CBMi4gFBVV95cUxPejJ6S2FfTzg5Y21CV1V0cE9nbURKaFRHYy1DOVVJZTJBYkFPWHBsVDhfNDlQdnp5dm9XTnRLZ19CbDA4VzQ0TFRlZnZxVS1KeFZXbWxWalhBUzdXWFFKUlZTTW1ISjdFQlh1YWtSX0pDVlZHTmphVnBMdnl5MVV6UFM3eG5ya01taFRiLXpNaVF1bjhSVm1Gckt3NG5XTjdjenVsVkQ5TmpFc3lxSjNDRDZRMXZIamttOWNiTG5VQ3BOYWl3aHpaR3J6bl9aVVRncWIzWUFjam1FM3doWHBpU253?oc=5) (Thu, 13 Aug 2026 23:01:34 GMT)
- [Stablecoins Dominate Crypto Purchases as Mercuryo Reports 60% Share in H1 2026 - FF News](https://news.google.com/rss/articles/CBMikAFBVV95cUxNTFFHa1RzRE13ZkY2TTN3NTlmQTd4bXFFNVI5YjF1b3hiSmVRam1KMDY2bDV0NTFzblhrSnc0QjZzM1lXdzlnc2xrVTdlY05aQzR3UUg0QTVzTTRVa19jMDl4ajRVT3J2elZDRGdJUnlrYXRXWXBVQWFsQkNGa1pfc196U3NlclA5dS1JYXE4MlE?oc=5) (Thu, 13 Aug 2026 20:10:07 GMT)
- [Chime Financial Considers Adding Stablecoins To Its App - Yahoo Finance](https://news.google.com/rss/articles/CBMirgFBVV95cUxOU1pLSmhJdm1MWF9aenZFRjZVT2hydkpZbkVkVXl3VV96MzUwRFZ5aTBYRXlXTlB5a1VzcWtTNzlCYWF0Q0JwNWhtOGt5UUwxeWhnWjBBOXl2T3FQZm1Xa0Z6dzVfNDdzbDBOWERZQjRxaURsX1ZqcW8tMWlVTW4xS3EwUDNpWWItY1p2dGpQUnltZHRId3psdWlhakFyaDZGTE5iUXBqdUlCQUZ1REE?oc=5) (Thu, 13 Aug 2026 19:47:00 GMT)

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
