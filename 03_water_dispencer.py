from collections import deque

disp_volume = int(input())
water_line = deque()

name = input()

while name != "Start":
    water_line.append(name)
    name = input()

command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        liters_to_give = int(data[0])
        person_name = water_line.popleft()
        if liters_to_give <= disp_volume:
            disp_volume -= liters_to_give
            print("{0} got water".format(person_name))
        else:
            print("{0} must wait".format(person_name))
    else:
        liters_to_add = int(data[1])
        disp_volume += liters_to_add
    command = input()
print("{0:.0f} liters left".format(disp_volume))


















