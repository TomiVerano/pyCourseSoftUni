
factor = int(input())
power = int(input())
numbers_list = []
for num in range(1, power + 1, 1):
    numbers_list.append(factor * num)
print(numbers_list)

#num_list = [power]
#for num in range(1, len(num_list) + 1, 1):
    #num_list[num] = num * factor
#print(num_list)