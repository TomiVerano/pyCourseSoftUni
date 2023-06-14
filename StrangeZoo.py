tail = input()
body = input()
head = input()

zoo = [tail, body, head]
zoo[0], zoo[2] = zoo[2], zoo[0]
print(zoo)