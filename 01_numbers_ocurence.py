numbers = tuple(map(float, input().split()))
#print(numbers)

nums_occurances = {}
for num in numbers:
    if num not in nums_occurances:
        nums_occurances[num] = 0
    nums_occurances[num] += 1

[print(f"{key} - {value} times") for key, value in nums_occurances.items()]
