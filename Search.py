n = int(input())
key_string = input()
strings_list = []
for string in range(n):
    curr_string = input()
    strings_list.append(curr_string)
print(strings_list)
for i in range(len(strings_list) - 1, -1, -1):
    string_element_index = strings_list[i]
    if key_string not in string_element_index:
        strings_list.remove(string_element_index)
print(strings_list)