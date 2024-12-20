import requests
import datetime

# CoinMarketCap API key
api_key = 'd7444da5-2275-4026-887e-1f5dfb3c6d92'

# CoinMarketCap API URL for historical cryptocurrency quotes
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
}

def pull_historical_price(date):
    start_timestamp = int(datetime.datetime.strptime(date, '%Y-%m-%d').timestamp())

    parameters = {
        'symbol': 'BTC',
        'time_start': start_timestamp,
        'time_end': start_timestamp + 86400,
        'convert': 'AUD',
    }
    try:
        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()

        if 'data' in data and 'quotes' in data['data']:
            historical_data = data['data']['quotes']
            prices = []

            for entry in historical_data:
                price = entry['quote']['AUD']['price']
                prices.append(price)

            if prices:
                average_price = sum(prices) / len(prices)
                return average_price
            else:
                print('No price data available for this day.')
        else:
            print('No historical data found. API is limited to previous 1 month.')
            
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