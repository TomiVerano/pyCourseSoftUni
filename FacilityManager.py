def chair_map_visitors():
    chairs = []
    visitors = []
    conference_count = int(input())
    for room in range(conference_count):
        current_room = input().split(' ')
        chairs.append(len(current_room[0]))
        visitors.append(int(current_room[1]))
    diff = int(0)
    game_on = True
    for count in range(len(chairs)):
        if chairs[count] < visitors[count]:
            print('{0:.0f} more chairs needed in room {1:.0f}'.format(visitors[count] - chairs[count], count + 1))
            game_on = False
        else:
            diff += (chairs[count] - visitors[count])
    if game_on:
        print('Game On, {0:.0f} free chairs left'.format(diff))

chair_map_visitors()