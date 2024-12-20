import csv

class User: # Base user class, providing read access.

    def __init__(self, name, file_path = 'holdings.csv'):
        self.name = name
        self.file_path = file_path

    def show_holdings(self):
        try:
            with open(self.file_path) as file:
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

class Admin(User):

    def add_holding(self, amount, date):
        try:
            with open(self.file_path, 'a', newline='') as file:
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

    def replace_holdings(self, holdings):
        try:
            with open(self.file_path, 'w') as file:
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