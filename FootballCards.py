is_game_over = False
team_a = []
team_b = []
for p in range(0, 11, 1):
    team_a.append('A' + '-' + str(p + 1))
    team_b.append('B' + '-' + str(p + 1))
input_cards = input().split()
for player in input_cards:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        is_game_over = True
        break
print('Team A - {0:.0f}; Team B - {1:.0f}'.format(len(team_a), len(team_b)))
if is_game_over:
    print('Game was terminated')
#print(team_a)
#print(team_b)
