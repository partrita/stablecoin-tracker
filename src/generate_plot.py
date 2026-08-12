import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def generate_plot():
    # File paths
    csv_path = "data/stablecoin_marketcap.csv"
    output_path = "data/stablecoin_marketcap_plot.png"
    pie_output_path = "data/stablecoin_dominance_plot.png"

    # Check if data file exists
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    # Read data
    df = pd.read_csv(csv_path)

    # Convert date to datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Security: Enforce explicit numeric conversion for market_cap to prevent ValueError during plot generation
    df["market_cap"] = pd.to_numeric(df["market_cap"], errors="coerce")

    df = df.dropna(subset=["date", "market_cap"])

    if df.empty:
        print("Error: No valid date data found in CSV.")
        return

    # Warn if very few data points
    if len(df) < 10:
        print(f"Warning: Only {len(df)} data rows available — charts may be sparse.")

    # Set style
    sns.set_theme(style="darkgrid")

    # --- Line Plot ---
    plt.figure(figsize=(12, 6))

    # Create line plot
    sns.lineplot(data=df, x="date", y="market_cap", hue="coin_name")

    # Customize plot
    plt.title("Stablecoin Market Cap Over Time")
    plt.xlabel("Date")
    plt.ylabel("Market Cap (USD)")
    plt.xticks(rotation=45)
    plt.legend(title="Coin Name", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()

    # Save plot
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")
    plt.close()

    # --- Pie Chart ---
    # Get latest date
    latest_date = df["date"].max()
    latest_df = df[df["date"] == latest_date].copy()

    # Sort by market cap descending
    latest_df = latest_df.sort_values(by="market_cap", ascending=False)

    # Warn if very few coins on the latest date
    if len(latest_df) < 2:
        print(
            f"Warning: Only {len(latest_df)} coin(s) on {latest_date.date()} — pie chart may be uninformative."
        )

    # Group coins with < 1% share into "Other" to reduce clutter
    total_cap = latest_df["market_cap"].sum()
    if total_cap > 0 and len(latest_df) > 3:
        threshold = total_cap * 0.01
        main = latest_df[latest_df["market_cap"] >= threshold]
        other_cap = latest_df[latest_df["market_cap"] < threshold]["market_cap"].sum()
        if other_cap > 0:
            other_row = pd.DataFrame(
                [{"coin_name": "Other", "market_cap": other_cap}],
                index=[len(latest_df)],
            )
            latest_df = pd.concat([main, other_row], ignore_index=True)

    plt.figure(figsize=(10, 8))

    # Create pie chart
    plt.pie(
        latest_df["market_cap"],
        labels=latest_df["coin_name"],
        autopct="%1.1f%%",
        startangle=140,
    )
    plt.title(f"Stablecoin Market Cap Dominance ({latest_date.strftime('%Y-%m-%d')})")
    plt.tight_layout()

    plt.savefig(pie_output_path)
    print(f"Pie chart saved to {pie_output_path}")
    plt.close()


if __name__ == "__main__":
    generate_plot()
