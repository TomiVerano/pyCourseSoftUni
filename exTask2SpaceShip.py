import math

ship_wight = float(input())
ship_hight = float(input())
ship_depth = float(input())
average_hight_spacemans = float(input())

calc_volume_ship = ship_depth * ship_hight * ship_wight
calc_volume_room = (average_hight_spacemans + 0.40) * 2 * 2
spacemans = math.floor(calc_volume_ship / calc_volume_room)
if (spacemans >= 3) and (spacemans <= 10):
    print('The spacecraft holds {0:.0f} astronauts.'.format(spacemans))
else:
    if spacemans > 10:
        print('The spacecraft is too big.')
    else:
        print('The spacecraft is too small.')