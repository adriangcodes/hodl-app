import csv

def show_holdings():
    try:
        with open('holdings.csv') as file:
            content = csv.DictReader(file)
            print('The following Bitcoin holdings are saved:')
            holdings_exist = False
            for row in content:
                holdings_exist = True
                print(row)
            if not holdings_exist:
                print('No holdings found in the CSV file.')
                
    except FileNotFoundError:
        print('The file holdings.csv cannot be found.')
    except PermissionError:
        print('You do not have permission to read holdings.csv.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        
def add_holding(file, amount, date):
    try:
        with open('holdings.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Amount', 'Date'])
            writer.writerow({'Amount': amount, 'Date': date})
            print(f'Bitcoin holding added: Amount = {amount}, Date = {date}')
        
    except FileNotFoundError:
        print('The file holdings.csv cannot be found.')
    except PermissionError:
        print('You do not have permission to write to holdings.csv.')
    except ValueError as ve:
        print(f'Validation error: {ve}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

# Sample holdings data for use in replace_holdings()

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
    try:
        with open('holdings.csv', 'w') as file:
            writer = csv.DictWriter(file, holdings[0].keys())
            writer.writeheader()
            writer.writerows(holdings)
            print('Bitcoin holdings updated - please review CSV file.')
            
    except FileNotFoundError:
        print('The file holdings.csv cannot be found.')
    except PermissionError:
        print('You do not have permission to write to holdings.csv.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')