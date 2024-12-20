from cmc_api_live import print_live_price
from csv_management import User, Admin
from portfolio_calculations_current import print_total_coins, print_portfolio_value
from portfolio_calculations_historical import calculate_portfolio_gains

# Establishing User and Admin access
user = User(name = 'User')
admin = Admin(name = 'Admin')

# Sample holdings data for use in replace_holdings
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

# CSV Management
## Both Users and Admins have read access
user.show_holdings()
admin.show_holdings()
## Only Admins have write access
admin.add_holding(0.001, '2024-12-19')
admin.replace_holdings(holdings)

## Portfolio Calculations
print_live_price()
print_total_coins()
print_portfolio_value()
calculate_portfolio_gains()