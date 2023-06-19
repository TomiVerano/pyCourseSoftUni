def check_supply(m_f, m_h, m_c):
    state = False
    if m_f <= 0:
        state = True
    elif m_h <= 0:
        state = True
    elif m_c <= 0:
        state = True
    return state


daily_portion = 300
month_food = float(input()) * pow(10, 3)
month_hay = float(input()) * pow(10, 3)
month_cover = float(input()) * pow(10, 3)

puppy_weight = float(input()) * pow(10, 3)
cover_daily = (puppy_weight * 1 / 3)
cover_daily = round(cover_daily, 2)
for day in range(1, 31, 1):
    month_food -= daily_portion
    month_food = round(month_food, 2)
    if day % 2 == 0:
        if check_supply(month_food, month_hay, month_cover):
            print('Merry must go to the pet store!')
            break
        else:
            if check_supply(month_food, month_hay, month_cover):
                print('Merry must go to the pet store!')
                break
            else:
                month_hay -= (month_food * 0.05)
                month_hay = round(month_hay, 2)
    if day % 3 == 0:
        if check_supply(month_food, month_hay, month_cover):
            print('Merry must go to the pet store!')
            break
        else:
            month_cover -= cover_daily
            month_cover = round(month_cover, 2)
if not check_supply(month_food, month_hay, month_cover):
    print('Everything is fine! Puppy is happy! Food: {0:.2f}, Hay: {1:.2f}, Cover: {2:.2f}.'.format(month_food * pow(10, -3), month_hay * pow(10, -3), month_cover * pow(10, -3)))
