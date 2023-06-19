def cupid_jump(list_houses, jump):
    changed_int_house = []
    for curr_house in list_houses:
        if check_index_jump(len(list_houses), jump):
            changed_int_house.append(int(curr_house) - jump )

    return changed_int_house


def check_index_jump(len_list_houses, jump):
    validator = True
    if len_list_houses < jump:
        validator = False
    return validator

def check_last_index()


house_list = input().split('@')
cupid_done = True

while cupid_done:
    input_command = input()
    if input_command != "Love!":
       cupid_done = False
       break
    else:
        jump_seq = input_command.split()
        jump_value = jump_seq[1]
