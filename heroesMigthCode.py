

def cast_spell(hero_name_c, mana_cost, spell, hero_list_c):
    for hero in hero_list_c:
        if hero[0] == hero_name_c:
            if hero[2] < mana_cost:
                print(f"{hero[0]} does not have enough MP to cast {spell}!")
            else:
                hero[2] -= mana_cost
                print(f"{hero[0]} has successfully cast {spell} and now has {hero[2]} MP!")
    return hero_list_c


def take_damage(hero_name_t, points, enemy_name, hero_list_t):
    for hero in hero_list_t:
        if hero[0] == hero_name_t:
            if hero[1] - points <= 0:
                print(f"{hero[0]} has been killed by {enemy_name}!")
                index = hero_list_t.index(hero)
                hero_list_t.pop(index)
            else:
                hero[1] -= points
                print(f"{hero[0]} was hit for {points} HP by {enemy_name} and now has {hero[1]} HP left!")
    return hero_list_t


def recharge(hero_name1, points, hero_list_1):
    for hero in hero_list_1:
        if hero[0] == hero_name1:
            if not hero[2] + points > 200:
                hero[2] += points
                print(f"{hero[0]} recharged for {points} MP!")
            else:
                var = 200 - hero[2]
                print(f"{hero[0]} recharged for {var} MP!")
                hero[2] = 200
                var = 0
    return hero_list_1


def heal(hero_name1, points, hero_list_1):
    for hero in hero_list_1:
        if hero_name1 == hero[0]:
            if not hero[1] + points > 100:
                hero[1] += points
                print(f"{hero[0]} healed for {points} HP!")
            else:

                var = 100 - (hero[1])
                print(f"{hero[0]} healed for {var} HP!")
                hero[1] = 100
                var = 0
    return hero_list_1


hero_list = []
numbers_of_heroes = int(input())
for heroes in range(numbers_of_heroes):
    tavern_shop = input().split()
    hero_name = tavern_shop[0]
    hero_hit_points = int(tavern_shop[1])
    hero_mana_points = int(tavern_shop[2])
    hero_stats = []
    hero_stats.append(hero_name)
    hero_stats.append(hero_hit_points)
    hero_stats.append(hero_mana_points)
    hero_list.append(hero_stats)

combat_command = input()
while combat_command != "End":
    command = combat_command.split(" - ")
    if command[0] == "Heal":
        hero_list = heal(command[1], int(command[2]), hero_list)
    if command[0] == "Recharge":
        #print(*command)
        hero_list = recharge(command[1], int(command[2]), hero_list)
    if command[0] == "TakeDamage":
        hero_list = take_damage(command[1], int(command[2]), command[3], hero_list)
    if command[0] == "CastSpell":
        hero_list = cast_spell(command[1], int(command[2]), command[3], hero_list)
    combat_command = input()

for hero in hero_list:
    print(f"{hero[0]}\n  HP: {hero[1]}\n  MP: {hero[2]}")