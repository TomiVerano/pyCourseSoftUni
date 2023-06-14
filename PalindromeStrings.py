def search_count_palindrome():
    text = input().split()
    palindrome = []

    for word in text:
        if word == ''.join(reversed(word)):
            palindrome.append(word)

    palindrome_key_word = input()
    print(palindrome)
    print('Found palindrome {0:.0f} times'.format(palindrome.count(palindrome_key_word)))


search_count_palindrome()


