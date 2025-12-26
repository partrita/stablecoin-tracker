import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
import json
import datetime
import os
import sys

URL = "https://www.coingecko.com/ko/categories/usd-stablecoin"
CSV_PATH = "data/stablecoin_marketcap.csv"

# Mapping slugs to CSV Display Names
SLUG_MAP = {
    "tether": "Tether",
    "usd-coin": "USDC",
    "usds": "USDS",
    "ethena-usde": "Ethena USDe",
    "dai": "Dai",
    "paypal-usd": "PayPal USD",
    "usd1-wlfi": "USD1",
    "falcon-finance": "Falcon USD",
    "falcon-usd": "Falcon USD",
    "global-dollar": "Global Dollar",
    "ripple-usd": "Ripple USD",
}

def normalize_name(slug):
    if slug in SLUG_MAP:
        return SLUG_MAP[slug]
    # Fallback: Title Case, replace hyphens
    return slug.replace('-', ' ').title()

def fetch_data():
    print(f"Fetching data from {URL}...")
    scraper = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "windows", "desktop": True}
    )
    try:
        response = scraper.get(URL)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching URL: {e}")
        sys.exit(1)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    tbody = soup.find('tbody')
    if not tbody:
        print("Error: Could not find table body")
        sys.exit(1)
        
    rows = tbody.find_all('tr')
    
    new_data = []
    # Format: 2024-12-26 12:34:56.000
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.000")
    
    count = 0
    for row in rows:
        if count >= 10:
            break
            
        # Get Name
        star_icon = row.select_one('.fa-star')
        if not star_icon:
            continue
            
        props_str = star_icon.get('data-analytics-event-properties')
        if not props_str:
            continue
            
        try:
            props = json.loads(props_str)
            slug = props.get('coin_name')
        except:
            continue
            
        coin_name = normalize_name(slug)
        
        # Get Market Cap (Index 10)
        cells = row.find_all('td')
        if len(cells) < 11:
            print(f"Skipping {slug}: not enough columns")
            continue
            
        mc_cell = cells[10] 
        mc_value_str = mc_cell.get('data-sort')
        
        try:
            market_cap = float(mc_value_str)
        except (ValueError, TypeError):
            print(f"Warning: Could not parse market cap for {coin_name} from '{mc_value_str}'")
            continue

        new_data.append({
            "date": timestamp,
            "coin_name": coin_name,
            "market_cap": market_cap
        })
        count += 1
        print(f"Fetched {count}. {coin_name}: {market_cap}")

    if not new_data:
        print("No data fetched.")
        return

    # Append to CSV
    df_new = pd.DataFrame(new_data)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    
    if os.path.exists(CSV_PATH):
        try:
            df_new.to_csv(CSV_PATH, mode='a', header=False, index=False)
            print(f"Appended {len(df_new)} rows to {CSV_PATH}")
        except Exception as e:
            print(f"Error appending to CSV: {e}")
    else:
        df_new.to_csv(CSV_PATH, index=False)
        print(f"Created {CSV_PATH} with {len(df_new)} rows")

if __name__ == "__main__":
    fetch_data()
