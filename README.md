# Stablecoin Tracker

<!-- START_dashboard -->

### 📊 Market Overview
*Last Updated: 2026-07-25 01:54:19 (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **$288,327,177,935** | 🔴 -0.16% | 🔴 -0.39% |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
- [This Week in Stablecoins: Visa, Goldman and Samsung Raise the Stakes - PYMNTS.com](https://news.google.com/rss/articles/CBMirwFBVV95cUxOWC1uNjR1dGFrTkpNUFdNc2owVmJNNktsNEFYdFg2NWkybC0xUUU0Y0pnaTN4dzdfeFc1T0EydVduLUIyUklEb0pqb1JpRXNmLXo3T1lqekREUk9DZFYwSkF0V01Dc0l4T0FjdWhPdlpwMnZwZUhnR19kOXJKMkEyeHE5RlNBRkl4V25nbjZNT25Qb2lURTkwbEtXalJxSDFiSnF4SmYwTHh4bDdVb2ZB?oc=5) (Fri, 24 Jul 2026 23:55:59 GMT)
- [Samsung Wallet Plans Stablecoin Integration to Build Mobile Financial Hub - PYMNTS.com](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPNlYyWW1oa2llQ3hoZno5UmlwSG9ubXFxLUxabUtkb1YyUEw2TlpKTGstcWFNbHdxV05iczdRRDRxQzRHOXNIaHh0eXBZMXU2SzJDaWhHUXdUODRVRmt1c2V5ejNOQmd6eVI5QVRjUjFtWk1qd1g0Zi1WY0N6aGs1cGNscHhsb1dDUDVEMkpNWnpQV2dRY1dfVmlDc1JFRUNERjNjalMzbEhWVTRlSGdoTWVPeEkxMWEt?oc=5) (Fri, 24 Jul 2026 20:51:45 GMT)
- [Stablecoin Development Corp (SDEV) details COO Blynn&#x27;s 1.4M RSU grant - Stock Titan](https://news.google.com/rss/articles/CBMiywFBVV95cUxOZGFIeHVhcmZLa1FaOXU5UWJ6VG52ME1PSm5OMndFOXlkeFQ2TWRHSTRBNEF4WTdNeUhOcmU4djFuZE0zU1lxVE5wQ0dGWUs5YlFlVndhZUdLY2hfZkROeXM4QXlHUHBITElSSElISkpBbWtxcDlETDlpcmtpWFdpOVdEMThBSS03MHc2Ylc1U3plelFscThrQmxmb1RjbjYyRmZidzN3YVVMMm9nU2VETmxac0lRZ1hoTVF3NFJMUVpCSk1hSGNOYVV5QQ?oc=5) (Fri, 24 Jul 2026 20:31:55 GMT)
- [Stablecoins are powering, not disintermediating, banks - Axios](https://news.google.com/rss/articles/CBMifkFVX3lxTE9fRGpjMFd2ejNNRXFzam9BX2J6QWVoa3BVcHI2VV85WWJHalIyeVVDTUNLSTlLWWswVWhzUDBBMEtvNFFSZ0Y1bHAyd0w5QTFtNGZCVTM2R20xbHRyV1N6ZzA3TDhEeVA1SlptTXRzbGdyMVJiSXIzUkJYejk1QQ?oc=5) (Fri, 24 Jul 2026 20:01:13 GMT)
- [Samsung Wallet Will Add Stablecoin Support, Including USDC - Decrypt](https://news.google.com/rss/articles/CBMickFVX3lxTE1hUzBKcjUxTGFULVVyOFZhYjlSajRzNjNxSk9XR2J2dEh1cGlpeGFyRXhxVXFyN0NyQUN3Zk5aZnJ5dWRuaE9wWlVJMENYeG9oUjFfWnltWDVILUxCbnIyWFE1NmJzTDlmQUg2ZXVrZlU0Z9IBekFVX3lxTE9MU3NxQnNPYWIzR01iMFhvTlR5QjBkWkI3Y3ZUWlNQS1BlNURkd2VTaDZxaTdNdWh4NFBON01WSDVfM29UZTM0ejRXNkxDMVMtZkVFdS1KQ3NSQ0J1Y2FJc1ZDeGoyal9nQjIxalFHSUVtX1ZQN0NTa3FB?oc=5) (Fri, 24 Jul 2026 19:30:01 GMT)

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
