first_player, second_player = input().split(", ")

maze_board = []

for r in range(6):
    maze_board.append(input().split())

first_player_rest = False
second_player_rest = False

while True:
    #player_one moves
    first_player_cord = input()
    if not first_player_rest:
        row, col = map(int, first_player_cord.strip("(").strip(")").split(","))
        position = maze_board[row][col]
        if position == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break
        if position == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        if position == "W":
            print("")
            print(f"{first_player} hits a wall and needs to rest.")
            first_player_rest = True
    else:
        first_player_rest = False

    #player_two moves
    second_player_cord = input()
    if not second_player_rest:
        row, col = map(int, second_player_cord.strip("(").strip(")").split(","))
        position = maze_board[row][col]
        if position == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break
        if position == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        if position == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            second_player_rest = True
    else:
        second_player_rest = False