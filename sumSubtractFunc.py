def sum_nums(num_a: int, num_b: int):
    return num_a + num_b


def subtract_nums(nu_a: int, nu_b: int):
    #if nu_a > nu_b:
    result = nu_a - nu_b
    #else:
        #result = nu_b - nu_a
    return result


def add_and_subtract(n_a: int, n_b: int, n_c: int):
    result = sum_nums(n_a, n_b)
    result = subtract_nums(result, n_c)
    print('{0:.0f}'.format(result))

num_a = int(input())
num_b = int(input())
num_c = int(input())
add_and_subtract(num_a, num_b, num_c)

