# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-09 01:24:37 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,638,030,884** | 🟢 +0.11% | 🔴 -66.57% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Banks are treading carefully on stablecoins despite market growth, S&amp;P Global says - CoinDesk](https://news.google.com/rss/articles/CBMiygFBVV95cUxQVGctLUoxTGxKZVlETnVwakhXd293OUVhZjJDYWVVTDRZZVBzREpJeENjNEljalotRU90dDVxZDZGeDZLcXI5WmtUNlY0cGtTcnF3QlVqMVBjV2N3SGNraGc0OUltQnNlLWk4YUhXWXBuSnJrY3MycFE2R1p6QWxPUG96WWp3MHVwQ1NYWE9qaVVMcFZvX2pDMVlLMGdrLVpHRG1SZ0d3cmIzWi04cDdqeldYdGJ2YlVwX09ONHIwYjFQNG5McFUtMGhB?oc=5) (Thu, 09 Apr 2026 12:36:54 GMT)
- [Banks, Credit Unions Face Setback In Push To Block Stablecoin Rewards - CU Today](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOVUNQbEdJTURHMjlobnliYkJCS1BUSG1XNzg5Y2hZWmdXOGRVbmYxN0pyM01XT3Y4dWlXbXVvUk1zbDhqVlhoRmJXdF9IWlAxZm9SNHduMGhRckNWd2xWTnlVYUI3dmxMV05OZ3JkSWprTDhNaC1CVktyLVZzd2FvMnZGTFhHYW5ocFhlVXRiS0E0V3UtWlRZZ2pSRUthaVBUVlFCTHJ0eXk?oc=5) (Thu, 09 Apr 2026 12:14:32 GMT)
- [US Treasury, FinCEN publish AML, BSA rule proposals for GENIUS Act stablecoins - ledgerinsights.com](https://news.google.com/rss/articles/CBMirAFBVV95cUxOQVpqaV83cW83RHBwT2dNVHVQSHUtRjFPT185QWxrZkVaLXByV2VjbTFudThESFU1R1FGV1dvcUhIaXFUZU54aDNSREFvekFJZ2NiMGllSlV1d2d6N2RpQzVJMUNpcGpnNVFyXzhQNU5zQ3IycjdDT0FCazJQcVlxSHhvSUN3NUF6QXdFRnJKNGJwWUFyNldLbVdySHJ3QWZkSllpb1RzZGFvbEpH?oc=5) (Thu, 09 Apr 2026 11:12:04 GMT)
- [Reg Wrap: FDIC sets out GENIUS Act stablecoin rule book - TheBanker.com](https://news.google.com/rss/articles/CBMiekFVX3lxTE00TVFITjZIdU5SclFycF8xNFVHbU1fUG9HWUxESzRTbmFnNXg2eS1iQURDSmpfUmVqckpOUmJHQmRab25DZTVuWFRvLVhCMngzaFo3emU3T3NjSzRnRjJvbFlCRF9YV0RwM2pGSmx4QU8yVmhhNFpzV2tR?oc=5) (Thu, 09 Apr 2026 11:06:55 GMT)
- [Swiss banks launch sandbox for CHF stablecoin - FinTech Futures](https://news.google.com/rss/articles/CBMinwFBVV95cUxQU1g3XzU5LXRRS3hEaFpDeGYwdFhWWlRlM2c2RWY2bW14SDFMRlE4TFhpOEdxc1RYWmlWYjAzRXRhQThZT2tfRGhsekpKTWY2M0lRdzZ2R3liWlhQdlRGc1JfaHg1RG1tV1hkWHRoaW8xX3ljZTlaT29fNVd0d3B6R0VZUE53N05ScDY3OFZ0RnlNZ05OWXdmUVNrN05PaE0?oc=5) (Thu, 09 Apr 2026 11:06:16 GMT)

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
