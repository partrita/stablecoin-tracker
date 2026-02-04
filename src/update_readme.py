import pandas as pd
import os
import feedparser
import datetime

def get_growth_symbol(value):
    if value > 0:
        return f"🟢 +{value:.2f}%"
    elif value < 0:
        return f"🔴 {value:.2f}%"
    else:
        return f"⚪ {value:.2f}%"

def update_news_archive():
    url = "https://news.google.com/rss/search?q=stablecoin+when:7d&hl=en-US&gl=US&ceid=US:en"
    archive_path = 'data/news_archive.csv'
    
    # 1. Fetch new items
    try:
        feed = feedparser.parse(url)
        new_items = []
        for entry in feed.entries:
            # Parse published date
            published = entry.published
            try:
                # Convert struct_time to datetime
                pub_dt = datetime.datetime(*entry.published_parsed[:6])
            except:
                pub_dt = datetime.datetime.now()
            
            new_items.append({
                'title': entry.title,
                'link': entry.link,
                'published': published,
                'published_dt': pub_dt
            })
    except Exception as e:
        print(f"Error fetching news: {e}")
        new_items = []

    # 2. Load existing archive
    if os.path.exists(archive_path):
        try:
            df_archive = pd.read_csv(archive_path)
            # Ensure published_dt is datetime
            df_archive['published_dt'] = pd.to_datetime(df_archive['published_dt'])
        except Exception as e:
            print(f"Error reading archive: {e}")
            df_archive = pd.DataFrame(columns=['title', 'link', 'published', 'published_dt'])
    else:
        df_archive = pd.DataFrame(columns=['title', 'link', 'published', 'published_dt'])

    # 3. Merge and De-duplicate
    if new_items:
        df_new = pd.DataFrame(new_items)
        # Concatenate
        df_combined = pd.concat([df_archive, df_new], ignore_index=True)
        # Drop duplicates by link (keep last discovered? or first? usually link is unique ID)
        df_combined = df_combined.drop_duplicates(subset=['link'], keep='last')
    else:
        df_combined = df_archive

    # 4. Sort and Save
    df_combined = df_combined.sort_values(by='published_dt', ascending=False)
    
    # Save to CSV
    df_combined.to_csv(archive_path, index=False)
    print(f"News archive updated. Total items: {len(df_combined)}")

    # 5. Return top 5 formatted strings
    top_5 = df_combined.head(5)
    news_lines = []
    for _, row in top_5.iterrows():
        news_lines.append(f"- [{row['title']}]({row['link']}) ({row['published']})")
    
    return "\n".join(news_lines)

def update_readme():
    csv_path = 'data/stablecoin_marketcap.csv'
    readme_path = 'README.md'

    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    # Read Data
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'])

    # Get unique dates sorted
    dates = sorted(df['date'].unique())

    if not dates:
        print("No data available.")
        return

    latest_date = dates[-1]

    # Latest Data
    latest_df = df[df['date'] == latest_date]
    total_market_cap = latest_df['market_cap'].sum()

    # Calculate Growth
    growth_1d_str = "N/A"
    growth_7d_str = "N/A"

    # 1 Day Growth
    if len(dates) >= 2:
        prev_date = dates[-2] # Assuming daily data, need to be careful if gaps
        # Ideally check if prev_date is actually 1 day ago, but for now just take previous record
        # Better: find date closest to 1 day ago

        target_1d = latest_date - datetime.timedelta(days=1)
        # Find closest date
        # For simplicity in this script, assuming daily run, we look for exact match or previous index

        # Let's filter for exact date to be precise
        df_1d = df[df['date'].dt.date == target_1d.date()]
        if not df_1d.empty:
            prev_cap = df_1d['market_cap'].sum()
            if prev_cap > 0:
                change = ((total_market_cap - prev_cap) / prev_cap) * 100
                growth_1d_str = get_growth_symbol(change)

    # 7 Day Growth
    target_7d = latest_date - datetime.timedelta(days=7)
    df_7d = df[df['date'].dt.date == target_7d.date()]
    if not df_7d.empty:
        prev_cap_7d = df_7d['market_cap'].sum()
        if prev_cap_7d > 0:
            change = ((total_market_cap - prev_cap_7d) / prev_cap_7d) * 100
            growth_7d_str = get_growth_symbol(change)

    # News
    news_section = update_news_archive()

    # Generate Markdown Content for README
    markdown_content = f"""
### 📊 Market Overview
*Last Updated: {latest_date.strftime('%Y-%m-%d %H:%M:%S')} (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **${total_market_cap:,.0f}** | {growth_1d_str} | {growth_7d_str} |

### 📈 Charts
| Market Cap History | Market Dominance |
| :---: | :---: |
| ![History](data/stablecoin_marketcap_plot.png) | ![Dominance](data/stablecoin_dominance_plot.png) |

### 📰 Latest News
{news_section}
"""

    # Generate Content for Quarto Website (No static charts)
    quarto_content = f"""
### 📊 Market Overview
*Last Updated: {latest_date.strftime('%Y-%m-%d %H:%M:%S')} (UTC)*

| Total Market Cap | 24h Change | 7d Change |
| :--- | :--- | :--- |
| **${total_market_cap:,.0f}** | {growth_1d_str} | {growth_7d_str} |

### 📰 Latest News
{news_section}
"""
    
    # Save Quarto Content
    with open('_dashboard_content.qmd', 'w', encoding='utf-8') as f:
        f.write(quarto_content)
    print("_dashboard_content.qmd updated successfully.")

    # Update README
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    start_marker = "<!-- START_dashboard -->"
    end_marker = "<!-- END_dashboard -->"

    if start_marker in content and end_marker in content:
        start_index = content.find(start_marker) + len(start_marker)
        end_index = content.find(end_marker)

        new_content = content[:start_index] + "\n" + markdown_content + "\n" + content[end_index:]

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("README.md updated successfully.")
    else:
        print(f"Markers {start_marker} and {end_marker} not found in README.md")

if __name__ == "__main__":
    update_readme()
