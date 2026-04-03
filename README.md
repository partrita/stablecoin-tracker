# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-03 01:28:55 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$296,929,940,140** | 🔴 -66.65% | 🔴 -0.07% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [CLARITY Act: Coinbase&#x27;s Top Lawyer Says a Stablecoin Yield Deal Is Very Close - fintechweekly.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxNSGNSNmQ2eWg3bS1UWUFoYVVieXBjbVZnY3lwOG9BTmJqUW9Jdkd4Mzd3MDhYdUxQRWtCM3o5X1U0NUNIVlJUOEZ1Wi04VE5oRllHNmIwTGtIOXdBRTRLRFRtandBVzY3UV96SkYwR1pXM3ZKb2JTTVN3VEJCV3VVRGZHRGgxR2d4MWhWNXJtWUpsdw?oc=5) (Thu, 02 Apr 2026 22:41:00 GMT)
- [Stablecoins Meet Real World Commerce, but KYC Keeps Breaking the Experience - PYMNTS.com](https://news.google.com/rss/articles/CBMiugFBVV95cUxNZmZfWVIzRzR3MFJPRHBVM2RiWnNsUy1jeVVLUVUyN1F6dTNJVVg0NHBjUEFzWnY5THAtejRzRHFiNzR3bU1JM3N6WXp0QUJuaUZSUFBCV2w0ZThkUThIZEx2VG8xRGpwQnJrRG9MMXBfd0hOblo0ajg4c253T0hxaTV4cVRrN2RnWkJvVkQ0djNlQlNBUEtKZDdmOUNSRXRzR1VtY3VUWjFWUWZyX2dmS3VNMkowbVNTREE?oc=5) (Thu, 02 Apr 2026 22:37:47 GMT)
- [Crypto market structure bill release pushed back as industries view revised stablecoin yield compromise this week - CoinDesk](https://news.google.com/rss/articles/CBMi7AFBVV95cUxPM1ZtRlkxVDY4NEx2cC1SMjdlOVNWQlBtWlRjeHVHY1JHYmlad1h4MUhoSHV6am1zQkFVQlhVTG51S3REc245ak5PYkpUbUU2SDVNVERfYjczUWpzb2tYeGhRc09vR1dMRW1rWEZ0OVR3UFUzSXNlTmtoVkdwS2hJZjdqWUszNnl2MzRvQkdzSUVRS25hTkFsRTQ3aFBDbFRMazRtNTAxNWJfNUd6dkFZM0pCNTIwNVJjZTc2SndLamhLbzFIaTVpcnd3UVhITlBIclVCQ0gySk5lRnBBaS1XM0plUUpwRzlCZFN5eg?oc=5) (Thu, 02 Apr 2026 22:14:37 GMT)
- [USDC Stablecoin Issuer Circle Unveils New Token to Give Bitcoin More Utility - finance.yahoo.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxObm52dFpvRWF4OWlqNFNkdHM4VE9xOXA2VVVxRVNPSkNIaXMtUEZQVW9aZlBldUFRQXdZVjhieTdEM0lLWXViTjVKR3JmVGd0bWxyV1JFYVU0VGQ5Q25EbWxRbnNXYXRjbDE4MFV6OXBhbTY0MXUteldPbmRYQzFfcVFEVVhPbVkxTWpKdEhNT3g0ek5kUEk0dHJ4U09Od21kNEY2Yw?oc=5) (Thu, 02 Apr 2026 21:04:47 GMT)
- [Proposed OCC regulations for payment stablecoins under the GENIUS Act - Nixon Peabody](https://news.google.com/rss/articles/CBMiwwFBVV95cUxON3ktSlMzWEJXbUlTNGtadDlUb3NDTGRJZmp4b0RJMmd0X3F4WkxHQlR4RXJ0UTNxb2JKeHZpZ1FUUEhVN0Vvcnl1X3FLZ2gyeEdfSEhIMGZleVBBNGFCaUJ4NVJJcW1kYmNzQk1JeEhOQnEwVVBhNkw3VzJyNXIxYW5mQlEzYlNwTERMMmhNSjI0SFhCdUdlU3B1NVo5S2pDRzdqY2k0d1EtYXVDYWxaeDJzVTlqZUhsekR4V25pNktfZTg?oc=5) (Thu, 02 Apr 2026 20:04:19 GMT)

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
