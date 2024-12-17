import csv

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

with open('holdings.csv', 'w') as file:
    writer = csv.DictWriter(file, holdings[0].keys())
    writer.writeheader()
    writer.writerows(holdings)