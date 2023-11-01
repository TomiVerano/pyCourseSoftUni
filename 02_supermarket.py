from collections import deque

list_d = deque()

end_clients = True
while end_clients:
    current_client = input()
    if current_client == "End":
        end_clients = False
    if current_client == "Paid":
        for item in list_d:
            print(item)
        list_d.clear()
    else:
        list_d.append(current_client)
if len(list_d) > 0:
    print("{0:.0f} people remaining.".format(len(list_d) - 1))


