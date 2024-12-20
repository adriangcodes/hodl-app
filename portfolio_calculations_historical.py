import csv
from cmc_api_live import pull_live_price
from cmc_api_historical import pull_historical_price

def calculate_portfolio_gains():
    live_price = pull_live_price()
    if live_price is None:
        print('Unable to retrieve live Bitcoin price.')
        return

    holdings_file = 'holdings.csv'
    try:
        with open(holdings_file, 'r') as file:
            portfolio_data = list(csv.DictReader(file))
    except FileNotFoundError:
        print('The file holdings.csv cannot be found.')
        return

    investment = 0
    total_current_value = 0
    gains_data = []

    for entry in portfolio_data:
        try:
            amount = float(entry['Amount'])
            date = entry['Date']

            historical_price = pull_historical_price(date)
            if historical_price is None:
                print(f'Failed to retrieve historical price for {date}. Skipping entry.')
                continue

            original_value = amount * historical_price
            current_value = amount * live_price
            gain = current_value - original_value

            investment += original_value
            total_current_value += current_value

            gains_data.append({
                'amount': amount,
                'purchase_date': date,
                'historical_price': historical_price,
                'current_value': current_value,
                'gain': gain,
            })

        except (KeyError, ValueError) as e:
            print(f'Error processing entry: {entry}. Error: {e}')

    print('All figures are in AUD.')
    print(f'Live Bitcoin Price: ${live_price:.2f}')
    print(f'Portfolio Investment: ${investment:.2f}')
    print(f'Current Portfolio Value: ${total_current_value:.2f}')
    print(f'Gain/Loss: ${total_current_value - investment:.2f}')