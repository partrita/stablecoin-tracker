# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-05 04:27:01 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$281,424,453,289** | 🟢 +0.09% | 🔴 -1.42% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Western Union Fights Revenue Slump With Stablecoin Card - PYMNTS.com](https://news.google.com/rss/articles/CBMimAFBVV95cUxQNmhGWkhCdk92YjNzTkhWbzZnNGJNRGQyaDdia1RWeXBLdHpvUnZsWXJrZ09FUlJJZUFYZERrRElPWlExQk1TZmZSNFJieE1RNlRlN2lzbE1WYmdkSWJJa0g2eWFQVWUzSGtra1ZIZlE1bHVpRERMYldrQURFM29xU3dqVUo0dGVQY29oSFByVDQ1QVJWQ29pcQ?oc=5) (Thu, 05 Nov 2026 02:14:51 GMT)
- [Stablecoin adoption hits new highs: Tron reaches 76.53M holders, RLUSD climbs past $2.5B - AMBCrypto](https://news.google.com/rss/articles/CBMirAFBVV95cUxQMS1PNlV5TkRoZTNOVlRRRFNxa1Z3Q2p5WkdDUFNvc3ZRbm9IdUpiTklrTWdDeEdFMVZuLWZVU1JXV29ZeTNra1RSSC1XVHF4T1NmRnAxT1ZJNm5jLXhXUmhQekV2dUx2R1ZOQWxtRHNlODIyVzdUcHJhTXFVc3A4aTNaV2lmelpLTmhzaEk2ZGJETFhsNjhReUhOTUwxVy1DTnJUZDZraWUyNjgy?oc=5) (Thu, 05 Nov 2026 01:00:17 GMT)
- [Circle Reports 17% Revenue Growth as Stablecoin Payments Network Expands - Finovate](https://news.google.com/rss/articles/CBMimAFBVV95cUxPMXhVOGt5STVZV0NGc0VFbi1qVWJDeHh6YTdaSkNSZzZFSmZHNUVnMGNRd1NQUTRuWXN4VkxPZjI1Z01CdEg4cVZMbXhkSE9tT2drSTcwWWcwYzNqeDZWa0I4ajVLaVNSN3gwY2hMUmR2RzlkdjFzZjlXSFJWb0VIdlFoSTZzbC04SDNkYnpVdUJhdFVaWEw3WQ?oc=5) (Thu, 05 Nov 2026 00:22:22 GMT)
- [The Stablecoin Era: Canada Proposes Stablecoin Regulations and Expands the Payment Regulatory Framework - Borden Ladner Gervais LLP (BLG)](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQSGdDd3Y2S1BtbVBtaEs1eHI4MFRpQlBueUgwV1VwOU1NY1dGOEt1TkpYMEdzbHQ5WlIyUV9wNnFfX0JTcy0ta2VUVkM3cnFKUjFHSTd5WHRNUmFiZWdUOUk4R09nbTJFM0V1RmtDTGhLQUFUXzlKSnJWQUFiTXFEYi1rWGN1QVNXNE5iUGlOOXV5YWF5bFFRZ2VWSXZUdG9QQmVLX0JDQWlLMzhSUmQ3QnpkS0ZaMDNaV0VwMUI4eXhxLTVucU03RklKdmlPWTlDNXRFcA?oc=5) (Wed, 04 Nov 2026 23:59:38 GMT)
- [Tokenization and stablecoins may weather Democrats&#x27; sweep as broader crypto rules face uncertainty - CoinDesk](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQdmswcTRmQmFqWFhPeFdtY1YtUi1ZUDU0WENyejFNZS1ENkVOdWpJdXFPLTc5ZXh1dUoycHEycVpGUGpnOHJidEc5TnRTTUt2XzFRd3A5b19DNXNsMmJWOFQyR3hhMF9BM2tCNndxQ1ZVbG9iVFZSY0tleHRodllQSUhlM3NqVHNZQnhkX2JmTHllenpJUUNJNV9YTE51ZkozQkdEazVYX0hhMS0zZWVjU2Z5MU00dURVdldBeDlxaFlha0FJRGpXcWVOU19zOFdfM0dRamFOTQ?oc=5) (Wed, 04 Nov 2026 23:21:04 GMT)

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
