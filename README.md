# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-02-28 01:11:41 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$292,927,493,231** | 🔴 -0.03% | 🟢 +0.16% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Regulatory Realignment: From Fed Policy to UK Framework Reform, February 2026 - OCC Proposes Implementing Regulations for Payment Stablecoin Issuers Under the GENIUS Act - JD Supra](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQaHh1VjF2MVRjUnlUc3ZFRmViWEcyc1ZtNURoc2ItRVpNS3lTU3BkY21fUW1pakp4dFBmNEZzTWhRTkNVTnJQcXNIektMZHhPY0o2Ml92M3FZamZsQXUzMUs0U2haUGdhN0g3bkRQM0dMSXNSWXQ4Q0FyRXc5S3BDSlVKOXN3Y1RU?oc=5) (Fri, 27 Feb 2026 22:44:32 GMT)
- [Solana debuts payments.org as stablecoin payments move into the mainstream - Yahoo Finance](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNeVBOU2YxeFZyV2tYS2FDb2oyUUpXX1FjUEx1bm5FRVA4REVtNUVCMXo2MVIwQ05GekVkaWp6OEVhWE9tV2l0LXFGejZsb0tKd2U5VW1jbllWRUJJSWZNRjVHTWlhSlhXU0NKS3g4OVlNQkR0Zi1udWdmUnlEVXFhYTBnbzlNcEdtMEU4?oc=5) (Fri, 27 Feb 2026 22:08:33 GMT)
- [JPYC raises $12m Series B as mainstream investors back yen stablecoin - ledgerinsights.com](https://news.google.com/rss/articles/CBMiogFBVV95cUxOeDhldVhBYUZKNTFRdDNNd0pvVVlmUWtIUS1sMDZCTlRVdmVzeERTRWdnQndUMDEzb2dTa0hqWGtnQlZiME1CSFNVT0dCLXl2T0g0WWZSWERJTVBFVzVLY0k4OENqY3Y1N19na1N0TGRvckxsOG1GTmRWZHVmRFdHQlBPRTIxeGl1WG5wVDhvQ3JVcmZrWlp2bEtwUWZURkUtLVE?oc=5) (Fri, 27 Feb 2026 18:42:09 GMT)
- [OCC Proposes Rules to Implement the GENIUS Act for Payment Stablecoin Issuers - JD Supra](https://news.google.com/rss/articles/CBMihAFBVV95cUxQMXNWUDlSX2VzVDk5dlFmVnA2eG5YalhMeEhjZ3VsbUF0czRFcFRHMVRXU3V5MlJpMlZSVVJzaWZ6cEZlSnowalpfSFZBYldPamJwdHRmcnZGVW81X2ZGSE5KMGZfRUFIVGNraTAyaUZhUW5Od3J4R2pGMjNMektZUmNfX3c?oc=5) (Fri, 27 Feb 2026 18:00:41 GMT)
- [This Week in Stablecoins: FinTech, Big Tech and Regulation - PYMNTS.com](https://news.google.com/rss/articles/CBMiogFBVV95cUxNbVBGSnpuRzYyMEtfc2FONGRlWW13Sm1FUVRpVDFLX2dQcjRXSDRxTkRvcU03eEpaSkYzdjM0Nnp5V0M4c09rOWhfLXpkN2dFajlsd2trU1ZqeUh4M0ZQdUttM012aWZ0ZGVRMzItT0hLTlNDS3RXNHhGZmMtSDVwZkM4bkxJaGNHYndoQWpHRGxRaFRrSjBLQkVaUVg4NE9Sc2c?oc=5) (Fri, 27 Feb 2026 16:24:49 GMT)

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
