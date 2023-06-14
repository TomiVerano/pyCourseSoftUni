spirit_points = int(0)
money = float(0)
multiplier = int(0)
quantity = int(input())
days_left = int(input())
for d in range(1, days_left + 1, 1):
    if d % 11 == 0:
        multiplier += 2
    if d % 2 == 0:
        spirit_points += 5
        money += ((quantity + multiplier) * 2)
    if d % 3 == 0:
        spirit_points += 13
        money += ((quantity + multiplier) * 8)
    if d % 5 == 0:
        spirit_points += 17
        money += ((quantity + multiplier) * 15)
    if d % 5 == 0 and d % 3 == 0 :
        spirit_points += 30
    if d % 10 == 0:
        spirit_points -= 20
        money += 23
        if d == days_left:
            spirit_points -= 30
print('Total cost: {0:.0f}'.format(money))
print('Total spirit: {0:.0f}'.format(spirit_points))
