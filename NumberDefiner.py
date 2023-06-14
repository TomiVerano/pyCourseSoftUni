number_to_define = float(input())
if number_to_define == 0:
    print('zero')
elif number_to_define >0:
    if number_to_define < 1:
        print('small positive')
    elif number_to_define > 100000:
        print('large positive')
    else:
        print('positive')
else:
    if abs(number_to_define) < 1:
        print('small negative')
    elif abs(number_to_define) > 100000:
        print('large negative')
    else:
        print('negative')