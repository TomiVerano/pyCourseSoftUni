import decimal

mount_set = input()
hours_enjoyed = int(input())
people_enjoyed = int(input())
night_or_day = input()
total = decimal.Decimal(0)
price_day_partOne = decimal.Decimal(10.50)
price_day_partTwo = decimal.Decimal(12.60)
price_night_partOne = decimal.Decimal(8.40)
price_night_partTwo = decimal.Decimal(10.20)

if mount_set == 'march' or mount_set == 'april' or mount_set == 'may':
    if night_or_day == 'day':
        if people_enjoyed >= 4:
            price_day_partOne -= price_day_partOne * 10 / 100
        if hours_enjoyed >= 5:
            price_day_partOne -= price_day_partOne * 50 / 100
        total += price_day_partOne * hours_enjoyed * people_enjoyed
    else:
        if people_enjoyed >= 4:
            price_night_partOne -= price_night_partOne * 10 / 100
        if hours_enjoyed >= 5:
            price_night_partOne -= price_night_partOne * 50 / 100
        total += price_night_partOne * hours_enjoyed * people_enjoyed

if mount_set == 'june' or mount_set == 'july' or mount_set == 'august':
    if night_or_day == 'day':
        if people_enjoyed >= 4:
            price_day_partTwo -= price_day_partTwo * 10 / 100
        if hours_enjoyed >= 5:
            price_day_partTwo -= price_day_partTwo * 50 / 100
        total += price_day_partTwo * hours_enjoyed * people_enjoyed
    else:
        if people_enjoyed >= 4:
            price_night_partTwo -= price_night_partTwo * 10 / 100
        if hours_enjoyed >= 5:
            price_night_partTwo -= price_night_partTwo * 50 / 100
        total += price_night_partTwo * hours_enjoyed * people_enjoyed

print('Price per person for one hour: {0:.2f}'.format(total/hours_enjoyed/people_enjoyed))
print('Total cost of the visit: {0:.2f}'.format(total))