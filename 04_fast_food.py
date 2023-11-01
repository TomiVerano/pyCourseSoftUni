from collections import deque

clients_food_list_int = []
init_food = int(input())
clients_food_list = (input().split())

for i in range(len(clients_food_list)):
    clients_food_list_int.append(int(clients_food_list[i]))

print(max(clients_food_list_int))
clients_food = deque(clients_food_list)
for i in range(len(clients_food)):
    if init_food >= int(clients_food[0]):
        init_food -= int(clients_food[0])
        clients_food.popleft()
    else:
        break
if len(clients_food) != 0 :
    unserved_clients = "Orders left: "
    unserved_clients += " ".join(clients_food)
    print(unserved_clients)
else:
    print("Orders complete")
