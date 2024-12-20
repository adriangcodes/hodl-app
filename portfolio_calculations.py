import csv 
from cmc_api_current import pull_live_price

def calculate_total_coins():
    total_coins = 0
    try:
        with open('holdings.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    amount = float(row['Amount'])
                    total_coins += amount
                except ValueError:
                    print(f"Invalid amount found in holdings.csv: {row['Amount']}. Skipping.")
        return total_coins
    
    except FileNotFoundError:
        print('The file holdings.csv cannot be found.')
    except PermissionError:
        print('You do not have permission to read holdings.csv.')
    except Exception as e:
        print(f'An unexpected error occurred while reading the holdings: {e}')
    
    return 0

def print_total_coins():
    total_coins = calculate_total_coins()
    if total_coins > 0:
        print(f'The total Bitcoin holdings are: {total_coins:.8f}')
    else:
        print('No Bitcoin is currently held in the portfolio.')

def print_portfolio_value():
    total_coins = calculate_total_coins()
    if total_coins == 0:
        print('No Bitcoin is currently held in the portfolio.')
        return

    live_price = pull_live_price()
    if live_price == 0:
        print('Unable to pull live Bitcoin price. Portfolio value cannot be calculated.')
    else:
        value = total_coins * live_price
        print(f'The current value of the Bitcoin portfolio in AUD is: ${value:.2f}')