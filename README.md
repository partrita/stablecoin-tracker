# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-10 02:18:44 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$291,024,022,223** | 🔴 -0.05% | 🟢 +0.38% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Nacha Launches Initiative to Explore Stablecoins in Money Movement - PYMNTS.com](https://news.google.com/rss/articles/CBMipwFBVV95cUxOOEdvdFJWS3JJZGdpclh1VHp0dThnNE04WDNLd0JDMVpBazhuZW54UEl1US15Ykw5N2VBV3FIdVhyLVZOLWlFU2xoaG5IRmZlUlFHTENXZm5ueVB1YWFxOUxab1NMa2FOSTdmdmQ3SVN3cTBwMG50VGlOUDAzdllsQjY4ZFVJX2ExakI0UXpjYnFfXzlnaVFFSEhpLWdac1ZQNmwtUlBOOA?oc=5) (Thu, 10 Sep 2026 01:07:30 GMT)
- [U.S. Bank Completes Cross-Border Payment Using USBDC Stablecoin on Stellar Network: how 14 outlets framed it - NewsCord](https://news.google.com/rss/articles/CBMi6gFBVV95cUxNVnEyXzN0dUROcE9Ndl8wZHNFN2dadnJPN0ZvMUxpSVBFQnlLVGNoeXJUbVdyZG9lbHpYRFhna3QzWGkwVlpEM2FSRDVJclR4TlNjV1B5VFNzZGFTbzl6STlhVXZCOExrMHI4ZHF3bTdMeFBKLVlFOWZsd2l0Y3FJa0tuQV9nUmFUcGF0SkVfWG1ZeDlUYm1rVmNGLVM4OUYtdDJVc283SXhqMHJpSTJycGlrZkdvSndLY3JQblA1dGRhd1V2cW5XeERnaWRmZlNOOGhpSk95SU14bHJ3NU8zeTc1cEpJcmc2eEE?oc=5) (Thu, 10 Sep 2026 01:04:08 GMT)
- [US Bank pilots custom-built stablecoin - Finextra Research](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQdFFzOGc2dVFtSENwQ0tnNWVGQVpNZ0ZDNURIdjk0TF84bVFfNHZJTkZvVm8xWEhKZkFXdFAwZk1SWndOWnJKV3ZzQ2pDVUtMYlJlZUowRHdrTjN1VTc1ZzZZUTR2VE5QWUtyTGVJWkg3dTY0WExSUldBXzlJSzMzVk8yWmpRN0hL?oc=5) (Wed, 09 Sep 2026 23:01:56 GMT)
- [MVB Partners With Velocity for Visa Direct Stablecoin Settlement Pilot - PYMNTS.com](https://news.google.com/rss/articles/CBMitAFBVV95cUxPR1dDWjV1YVJseXZLaGVZSVZuVzViMHpzc24wSDd4UUZ6LXFvaUpTM202M0VCSHpkZnNfNndHT3lRZ0xVV1Rrb29oQjdhaS1RcFQ2ZmhjTnZZVnJoVmZ5c0U1VTlwdDBWZWlMZVZmZWo0V2c4QmFkLWI2TndxMzFyaVZyZE9zYkRDRE5RZjRUYjg2WEdUUkJkU2tYWUVOQkx4ajhHd2J1X1kzQ3JLRVJ1X2pTV1Q?oc=5) (Wed, 09 Sep 2026 22:49:38 GMT)
- [Crypto Group Seeks Changes To Stablecoin Customer-ID Proposal - CUToday](https://news.google.com/rss/articles/CBMinwFBVV95cUxOXy1FUzQxSkxreXVxN3VLU3VMS3lQQjhYM3FYMmItSjYwc1JRdFRiUTB4bjlCRGFxTFMyU182VlRtM2k4cVd1SThnMV9aZjhEVjNGNS1DWHpGdU12cVZpRW5lV1F4bFJRaUJHYjlTa25yTlp5eVBKaVl0RkMwUmRYWm9pZFpWdEFHTGNnZkowMUlkQlFqQ0U0ZlJBXzZLVUE?oc=5) (Wed, 09 Sep 2026 22:49:00 GMT)

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
