# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-03-13 01:19:26 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,967,987,834** | 🟢 +0.05% | 🟢 +0.65% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [TruStage Warns Stablecoins Could Drain CU Deposits Without Industrywide Response - CU Today](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQUENVRmxQWFlhSC1Sc19aYzdzOFpOTTdxRWhMQmlqNnZNdkZ6dEhLSHUzdWFSd2RzS0JnY2ZxUm5BanF5d1dVeUJWZ3l6VFREbUNHMnYwR2VOTTl0VlN2S3BSbE5jYUlvVzdaSkJsZU5KYzZydnNtcDRaTk44Tk1mR0duNDUyQmthTFl5TmVqMHFWc29QUUpxQzhfSTN1cGg1UU9ReTNHLXJna2x5RFd4U3RPUmJheTB4?oc=5) (Fri, 13 Mar 2026 00:42:16 GMT)
- [Why this sanctioned stablecoin is climbing the ranks on Tron. ‘They’re turning to in droves’ - dlnews.com](https://news.google.com/rss/articles/CBMinwFBVV95cUxQVDZXSkM4Z0wtcjNnOXNFVjBIU3M4TXRtVHFqUm0zY3A5djJIamh3dlVHSXFHRFBEYmJ2RzFyRjhpQXNROHR1Znd4Z2VGQjdaYnR6aWUzaUlfM0YteVhlekZLT2N1QUV2WWMwZzRGWHgtakYxdWFvdDFyRFFZVGxja29iR1ZpemdscGt2Nk1fb3YxZlBkN3ZCMXFINHlfOGc?oc=5) (Thu, 12 Mar 2026 16:31:55 GMT)
- [Ethereum news (ETH): Lido launches stablecoin yield product to expand beyond ether - CoinDesk](https://news.google.com/rss/articles/CBMipAFBVV95cUxNc2ZRb1dJSW5DZXh2ZS1MMkJCRm53WXlVeFZEWlZhZ0FxcEhYdFdwNVFNN3lpVXdRamplZHFiYkp4Mndna0Y5ZkxuYjYzRk1Oa1NDbjVVWlg1aEZzSzVtM28xN0VBY0pDMWR1ZGdFUkVyYkZ5anVsanc4bUl1NU96bG1IZFRpVm5senU5MUVFQUFiNkRaaUJSaVlfSEhrSF9vaHRhbg?oc=5) (Thu, 12 Mar 2026 15:45:21 GMT)
- [Visa's Stablecoin Play Intensifies: Can it Future-Proof Its Network? - Yahoo Finance](https://news.google.com/rss/articles/CBMijwFBVV95cUxNLURLRG9CVGY4by0xSl93MFk3SWl4a0dORnpwTFhOOXEyTENnZVVJWVlUbENDSU9CQmtCSXhKRDBzVC1KLTNKa0JzNzE0aHRsOFNZTkFjSGJvVTVWWHRNTmFGZFpoYnJNbVpoT2NwRERPV2I5WVlfMkdIb3hoT1ctME1ocXVoX0FEdUtKM0ZJTQ?oc=5) (Thu, 12 Mar 2026 15:43:00 GMT)
- [Circle (CRCL) outpaces crypto stocks as stablecoin thesis gains momentum: William Blair - CoinDesk](https://news.google.com/rss/articles/CBMizAFBVV95cUxNa0NpcnBENm5nSG9jb0tTNVRoa3VHYjBwN216MTlodnNUWmtHMnZhOXFwakhqWEhQWk9VUmRsVmVNTTFlOWtRN2FyQ0NCUmloNEZpOEFiZ1FvYWx1THBlaF92UnE5enBFYUFEMjN1VHYtdkwyRHlDQWo5Tm13NE12SkRRbU5fbWFiVnBob0p2SUMzOEVvSnFsbDh1N3V0MlROWHZtRlUySE9lOWQ5ektERXp5Q090dTJObjg5Qjd6cnBYbmh2NTlVTnFMTGE?oc=5) (Thu, 12 Mar 2026 15:02:11 GMT)

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
