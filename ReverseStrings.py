def reverse_string(word):
    rev_word = ""
    for ch in reversed(word):
        rev_word += ch
    return rev_word


pair_strings = {}

while True:
    current_string = input()
    if current_string == "end":
        break
    else:
        rev = reverse_string(current_string)
        if current_string not in pair_strings:
            pair_strings[current_string] = rev
for item in pair_strings:
    print(f"{item} = {pair_strings[item]}")