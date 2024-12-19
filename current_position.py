import csv 
from cmc_api_current import pull_live_price

def calculate_total_coins():
    total_coins = 0
    with open('holdings.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_coins += float(row['Amount'])
        return total_coins

def print_total_coins():
    total_coins = calculate_total_coins()
    print(f'The total Bitcoin holdings are: {total_coins:.8f}')

def print_portfolio_value():
    total_coins = calculate_total_coins()
    live_price = pull_live_price()
    if total_coins == 0:
        print('No Bitcoin is currently held in the portfolio.')
    else:
        value = total_coins * live_price
        print(f'The current value of the Bitcoin portfolio in AUD is: ${value:.2f}')