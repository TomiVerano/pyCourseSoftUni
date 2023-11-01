numbers_dictionary = {}
line = input()
while line != "Search":
    number_as_string = line
    number = input()
# In case the number contains chars and strings ( Reference Exception)
# Passing non-integer type to the variable number
    try:
        number1 = int(number)
        #break
    except ValueError:
        print("Value Error")
        numbers_dictionary[number_as_string] = number
    line = input()
    while line != "Remove":
        searched = line
#In case the number you want to remove is not in the dictionary ..... (Key Error Exception)
#Searching a non-existent number
        try:
            numbers_dictionary.get(searched)
            break
        except KeyError:
            print("Key Error Exception -> {0} is not in the dictionary".format(numbers_dictionary[searched]))
        line = input()
        while line != "End":
            searched = line
# In case the number you want to delete is not in the dictionary ..... (Key Error Exception)
# Removing a non-existent number
            try:
                del numbers_dictionary[searched]
            except KeyError:
                print("Key Error Exception -> {0} is not in the dictionary".format(numbers_dictionary[searched]))
                break
            print(numbers_dictionary)
