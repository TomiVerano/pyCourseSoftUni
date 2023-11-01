def create_file(name):
    f = ""
    try:
        f = open(name, "w")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
    return 0

def add_file(name, content):
    f = ""
    try:
        f = open(name, "a")
        f.writelines(content + "\n")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
    return 0

def rename_file(name, oldstring, newstring):
    new_string_format = ""
    f = ""
    try:
        f = open(name, "r+")
        while True:
            # Get next line from file
            line = f.readline()
            list_line = line.split()
            if oldstring in line:
                index = list_line.index(oldstring)
                list_line.pop(index)
                list_line.insert(index, newstring)
                new_string_format = " ".join(list_line)
                #print(new_string_format)
            else:
                new_string_format = " ".join(list_line)
                #print(new_string_format)
            #list_line.clear()
            # end of file is reached
            # if line is empty
            if not line:
                break
        f.close()
    except:
        print("Something went wrong when writing to the file")
    try:
        f = open(name, "w")
        f.close()
        f = open(name, "a")
        f.writelines(new_string_format)
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
    return 0

#def delete_file(name):
    #return 0


is_done = True
while is_done:
    line = input()
    if line == "End":
        is_done = False
    else:
        command = line.split("-")
        if command[0] == "Create":
            create_file(command[1])
        if command[0] == "Add":
            add_file(command[1], command[2])
        if command[0] == "Replace":
            rename_file(command[1], command[2], command[3])
#no time for more coding :( deadline!!!
#"Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist, create it, and add the content
#"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string with the new string. If the file does not exist, print: "An error occurred"
#"Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"