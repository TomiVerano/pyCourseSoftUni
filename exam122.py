average_mine = float(0)
expected_income = float(0)
days_of_mining = int(0)

miners_pools = int(input())
for m in range(0, miners_pools + 1):
    if m >= 1 and (average_mine/days_of_mining) >= expected_income:
        print('Good job! Average gold per day: {0:.2f}.'.format(average_mine/days_of_mining))
    if m >= 1 and (average_mine/days_of_mining) < expected_income:
        print('You need {0:.2f} gold.'.format((expected_income - (average_mine/days_of_mining))))
    expected_income = float(input())
    days_of_mining = int(input())
    average_mine = float(0)
    for c in range(0, days_of_mining + 1):
        real_income = float(input())
        average_mine += real_income