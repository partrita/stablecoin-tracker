# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-04 01:26:48 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$289,923,587,636** | 🟢 +0.12% | 🔴 -0.75% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stablecoin Rewards Remain Roadblock to Crypto Bill After White House Summit - PYMNTS.com](https://news.google.com/rss/articles/CBMiuwFBVV95cUxORndFZGdjTGVFSFU3TXNMUmQycVB1MHpUR05YbWhENS1ULWJlRXltanVUWGNKZFlBVmUtOEUxMUY4TGxackx5ekNYU3JJQTgxTVJSRW5jM3JfOU5IbkJUamlfR181anpsN2NGeXRZZHBPRkZvcjVFSkRjRUNrNml3ZmZLNkU0RnRnbXVKVWhJN0xUQjJ5MmxkekFzTVlqcDA0LVBOUUJjbWNWRjl1STY0Tlk4ZHZObmhza01v?oc=5) (Tue, 03 Feb 2026 20:37:10 GMT)
- [YC startups can now receive investment in stablecoin - TechCrunch](https://news.google.com/rss/articles/CBMikAFBVV95cUxNU3A3cUdRVk53UU0zSlBiRUFRNDVtR3BrVVVId2FTMUxQa3duaTVPMUsxQU1mVW5GT1JiMmZnakItdmdGVFpXX0UtMUdoa3pNaFlmWFlERTVBSTFOUTdVX0xqaTJkcnNUdmhPczl2YkpUWXFlMmhxa3F0Qnp0UGtTOUMtY2xWbzNjQ0p5MS1QZzk?oc=5) (Tue, 03 Feb 2026 19:54:12 GMT)
- [Stripe’s Stablecoin Expansion Faces Sanctions Scrutiny - PYMNTS.com](https://news.google.com/rss/articles/CBMingFBVV95cUxNN0pad1NKZjlYNVpWYVRkZkpSN3IybWtnc0RnRkdORGlZcExnU1NOZURWUGxjYmZmOGR2Y21MeFN4TlZ5cF9IODRrWklWY2NCT3p1bzdJSXhpQzVHYlZwZHhOMHEzWjhGQlhQTjFhMjlub0dTUlRWQldIWkhNcEx2M3R6aTU1MlhhVExVYnVFN3dJM0lMTUEyZEZjSnp0QQ?oc=5) (Tue, 03 Feb 2026 19:02:02 GMT)
- [ING Groep Links Crypto ETNs And Stablecoin To Value Story - Yahoo Finance](https://news.google.com/rss/articles/CBMifkFVX3lxTE9Ydmp4ekw0QUtoLURjSWlyVHFuNjU3a25aUTRDZU9ndGNYbWNJa1lZenl2cjVOTWc5YTlpRk9TeXVyRXM3TXRYenF1ZTBoZHpFVHp2SFdxYmtsaVZxdHFxOHZLLWRaRTVIUEhpQXJrM2hfZGd6UmJQN1VEdFdjdw?oc=5) (Tue, 03 Feb 2026 18:18:28 GMT)
- [S&P projects 1,600x upper-bound increase in euro stablecoin issuance to $1.3 trillion by 2030 - The Block](https://news.google.com/rss/articles/CBMixAFBVV95cUxNcEJjN0JvM053ajBZYkVxN0E4c0E1S01RSXZMejROXzRNYXVFbUIteEpCeFdTSF9YWF9zbUVWRm5EYmNkRl8wOF9mdUVPTnRzU1JpTlg1NjRObXJyVUlWelRiMG9iZEpKNmlVZkJBcVdBcE9VbEl3MVdoZERsa3JoNGZmNHAzNHJlci1jdjItSUYzdEFJVGx5WnBoWDV0cHAxSHgtVGVNRjlPcldNdFZWY0xtbU40dmxuYVJlM01rNHB0ZmMw?oc=5) (Tue, 03 Feb 2026 15:42:55 GMT)

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
