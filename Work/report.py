# report.py
#
# Exercise 2.11
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            stock = {
                 'name'   : row[0],
                 'shares' : int(row[1]),
                 'price'   : float(row[2])
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report(portfolio, prices):

    rows = []
    for s in portfolio:
        current_price = prices[s['name']]
        change = current_price - s['price']
        summary = (s['name'], s['shares'], current_price, change)
        rows.append(summary)
    return rows
        
        

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

#exercise 2.7
total_cost = 0.0
current_value = 0.0

for s in portfolio:
    total_cost += s['shares'] * s['price']
    current_value += s['shares'] * prices[s['name']]

#output
print('Total cost', total_cost)
print('Current value', current_value)
print('Gain/Loss', current_value - total_cost)
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
dashes = ('----------', '----------', '----------', '----------')
print('%1s %1s %1s %1s' % dashes)
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)