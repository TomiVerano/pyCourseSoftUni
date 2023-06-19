
def blacklist(f_list, name):
    if name not in f_list:
        print('{0} was not found.'.format(name))
    else:
        name_index = f_list.index(name)
        f_list.pop(name_index)
        #print(*f_list)
        f_list.insert(name_index, "Blacklisted")
        #print(*f_list)
        blacklist_list.append(f_list[name_index])
        #print(*blacklist_list)
        print('{0} was blacklisted.'.format(name))
    return f_list


def error_name(f_list, index):
    if (index >= 0) and (index < (len(f_list))):
        username = f_list[index]
        if not (username == "Blacklisted" or username == "Lost"):
            f_list.pop(index)
            f_list.insert(index, "Lost")
            print('{0} was lost due to an error.'.format(username))
    return f_list


def change_name(f_list, index, new_name):
    if (index >= 0) and (index < len(f_list)):
        #if new_name in f_list:
        curr_name = f_list[index]
        f_list.pop(index)
        f_list.insert(index, new_name)
        print('{0} changed his username to {1}.'.format(curr_name, new_name))
    return f_list

counter = int(0)
blacklist_list = []
friend_string = input().split(", ")
list_done = True

while list_done:
    text_comm = input()
    if text_comm == "Report":
        list_done = False
        break
    else:
        command = text_comm.split()
        if command[0] == "Blacklist":
            friend_string = blacklist(friend_string, command[1])
        if command[0] == "Error":
            friend_string = error_name(friend_string, int(command[1]))
        if command[0] == "Change":
            friend_string = change_name(friend_string, int(command[1]), command[2])

print('Blacklisted names: {0:.0f}'.format(len(blacklist_list)))
for name in friend_string:
    if name == "Lost":
        counter += 1
print('Lost names: {0:.0f}'.format(counter))
friend_print = " ".join(friend_string)
print(friend_print)

