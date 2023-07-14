
def add_stop(index1, country1, tour):
    new_stop = {}
    for stop in tour:
        if index1 not in tour:
            new_stop[country1] = index1
    tour.append(new_stop)
    return tour


def remove_stop(start_index, stop_index, tour):
    while start_index != stop_index:
        for stop in tour:
            for key, value in stop.items():
                if value == start_index:
                    tour.remove({key: value})
        start_index += 1
    return tour


def switch_stop(old_country, new_country, tour):
    new_stop = {}
    for stop in tour:
        if old_country in stop:
            new_stop[new_country] = stop[old_country]
            tour.remove({old_country: stop[old_country]})
    tour.append(new_stop)
    return tour


list_tour_start = {}
list_tour_end = {}
start_tour = []
tour_list = input().split("::")
list_tour_start[tour_list[0]] = int(0)
list_tour_end[tour_list[1]] = int(-1)
start_tour.append(list_tour_start)
start_tour.append(list_tour_end)
command = input()
while command != "Travel":
    list_command = command.split(":")
    if list_command[0] == "Add Stop":
        start_tour = add_stop(int(list_command[1]), list_command[2], start_tour)
    if list_command[0] == "Remove Stop":
        start_tour = remove_stop(int(list_command[1]), int(list_command[2]), start_tour)
    if list_command[0] == "Switch":
        start_tour = switch_stop(list_command[1], list_command[2], start_tour)
    command = input()

# can't sort a list of dict ,so I need to fool the system "somehow"
final_print = []
final_print.append("Ready for world tour! Planned stops: ")
for i in range(-1,10000):
    for stop in start_tour:
        for key, value in stop:
            if value == i:
                if not i == -1:
                    final_print.append(stop[key])
                else:
                    final_print.append(stop[key])
#print("Ready for world tour! Planned stops: {string}")
print(*start_tour)