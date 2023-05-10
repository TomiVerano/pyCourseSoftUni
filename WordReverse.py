# Write a program that receives a single word, reverses it, and prints it.
word_is = input()
reverse_is = ""
for c in range(len(word_is) -1, -1, -1):
    reverse_is += word_is[c]
print('{0}'.format(reverse_is))
