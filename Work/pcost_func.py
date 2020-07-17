# pcost_func.py
#
# Exercise 1.30
def portfolio_cost(filename):
        cost_all = 0.0

    with open('Data/portfolio.csv', 'rt') as f:
        headers = next(f).split(',')
        for line in f:
            row = line.split(',')
            share_count = int(row[1])
            share_price = float(row[2])
            cost_all = cost_all + (share_count * share_price)
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)