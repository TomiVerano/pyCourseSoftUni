





user_plate = {}
parking_manifest = []
num_auto = int(input())

for auto in range(num_auto):
    reg_command = input().split()
    if reg_command[0] == "unregister":
        type_command, username,  = reg_command
        if username in user_plate:
            parking_manifest.append(username + " unregistered successfully")
            del user_plate[username]
        else:
            parking_manifest.append("ERROR: user " + username + " not found")
    elif reg_command[0] == "register":
        type_command, username, l_plate = reg_command
        if username not in user_plate:
            user_plate[username] = l_plate
            parking_manifest.append(username + " registered " + l_plate + " successfully")
        else:
            if l_plate in user_plate.values():
                parking_manifest.append("ERROR: already registered with plate number " + l_plate)



print_manifest = "\n".join(parking_manifest)
print(print_manifest)
for user, plate in user_plate.items():
    print(f"{user} => {plate}")







