
def remove_Symbols(list_line, symbols):
    list_edit = ""
    for sym in symbols:
        list_line = list_line.replace(sym, "@")
    list_edit = list_line
    return list_edit


file1 = open("text.txt", "r")
symbols = "-,.!?"
line_count = 0
line_replace = []
while True:
    # Get next line from file
    line = file1.readline()
    line = remove_Symbols(line, symbols)
    # end of file is reached
    # if line is empty
    if not line:
        break
    if line_count % 2 == 0:
        text = line.strip()
        s = text.split()[::-1]
        stack = []
        for i in s:
            # appending reversed words to stack
            stack.append(i)
        # printing reverse words
        print(" ".join(stack))
    line_count += 1
file1.close()



