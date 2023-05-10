# Write a program that receives a number n on the first line. On the following n lines, it receives different integer
# numbers. If the program receives an odd number, print "{num} is odd!" and end the program. Otherwise, if all
# numbers given are even, print "All numbers are even.".
numbers_len = int(input())
bool_all = True
for n in range(numbers_len):
    current_number = int(input())
    if current_number % 2 != 0:
        print('{0:.0f} is odd!'.format(current_number))
        bool_all = False
        break
if bool_all:
    print('All numbers are even.')
