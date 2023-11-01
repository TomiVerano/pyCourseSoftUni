def next_dirr(command, curr_r, curr_c):
    if command == 'up':
        if 0 <= (curr_r - 1) < see_rows:
            return curr_r - 1, curr_c
        else:
            return (see_rows - 1), curr_c
    if command == 'down':
        if 0 <= (curr_r + 1) < see_rows:
            return curr_r + 1, curr_c
        else:
            return int(0), curr_c
    if command == 'left':
        if 0 <= (curr_c - 1) < see_cols:
            return curr_r, curr_c - 1
        else:
            return curr_r, (see_cols - 1)
    if command == 'right':
        if 0 <= (curr_c + 1) < see_cols:
            return curr_r, curr_c + 1
        else:
            return curr_r, int(0),


see_rows = int(input())
see_cols = see_rows
w_trap = False

see_map = []
boat_row, boat_col = None, None
fish_quota = int(20)
curr_catch = int(0)

for r in range(see_rows):
    row = list(input())
    see_map.append(row)
    if 'S' in row:
        boat_row = r
        boat_col = row.index('S')


command = input()
while command != "collect the nets" or curr_catch == 20:
    #for row in see_map:
        #print(''.join(row))
    next_row, next_col = next_dirr(command, boat_row, boat_col)
    #print(command)
    #print("-----------------------")
    see_map[boat_row][boat_col] = "-"
    boat_row = next_row
    boat_col = next_col
    if see_map[next_row][next_col] == "W":
        print("You fell into a whirlpool! The ship sank and you lost the fish you caught."
              " Last coordinates of the ship: [{0:.0f},{1:.0f}]".format(next_row,next_col))
        w_trap = True
        curr_catch = 0
        break
    if see_map[next_row][next_col].isdigit():
        #fish_quota -= int(see_map[next_row][next_col])
        curr_catch += int(see_map[next_row][next_col])
        see_map[next_row][next_col] = "-"
    see_map[next_row][next_col] = "S"
    command = input()
    #print(see_map[next_row],[next_col])

if curr_catch > 0:

    if curr_catch < 20:
        print("You didn't catch enough fish and didn't reach the quota! You need {0:.0f} tons of fish more.".format(fish_quota - curr_catch))

    else:
        print("Success! You managed to reach the quota!")

    print("Amount of fish caught: {0:.0f} tons.".format(curr_catch))
    if not w_trap:
        for row in see_map:
            print(''.join(row))



