def 

def parse_text(string_text):
    list_words = []
    for ch in string_text:
        if ch == '@' or ch == '#':
            continue
        else:
            list_words.append(str(ch))
    return list_words


input_text_string = input()
list_words = []
list_words = parse_text(input_text_string)
print(list_words)