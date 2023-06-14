n = int(input())
for c in range(0, n, 1):
    code_word = int(input())
    if code_word == 88:
        print('Hello')
    elif code_word > 88:
        print('Bye.')
    elif code_word < 88:
        if code_word != 86:
            print('GREAT!')
        else:
            print('How are you?')






