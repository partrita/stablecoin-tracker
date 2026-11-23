# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-11-23 04:55:35 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$271,031,612,871** | 🟢 +0.05% | 🔴 -1.47% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Visa Direct advances stablecoin-powered money movement in Asia Pacific - CoinGeek](https://news.google.com/rss/articles/CBMilwFBVV95cUxNdGhZcTlaWGxHTl95b3J5enc0ZnFuYTJHLUVlejROQzZiRC1wQl85RnAzbThELXF0SmpPM3BIaWNnaVlaZXJvb3FoOHE3dGtZX1dQUDRLTzdqMG5mS24ybi1uSUYzZDhySlR5Mm1KWTRtendlb180TVlramdzRVdxLXBBVnFMU2V5RUxNRUVOeGVLMmkxM2tj?oc=5) (Mon, 23 Nov 2026 04:00:00 GMT)
- [Curve Founder Says Onchain FX Will Scale From Stablecoin Swaps, Not Bank Desks - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE9GM3pFTkhHcXc3ekR6eHpLREpaUkJzNnJRcHZON0pURTN1RmpnVGc1clM1VGZ4VnpzVUFnS3VTRnJYbE1kNVh5enA2bUY1bm4xR2JEZzBlR2lkXzNWc1ByWXVQWjFveDBXRkVEVVM4eXQ0QUxNaVE?oc=5) (Mon, 23 Nov 2026 03:35:00 GMT)
- [Aptos named sole Move-based chain in PayPal’s PYUSD0 stablecoin rollout - Crypto Briefing](https://news.google.com/rss/articles/CBMic0FVX3lxTE1KaW5abnRiamF3VVJ1MmxzWkVPdXlUQkVpXy1iZ2w2TDBmczhKV0RRRnJBVFJXSEhqZlRzYjF1NXFXeDhOVlhlNUNyQVNWRFQ4MVB4R19TWUhIRUZORGZSbTI4TFBQNk1DUFhSMG5zR3JfTHM?oc=5) (Sun, 22 Nov 2026 23:05:37 GMT)
- [Senators want state-licensed firms to keep issuing stablecoins after Jan. 18 - CryptoSlate](https://news.google.com/rss/articles/CBMiogFBVV95cUxOdlVmdjFvSEFuZGMwODFId1c1U1FaaFhvZHk4NG9jTnpuUk9HczBwQ183NGpLQ2NMMWxmUXJoalV4VjdueHF1aUlQX1RpX1pIWk52SHVzbkZ3b3l3R2JqbHltUDlhUWJiTmFvOURUcHo5Nmo4M280T1c1NHdka1VHdzN5SkIyT3JTVlJsaXlkQzEwLXk1V3QyNC13aFFncmRkSUE?oc=5) (Sun, 22 Nov 2026 22:05:49 GMT)
- [Sky Protocol Handles Over $2 Billion in One-Day Stablecoin Redemptions While Maintaining Dollar Peg and Contesting Illicit Activity Allegations - Crowdfund Insider](https://news.google.com/rss/articles/CBMimwJBVV95cUxQdXlOOEphVHJJU2JtYVZla0RsTllkRnI0OFlSblhSdG92NV9DR1dYazhITVJ6SXl4eld6alNLTm1uY3EydDZiSW9Jc3Z4M0t2RjYxaFRzUkZxQUp1dXI4VEZlSHlFZjZqaTh4U3l4MERWY093NVo5VncwRlA2RHI5ZWVaTm1TZjJ5VlRCbkVCSVllY244S3hQREdGUll5bmtWdDRuVGNqUzVBeEZTSUc1d2FBVmpTeWRkb0NtcTVEcHItLWFzVlRlNllYVTBsUncxaXhZWk9Vc1hLQmJLLVIxOEFyT2R4VVYxcFd5bDR2S1Y0LXBhZTZhS0gxZllxaVlLQzBKZGJVX1RSNmh0b0x2bzVmV2RielhRNmxJ?oc=5) (Sun, 22 Nov 2026 16:44:28 GMT)

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
