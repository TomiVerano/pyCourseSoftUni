
string_counter = int(input())
for s in range(0, string_counter, 1):
    current_string = input()
    if '.' in current_string or ',' in current_string or '_' in current_string:
        print('{0} is not pure!'.format(current_string))
    else:
        print('{0} is pure.'.format(current_string))
