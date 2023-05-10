# Write a program that reads a floating-point number and:
# prints "zero" if the number is zero
# prints "positive" or "negative"
# adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds
# 1 000 000

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