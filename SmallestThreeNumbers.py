def print_smallest_number(num1: int, num2: int, num3: int):
    state_one = True
    if num1 > num2 and num1 > num3:
        if num2 > num3:
            print(num3)
            state_one = False
        else:
            print(num2)
            state_one = False
    else:
        if num2 > num1 and num2 > num3:
            if num1 > num3:
                print(num3)
                state_one = False
            else:
                print(num1)
                state_one = False
    if state_one:
        print(num2)


num = int(input())
num_s = int(input())
num_t = int(input())
print_smallest_number(num, num_s, num_t)


