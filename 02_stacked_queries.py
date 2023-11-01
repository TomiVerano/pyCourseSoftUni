from collections import deque
the_list_query = []
the_query = deque()
print_numbers = ""
command_length = int(input())
for i in range(command_length):
    command = input().split()
    if command[0] == "1":
        the_query.append(int(command[1]))
        the_list_query.append(int(command[1]))
    if command[0] == "2":
        if len(the_query) > 0:
            the_query.pop()
            the_list_query.pop(-1)
    if command[0] == "3":
        print("{0:.0f}".format(max(the_list_query)))
    if command[0] == "4":
        print("{0:.0f}".format(min(the_list_query)))
the_query.reverse()
for number in the_query:
    print_numbers = print_numbers + str(number) + ", "
print(print_numbers[:-2])
