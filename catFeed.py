import decimal

cat_count = int(input())
group_small = int(0)
group_medium = int(0)
group_large = int(0)
calc_consumation = decimal.Decimal(0)
for c in range(cat_count):
    food_vol = int(input())
    calc_consumation += food_vol
    if (food_vol >= 100) and (food_vol < 200):
        group_small += 1
    if (food_vol >= 200) and (food_vol < 300):
        group_medium += 1
    if (food_vol >= 300) and (food_vol < 400):
        group_large += 1
calc_consumation /= 1000
calc_consumation *= decimal.Decimal(12.45)
print('Group 1: {0:.0f} cats.'.format(group_small))
print('Group 2: {0:.0f} cats.'.format(group_medium))
print('Group 3: {0:.0f} cats.'.format(group_large))
print('Price for food per day: {0:.2f} lv.'.format(calc_consumation))



