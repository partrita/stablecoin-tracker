# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-06-14 02:49:08 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$293,429,182,320** | 🟢 +0.00% | 🔴 -0.55% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [Clarity Act Stablecoin Yield Clause: The $20B Bank vs Crypto Exchange Battle - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxONXBKZzdBakU2cFlWRW9RMHhUU25YNmNKQVp1aDhrZVNFbUF6MWpYZGE3ODR5TVNZZ3VhYmJNTExHR2ExMmVPOGtNVnRZbU9aN3JUQndCdnRsREpfUzdNQnZTX0ltWnh1Y2RGODdneTZEZkQ3R3A1ejVYNHhzQTQ0QlBGOXppbDIzMkRZRkRCVDZkcnYyaHhJcW5FbmtWcFRLMkE?oc=5) (Sat, 13 Jun 2026 22:08:07 GMT)
- [Visa (V) Expands AI Commerce Push, Unveils Stablecoin and Tokenization Capabilities - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxPZU8ySk5aZWpJYWVmM012MDlCb0dleHc1RmhmRXBtTG5XREc5bmJDVllMSEFrQVliY2taQ1llZjU1eDQ5VVRQX2NVYnB3d2xQS3RHRm5mcVNHWjlSa0lqb3dqSkVhTURselZCOVh3N2ZsTDNlNjdET0tIcVVjZGdPWVF6NmZzRlFVcE1tZTlLbDh2Rk5pR2VFTk5kSQ?oc=5) (Sat, 13 Jun 2026 17:59:56 GMT)
- [Stablecoins Were Meant to Disrupt Finance. Instead, They Became Idle Cash. - CoinDesk](https://news.google.com/rss/articles/CBMitgFBVV95cUxQOXRqMmYwUW5yMTZscmFaU0xEYWROSzhMNkhLVG0wQkhicEY3aml0b0Q3R3J4a0VTMkg1SzV2QWYxRjY3ekVodjBPNXRMcGZQY1FUZW91Y3B5R1p2dUlVSHlQOTkxLVljZUpwcDBaY3Jtd0ZnWHpULXpVVTc1XzFwREZiQUZjSktwV0h5MjFOMWgxaURzS3ZUNTJhME92WmpGZG5aaG93VEowM2pTem84Q3daaHo3UQ?oc=5) (Sat, 13 Jun 2026 16:53:46 GMT)
- [Ripple wants AI agents to pay in XRP and RLUSD. The market is still mostly USDC - CoinDesk](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOV1FnQnhiNkY5ZW04TmR6Vk02VjFvZzF4RlFkZmVQQzR4M3hRZzlpbXVZMEgzRkp1a3BhdXctY3JOTFhrRzR2THpHUmRXdWxBZUNSUnhJNkRHN05TTGVoYVdWWVdKakFzLXhiYkZRUUVPLVVlWmlFRWFkR2Z4bFZDZDlUSDc1amphQ3BheUxZTlU1MFJPSzJpNTZmZkstNlB0SmF1SEpyWFk5Q1pYbC1xaEktclZ0YkxtV3l3?oc=5) (Sat, 13 Jun 2026 11:30:37 GMT)
- [BPInsights: June 13, 2026 - Bank Policy Institute](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9CM01TYkJncTl4WHpYVW94MzB3TVZMenAxRU9jVTU3MjVEN1FueDlUcjBpNTQxb2tGdnBCck93R0RIQ09hTGNnWExid2pkY0Y4VEE?oc=5) (Sat, 13 Jun 2026 11:00:00 GMT)

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
