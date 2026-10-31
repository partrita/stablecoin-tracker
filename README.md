# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-31 03:27:39 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$284,331,199,566** | 🔴 -0.11% | 🔴 -1.21% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoins as a vehicle for dollarisation: Evidence from capital controls and currency crises - CEPR](https://news.google.com/rss/articles/CBMirwFBVV95cUxQb0Y4N00zMW5tQkVZUmFLbzFqWHBROUJvZVNiTlc5Zk0zSFlaOVpyQ2swR0dKM2VKSUhKbHJVaHpqSUF5VUI4RjlNd1MtaXQ2U0ZnUWRRTThRdUFtR0Nwak0tNE1hQ1E0eUZrOG5CVzBGNGQ0LWxYaXVvdUJDNjJ0Sm1uY0stUkVFT19lX0VpbzZrQkFBQXBncVlxWG8xYUxuM3lUNEZfOUZ0UVZBU2pj?oc=5) (Sat, 31 Oct 2026 00:13:03 GMT)
- [Implementing the GENIUS Act: The OCC’s Final Rule on the Issuance of Payment Stablecoin - Arnold &amp; Porter](https://news.google.com/rss/articles/CBMisAFBVV95cUxQelpFbi1qck9GYVo4aFFkTE13ZGN4M1ZpRkxSN1prUEluZjBMWDBJeGVPT0I0bXB6cEh3eVh5bWFKYmVxUGhyejlZam5kdlJFaHR2ZmVfc3gzUUQwdVVjdTAwTl9VcU1KazJEQ0M3b0ZhRzdNR1ZhbTRLVF9yMlhVcjJuTjQ5QWcyNHZIaERCREZfUlVad2tiRW12UmliMnNSOTh6R2VjNUVVYm9VTHlSSg?oc=5) (Fri, 30 Oct 2026 22:04:11 GMT)
- [Brazil&#x27;s Bloquo raises $3.67M seed for stablecoin payments infrastructure - Dealroom](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPbmh6VHNPSVBBMjVjOWRtekZ6VjR3M3RDSVdVYVpQVHJlcUZMaXdVNVdSSXpwa1NZaEx2QjlYVXBIc1ZEa1AzVXZEd0NSeWFsS2NqMjlTWDhWNDJtcGhMOElhdDJwWV9oTWRoci1kbk15UkRjZDk2ZzZ0MElpcE1meHVteVNFVy0ybmxnODN2bGJnVUl5Rm5BeF92cXhjRDhPc2JrckFodWdEZw?oc=5) (Fri, 30 Oct 2026 20:21:14 GMT)
- [U.S. stablecoin rules raise the stakes overseas - Axios](https://news.google.com/rss/articles/CBMilgFBVV95cUxQVk1VZm5RaFoycXFlUEFIdUlfdk9ndEdOeko5WTNTbVdTQ3dRRm8zVjM1cTVJdlpUbEx2Vld3d0wxdUxlUUhVb2k3S00xbFFkWnNlY3dyaE9ydWVFcnFlaUJVcEgyY1FMYkVmYWhSS0V0NVBpRGxmQW5qQXpGQWNBZ3ZWTFRhVlJPdkM1Z1BRS3JyUmhiVlE?oc=5) (Fri, 30 Oct 2026 20:14:23 GMT)
- [Stablecoin Payments Rails Collide With Regulation October 2026 - FinanceX Magazine](https://news.google.com/rss/articles/CBMirgFBVV95cUxNZTMzY0EydHJiZFFtYjZVVzlkZXU1dWhyVk5lSkpMbzdDSmpQOFRMN25BTmVuUVBicW9HdEptdDRJMG5FMndSa1VFWndsR0RIX3pDaElGNnV5M3AyVUlkUlN2c2dhY2ZkQU1RbWR0Tk5xNVpjcmEyMWlBUDNmMW9sTzB1emhBRE4xRjBBX0dkMHlJTWJBTGdaMU9COFJTdVFhQThMdmV4SjR3Z0lTT3c?oc=5) (Fri, 30 Oct 2026 19:04:15 GMT)

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
