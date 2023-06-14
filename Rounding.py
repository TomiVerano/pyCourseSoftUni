def round_number(string_numbers):
    rounded_number = []
    for num in string_numbers:
        rounded_number.append(round(float(num)))
    print(rounded_number)


input_number = input().split()
round_number(input_number)
