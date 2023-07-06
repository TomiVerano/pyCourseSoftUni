
statistics = {}

while True:
        command1 = input()
        if command1 == "statistics":
            break
        command = command1.split(": ")
        product = command[0]
        quantity = int(command[1])
        if product in statistics:
            statistics[product] += quantity
        else:
            statistics[product] = quantity

print("Products in stock:")
total_products = len(statistics)
total_quantity = sum(statistics.values())
for product, quantity in statistics.items():
    print(f"- {product}: {quantity:.0f}")
print("Total Products: {0:.0f}".format(total_products))
print("Total Quantity: {0:.0f}".format(total_quantity))