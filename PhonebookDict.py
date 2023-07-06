phonebook = {}

while True:
    entry_string = input()
    if "-" not in entry_string:
        break
    name, phone_number = entry_string.split("-")
    phonebook[name] = phone_number
for search in range(int(entry_string)):
    search_name = input()
    if search_name in phonebook.keys():
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print("Contact {0} does not exist.".format(search_name))