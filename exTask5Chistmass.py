import decimal

not_done = True
count_adults = 0
count_kids = 0
money_toys = decimal.Decimal(0)
money_sweaters = decimal.Decimal(0)
while not_done:
    key_word = input()
    if key_word == 'Christmas':
        not_done = False
    else:
        current_years_old = int(key_word)
        if current_years_old <= 16:
            count_kids += 1
        else:
            count_adults += 1
money_toys = count_kids * decimal.Decimal(5)
money_sweaters = count_adults * decimal.Decimal(15)
print('Number of adults: {0:.0f}'.format(count_adults))
print('Number of kids: {0:.0f}'.format(count_kids))
print('Money for toys: {0:.0f}'.format(money_toys))
print('Money for sweaters: {0:.0f}'.format(money_sweaters))


