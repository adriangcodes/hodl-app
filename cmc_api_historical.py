import requests
import datetime

# Your CoinMarketCap API key
api_key = "d7444da5-2275-4026-887e-1f5dfb3c6d92"

# API URL for cryptocurrency historical quotes
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical"

# Define the date and convert it to a timestamp
date = "2023-01-01"  # Example date in YYYY-MM-DD
start_timestamp = int(datetime.datetime.strptime(date, "%Y-%m-%d").timestamp())

# Parameters
parameters = {
    "symbol": "BTC",  # Bitcoin's ticker symbol
    "time_start": start_timestamp,  # Start date as a Unix timestamp
    "time_end": start_timestamp + 86400,  # End timestamp (next day to ensure full data)
    "convert": "USD",  # Convert price to USD
}

# Headers
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": api_key,
}

# Making the API request
try:
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    # Extracting the historical price data
    if "data" in data and "quotes" in data["data"]:
        historical_data = data["data"]["quotes"]
        for entry in historical_data:
            time = entry["timestamp"]
            price = entry["quote"]["USD"]["price"]
            print(f"On {time}, Bitcoin's price was: ${price:.2f}")
    else:
        print("No historical data found.")
except Exception as e:
    print(f"An error occurred: {e}")