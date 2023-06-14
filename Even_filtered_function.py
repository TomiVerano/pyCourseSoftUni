numbers_text = input().split()
even_int = [int(s) for s in numbers_text]
even_numbers_iterator = filter(lambda x: x % 2 == 0, even_int)
even = list(even_numbers_iterator)
print(even)