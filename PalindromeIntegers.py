def chech_if_number_is_palindrome(number):
    is_palindrome = False
    #for num in number
    rev_number = number[::-1]
    if number == rev_number:
        is_palindrome = True
    return is_palindrome


numbers_string = input().split(', ')
#numbers_int = [int(x) for x in numbers_string]
for num in numbers_string:
    print(str(chech_if_number_is_palindrome(num)))






