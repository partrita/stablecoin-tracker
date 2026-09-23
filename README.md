# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-09-23 02:36:03 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,266,125,895** | 🟢 +0.25% | 🟢 +0.68% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Reap and Visa Collaborate to Launch Stablecoin Card Programs Across 100+ Markets - TradingView](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOSzktX01XZFJya2hYYzdQdWhKVDdjellnSmlTVUpZM29lNlNGZURQM29QRXAxOVdEY1JERUVpYmZ5NGtDZnMwTnJpOHpNSmd0YVVWVDhYTEtPNGd4c2NiazRmQ1dYanJvbzNwVEhONzE1TWhuTU53cHJxUE5fWEkyU0tVY3FZNjh3eFc2OFc0UHBvQVJ3Xzd4elFTQlBNUExnaEtlWHJaMmNXdVVnOEVpZEptY0ZmNTNVRzd3bWhxUjJSdURSRmEzaGdra2liTGprbEpmWG9CYw?oc=5) (Wed, 23 Sep 2026 02:26:00 GMT)
- [SoFi Bank goes live with stablecoin settlement across Mastercard network - Finextra Research](https://news.google.com/rss/articles/CBMitgFBVV95cUxQTnRaNVBPbklIMHlWOUNITUpseXcxMzVvRDNwY3RYRm9qNmtabzFETHk0T1M4M1RIY2Z2NFBJam1XcVc5NHpkM1JXdThSM0I3c1Vmb1V3ZTlzc0JJeGg1YjdWODI0eVo2ckZKS3RRcm85SFprVVk3Uy1wSHNhYThWQXU1YmFLNHVBSUlrR2FaNXFWVTRuMTJiSnEyVDBuMER6bnpMRVNEWWF0WkRhTXd2M0JGc3FJUQ?oc=5) (Tue, 22 Sep 2026 23:05:54 GMT)
- [SoFi&#x27;s Stablecoin Goes Live Across Mastercard&#x27;s Network - TradingView](https://news.google.com/rss/articles/CBMitgFBVV95cUxQTzdHVUgtUkcwSF80ZmN6Zm5OQkpOaktzdVFBQks2TXlsMTRsc3R6aDc1c05PRW9aRC1HS0ZvMTB5bVJRSl9mTTQ0cHVSNndwM25meVpxOUFLU1U5MDAxNXZ5bjc2XzhmWGRnVHc5eTFjeUZBX2h2aG5nQjN3alNYcmU4VjJpLUlRcG1uRHpLTU9URGFNcTZ6aUppeWR0dk5QajlCR3lfQVdPd3FXU1dtWksyX2lvUQ?oc=5) (Tue, 22 Sep 2026 22:05:07 GMT)
- [Why newly granted federal approval won’t save these 3 crypto banks - CryptoSlate](https://news.google.com/rss/articles/CBMiggFBVV95cUxNajdEMy1mMlRsc1JUekFXNU1RZmIwbXo5MlViN0ZNdlQ4VUQwR1dreGxTbVNpT2U3d3ZKSTMtbEpkRmtZV1Qzc0E1M2pZYjZNcThSdDJkaU5iakR5Y3d3a0VxY2o3OGJGTFB0aldjMEF1bG9keGVXeDF5Y0Z0c1Vxc0pB?oc=5) (Tue, 22 Sep 2026 21:20:03 GMT)
- [The Fed’s New SVB Report Exposes the Old-Fashioned Bank Risk Behind Digital Assets - PYMNTS.com](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPUm0xSktLWDE3TTl1MjBBajlmeW5DeDFvSERFdmtESnN5NUVWZGk5UGl5UVdXUm1TZXNQZkx5MWZ1R2NzRWkzc3Vrd056RjMyZ0RfMlpGVmFkTVpsNkNXejhUUVZUVjQ2bDFWMHFYSjdjNWo5aEdWV3hEczR5eHdBdTZ0QVNCckw0QURtZzE4dTV2bjRSckNqOU92ZnpGbktoUDNFNHRsNmV2WFdxd2pMeU5iNHpuZnJ0Qk9MdTlCSnlXWGs?oc=5) (Tue, 22 Sep 2026 21:03:27 GMT)

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
