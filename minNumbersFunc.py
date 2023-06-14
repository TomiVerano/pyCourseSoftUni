def find_min_number(list):
    result = min(list)
    print(result)


nums = []
for num in range(3):
    nums.append(int(input()))
find_min_number(nums)