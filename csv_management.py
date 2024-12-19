import csv

def show_holdings():
    with open('holdings.csv') as file:
        content = csv.DictReader(file)
        for row in content:
            print(row)
            
def add_holding(file, amount, date):
    with open('holdings.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Amount', 'Date'])
        writer.writerow({'Amount': amount, 'Date': date})
        print(f'BTC holding added: Amount={amount}, Date={date}')
        
holdings = [
    {
        'Amount': '0.05',
        'Date': '2024-12-15'
    },
    {
        'Amount': '0.1',
        'Date': '2024-12-16'
    },
    {
        'Amount': '0.2',
        'Date': '2024-12-17'
    },
]

def replace_holdings():
    with open('holdings.csv', 'w') as file:
        writer = csv.DictWriter(file, holdings[0].keys())
        writer.writeheader()
        writer.writerows(holdings)
        print('BTC holdings updated - please review CSV.')