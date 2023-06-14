init_energy = int(input())
distance = input()
battle_won = int(0)

while distance != 'End of battle':
    distance = int(distance)
    if init_energy >= distance and init_energy > 0:
        init_energy -= distance
        battle_won += 1

        if battle_won % 3 == 0:
            init_energy += battle_won
    else:
        print('Not enou')
        break

    distance = input()
else:
    print('Won battles')