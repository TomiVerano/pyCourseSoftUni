def print_result(list, class_word):
    result_string = class_word + ': '
    if list:
        for item in list:
            result_string += str(item) + ', '
        print(result_string[:-2])
    else:
        print(result_string)

def sort_odd(list):
    list_odd = [num for num in list if num % 2 != 0]
    return list_odd


def sort_even(list):
    list_even = [num for num in list if num % 2 == 0]
    return list_even


def sort_negative(list):
    list_negative = [num for num in list if num < 0]
    return list_negative


def sort_positive(list):
    list_positive = [num for num in list if num >= 0]
    return list_positive


def sort_string_numbers():
    numbers = [int(num) for num in input().split(', ')]
    print_result(sort_positive(numbers), 'Positive')
    print_result(sort_negative(numbers), 'Negative')
    print_result(sort_even(numbers), 'Even')
    print_result(sort_odd(numbers), 'Odd')


sort_string_numbers()
