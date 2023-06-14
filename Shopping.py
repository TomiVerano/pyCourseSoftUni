# Write a program that reads an integer number representing a budget. On the following lines, it reads integer
# numbers representing the prices of each product you should buy until it receives the command "End".
# During the iterations, if there is not enough budget left to buy the next product, it prints "You went in
# overdraft!" and end the program.

all_bought = True
budget = float(input())
while all_bought:
    current_product = input()
    if current_product == 'End':
        all_bought = False
        print('You bought everything needed.')
        break
    else:
        current_product_price = float(current_product)
        budget -= current_product_price
        if budget < 0:
            print('You went in overdraft!')
            all_bought = False
            break
