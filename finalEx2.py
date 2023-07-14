def slice_key(start_i, stop_i, key_g):
    mod_key_s = ""
    mod_key_g = []
    for ch in range(len(key_g)):
        if ch not in range(start_i, stop_i):
            mod_key_g.append(key_g[ch])
    mod_key_s = "".join(mod_key_g)
    print(mod_key_s)
    return mod_key_s


def flip_up(start_i, stop_i, key_g):
    mod_key_s = ""
    mod_key_g = []
    for ch in range(len(key_g)):
        if ch in range(start_i, stop_i):
            mod_key_g.append(key_g[ch].upper())
        else:
            mod_key_g.append(key_g[ch])
    mod_key_s = "".join(mod_key_g)
    print(mod_key_s)
    return mod_key_s


def flip_lo(start_i, stop_i, key_g):
    mod_key_s = ""
    mod_key_g = []
    for ch in range(len(key_g)):
        if ch in range(start_i, stop_i):
            mod_key_g.append(key_g[ch].lower())
        else:
            mod_key_g.append(key_g[ch])
    mod_key_s = "".join(mod_key_g)
    print(mod_key_s)
    return mod_key_s


def contains_sub(sub_string, key_g):
    if sub_string in key_g:
        print(f"{key_g} contains {sub_string}")
    else:
        print("Substring not found!")
    return key_g


gen_key = input()
command = input()
while command != "Generate":
    list_comm = command.split(">>>")
    if list_comm[0] == "Slice":
        gen_key = slice_key(int(list_comm[1]), int(list_comm[2]), gen_key)
    if list_comm[0] == "Flip":
        if list_comm[1] == "Upper":
            gen_key = flip_up(int(list_comm[2]), int(list_comm[3]), gen_key)
        elif list_comm[1] == "Lower":
            gen_key = flip_lo(int(list_comm[2]), int(list_comm[3]), gen_key)
    if list_comm[0] == "Contains":
        gen_key = contains_sub(list_comm[1], gen_key)
    command = input()

print(f"Your activation key is: {gen_key}")








