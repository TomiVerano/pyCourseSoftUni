from collections import deque

egg_line = deque([int(x) for x in input().split(", ")])
list_line = deque([int(x) for x in input().split(", ")])

box_filled = int(0)

while egg_line and list_line:
    curr_egg = egg_line.popleft()
    curr_list = list_line.pop()
    if curr_egg <= 50 and curr_list <= 50:
        box_filled += 1
    if curr_egg <= 0:
        list_line.appendleft(curr_list)
    if curr_egg == 13:
        first_papper = list_line.popleft()
        list_line.append(first_papper)
        list_line.appendleft(curr_list)

if box_filled == 0:
    print("Sorry! You couldn't fill any boxes!")
else:
    if not egg_line :
        pappers_left = int(", ".join(list_line))
        print("Great! You filled {0:.0f} boxes.".format(box_filled))
        print("Pieces of paper left: {0}".format(pappers_left))
    if not list_line:
        eggs_left = str(", ".join(egg_line))
        print("Great! You filled {0:.0f} boxes.".format(box_filled))
        print("Eggs left: {0}".format(eggs_left))
