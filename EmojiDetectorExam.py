import collections
def calc_ansii(string):
    number = int(0)
    for ch in string:
        number += ord(ch)
    return number


def check(text, symbols):
    var = ""
    emoji_string = []
    for i in range(len(symbols)):
        curr = text.split((symbols[i]*2))
        for item in curr:
            if item.isalpha() and item[0].isupper() and len(item) >= 3:
                for ch in range(1, len(item), 1):
                    var += item[ch]
                if var.islower():
                    var = ""
                    ar_var = str()
                    var = (symbols[i]*2) + str(text.find(item)) + item + symbols[i]*2
                    emoji_string.append(var)
                    var = ""
                var = ""
    return emoji_string


def cool_calc(string_text):
    cool_koef = int(1)
    for ch in range(len(string_text)):
        if string_text[ch].isdigit():
            cool_koef *= int(string_text[ch])
    return cool_koef


animals_final = {}
symbols = ":*"
text_emoji = input()
emoji_list1 = check(text_emoji, symbols)
#emoji_list1 = sorted(emoji_list12, key=len)

print(f"Cool threshold: {cool_calc(text_emoji):.0f}")
print(f"{len(emoji_list1):.0f} emojis found in the text. The cool ones are:")

#for animal in emoji_list1:
    #print(animal)

for animal in emoji_list1:
    var = ""
    var_d = ""
    for ch in range(len(animal)):
        if animal[ch] != symbols[0] or animal[ch] != symbols[1]:
            if animal[ch].isdigit():
                var_d += animal[ch]
            else:
                var += animal[ch]
    if calc_ansii(var) > cool_calc(text_emoji):
        if var not in animals_final.values():
            animals_final[int(var_d)] = var

        #print(calc_ansii(var))
        #print(animal)

#for i in range(len(text_emoji)):
    #if i in range(54, 60):
        #print(text_emoji[i])

final = dict(sorted(animals_final.items()))
for animal in final.values():
    print(f"{animal}")