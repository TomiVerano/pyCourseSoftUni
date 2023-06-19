def chat(f_list, message):
    #if message not in f_list:
    f_list.append(message)
    return f_list


def delete(f_list, message_to_delete):
    if message_to_delete in f_list:
        index = f_list.index(message_to_delete)
        f_list.pop(index)
    return f_list


def edit(f_list, message, edited):
    if message in f_list:
        index_message = f_list.index(message)
        f_list.pop(index_message)
        f_list.insert(index_message, edited)
    return f_list


def pin(f_list, message):
    if message in f_list:
        index = f_list.index(message)
        f_list.pop(index)
        f_list.append(message)
    return f_list


def spam(f_list, list_message):
    for message in list_message:
        f_list.append(message)
    return f_list





chat_final = []
chat_list = []
chat_logged = True

while chat_logged:
    command_string = input()
    if command_string == "end":
        chat_logged = False
        break
    else:
        command = command_string.split()
        #print(command)
        #print(chat_list)
        if command[0] == "Chat":
            chat_final = chat(chat_final, command[1])
        elif command[0] == "Edit":
            chat_final = edit(chat_final, command[1], command[2])
        elif command[0] == "Spam":
            chat_list = command[1:]
            chat_final = spam(chat_final, chat_list)
        elif command[0] == "Delete":
            chat_final = delete(chat_final, command[1])
        elif command[0] == "Pin":
            chat_final = pin(chat_final, command[1])

for message in chat_final:
    print(message)