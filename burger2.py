def daily_profit(cash, spends):
    return cash + spends

def total_profit(profit):
    list_profit = []

    return list_profit


number = int(input())

for city in range(number):
    profit = float(0)
    city_name = input()
    cash = float(input())
    spends = float(input())
    profit = daily_profit(cash - spends)
    if city % 3 == 0:
        profit = daily_profit(cash, (spends + (spends * 0.5)))
    if city % 5 == 0:
        cash -= (cash * 0.1)
        profit = daily_profit(cash, spends)
print('In {0} Burger Bus earned {1:.2f} leva.'.format(city_name, profit))
print('Burger Bus total profit: {0:.2f} leva.'.format(total_profit))
