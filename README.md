# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-25 01:24:15 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,483,946,142** | 🟢 +0.08% | 🟢 +0.34% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [$154B in Illicit Crypto Flows Raises Stablecoin Questions - PYMNTS.com](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPTHBGSFhQSnNkTXNFblIxb284X3lCUlJmQVlaenJNS1ByYThYSVF5N2NMTmJfUTZub21CYXY0WUt6Z0RsV1Y5LWJpY3ktaEw0azluNVRNUUdwQTB2SlYtdW9DTHZCN0FqQ2FpcGVOMGhwX2lCLU1UWnFxallUNVNUd1NYMmJ6azRnUW42YnBjN2k3TG5KZzMtQm45a0Q5SXdFQi1pdkNsYmh4cGVoRHBISkFicXJULWV3b3I0?oc=5) (Tue, 24 Feb 2026 23:12:38 GMT)
- [Meta Gets Back into Crypto, Plans Stablecoin Integration Later This Year - Gizmodo](https://news.google.com/rss/articles/CBMipAFBVV95cUxORkNOUWoyRVQxNV9qLU9tTGVCOVZvMlZXejBuMWNHdndhWEFsVmNUMmRhSDc5cGNlNERNeVRfb0I2eEgycG92bG9NcWt3WnlYUExfXzFybGN4Qnd3eHpOTW4tMUttbkx6bjlUaHZwbnBOcU1tR2ZmTUtYZk1PRjVwSXI1cE1NblFISU5HalktOUtvQk53ZGxIZ1ljeXNaYXVWSlFCNw?oc=5) (Tue, 24 Feb 2026 22:20:58 GMT)
- [Stablecoin rules in the UK are being finalized, and are at risk of preventing the UK from being globally competitive in the digital economy. For example, the Bank of England is proposing a cap on stablecoin holdings for individuals and businesses. The UK has - x.com](https://news.google.com/rss/articles/CBMickFVX3lxTFBmejVaY0h2bkpLM01IWUE2TlBuVUVEdEJmV0xxN0dpN3ZNa3EyNTZhblNYVmI3SVJGOTBiZE5ibGI2cUdmWDNYYm1YMnBHU2ptc1ZkanJKbjVKRDI0emFKQ29ZZnRvd1ozWEQzOE1ObnVBZw?oc=5) (Tue, 24 Feb 2026 22:06:34 GMT)
- ['Stablecoin Summer': Stripe Makes Tender Offer at $159 Billion Valuation - Decrypt](https://news.google.com/rss/articles/CBMijgFBVV95cUxNRkRNYTRjOXF0WkZFNU8wWUVrazVscmdSalFCOU5XTldmYVRtQW1hVjM2TDNZbkdwNTBydVNMOVZDN0pLOUNISEtuYnFzY01ic2syWmp1SkxMbFlERUxHamlrRkdPazhJOVFMQjcySHZoZkJxX081cTBqY2NBSDdkemFuUWJzRzBBaWlYTmp30gGWAUFVX3lxTE1WRUxXeXNmYlZrNnJzWjJoRVJFNmEycnVxSEkwN1Vuc05qTjZZaHdHSXJ0SjZ3VzJfNEZURHFkTzB3aHF2cWhKcWpZOWNJLWliSzlrOGJYTW00ZDBaLWpsWTVCTkpucmpJTjg5cnpkUm13bXZPMlVGQm1jcDBqRUF5OVRadjJPOWFMNXJMZXFRd1J1YWxTUQ?oc=5) (Tue, 24 Feb 2026 21:29:29 GMT)
- [Meta Testing Stablecoin Payments As Digital Currencies Take Off - Bloomberg](https://news.google.com/rss/articles/CBMitAFBVV95cUxNeE55OFN3di1pdWFHSGg3dTNXbkw3YUotRndpd2VNUXc1NE94ZEZZT2dhQnBlY1kxY0Zzdm5XYmpkcWI1YWc5X0FHaVNrT0ZpZjhMTHFFU3YtYU1aX01RR1hOTnhwdVBMa21zR25jeXNxY2ppcmQ1aWdudEVfTmZmZlZ1MjZUTXZwN0hRakc1ZlJfSmVncm8ta0JWMHQ5RmJJY2xzME55T3Zrc0daQ1I0YmVUOVQ?oc=5) (Tue, 24 Feb 2026 21:05:09 GMT)

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
