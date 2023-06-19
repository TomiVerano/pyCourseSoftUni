def insert_space(init_message, index_space):
    init_message = init_message.insert(index_space, ' ')
    return init_message


def reverse(init_message, string_to_rev):
    #check = ''.join(init_message)
    #print(check)
    #print(string_to_rev)
    if True:
        #rev the subtring as list
        list_to_rev = list(string_to_rev)
        list_to_rev.reverse()
        print(list_to_rev)
        #list to string
        string_message = ' '.join(init_message)
        string_rev = ' '.join(list_to_rev)
        #find startindex of substring
        start_index = string_message.find(string_to_rev)
        string_message1 = string_message[:start_index]
        string_message2 = string_message[len(string_message):]
        #string_to_rev_string = ''.join(string_to_rev)
        string_to_rev_string = ''.join(list_to_rev)
        #string_to_rev_string.replace(" ","")
        final = string_message1 + string_message2 + string_to_rev_string
        #print(final)
        aha = final.split()
        #print(aha)
        return aha
    #else:
        #print('error')
        #return list(['no', 'no'])



def change(init_message, char_rem, char_rep):
    # list_message to string message
    string_message = ' '.join(init_message)
    print(string_message)
    # replace characters
    new_message = string_message.replace(str(char_rem), str(char_rep))
    #string_message to list message
    init_message = new_message.split()
    return init_message


init_message = input().split()
#action_1 = input()
decode = True

while decode:
    command_inp = input()
    if command_inp == "Reveal":
        decode = False
        #print('You have a new text message: {0}'.format(init_message))
        break
    else:
        command = command_inp.split(':|:')
        action = command[0]
        if action == "InsertSpace":
            init_message = insert_space(init_message, int(command[1]))
        elif action == "Reverse":
            init_message = reverse(init_message, command[1])
        elif action == "ChangeAll":
            init_message = change(init_message, command[1], command[2])
#format_message = ''.join(init_message)
print('You have a new text message: {0}'.format(init_message))