total = float(0)
days_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

for day in range(1, days_plunder + 1, 1):
    total += daily_plunder
    if day % 3 == 0:
        total += daily_plunder * 0.5
    if day % 5 == 0:
        total -= (total * 0.3)
if total >= expected_plunder:
    print('Ahoy! {0:.2f} plunder gained.'.format(total))
else:
    result = (total / expected_plunder) * 100
    print('Collected only {0:.2f}% of the plunder.'.format(result))
