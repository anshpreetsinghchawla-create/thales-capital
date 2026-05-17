import yfinance as yf
import numpy as np
import pandas as pd
from datetime import datetime

def fetch_data(tickers, start_date, end_date = datetime.today().strftime('%Y-%m-%d')):
    data = {}
    for ticker in tickers:

        df = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        data[ticker] = df.dropna()
    return data

universe = ['SPY', 'QQQ', 'IWM', 'TLT', 'GLD', 'SLV', 'EURUSD=X']
start_date = '2023-01-01'
end_date = datetime.today().strftime('%Y-%m-%d')
data = fetch_data(universe, start_date, end_date)
close_data = {ticker: df['Close'] for ticker, df in data.items()}
close_data = pd.DataFrame(close_data)
close_data = close_data.dropna()
close_data.to_csv('data.csv')