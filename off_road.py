from collections import deque

fuel_init = deque([int(x) for x in input().split()])
aci = deque([int(x) for x in input().split()])
fuel_to_go = deque([int(x) for x in input().split()])

result = "Reached altitudes:"
list_of_ra = []
number_of_alt = int(1)
number_of_alt_r = int(0)

while fuel_init or aci or fuel_to_go:
    curr_fuel = fuel_init.pop()
    curr_aci = aci.popleft()
    curr_f_t_g = fuel_to_go.popleft()
    if (curr_fuel - curr_aci) >= curr_f_t_g:
        list_of_ra.append(f"Altitude {number_of_alt}")
        print(f"John has reached: Altitude {number_of_alt}")
        number_of_alt_r += 1
    else:
        print(f"John did not reach: Altitude {number_of_alt}")
        break
    number_of_alt += 1

if not fuel_init:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print("John failed to reach the top.")
    if number_of_alt_r == 0:
        print("John didn't reach any altitude.")
    else:
        for alt in list_of_ra:
            result += f" {alt},"
        print(result[:-1])
