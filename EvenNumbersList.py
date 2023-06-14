def string_extract_indices_even_numbers():
    string_numbers = list(map(int, input().split(', ')))
    indices = map(lambda x: x if string_numbers[x] % 2 == 0 else 'no', range(len(string_numbers)))
    even_indices = list(filter(lambda x: x != 'no', indices))
    print(even_indices)


string_extract_indices_even_numbers()
