# pcost.py
#
# Exercise 1.27
cost_all = 0.0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    for line in f:
        row = line.split(',')
        share_count = int(row[1])
        share_price = float(row[2])
        cost_all = cost_all + (share_count * share_price)

print ('Total cost ', round(cost_all, 2))
