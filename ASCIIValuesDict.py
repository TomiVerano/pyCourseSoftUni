characters = input().split(", ")

#asc = {}
asc = {x:ord(x) for x in characters}

#for ch in range(len(characters)):
    #asc[ch] = ord(ch)

print(asc)