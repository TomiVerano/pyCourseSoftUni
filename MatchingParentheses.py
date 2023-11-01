from collections import deque
x = ""
stack = []
#math_eq = deque()
list_print = []
index = int(0)
expresion = input()

for i in range(len(expresion)):
    if expresion[i] == ')':
        start_index = stack.pop()
        x = expresion[start_index : i + 1]
        list_print.append(x)
        #list_print.append("\n")
    if expresion[i] == '(':
        stack.append(i)
for item in list_print:
    print(item)

