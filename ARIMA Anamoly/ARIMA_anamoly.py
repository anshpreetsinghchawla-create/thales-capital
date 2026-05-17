import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

data = yf.download('TSLA', start='2020-01-01', end='2025-01-01' )
close_prices = data['Close']

plt.figure(figsize=(10, 6))
plt.plot(close_prices, label ='AAPL Close')
plt.title('AAPL Close Prices')
plt.legend()
plt.show()

returns = close_prices.diff().dropna()

plt.figure(figsize=(10, 6))
plt.plot(returns, label='difference returns')
plt.title('stationary series')
plt.legend()    
plt.show()

model = ARIMA(close_prices, order = (1,1,1))
results = model.fit()

print(results.summary())


forecast = results.get_forecast(steps=30)
mean_forecast = forecast.predicted_mean
conf_int = forecast.conf_int()

plt.figure(figsize=(10, 6))
plt.plot(close_prices, label="Historical")
plt.plot(mean_forecast, label="Forecast")
plt.fill_between(conf_int.index,
                 conf_int.iloc[:, 0],
                 conf_int.iloc[:, 1], color='pink', alpha=0.3)

plt.legend()
plt.title('AAPL Price Forecast')
plt.show()

residuals = results.resid

plt.figure(figsize=(10, 6))
plt.plot(residuals, label = 'Residuals')
plt.axhline(y = 3*residuals.std(), color = 'r', linestyle = '--', label = 'Upper Threshold')
plt.axhline(y = -3*residuals.std(), color = 'g', linestyle = '--', label = 'Lower Threshold')
plt.title('Residuals with Anomaly Thresholds')  
plt.legend()

plt.show()

anomalies = residuals[(residuals > 3*residuals.std()) | (residuals < -3*residuals.std())]
print("Anomalies detected at:")
print(anomalies)