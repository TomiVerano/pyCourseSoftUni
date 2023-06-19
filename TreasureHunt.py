def loot(loots, list_of_items):
    for item in list_of_items:
        if item not in loots:
            loots.insert(0, item)
    return loots

def drop(loots, index_drop):
    if index_drop in range(len(loots)):
        remove = loots.pop(index_drop)
        loots.append(remove)
    return loots



def steal(loots, steal_count):
    if steal_count >= len(loots):
        print(", ".join(loots))
        loots = []
    else:
        steal_index = len(loots) - steal_count
        loots = loots[0:steal_index]
        print(", ".join(loots))
    return loots

init_loot = input().split("|")
command = input()
while command != "Yohoho!":
    command = command.split()
    action = command[0]
    if action == "Loot":
        items = command[1:]
        init_loot = loot(init_loot, items)
    elif action == "Drop":
        index = int(command[1])
        init_loot = drop(init_loot, index)
    elif action == "Steal":
        count = int(command[1])
        init_loot = steal(init_loot, count)
    if not init_loot:
        print('Failed treasure hunt.')
    else:
        average_gain = sum(len(item) for item in init_loot) / len(init_loot)
        print('Average treasure gain: {0:.2f} pirate credits.'.format(average_gain))