# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-26 02:28:50 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$287,516,167,709** | 🔴 -0.05% | 🔴 -0.74% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Standard Chartered-led Anchorpoint plans retail stablecoin on public blockchain - South China Morning Post](https://news.google.com/rss/articles/CBMi2AFBVV95cUxNeTJ4ZDQxZDFSemN2N0xnVzVvaDA5T3JVQmRfc2NZckJnSWlmUEZyUnZpMkRfY05KTnJpNzB3UkgwRUtaWVh5R1hma1VWTzhCWUFCYnRoQzh6WjZWR25CVzVyMzRVVDg0VVVzUEVobm8xVzN5OVl1ZnpkXzl4WUVIenNySzlxZlVPaWVNWC0xcVBjcnhhR1J4S3hPR29fUmVSQXIxamhMc3A0TDZPMTZ0QmM3UGN0Y3BnRzF4VmpQS1VLODJsVHF6RjJWUVE4b1QycmNWeG9kbknSAdgBQVVfeXFMTW5rbDVaVHE0YjEtSGdObDd2VFhBZWhwVVBEZ3NaSVhhcWJZRm9wRkdLeE1pUFZnZ0JoVEswRWUyNlFORUdZQzVFVlhKWndTd2NkSjBIWk9LRGsyS0RZbDBQaTJlRE5rT3NCZGU0SV81cldtOTRYZmdzUGdQSUktaUJvN1FMbm9SRHk0d1VHSGM1UGRTTl9mMk5rOWJxdG42d2JrMURlTWFGNzZGY3JSSXdvNUplajlqOGowUzJBYzduQWlLM0FJem1MTEptR0R0RmpYMHpRTjNr?oc=5) (Sun, 25 Oct 2026 23:00:15 GMT)
- [Exchange Stablecoin Reserves at 60.6B, a 12-Month Low - CryptoQuant](https://news.google.com/rss/articles/CBMidkFVX3lxTE1jQ21HQUNXMkZNaDJkTkFlZ0xnd1VMcExEUExOamstYjc1RkZmMzNzbDYxcTBDWmpHVnZ1OVdYYVVEMkdfSTVSZjRwbzAwQnVqZ19BZjktUEtTS1V4R2VFTTZrMFBEcDRaTDRmbXgwY1k4MFRhRnc?oc=5) (Sun, 25 Oct 2026 20:04:44 GMT)
- [Bank Lobby Presses OCC For Clarity On Stablecoin Rewards After Final Rule - TradingView](https://news.google.com/rss/articles/CBMiywFBVV95cUxOb20tbzM2WFdsY2w4WV9uZkEtWnVfU2hhZkh2UEs1Q05hZjdmbHRNN01TUlplaWZpVnZkUUNEUlNfLVR2N0ctX2VOb2IwR0Z3b0V4dWlwbHpUNm1OOTZ4Qk5VeFRpVEZaRjFMNDdyUW9TUTlQZXZUaVZOYkV0cE1zZ19HR0N6LUY5dzBLX0dlQzZZZnNTRHljNnQ3ajNmNzVBNkVZUnNHTnp4ODlKVTdsNUxtZk43Q21NZzhPSk04YTBhQXJ6ejdqTWNTdw?oc=5) (Sun, 25 Oct 2026 19:00:00 GMT)
- [‘This Is The Blockbuster Moment’: Credit Union Leaders Warn Of Risks In OCC Stablecoin Rule - CUToday](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQaE9rakNSenVVdWduRElWNnp6ckRnRHhLVkVRZ2o4N1JoUU5hb1d3MWp5R3VOUWJsdkpRTG45OTV1Qms0c04wWVdiVWU4LVBpb2REanB1djhFcUl3MzJDY3dSZHNER1BBMWtEcm1nQ2VtVlZONktpWHhqS3VJc05MbVF1Nkg5ejVuT2RDNG5KdEJGVEFUT2FlVGRtNGUyNmdyRGRSS1VpRWp1bHVXcVhmdjhoOFE3TWkzNUZIcEgwb21yc0U?oc=5) (Sun, 25 Oct 2026 12:51:49 GMT)
- [Reserve Composition and Design in Stablecoin Regulation - orfonline.org](https://news.google.com/rss/articles/CBMimgFBVV95cUxObF95UUtJM1NodkVkNGVjUmV5cW9uZnJsdDdMYjkzTVhlNmFXNzE5NWJxR19mdExJQTg5UXA3cDBNQnJBZEZDVl9vNmI5RGcxZTRxTU5xdVlqQTFxXzRwa250YlNUdnZNTWdfRDlUTmF3M2Zha3pIdFJjT2FydUhKRS0tVWVDNEFUaDZiZ2s3NTluYXVWUm55MEJn?oc=5) (Sun, 25 Oct 2026 05:48:40 GMT)

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
