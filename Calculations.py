def multiply_two_arg(a, b):
    product = a * b
    print('{0:.0f}'.format(product))


def subtract_two_arg(a, b):
    product = a - b
    print('{0:.0f}'.format(product))


def add_two_arg(a, b):
    product = a + b
    print('{0:.0f}'.format(product))


def divide_two_arg(a, b):
    if a == 0:
        print('error Division by zero@')
    else:
        product = a / b
        print('{0:.0f}'.format(product))


def calculator(string_command, a, b):
    if string_command == 'multiply':
        multiply_two_arg(int(a), int(b))
    if string_command == 'divide':
        divide_two_arg(int(a), int(b))
    if string_command == 'add':
        add_two_arg(int(a), int(b))
    if string_command == 'subtract':
        subtract_two_arg(int(a), int(b))


user_input = input()
data_param_one = input()
data_param_two = input()
calculator(user_input, data_param_one, data_param_two)
