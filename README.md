# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-10-08 03:44:57 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,177,306,979** | 🔴 -0.25% | 🟢 +0.27% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Samsung Wallet to Bring Stablecoin Access to Eligible Galaxy Users in the US - Samsung Mobile Press](https://news.google.com/rss/articles/CBMihgFBVV95cUxNZnpfOFJvUl84TF9rZExZeU9rNFVUZE9mWDVuRklpOGxlTml3ZFZEQlJsY2hCV05TdUtnRDRiQzJXU2F5WjRqUHNhcVFvZ0xBckpPUlhnLWRtc0FHYkZoWHc5TlBtNHJGZHk4ZHFRLV9XZUFNUTNXcllua0FzLXBpZ3V3MzlGUQ?oc=5) (Thu, 08 Oct 2026 02:02:16 GMT)
- [Stablecoin Push Altering The Investment Case For Visa Stock (V)? - Simply Wall Street](https://news.google.com/rss/articles/CBMiywFBVV95cUxORjdvRWptMmduUjJ4NGRkRnV4eUJ3RGNtTFQ5YmppRFhFU0R3ZnRFWFpMRkpGX3VZSjMtdmVIR1I5Y1FIWFV4OFY2WlhFZnp0Ql9QVUFMNlVNTHl5MC1YeWVoQkQxcnNKSVFMZUlFM1JzbU9qamIwamRYX2NXcFgtaVNLTVVGSzk3dFQxR0dnWEc5cnZ5WnJXdGQwRXVCR3Fpc3JMZUJKa1BQM21xQS1xYUtkaEUzcDFhNlBuT0VVVXg5VVd0WHdjS3NWWdIB0AFBVV95cUxNS3hCaEZGcnRUWEhWUmUwYXNxM2dDOU0wWE0xY0FGc29YOVpQckg0LVQ2WEc1UHBFM0JFOEZ6N3o0SXg5emEwSjI0Zk5Sc3JLdXNaWkgtanhLcmpuQk5BVXdrSzJiY21hNE54MHZZX0NLNDFYeFF1RlBVNl9JSDI3VkE5RXJ1ZnRQaDZ4Z3FpcEowMUl2bWxkUW9vVF9hWXNmeXQ5ZDJmSEJsNlR1YU9vWkVEaDJDTmZ1eV9WMmw0Q1hUelluSVlORDR2OFJiR2pk?oc=5) (Thu, 08 Oct 2026 01:41:57 GMT)
- [Anyflo exits stealth, acquires Sui&#x27;s Native to simplify stablecoin payments - Dealroom](https://news.google.com/rss/articles/CBMirAFBVV95cUxPV3F3Tm9QWl9uSndlSzNzSU9mbFpSTG5ZVXlEdVA5aHZkRkxnTmh6aFhSZWJfbmdxbDZ2dWMxbmZydUxGdDZPS2VmTkdPMFBVWTJfU2kxdTJmOVBqLTh2UnJuNllidE5WLXdTNjFpMm9rMHFhQTBoeGhvZ1hHUnFYa2lZbmVnWl8wYVRJYzYwYW1yeXBKU0lTZGdhV3pFUkNoRW42UlRVVzNUY2R0?oc=5) (Thu, 08 Oct 2026 01:39:28 GMT)
- [Anyflo emerges from stealth with acquisition of Native, to simplify stablecoin payments for enterprises - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOclk3V3BwcTB4d0xRb2I1bGhzWlRoRHdFVDJvUGJGZkhyeUJsb1FtQzB6ZHlra0R2NDJubmpjU3lRcl9DWDlpVVNoZi1uR1JveFhGVGxaRGxwY1ZqNTNUeVlCZXlJbnF6c2dFbFpDbVNaeVU0d0tnVTB6SHBVdnZiN2FUOWhCVlRlYnIyRFRodFBNVjk1N2FCTjRSZWZSVWhVVWtCQUMzYkZkdw?oc=5) (Thu, 08 Oct 2026 01:00:00 GMT)
- [North Dakota Lenders Report Faster Settlement With State Bank’s Stablecoin - PYMNTS.com](https://news.google.com/rss/articles/CBMiswFBVV95cUxQUnl5U0Fway1EdmVuTGMtdkgwTmlFVnh0OWphVGhXWHZycEhGY0xUNm8xNm9HMTJRYW1lZEc1bmUydEVxcC1KbURKczZreUZYLWpPU0FlX25Ld1BWMTRySHBlMGRsc29MUV8tcnYxSDVBQUlsNjdja3dISG5ZajNXMXdXazVsTHhsS0FYTlc3VkdIU2lBT2ltcENrNjEwMTdqYXFiOG5VSHBldkFqUjNjeWJVVQ?oc=5) (Thu, 08 Oct 2026 00:49:53 GMT)

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
