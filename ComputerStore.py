message = 'Congratulations you\'ve just bought a new computer!'
final_sum = float(0)
tax = float(0)
list_prices = []
is_not_fin = True
while is_not_fin:
    current_price = input()
    if current_price == 'special' or current_price == 'regular':
        is_not_fin = False
        break
    else:
        if float(current_price) > 0:
            final_sum += float(current_price)
        else:
            final_sum = '0'
            print('Invalid price!')
print(message)
if current_price == 'special':
    print('Price without taxes: {0:.2f}$'.format(final_sum))
    tax = final_sum * 1/5
    final_sum += tax
    print('Taxes: {0:.2f}$'.format(tax))
    print('-----------')
    final_sum -= final_sum * 10/100
    print('Total price: {0:.2f}$'.format(final_sum))
else:
    print('Price without taxes: {0:.2f}$'.format(final_sum))
    tax = final_sum * 1 / 5
    final_sum += tax
    print('Taxes: {0:.2f}$'.format(tax))
    print('-----------')
    print('Total price: {0:.2f}$'.format(final_sum))

