# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-02 03:19:48 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,934,458,752** | 🟢 +0.18% | 🔴 -0.25% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Fiserv Digital Asset Platform Goes Live With Bank of North Dakota Stablecoin - PYMNTS.com](https://news.google.com/rss/articles/CBMitwFBVV95cUxOR2Nnd1l1UFM5SVdVOGpjZk53SEdxRzdCd1NnczlQVjItajRqLWM1eGc4bmVZa1NiQlB0cm1JeHg2a0w5VWhpRkx2dW5tOERMLXFiTTZLWE5hSEpMc09FTFV1QXZ4SUJuZjNYcnlJOGdhaml4cVZwbjdCY1FPblJHZEdQTU41M3hVS2NsWWxfMEw4UjhaMklNTDJ4YkdzREJxcG5BU0pQbTZnbE5Rc3FxX3dWNFdxR0E?oc=5) (Fri, 02 Oct 2026 01:08:39 GMT)
- [Exodus Movement Launches Exodus Checkout to Enable Stablecoin Payments, Debuts with DGO in Latin America - Quiver Quantitative](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQcnhNQzZWcU0zQTlVNm5ERDUzaDJtczB3TENNLTQyT3o0NlphTldZYXVXMUt2WU9IZ1B1WUJIQXhkUzBLYlZ1S0hydGtaQzlCN2E4YVZ4Ukx5QXhoMDFIcDJsdEdjUWdlZmpkZjFxd2VfaXRnNnRlcTNZSFA4UkpDM1FHUzFCOGtpWUZLUW5XM0lsTUdIS1EzOUFTQzVYQ0ZEOVE0OGFNcGJ2czR4WFFBNlBYd1VWUXo1ZklIaEJuNHJWV0xHSkRycnJtbHRHNkJXTDRHVF9R?oc=5) (Thu, 01 Oct 2026 22:40:00 GMT)
- [Eligible customers of DIRECTV&#x27;s streaming service in Argentina can now pay with digital dollars. - Stock Titan](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPSzZTWUt6b2ZjLTlBaVh6LWM5d2prNEQ4NFpqM3BxV3RzYlJXcG5pQ3h1cTluQTkycDBmOGsycmZOOXJjdkdFOEFMNXB6YVYzQ3VQeVVmNGZWUmdlLWdfMlVXaVR5WUp4STI3cTlKa0pseDZrX2RRNGtLOUhZVkdRWHpacDdHRGVvb3pTM0xrNEpJSlBlUmFSbmZFUGt3RlpMYWg1ajB3OWliMlA1cm5BLWZkYnhwbUYxTElkcndURDM?oc=5) (Thu, 01 Oct 2026 22:30:00 GMT)
- [Stablecoin Issuers Are Buying More Short-Term Treasuries - altcoinbuzz.io](https://news.google.com/rss/articles/CBMijgFBVV95cUxNZkJjTDNfcVdiTEpYZHFWY3VRRzd1NHZXOGN1TXg4ZTkydHgwcldUZkczcHNkbGtkQmpheTRYcXliMlBhN3NkSFdJdF9lQm1mNm5vcEYtcWFBQVlqUWFWUTVPcy1qUk90RXZLTE4zZUVQR3NNbU9zVVAyS1Z4YnF0UVpOQS0ydEl3cjN5OWxn?oc=5) (Thu, 01 Oct 2026 20:12:09 GMT)
- [Open Standard&#x27;s &#x27;shared stablecoin&#x27; goes live - American Banker](https://news.google.com/rss/articles/CBMikAFBVV95cUxPdDQyd2lqaDRUYkw0VkVORFJuOEVXYjVVTjZMdkZZcjRoZ3BYMUM0WVVzQTdBNTIxQzVfbDNIaE50Yy0zM3YyTWFwY2VsSDRkY3FRMXU4Smh5X0ZxNlM3ekZMOFFxazlsekZtNUp6UXljTFliMkxmdDFzSFFLblctLUl4SVBDUnJSc2F4c2pSMzI?oc=5) (Thu, 01 Oct 2026 19:59:00 GMT)

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
