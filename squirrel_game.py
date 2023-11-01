from collections import deque

def is_valid(value,max_value):
    return 0 <= value <= max_value


def next_move(command, curr_row, curr_col):
    if command == "up" and is_valid(curr_row - 1, rows):
        return curr_row - 1, curr_col
    if command == "down" and is_valid(curr_row + 1, rows):
        return curr_row + 1, curr_col
    if command == "left" and is_valid(curr_col - 1, cols):
        return curr_row, curr_col - 1
    if command == "right" and is_valid(curr_col + 1, cols):
        return curr_row, curr_col + 1


rows = int(input())
cols = rows
set_direction = deque((input().split(", ")))

the_map = []
row_squirrel, col_squirrel = None, None
hazelnut = int(3)

for i in range(rows):
    row = list(input())
    the_map.append(row)
    if "s" in row:
        row_squirrel = i
        col_squirrel = row.index("s")
    #if "h" in row:
        #hazelnut +=row.count("h")

while hazelnut != 0 or len(set_direction) == 0:
    comm = set_direction.popleft()
    if next_move(comm, row_squirrel, col_squirrel):
        next_row, next_col = next_move(comm, row_squirrel, col_squirrel)
        if the_map[next_row][next_col] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            break
        if the_map[next_row][next_col] == "h":
            hazelnut -= 1
            the_map[next_row][next_col] = "*"
    else:
        print("The squirrel is out of the field.")
        break
if hazelnut == 0:
    "Good job! You have collected all hazelnuts!"
print("Hazelnuts collected: {0:.0f}".format(hazelnut))

