# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-04-10 01:48:31 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$297,828,539,073** | 🔴 -66.65% | 🟢 +0.30% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Stifling Stablecoin Yield Is Bad Financial Policy - Forbes](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOVVpZMkQySnJWZXB3R2NGdU02b1hZNTB0UnhfdWRUTXJ4UVpoZ05SeVRvTXczMjB2czhPcEt2QjRpTFB0YWU3NG1QQ1E3SGZxa0E1NHo0SW9HLWN2TGp2OXNfTEFPMzhmZ1RHemhiUnpxQ29zWTFaeGRPd28yb1U1Mnhkd2VZclV1a05xS0RYTkhUMGlHd1BydG5RbDk2S1d4RExvY09CMW8?oc=5) (Thu, 09 Apr 2026 23:48:53 GMT)
- [FINANCIAL TECHNOLOGY—Treasury... - VitalLaw.com](https://news.google.com/rss/articles/CBMikgJBVV95cUxOcmpCYm5wSWxJNUVBU01RTDRLbFF5Q3R6dWgwcVdKeklpNHRNYXZGa3JPbmJYU2d5QVJlMjkyZTh1ZkdZY0h5TXNfeWhPQTY1OXZWS0E4ZTgwWGVMWHp3OFlWcFZnbC1xSDRyNFV3WlJidEdtUDlZWGJlR29saXBLeDNqaVRfRHU0QzhyYXVEdnVrS2w4NE9VRjYyNkNtZnI1dFhuWnFaNnNWbDlLZExSMUZ4ZXBQRXlzWFJFbEtwU2dQeXZndFpDSDB6TkQxeE5EVUg2YnAyY1hpcnU0cmNaSXdsMUp4bXA4eWZXdmJIRHNRa2RTQzN1U3NSUGwyLTRHSGVVbV9JdFdGZnljcllfZHBB?oc=5) (Thu, 09 Apr 2026 23:14:52 GMT)
- [White House and Crypto Industry Fight Bank Lobby Over Stablecoin Income - The New York Times](https://news.google.com/rss/articles/CBMikgFBVV95cUxOVk5penlDYURFWUxHOHg5cmVlWFZJX1NEQW9haTQ4THYyZ2xNQk0ydnQtSGplS05ZdHNJVTFXcHgwanhTNXJWdjh5bGVfUk9YNlB1ZWdWNzVranNacXhsM0VNZWFRWncwRHRyb2FWLTVXVHFCS05Ub0Z4c2I4bjVOeElydmgxdkp6UGVheFk3MTF1dw?oc=5) (Thu, 09 Apr 2026 20:54:05 GMT)
- [Inside FIS&#x27; plans to meet banks&#x27; interest in digital assets - American Banker](https://news.google.com/rss/articles/CBMilgFBVV95cUxQZGM5RzBJSWpYNndBZ3lVXzJSaDVLUTFQOHZDSEVaRlRXQTNHN3pnQ0twa0xyMjlHak5yeDg1TWhQc2xTSFBiOE1LTW14Rm5zRUgzeUlWSEJzNVRNYnlaUEdHb29QOXkwU2lmOWFYOXRJSXN3bDBxUXpSeGlDd0h6YVdnOWtrSlo4ekFmZ3pNVmRsRWV2c2c?oc=5) (Thu, 09 Apr 2026 19:28:00 GMT)
- [Stablecoins could reach $1.5 quadrillion by 2035 – Here’s how - AMBCrypto](https://news.google.com/rss/articles/CBMihwFBVV95cUxOYkM2SHVDcktZeGtFMmlRYmtLWEFOZ3FhQmMzVVgyeW1TTjBfeGdob1h0TExPRlpUR2NVZ2dmc0pLVFl0RXJaU2tGTVZYUTFNRDhsaWV5djYydHZGMUxuNi1PUXE2ZU5QczBmSmVDM0xad2VBWGVSQk92Mkp5amdaVVpZdGZ5dTDSAYwBQVVfeXFMT1V5VkVJTUJ2eXBnUjZRTW5NUjZCM0puRlEwelUzUk9Ub3dxZ1dXVVR3TmRhekdaOFlQc1hSM3lpY0c0dEV2VzJjdC0xSHJTN1ZvMzYwUGFvVG5YaFdzZ25mOFFWUkFoQ245QlFUbGMzMFpOeGkwTVRwaVA0RlREbng1d1Z5RXo1NUtGbmU?oc=5) (Thu, 09 Apr 2026 19:00:29 GMT)

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
