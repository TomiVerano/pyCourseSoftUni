def sum_even_odd(numbers_string):
    sum_even = int(0)
    sum_odd = int(0)
    for ch_num in numbers_string:
        if int(ch_num) % 2 == 0:
            sum_even += int(ch_num)
        else:
            sum_odd += int(ch_num)
    print('Odd sum = {0:.0f}, Even sum = {1:.0f}'.format(sum_odd, sum_even))


number = input()
sum_even_odd(number)

