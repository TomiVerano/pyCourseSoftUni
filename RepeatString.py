string_words = input().split()
result = ""

for word in string_words:
    length = int(len(word))
    result += word * length
print(result)
