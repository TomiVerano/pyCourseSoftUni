bool_ignore = True
total_sum = float(0)
number_orders = int(input())
for c in range(0, number_orders, 1):
    bool_ignore = True
    price_capsule = float(input())
    if price_capsule < 0.01 or price_capsule > 100:
        bool_ignore = False
    days = int(input())
    if days < 1 or price_capsule > 31:
        bool_ignore = False
    capsule_modules = int(input())
    if capsule_modules < 1 or capsule_modules > 2000:
        bool_ignore = False
    if bool_ignore:
        print('The price for the coffee is: ${0:.2f}'
              .format(price_capsule * days * capsule_modules))
        total_sum = total_sum + (price_capsule * days * capsule_modules)
print('Total: ${0:.2f}'.format(total_sum))