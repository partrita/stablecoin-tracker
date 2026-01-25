# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-01-25 01:14:24 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,163,416,550** | 🟢 +0.01% | 🔴 -1.06% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [How stablecoins can expand financial access to the most underserved and unbanked - weforum.org](https://news.google.com/rss/articles/CBMijAFBVV95cUxNWE0zeVFWR1JkQzR0RGdELWpjLU5qRk9iR1l0dkJLWmJmd2s1d3VxckwtVmlTb3BOT3otOWFDaWhoMVlyMEI0SmtfMjVnV2gwaXhYYWt1ZXFFa3hVcXJqcm9iTUM0MTVwNzhvRVAtVmdGLVBPT2huUVY5dlUxT0EtbjVNWEtISHRfYTViZg?oc=5) (Mon, 19 Jan 2026 13:00:00 GMT)
- [Venezuela shows how locals turn to Tether-issued USDT stablecoin as governments wobble - CNBC](https://news.google.com/rss/articles/CBMitAFBVV95cUxQMUNOOGNsTGg1MC1HM1licG9oX1h0MzlCTElXMHdEVnFUbVM1a3JhdHRqTkhlUlc4WVBOODRhSHRhM1cxODJ4ZkFqZFZxZmxtOC1udnpIUlZLWFdjYzh2bzJBZjIyd0hwT2dHUi1VQWtFMEtJN2k3d2FENEt5R2VTLURhU1FBYXFFbXpjcEF1b1FlTTR0T2xyYWloZkFpbFJqTEI0ck9Tb0ZoV0QtLTVWTUIxRm_SAboBQVVfeXFMUHplazM1ZFc0UGVYbEp3OWhZcXN6aEh2UW5VMVFMSm96MWtFMDBDWjFITWdGR05fU3hvZXNGYkFsbkUxT2QtOWs4ckVSc180S0RnNk1KRlE1MjNvZ2N1eW11ZlZWTlhEd3ZQMXUydXphYmlqdmZTdGtrM2xLSW5MNUJuS0FNSml2QmVKX09pZTh6Y3NpRklxczFVQW9pVmRjay1DVVp5dnZhczUxd3hwSTJtN0Yzd3NLdFlB?oc=5) (Mon, 19 Jan 2026 13:50:12 GMT)
- [Wyoming has big plans for stablecoin - Payments Dive](https://news.google.com/rss/articles/CBMihAFBVV95cUxPOG5LMUIzUDAzWUV1M29ib2ZiZDJqTHhxVy1FUXdIZF9tQlE5c3RGSXJkNDVUOTlCaS1EbnhGX05QSDY1WU1peU5OZ3hlbXdpU2FuNkRlcFNFNlc1Vm1qV3JXb21adUMwYTh1MlA1N3ZkNGNSdy1wRks1VmpnOWFNLUhmQ2o?oc=5) (Wed, 21 Jan 2026 16:35:54 GMT)
- [Hong Kong to issue first batch of stablecoin licenses in Q1, finance chief says - The Block](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbzJJS1VmdFNIaFNCUmJOa1VOUTN5M0ViaVl3ZGlnSVdaM05xUi1sUk9XZWc5RVNFMUpfQmh5djZzdjNwdnMzQXM0ZFk0UUpsM2dnY2dRYm5teE5mYi1FdEZUWk1ZX1JIVTlWZlVVcGpKNV8yX0h6U3lmZVpYa1AxQw?oc=5) (Wed, 21 Jan 2026 04:13:33 GMT)
- [Hong Kong Set to Issue First Stablecoin Licenses in Q1 2026 - Yahoo Finance](https://news.google.com/rss/articles/CBMie0FVX3lxTE9waW0xTUprSkhvQkZfeENRc2ctbmlHR25BNzRFVUszby1EUkYwWjlGaEsyT1FIcEdXM0ZXdHVaaWRKN1NIWlROWmhhcFhvTTVvVnpycmFQQzVCcjE5N1N4WTdlTDEyM1B3UDgxdjRzTThSay1UMFJKN0tKQQ?oc=5) (Wed, 21 Jan 2026 17:33:25 GMT)

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
