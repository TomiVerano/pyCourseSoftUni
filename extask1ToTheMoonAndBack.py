import math

average_speed = float(input())
volume_fuel = int(input())
distance = 384400
time_to_stay = 3
time_for_travel = math.ceil((distance * 2) / average_speed)
total_time = time_for_travel + time_to_stay
total_fuel = (volume_fuel * (distance * 2)) / 100
print('{0:.0f}\n{1:.0f}'.format(total_time, total_fuel))
