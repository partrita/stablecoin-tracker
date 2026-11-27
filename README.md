# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-27 05:58:28 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$270,845,728,132** | 🔴 -0.05% | 🔴 -0.39% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Visa and NBX plan stablecoin-linked payment card - Electronic Payments International](https://news.google.com/rss/articles/CBMipAFBVV95cUxQUl83RmxZdWdodGhrVEtBRm4ydVVZS3VHMGlKS3N2OU9ZYTMxR0FLWUJqQm93cWluWi1PZ1c4cF9tV1NKRGlVWjFjM0R3T2JCdXBJdl90VXpJTlFnQWtxdnpjOVVINkxZRlozSUZ6YU5zTU1TWEo2S2laY0hCZlRRYzVJdElJc2ZTQmkwY0RZckxpS1RHM2x4N1pZNVJ0dk5lN1JKRQ?oc=5) (Fri, 27 Nov 2026 05:48:39 GMT)
- [Ripple&#x27;s lending plan moves closer to tapping XRP Ledger&#x27;s $800 million in stablecoins - CoinDesk](https://news.google.com/rss/articles/CBMizAFBVV95cUxOY0k5aC1VNWtUdzd2MGNURlNHQ1dCNndEY3FwQXNvMGNXaHVPcFNpX3NYSTYtcGI1SE9Fc0lwVGMtX0ZtWDY4UmxoVXRfdmFLcHAtbGtKLTV2RG11N1Z2YThiWjZ0MUF6V29TNld1SlBaS0NsR2FhM3Z4aVZ5WVdkY2MweUgzS0RoUmxPcU82VG5qVXdacUhCZXR2a3I0X3lIT2M2WUpZdmVSSllnLTZzSW54TlpCc1czUkVQZTYwQ0pIX0QxT01kbkhaVjY?oc=5) (Fri, 27 Nov 2026 05:12:38 GMT)
- [Bank of Japan executive director stresses need for stablecoin frameworks - Crypto Briefing](https://news.google.com/rss/articles/CBMie0FVX3lxTE1HYzRhdVRtUnNLYWk3aDZuNXNmeWVadG1EbGplMlYySWtGLTJNRURQdkh1ODA0UFJPaHBCanNuTl9xS0F6UkVfdEhCSWlXYk91MHkyVEJiVE9ORlNwdzdSWnR3c2M5LVJZdW9HcFJYVFJDZVBUb1lZam5fTQ?oc=5) (Fri, 27 Nov 2026 00:57:44 GMT)
- [The chokepoints Europe cannot see - CEPR](https://news.google.com/rss/articles/CBMibEFVX3lxTE1saTRpV3U5NFladEJvdkJlcmozUVpaUF9vODAzcVBGX29wS2RvZExIRTk2ZGJERHduYW5wcXQwU214TlJ4Y2diN05uZTRzVmM1U0ZEaTBFZEdIbUkxTTF4Z0gzSGpoRlV6dFR4Wg?oc=5) (Fri, 27 Nov 2026 00:24:38 GMT)
- [TRON leads stablecoin market cap growth with $195.5 million daily gain - Crypto Briefing](https://news.google.com/rss/articles/CBMieEFVX3lxTE5wWkFWNTV3QTFCY3l0M1JuX1duM0w3UkVSaW5fU3J1S1ItNUVnWEhHMC1KUDNYcnY5XzBFSktDMlpodjRVbm8zVEttbmdYY2hZZUVqeS1ucUpNdTczazc1Z1dGSjczTEE5amJGS1VVQ05JRlVLT2UtVA?oc=5) (Thu, 26 Nov 2026 21:59:31 GMT)

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
