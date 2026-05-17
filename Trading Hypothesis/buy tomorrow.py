import yfinance as yf
import pandas as pd
import numpy as np
from tqdm import tqdm

# PARAMETERS
Z_THRESHOLD = 2  # 2σ or 3σ
START_DATE = "2018-01-01"
END_DATE = "2025-01-01"

# Get S&P 500 tickers
sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = sp500['Symbol'].tolist()[:500]

# Store results
trades = []

for ticker in tqdm(tickers, desc="Processing tickers"):
    try:
        data = yf.download(ticker, start=START_DATE, end=END_DATE, progress=False)
        data['Return'] = data['Adj Close'].pct_change()

        mean = data['Return'].mean()
        std = data['Return'].std()

        # Find days with >2σ drop
        data['Signal'] = data['Return'] <= (mean - Z_THRESHOLD * std)

        # Next-day return (buy after drop)
        data['Next_Return'] = data['Return'].shift(-1)

        # Collect trades
        trade_returns = data.loc[data['Signal'], 'Next_Return'].dropna().tolist()
        for r in trade_returns:
            trades.append(r)

    except Exception as e:
        continue

# Convert to numpy array for analysis
trades = np.array(trades)

# Metrics
total_trades = len(trades)
profitable_trades = np.sum(trades > 0)
prob_profit = profitable_trades / total_trades * 100
total_profit_pct = np.mean(trades) * 100
cumulative_profit = np.prod(1 + trades) - 1

print(f"Total Trades: {total_trades}")
print(f"Probability of Profit: {prob_profit:.2f}%")
print(f"Average Profit per Trade: {total_profit_pct:.3f}%")
print(f"Cumulative Profit: {cumulative_profit * 100:.2f}%")
