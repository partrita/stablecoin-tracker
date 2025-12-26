# stablecoin-tracker

스테이블코인 시장의 흐름을 한눈에 파악하는 데이터 트래커

## 데이터 수십 스클립트 실행 방법

명령어 뒤에 `--output` 옵션으로 저장 경로를 지정해 주세요.

```{bash}
uv run src/get_coingekodata.py --output ./stable_coin_data.csv
```

## 💡 주요 변경 사항 및 팁

- cloudscraper 적용: 일반 requests와 달리 실제 브라우저인 것처럼 위장하여 Cloudflare의 봇 감지를 통과합니다.
- time.sleep(5): 코인게코는 매우 짧은 시간 내에 대량의 요청이 들어오면 IP를 일시 차단합니다. 10개의 코인을 가져오므로 최소 5초 정도의 간격을 두는 것이 안전합니다.
- encoding='utf-8-sig': 저장된 CSV를 엑셀(Excel)에서 열었을 때 한글이나 특수문자가 깨지지 않도록 인코딩을 최적화했습니다.

