
#incoming = input()


students_rapper = {}
print_info = []

while True:
    incoming = input()

    if ':' not in incoming:
        break

    command = incoming.split(":")
    student, id, course = command
    #print_info.append(student + " - " + id)
    if course not in students_rapper:
        students_rapper[course] = [student + " - " + id]
    else:
        students_rapper[course].append(student + " - " + id)

#subst = []
#if incoming.index("_"):
    #remove = incoming.index("_")
    #for ch in range(len(incoming)):
        #if incoming[ch] != "_":
            #subst.append(incoming[ch])
        #else:
            #subst.append(" ")
    #print(subst)
    #incoming = "".join(subst)
#print(remove)
    #print(incoming)
if "_" in incoming:
    mod_error = incoming.replace("_", " ")
    incoming = ''
    incoming = mod_error

info = "\n".join(students_rapper[incoming])
print(info)
#print(students_rapper.items())
    #print(incoming)
#for key_item in students_rapper.keys():
    #if key_item == incoming:
        #print(students_rapper[key_item])






