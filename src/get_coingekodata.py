import click
import cloudscraper
import pandas as pd
import time
import os

# 수집 대상 리스트 (코인 이름, API 엔드포인트)
COIN_DATA_URLS = [
    ["Tether", "https://www.coingecko.com/market_cap/tether/usd/max.json"],
    ["USDC", "https://www.coingecko.com/market_cap/usdc/usd/max.json"],
    ["USDS", "https://www.coingecko.com/market_cap/usds/usd/max.json"],
    ["Ethena USDe", "https://www.coingecko.com/market_cap/ethena-usde/usd/max.json"],
    ["Dai", "https://www.coingecko.com/market_cap/dai/usd/max.json"],
    ["PayPal USD", "https://www.coingecko.com/market_cap/paypal-usd/usd/max.json"],
    ["USD1", "https://www.coingecko.com/market_cap/usd1-wlfi/usd/max.json"],
    ["Falcon USD", "https://www.coingecko.com/market_cap/falcon-usd/usd/max.json"],
    [
        "Global Dollar",
        "https://www.coingecko.com/market_cap/global-dollar/usd/max.json",
    ],
    ["Ripple USD", "https://www.coingecko.com/market_cap/ripple-usd/usd/max.json"],
]


@click.command()
@click.option(
    "--output",
    "-o",
    type=click.Path(),
    required=True,
    help="저장할 CSV 파일 경로 (예: ./stable_coin.csv)",
)
def save_coin_data(output):
    """Cloudflare를 우회하여 코인게코 데이터를 수집하고 CSV로 저장합니다."""

    # Cloudflare 우회를 위한 스크래퍼 생성
    scraper = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "windows", "desktop": True}
    )

    all_dfs = []
    click.echo(f"🚀 총 {len(COIN_DATA_URLS)}개의 코인 데이터 수집을 시작합니다...")

    with click.progressbar(COIN_DATA_URLS, label="데이터 다운로드 중") as bar:
        for name, url in bar:
            try:
                # 데이터 요청
                response = scraper.get(url, timeout=15)

                # 403 에러가 여전히 발생할 경우를 대비한 처리
                if response.status_code == 403:
                    click.echo(
                        f"\n[차단] {name}: 서버에서 접근을 거부했습니다. (403 Forbidden)"
                    )
                    continue

                response.raise_for_status()
                data = response.json()

                # JSON 데이터 프레임 변환 ('stats' 키 사용)
                if "stats" in data:
                    df = pd.DataFrame(
                        data["stats"], columns=["timestamp", "market_cap"]
                    )
                    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
                    df["coin_name"] = name

                    all_dfs.append(df[["date", "coin_name", "market_cap"]])

                # 중요: 코인게코의 IP 차단을 피하기 위해 요청 간 간격을 둡니다.
                time.sleep(5)

            except Exception as e:
                click.echo(f"\n[오류] {name} 수집 실패: {e}", err=True)

    # 데이터 통합 및 저장
    if all_dfs:
        final_df = pd.concat(all_dfs, ignore_index=True)

        # 출력 디렉토리 생성
        directory = os.path.dirname(output)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        final_df.to_csv(output, index=False, encoding="utf-8-sig")
        click.echo(f"\n✅ 성공! 총 {len(final_df)}행의 데이터가 저장되었습니다.")
        click.echo(f"📍 저장 위치: {os.path.abspath(output)}")
    else:
        click.echo("\n❌ 수집된 데이터가 없습니다. 잠시 후 다시 시도해 주세요.")


if __name__ == "__main__":
    save_coin_data()
