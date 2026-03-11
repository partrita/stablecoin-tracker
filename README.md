# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-11 01:15:42 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,622,124,755** | 🟢 +0.16% | 🟢 +1.23% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [How CFOs Are Tweaking Their Tech for Stablecoin Use - PYMNTS.com](https://news.google.com/rss/articles/CBMimwFBVV95cUxQRjhPb0Foc1JuU1dYQ3c0MUdyNWZFM2RpZmlNLW03SlRxZUo0anY4bXBWd2RYV3lVMXdSOVRoZVRxRGVoWHJpcFo3WVlMWTdyaFlZdGk3Qkp5QVNjcXJ3c0p4eTVYS3BISEZXVml0OHpnSGV2TXpIa3BycW1FeXgtMVZQUWRPbVlLR2xTZ3p3THFiRWc4bTh5V3p5TQ?oc=5) (Tue, 10 Mar 2026 20:59:46 GMT)
- [The $300 billion digital dollar boom could eat into traditional banks' profits, warn Jefferies analysts - CoinDesk](https://news.google.com/rss/articles/CBMiwwFBVV95cUxObFFVZDhiN2FobmVDamZoSXV1dm9yd3RGdWxFNlBMbHhSZ2ZzSkZZeUZOanp3dS1yVmNQa3pObXVtWFN6eUl4STJUaDBZeEZWTm4tc2M5a3hEczJ1YVhzN3dXQWlFOXZHeW5VcVZzRGpPM0kwVEhLd01qbDYxa2pnU1hMbEdCMHYyUDQ2OHJKOUxfZzJCZDM5bnEtbWd1SHFuOHZBb0pvTVJ4NGxPWk55elZpa0gzNDd1T0MwTXRMYUtRZ2c?oc=5) (Tue, 10 Mar 2026 20:49:50 GMT)
- [Senators try to unlock stalled crypto Clarity Act with compromise on stablecoin yield - CoinDesk](https://news.google.com/rss/articles/CBMixwFBVV95cUxPTW5LdGllaHJCRVZJY1lDdEI2VFRYSDBjWUs0VmozZFdkeUUxMjR4WENWbEdnV3VFS2xsVlJNZzItNFVlbERESjNxSl9McVNSNWhrTjZlZW1DR1daOHR0U1VnVmhrYm9FajNPOGdMci15eWVNWGR1V2FHNnR2clNwUTN1Ym1fb1ZONEI3Q0dkaUpUR05qcUVabmJJVENFV3FPa1NsV3pzNVBrRUx5NjFiaWY1c2tGTVhjb0dRcm1RSHBFYU5NaWMw?oc=5) (Tue, 10 Mar 2026 19:01:55 GMT)
- [ABA survey finds consumers support stablecoin yield limits tied to banking risk - The Block](https://news.google.com/rss/articles/CBMizwFBVV95cUxOTmotbEZXRlp4MmJweHAzSWRfUHlnb1hyZUQ2MDdvWmhtSm1DT2o2RXp6aWhWbmQyWkt0TjZVVFNXdVdnakNqY2FtZG1hTUQtM1hTbHV6dGI5bWVHLVRoVUI3clVPUVd1ZVNadDNwODctZVFXQXJITG44b00ydnFyaGJrRUllVmpxZllpSXpLN1JyV0VzN2REU3RqXy15RTgxX3RqSl9ZNTRnclB2NFpaanI1NUdoeXl4VHhneHBnUnJxOHhvSTlrTElmWGlvdjQ?oc=5) (Tue, 10 Mar 2026 18:44:59 GMT)
- [Circle (CRCL) may rally another 60% driven by stablecoin adoption, AI agentic finance: Bernstein - CoinDesk](https://news.google.com/rss/articles/CBMixgFBVV95cUxNOE9jYzQ5Snl2MThQVXZoUkkyMHJfY1lnOEU3aU8wa3BMbHpEdlJxVzRwemNLcjExYUNXWlBSbVVMSjZPaFRoc3J0dG8tVjFpSFFuX05PR1ZrZGpqZkNuWnFkaWZvMUJoNklBejhzbkhXeTQtWUpIZ3BIR2NnT2lEUW5VSUhCNjJUcGVwUGRDSzAzSjB2ckM3VThoODNLbExjZVVVdXZGRDRpMHNSWEs0NkpEbGF4aVRwSE9KejNNMVlRclpVUmc?oc=5) (Tue, 10 Mar 2026 18:34:47 GMT)

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
