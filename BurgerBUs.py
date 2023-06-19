def profit(earned, expences):
    money = earned - expences
    money = round(money, 2)
    return money



city_count = int(input())

total_profit = float(0)
#profit = float(0)
for city in range(1, city_count + 1, 1):
    daily_profit = float(0)
    city_name = input()
    earned_money = float(input())
    expences = float(input())
    if earned_money < 0 or expences < 0:
        continue
    else:
        if not (city % 5 == 0) and not (city % 3 == 0):
            daily_profit = profit(earned_money, expences)
        else:
            if city % 3 == 0:
                expences += (expences * 0.5)
                expences = round(expences, 2)
            elif city % 5 == 0:
                earned_money -= (earned_money * 0.1)
                earned_money = round(earned_money, 2)
            daily_profit = profit(earned_money, expences)
        total_profit += daily_profit
        total_profit = round(total_profit, 2)
        print('In {0} Burger Bus earned {1:.2f} leva.'.format(city_name, daily_profit))
print('Burger Bus total profit: {0:.2f} leva.'.format(total_profit))

