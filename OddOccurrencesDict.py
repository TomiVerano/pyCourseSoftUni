info = {}
line_string = input().split()

for word in line_string:
    lower_word = word.lower()
    if lower_word not in info.keys():
        info[lower_word] = int(1)
    else:
        info[lower_word] += int(1)

clear_info = []
for item in info.keys():
    if info[item] % 2 != 0:
        clear_info.append(item)
        #print(item)
    #if item[2] % 2 != 0:
        #clear_info.append(item)

#print(info)
#print(clear_info)
final_print = " ".join(clear_info)
print(final_print)
