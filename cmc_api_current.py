import requests

api_key = "d7444da5-2275-4026-887e-1f5dfb3c6d92" # CoinMarketCap API key

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest" # CoinMarketCap API URL for cryptocurrency quotes

parameters = {
    "symbol": "BTC",  # Ticker symbol for Bitcoin
    "convert": "AUD"  # Convert price to AUD
}

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": api_key,
}

def pull_live_price():
    try:
        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()

        live_price = data["data"]["BTC"]["quote"]["AUD"]["price"]
        return live_price

    except Exception as e: # Expand error handling
        print(f"An error occurred: {e}")
        return 0
    
def print_live_price():
    price = pull_live_price()
    print(f"The current price of Bitcoin in AUD is: ${price:.2f}")
    # return price
