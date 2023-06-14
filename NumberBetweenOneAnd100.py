# Write a program that reads different floating-point numbers from the console. When it receives a number between
# 1 and 100 inclusive, the program should stop reading and should print "The number {number} is between 1
# and 100".
#number_is = True
#while (number_is):
#    current_number = float(input())
#    if current_number < 1 or current_number > 100:
#        continue
#    else:
#        print('The number {0:.1f} is between 1 and 100'.format(current_number))
#        number_is = False
#        break
current_number = float(0)
while current_number < 1 or current_number > 100:
    current_number = float(input())
#print('The number {0:.1f} is between 1 and 100'.format(current_number))

print(f'The number {current_number} is between 1 and 100')