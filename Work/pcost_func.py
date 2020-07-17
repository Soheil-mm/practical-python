# pcost_func.py
#
# Exercise 1.30
def portfolio_cost(share):
        cost_all = 0.0

    with open('Data/portfolio.csv', 'rt') as f:
        headers = next(f).split(',')
        for line in f:
            row = line.split(',')
            share_count = int(row[1])
            share_price = float(row[2])
            cost_all = cost_all + (share_count * share_price)

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)