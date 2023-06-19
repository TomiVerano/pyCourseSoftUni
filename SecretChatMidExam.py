def insert_space(command_text, message):
    new_message = ''
    command = command_text.split(':|:')
    command_instruction = command[0]
    command_index = command[1]
    if command_instruction == 'InsertSpace':
        command_index = int(command_index)
        for ch in range(len(message)):
            if ch == command_index:
                new_message += ' '
            new_message += message[ch]
    return new_message


def reverse_substring(command_text, message):
    new_message = ''
    command = command_text.split(':|:')
    command_instruction = command[0]
    command_substring = command[1]
    if command_instruction == 'Reverse':
        bool_sub_string = message.__contains__(command_substring)
        if bool_sub_string:
            start_index = message.find(command_substring)
            for ch in range(len(message)):
                if ch >= start_index or ch <= len(command_substring):
                    continue
                else:
                    new_message += message[ch]
                    rev_command_substring = command_substring[::-1]
                    new_message += rev_command_substring
    return new_message

concealed_message = input()
reveled_message = ''
while True:
    command_text = input()
    if command_text == 'Reveal':
        print('You have a new text message: {0}'.format(reveled_message))
    else:
        new_message = insert_space(command_text, concealed_message)
        sec_new_message = reverse_substring(command_text, concealed_message)
        print(new_message)
        print(concealed_message)
        print(sec_new_message)