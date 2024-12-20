import requests

# CoinMarketCap API key
api_key = 'd7444da5-2275-4026-887e-1f5dfb3c6d92' 

# CoinMarketCap API URL for live cryptocurrency quotes
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest' 

parameters = {
    'symbol': 'BTC',
    'convert': 'AUD'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
}

def pull_live_price():
    try:
        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()

        live_price = data['data']['BTC']['quote']['AUD']['price']
        return live_price

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Request error occurred: {req_err}')
    except KeyError as key_err:
        print(f'Key error accessing response data: {key_err}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    
    return 0
    
def print_live_price():
    price = pull_live_price()
    if price > 0:
        print(f'The current price of Bitcoin in AUD is: ${price:.2f}')
    else:
        print('Unable to pull Bitcoin live price.')
