text = 'g#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r'
text_split1 = text.split('@')
text_split2 = text.split('#')
print(*text_split1)
print(*text_split2)
t =''.join(text_split1)
text_split3 = t.split('#')
print(text_split3)