def check_counter(version):
    digit_string = ''
    version[-1] += 1
    for index in range(len(version) - 1, -1, -1):
        if version[index] > 9:
            version[index] = 0
            if index - 1 >= 0:
                version[index - 1] += 1
    for digit in version:
        digit_string += str(digit) + '.'
    print(digit_string[:-1])


def update_version():
    curr_version = [int(x) for x in input().split('.')]
    check_counter(curr_version)


update_version()