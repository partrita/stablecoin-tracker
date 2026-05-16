# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-05-16 02:09:22 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$300,833,778,121** | 🟢 +0.06% | 🟢 +0.21% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [NCUA Stablecoin Plan Opens Door To Credit Union-Backed Digital Dollar Issuers - CU Today](https://news.google.com/rss/articles/CBMitAFBVV95cUxNZ3JtS1VnMDA5NGFfSVlaX0V4WmxZMEZHMWpVRzFfVEZkc0loY0ZVQkZvVVlLQmFMYzlRblIxMnhkdUdfLVMyS3hDakVtc1lybDZsTHV3RkZ6UV81aExLdElMNE45TVJ3MEJKMjFxTUJDRmg2MWcyZERrSmFLZy1udkxVR0t4NVdZRGlTOUFrRGlVOExjdkRPbm1Hc3pFcW5jYThmWEdGSUNBVFBfakJySHotdlE?oc=5) (Fri, 15 May 2026 21:14:56 GMT)
- [50 CUs Join Stablecoin, Faster Payments Pilot Led by CrossState and Metallicus - Credit Union Times](https://news.google.com/rss/articles/CBMiswFBVV95cUxPNzZpNnkwS2s2eG9HcEp6RE1ELUFKXzZOd280amUwczZZX2x3UDBGcWYzdHg1eXNwa2ZVSGg5QnBxUjJTR1IwaDhRaWM0b1RLRGpPVXNfdWN2REh5QnEtLV9nbE82clpuLXJMSFFxWFk4R3dPeGt3b1BuTkM1TF9rYlhubEJzSE1XVExHXzBvQmpoY0YyUUVUTFpmMV9NMmRlRy1MdGphTVB2NnZ1MW41dFdpd9IBuAFBVV95cUxQdVdTdDJHRnhyMEZtYWdfYkVLWE56NFBLV1NkRE95TjJIV0owZ3E0RWNxcFhkXzR4bGRueDE3M24xQkNUaGFVQm5KTm9kaUZWdGRpM2JkUkpJOUFkQ2duczR1ZU1wUklwQUFKMzR6RnB4dlFzaFJUbXFwUExYaXp4dEVkYlJqVWY2YnhLMlREODVXQW5RZEEyRG5LdWstdkhSZE5uS0ZEdFdrcF9ZaUlYNlYwOHZPOHZ2?oc=5) (Fri, 15 May 2026 21:11:47 GMT)
- [Europe Vies To Close Stablecoin Gap - Global Finance Magazine](https://news.google.com/rss/articles/CBMic0FVX3lxTE9hSUpsWVBEVzBadDZKc1BRT1NBQUNCRWIyWFdKX1QxX1VXb0VHUVljN0NLekk2cjdnWnI2dTNwSU5FN3UzSWo1NHIzVmRuOTZzbXI5RE0tYkVsUG9paWtaTG10eDB1U0RUVXBGaldvMVNrc0U?oc=5) (Fri, 15 May 2026 20:47:20 GMT)
- [CRCL vs. ARC: Why Stablecoin Balances Beat Stablecoin Velocity - Messari](https://news.google.com/rss/articles/CBMijwFBVV95cUxPYlJLNFozZHZDYzd6WFMzWlhwZDBLakNBb3J2eldJX1VCRV9FeDJiNG9vUTZkMk15WFltZ0hhWnhhMllnck5WVVBKRU54S0RNTnhKNkdkTHk0N2tOWDVtRWR1cHV2VEwwS09PMlBsdkZub3ItSVdlczc1eEVPWDF2c21FS25tc3VzQkJjZjdfNA?oc=5) (Fri, 15 May 2026 16:08:53 GMT)
- [How Stablecoins Are Crashing the Agentic Commerce Party - Digital Transactions](https://news.google.com/rss/articles/CBMilwFBVV95cUxPMXRxelR6cUQ5UEo4MjZRd250MEo2THBadHBreEE5MmtXbWc1X210VF9ZQUhiVDY5X2FlYmE4cm1jSjhoM2IwYUkzNGlTaFV1T2s2T1BtS2xhQXlsMmhQYjM1MlhGejJUWXphMi0wQ3AyY3ZjWVRMVmVnNWZKeDdXZmZLd09oZW1JcGdKUnpXMDluaHRxakdR?oc=5) (Fri, 15 May 2026 14:46:54 GMT)

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
