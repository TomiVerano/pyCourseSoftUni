resourses = {}

while True:
    current_resourse = input()
    if current_resourse == "stop":
        break
    current_quantity = int(input())
    if current_resourse not in resourses.keys():
        resourses[current_resourse] = 0
    resourses[current_resourse] += current_quantity
for resource, quantity in resourses.items():
    print(f"{resource} -> {quantity}")