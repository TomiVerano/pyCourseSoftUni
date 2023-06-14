survivers = ''
real_numbers = []
number = input().split()
n_remove = int(input())
for string_number in number:
    real_numbers.append(int(string_number))

for i in range(n_remove):
    real_numbers.remove(min(real_numbers))
for number in real_numbers:
    survivers += str(number)
    survivers += ', '
#print(real_numbers)
print(survivers[:-2])

# print(real_numbers)
