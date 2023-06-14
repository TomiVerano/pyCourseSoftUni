def print_chars_range(char_a: chr, char_b: chr):
    char_list = []
    start_index = ord(char_a)
    stop_index = ord(char_b)
    #if start_index > stop_index:
        #diff_range = (start_index - stop_index)
    #else:
        #diff_range = (stop_index - start_index)
    for curr_char in range(start_index + 1, stop_index, 1):
        #print('{0}'.format(chr(curr_char)))
        char_list.append(chr(curr_char))
    print(*char_list)


char_a = input()
char_b = input()
print_chars_range(char_a, char_b)