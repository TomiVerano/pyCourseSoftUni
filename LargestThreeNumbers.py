# Write a program that receives three whole numbers and prints the largest one.

first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number > second_number and first_number > third_number:
    print('{0:.0f}'.format(first_number))
elif second_number > first_number and second_number > third_number:
    print('{0:.0f}'.format(second_number))
else:
    print('{0:.0f}'.format(third_number))