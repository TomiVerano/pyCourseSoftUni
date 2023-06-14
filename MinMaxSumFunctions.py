def all_in_one_f_min_max_sum(int_numbers):

    min_number = min(int_numbers)
    max_number = max(int_numbers)
    sum_number = sum(int_numbers)
    print('The minimum number is {0:.0f}'.format(min_number))
    print('The maximum number is {0:.0f}'.format(max_number))
    print('The sum number is: {0:.0f}'.format(sum_number))

string_numbers = input().split()
int_numbers = [int(x) for x in string_numbers]
all_in_one_f_min_max_sum(int_numbers)