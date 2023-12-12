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




# Q1.py	

# Load data from the file
with open("daily_averages_2022.txt", "r") as f:
	daily_averages = [float(line) for line in f.read().splitlines()]

# Compute mean and standard deviation
mean_price = sum(daily_averages) / len(daily_averages)
std_dev_price = (sum((x - mean_price) ** 2 for x in daily_averages) /len(daily_averages)) ** 0.5
	
# Print the results
print(f"Mean Price: {mean_price}")
print(f"Standard Deviation: {std_dev_price}")
