# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-04 02:51:38 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$296,541,259,457** | 🔴 -0.26% | 🔴 -1.10% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [FDIC Issues Proposal on Illicit Finance Standards under GENIUS Act - fintechanddigitalassets.com](https://news.google.com/rss/articles/CBMitgFBVV95cUxPbC13SDdzU1pRNzlsZzc0VkptM1p1VGpraHlUTEFSQnYxVkdqbV9KVl9faVJJTUcyRDg0NW50enJpZHUyNWtTOEhNdDI1Sk5jUUg1aW1ENm8yRHdYbnM5b0JvOFJZZnNzVDc3aHBFNHNmeThUMmd3NW42X0NnYjlEcXlnekdhNGhxOFU1clh3SzlFNmdERHhlMUhzNE5VVzZqb1N1SFVrUW1jSmZnZ1ZoUHJMU2xEQQ?oc=5) (Wed, 03 Jun 2026 22:18:45 GMT)
- [Stablecoins Are Just Wildcat Banking With Better Wi-Fi - PYMNTS.com](https://news.google.com/rss/articles/CBMirAFBVV95cUxNajJDbjhpN1VBWGJKV3Y0TGNxbjFfMERRR0Z3UkVFUVIyWVRFNGFfSTdKLThfdDlUVFZQa2RlZXcxbG8yNW1vdVVVdHEtYWhRVjctS3ZKNzc0QzdNVFRjd0hnQnJJUUYwWDZ0YldMUXYzVE9KbHNScUlQcEFkXzR0WGNzNkdDRjNNbDdyYzRyd1FFa1ZnUjk3dkNwZTBVMXpLYWVWMFZmWEJNU05z?oc=5) (Wed, 03 Jun 2026 21:13:56 GMT)
- [Tether Debuts Tokenized Gold Stablecoin Visa Card That Pays Out Crypto Rewards - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxPWHVzaEltNURpWThuaFJGQVJ0c3kzRFV4QlByLUFDb3ZnQkZCdzd3dXdvWUc2MGRpcUN2TC1vMHN3Ylp2Y1l0Y01WdjF5bWp2UTBqNm5RLUJ0Q0hrZm5IVk9icXM2dThMbWE2VU9OWVhTMGpnWHJuSjRyZGljS1NxSDFfR24xSkN6SlZodGkwa2lmZFZnaklKN2FZczRaQ1BsVTRqdnpkVQ?oc=5) (Wed, 03 Jun 2026 21:03:50 GMT)
- [GENIUS Act &amp; Stablecoin Regulation FAQ: What Broker-Dealers and Banks Need to Know - Nasdaq](https://news.google.com/rss/articles/CBMizAFBVV95cUxQM203amVKWFFCU2ZmNFNDcWlkYnZHYVpfNk9iMjR1VmNtTENFT3hoTEFUMk9FSEhkMTVBd3FGWU9MZmRBMXBTZnZsSjdDbUhvdDVTM2FxV1A5TnpBeGZFRVlRTEk1UnU5TnVOcF9fTVQ4VUxvUlp4bkU1Slp0NnVPM3FXVnZHWjZqcDI2UmQ5WFJ2WC11WjF5bFBuQTQ3bUlIWmdvVG0yS2NiZVQ0VlBVcFk0SWYxaC01UXpIaWpZRFJWcXF0RlptSDVJamQ?oc=5) (Wed, 03 Jun 2026 20:35:10 GMT)
- [LATEST: US stablecoin issuers to fall under BSA and AML rules - AML Intelligence](https://news.google.com/rss/articles/CBMiowFBVV95cUxOb2pPWU5XRTdjd1Zxa2M2VjFxLUtBUnlVOVZIeDBHay1KbEtQWUF0aXBwV0hPbEpWN3UtSThPQk1Zbi0xeUt2ZTJPRkRhTWNZV3VZMmgyUHRuVElGZXJDenNmbVBvZUZ3bjNVSk1MUi14R2pWSzh6cTNqdGhRNmU3VjgyeWZ3ODc3MnNDZGpRRE9RZjlDTzFWRW1tMVM2SjJwRzU4?oc=5) (Wed, 03 Jun 2026 20:31:57 GMT)

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
