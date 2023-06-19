def urgent(g_list, products):
    urgent_product = products[1]
    if urgent_product not in g_list:
        g_list.insert(0, urgent_product)
    return g_list


def unnecessary(g_list, products):
    unnecessary_product = products[1]
    if unnecessary_product in g_list:
        g_list.pop(unnecessary_product)
    return g_list


def correct(g_list, products):
    replaced = products[1]
    substitute = products[2]
    if replaced in g_list:
        index = g_list.index(replaced)
        g_list.pop(index)
        #print(index_replaced)
        g_list.insert(index, substitute)
    return g_list


def rearrange(g_list, products):
    rearrange_product = products[1]
    if rearrange_product in g_list:
        index = g_list.index(rearrange_product)
        g_list.pop(index)
        g_list.append(rearrange_product)
    return g_list


init_g_list = input().split('!')
go_shopping = True
while go_shopping:
    input_text = input()
    if input_text == "Go Shopping!":
        go_shopping = False
        final_g_list = ", ".join(init_g_list)
        print(final_g_list)
        break
    else:
        command = input_text.split()
        if command[0] == "Urgent":
            init_g_list = urgent(init_g_list, command)
        elif command[0] == "Unnecessary":
            init_g_list = unnecessary(init_g_list, command)
        elif command[0] == "Correct":
            init_g_list = correct(init_g_list, command)
        elif command[0] == "Rearrange":
            init_g_list = rearrange(init_g_list, command)
