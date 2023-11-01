from collections import deque

egg_line = deque([x for x in input().split(", ")])
list_line = deque([x for x in input().split(", ")])

box_filled = int(0)

while egg_line and list_line:
    curr_egg = egg_line.popleft()
    curr_list = list_line.pop()
    if (int(curr_egg) + int(curr_list)) > 50:
        curr_egg = egg_line.popleft()
        curr_list = list_line.pop()
    else:
        if int(curr_egg) <= 0:
            list_line.append(curr_list)
        elif int(curr_egg) == 13:
            first_papper = list_line.popleft()
            list_line.append(first_papper)
            list_line.appendleft(curr_list)
            #print("{0}".format(", ".join(list_line)))
        elif int(curr_egg) > 0 and int(curr_egg != 13):
            box_filled += 1
if box_filled == 0:
    print("Sorry! You couldn't fill any boxes!")
else:
    if not egg_line :
        pappers_left = ", ".join(list_line)
        print("Great! You filled {0:.0f} boxes.".format(box_filled))
        print("Pieces of paper left: {0}".format(pappers_left))
    if not list_line:
        eggs_left = ", ".join(egg_line)
        print("Great! You filled {0:.0f} boxes.".format(box_filled))
        print("Eggs left: {0}".format(eggs_left))
