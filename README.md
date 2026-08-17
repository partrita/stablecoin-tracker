# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-08-17 00:44:46 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$286,688,886,481** | 🔴 -0.01% | 🔴 -0.14% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Hong Kong’s Stablecoin Bifurcation: Two Paths for Tokenized Money - forkast.news](https://news.google.com/rss/articles/CBMijgFBVV95cUxOSmRjcDBZZy1hMUFtbkI4U2tndHRCYThHZmNEMnh6WDFNQm1NYXlQTFBfMFdsODRWN0JHTTZGQXBzQ3g5cE93ZFdLSkxnZzNOaExnVFhmZHFpbW5feW1qWGFSM0tZSG1LZ3lnTmFhRmtDTUdHM29PYW8yTlk3V1ZhalRWT0huem5pZDZSR0FR?oc=5) (Sun, 16 Aug 2026 22:37:13 GMT)
- [The stablecoin yield clash that won&#x27;t go away has banks, crypto battling over tradition - CoinDesk](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPRE5jRnNUVlBaaUUzakR0MkdmSmRCSFNPTm1uVUJOUm1iR0ttN3hydm83SjRoUUJlNXltQzFiTmo2aXk4NFNqeTJwYUZDTlNvc2lMMnU1MjlBYVpZMkkxN1J6VXdBZTRvUHRWV1FQamxUaVpSTXNIdG1oQ2dzdEdidzM4NFBQOGxjZF9QOWZTNUNjWFZUZ1REQ1B4Z3puWFN6TEI1LWxfSkRFZjNqMklWTGNIcHdrNmN5TDdPUE5qdllTLVA3V2U0aC1HTlhYODhsaFE?oc=5) (Sun, 16 Aug 2026 13:00:00 GMT)
- [Asia&#x27;s weekly TOP10 crypto news: HK‑Licensed Stablecoin Faces Multi‑Risks, Cambodia Drafts Digital‑Asset Legislation and Top10 News - Substack](https://news.google.com/rss/articles/CBMifEFVX3lxTE8wbFdkYklObkFqZzF4VWFjZjdSbkRDbDhxa19iTlQzc2lmWWdZazlvRVFJakg4UTlKRTgtNVFSNzgyUU1sX3lldHhSRk9MSUlmSVBHMVpkRWw2cnpEX2dyMGVjR2k2N2pqaVFDWG9fV2JwU2M0ZkZ2eURaODI?oc=5) (Sun, 16 Aug 2026 11:47:27 GMT)
- [Ethereum: Stablecoin Contraction and a Rising Futures Premium Diverge From a Quiet Spot Market - cryptoquant.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE5sWnhPeTZnOGlyRmpZclZ4aTU3cml6M0V6VDBXY014XzZIcE0yWkZfUER0OXZfenVUZGJ6ci1zSlZwSjV1c0N4aUhNYWpPRXo3TXRpRzBXY1ktQmo0NE5qa1hEZmt1OFl4aE44aktYT0RPVXh1aEE?oc=5) (Sun, 16 Aug 2026 09:23:36 GMT)
- [Wall Street is split on Circle Internet Group, and the divide reveals a real stablecoin infrastructure question - MarketScale](https://news.google.com/rss/articles/CBMi-wFBVV95cUxONnBFV28zQjQ4ZEp6ZWw5eDh3VkRkRjN6X2FvU2dieEFVaUo1eHJ4V2VTNjFsOXpxMEFsWF90STlOZHNiTEJCTERtOGtOU3czQ0NvakU0N3N3aGgwb2FEQ0F2eEVsSC05dE1IZFdWaXZGQzd4LW9OYW1KcDgzVFpDdEhWcGRkNDhGZE1mazM4Uk5CTHB1NzEwV0hNRVV5QWlBaFIzNFI5a1A5bHhqNG9zQVZGVUlNdl83YmdCSWVFNVJpZ0RUT3h6eFZLeHdwcmp4dl9CVDc1QWdXRU14Z0YwazRPRV9EdnVlcnVpOE1qdWFsekZFX29sdkowVQ?oc=5) (Sat, 15 Aug 2026 21:54:04 GMT)

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
