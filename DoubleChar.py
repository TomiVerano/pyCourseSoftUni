false_is = True
converted_string = ''
while(false_is):
    current_string = input()
    if current_string == 'End':
        false_is = False
        break
    if current_string == 'SoftUni':
        continue
    else:
        for c in range(len(current_string)):
            for d in range(0, 2, 1):
                converted_string += current_string[c]
        print(converted_string)
        converted_string = ''
        current_string = ''