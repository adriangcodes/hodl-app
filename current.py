import csv 
from cmc_api_current import current_bitcoin_price

total_holdings = 0

with open('holdings.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_holdings += float(row['Amount'])

current_value = total_holdings * current_bitcoin_price

print(f"The current price of Bitcoin (BTC) in USD is: ${current_bitcoin_price:.2f}")
print(f'The total BTC holdings are: {total_holdings:.8f}')    
print(f'The current value of the portfolio in USD is: ${current_value:.2f}')