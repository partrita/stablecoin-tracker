import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_plot():
    # File paths
    csv_path = 'data/stablecoin_marketcap.csv'
    output_path = 'data/stablecoin_marketcap_plot.png'

    # Check if data file exists
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    # Read data
    df = pd.read_csv(csv_path)

    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Set style
    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(12, 6))

    # Create line plot
    sns.lineplot(data=df, x='date', y='market_cap', hue='coin_name')

    # Customize plot
    plt.title('Stablecoin Market Cap Over Time')
    plt.xlabel('Date')
    plt.ylabel('Market Cap (USD)')
    plt.xticks(rotation=45)
    plt.legend(title='Coin Name', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # Save plot
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    generate_plot()
