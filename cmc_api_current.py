import requests

# CoinMarketCap API key
api_key = "d7444da5-2275-4026-887e-1f5dfb3c6d92"

# API URL for cryptocurrency quotes
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

parameters = {
    "symbol": "BTC",  # Ticker symbol for Bitcoin
    "convert": "USD"  # Convert price to USD
}

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": api_key,
}

try:
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    current_bitcoin_price = data["data"]["BTC"]["quote"]["USD"]["price"]
    # print(f"The current price of Bitcoin (BTC) in USD is: ${current_bitcoin_price:.2f}")
except Exception as e: # Expand error handling
    print(f"An error occurred: {e}")