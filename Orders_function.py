def sum_products(product_output, quantity_output):
    if product_output == 'water':
        print('{0:.2f}'.format(quantity_output * 1.00))
    if product_output == 'coffee':
        print('{0:.2f}'.format(quantity_output * 1.50))
    if product_output == 'coke':
        print('{0:.2f}'.format(quantity_output * 1.40))
    if product_output == 'snacks':
        print('{0:.2f}'.format(quantity_output * 2.00))


product = input()
quantity = int(input())
sum_products(product, quantity)


