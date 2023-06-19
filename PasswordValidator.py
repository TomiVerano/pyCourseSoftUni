import symbol

def validating_pasword(password):
    state = True
    counter = int(0)
    for num in password:
        if num.isnumeric():
            counter += 1
    if counter < 2:
        print('Password must have at least 2 digits')
        state = False
    return state


def valid_long(password):
    state = True
    if len(password) < 6 or len(password) > 10:
        print('Password must be between 6 and 10 characters')
        state = False
    return state


def valid_digit(password):
    state = True
    if not password.isalnum():
        print('Password must consist only of letters and digits')
        state = False
    return state


def valid(state1, state2, state3):
    if state1 and state2 and state3:
        print('Password is valid')

password = input()
valid(valid_long(password), valid_digit(password), validating_pasword(password))
