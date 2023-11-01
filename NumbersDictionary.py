numbers_dictionary = {}
while True:
    line = input()
    if line == "Search":
        break
    number_as_string = line
    # In case the number contains chars and strings (TypeError Exception)
    # Passing non-integer type to the variable number
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("Value Error var number is define to be integer")
while True:
    line = input()
    if line == "Remove":
        break
    searched = line
    # In case the number you want to remove is not in the dictionary ..... (Key Error Exception)
    # Searching a non-existent number
    if searched not in numbers_dictionary:
        print("Key value error -> var searched")
    else:
        print(numbers_dictionary[searched])
while True:
    line = input()
    if line == "End":
        break
    searched = line
    # In case the number you want to delete is not in the dictionary ..... (Key Error Exception)
    # Removing a non-existent number
    if searched not in numbers_dictionary:
        print("Key value error -> var searched")
    else:
        del numbers_dictionary[searched]
print(numbers_dictionary)