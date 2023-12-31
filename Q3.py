import pandas as pd
from alpha_vantage.timeseries import TimeSeries

# Replace with your own API key
key = 'CIRHMIC9RGPDRCXW'

# Initialize Alpha Vantage TimeSeries object
ts = TimeSeries(key, output_format='pandas')

# Get daily stock data for the past year
data, meta = ts.get_daily('NKE', outputsize='full')

# Extract the closing prices and calculate daily averages
closing_prices = data['4. close']
daily_averages = closing_prices.groupby(closing_prices.index.date).mean()

# Filter data for the year 2022
daily_averages_2022 = daily_averages.loc[pd.to_datetime('2022-01-01'):pd.to_datetime('2022-12-31')]

# Save only the daily average prices for 2022 to a text file (CSV)
daily_averages_2022.to_csv('daily_averages_2022.txt', header=False, index=False)

print("Data saved to 'daily_averages_2022.txt'")

# Q3.py

# Load data from the file
with open("daily_averages_2022.txt", "r") as f:
    stock_prices = [float(line) for line in f.read().splitlines()]

# Initialize variables
current_max_val = float('-inf')
max_profit_val = 0

# Find the largest possible profit
for price in reversed(stock_prices):
    current_max_val = max(current_max_val, price)
    potential_profit = current_max_val - price
    max_profit_val = max(potential_profit, max_profit_val)

# Print the result
print(f"Largest Possible Profit: {max_profit_val}")
