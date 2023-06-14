original_word = input()
re_writed = input()
last_string = original_word
for c in range(len(original_word)):
    first_part = re_writed[:c + 1]
    second_part = original_word[c + 1:]
    new_string = first_part + second_part
    if new_string == last_string:
        continue
    else:
        print('{0}'.format(new_string))
        last_string = new_string
