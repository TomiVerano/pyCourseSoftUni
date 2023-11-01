from collections import deque


monsters = deque([int(x) for x in input().split(",")])
soldiers = deque([int(x) for x in input().split(",")])


#print(*monsters)
#print(*soldier)
init_length_m = len(monsters)
init_length_s = len(soldiers)
counter = int(0)
damage = int(0)
while True:
    counter += 1
    curr_sol = soldiers[-1] + damage
    #print(curr_sol)
    damage = int(0)
    curr_monst = monsters[0]
    #print(curr_monst)
    if curr_sol - curr_monst >= 0:
        monsters.popleft()
        soldiers.rotate()
        if curr_sol - curr_monst != 0:
            damage = curr_sol - curr_monst
    else:
        if curr_monst - curr_sol > 0:
            monsters[0] = curr_monst - curr_sol
            soldiers.pop()
            monsters.rotate(-1)
    if len(soldiers) == 0 or len(monsters) == 0:
        break

if len(soldiers) == 0:
    print("The soldier has been defeated.")
    print("Total monsters killed: {0:.0f}".format(init_length_m - len(monsters)))
if len(monsters) == 0:
    print("All monsters have been killed!")
    print("Total monsters killed: {0:.0f}".format(init_length_m))

