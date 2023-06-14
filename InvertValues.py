numbers_int = []
numbers_string = input().split()
for num in numbers_string:
    num_int = int(num)
    if num_int > 0:
        num_int = -num_int
        numbers_int.append(num_int)
    else:
        num_int += 2 * -num_int
        numbers_int.append(num_int)
print(numbers_int)
