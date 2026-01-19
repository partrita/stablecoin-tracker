import pandas as pd
import os
import datetime

def generate_dashboard():
    csv_path = 'data/stablecoin_marketcap.csv'
    output_html = 'index.html'

    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    # Read Data
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'])

    # Get latest data
    latest_date = df['date'].max()
    latest_df = df[df['date'] == latest_date].copy()
    latest_df = latest_df.sort_values(by='market_cap', ascending=False)

    # Calculate Total Market Cap
    total_market_cap = latest_df['market_cap'].sum()

    # Add Share column
    latest_df['Share'] = (latest_df['market_cap'] / total_market_cap * 100).map('{:.2f}%'.format)

    # Format Market Cap for display
    latest_df['Market Cap (USD)'] = latest_df['market_cap'].apply(lambda x: f"${x:,.0f}")

    # Select columns for table
    table_df = latest_df[['coin_name', 'Market Cap (USD)', 'Share']].reset_index(drop=True)
    table_df.index += 1 # Rank starting from 1
    table_df.index.name = 'Rank'

    # Convert to HTML table
    table_html = table_df.to_html(classes='table table-striped table-hover', border=0)

    # HTML Template
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stablecoin Market Cap Tracker</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{ padding-top: 20px; padding-bottom: 20px; }}
        .plot-container {{ text-align: center; margin-bottom: 30px; }}
        img {{ max-width: 100%; height: auto; border: 1px solid #dee2e6; border-radius: 4px; }}
        .footer {{ margin-top: 50px; text-align: center; color: #6c757d; }}
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center mb-4">Stablecoin Market Cap Tracker</h1>
        <p class="text-center text-muted">Last Updated: {latest_date.strftime('%Y-%m-%d %H:%M:%S')} (UTC)</p>

        <div class="row">
            <div class="col-md-8 offset-md-2">
                <div class="card mb-4">
                    <div class="card-header">Market Cap Overview</div>
                    <div class="card-body">
                         <div class="alert alert-info">
                            <strong>Total Market Cap:</strong> ${total_market_cap:,.0f}
                        </div>
                        {table_html}
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
             <div class="col-lg-6">
                <div class="plot-container">
                    <h3>Market Cap History</h3>
                    <img src="data/stablecoin_marketcap_plot.png" alt="Market Cap History">
                </div>
            </div>
            <div class="col-lg-6">
                <div class="plot-container">
                    <h3>Market Dominance</h3>
                    <img src="data/stablecoin_dominance_plot.png" alt="Market Dominance">
                </div>
            </div>
        </div>

        <div class="footer">
            <p>Data Source: CoinGecko | Automation: GitHub Actions</p>
        </div>
    </div>
</body>
</html>
"""

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Dashboard generated at {output_html}")

if __name__ == "__main__":
    generate_dashboard()
