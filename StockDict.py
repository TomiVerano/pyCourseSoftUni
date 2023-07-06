stock_string = input().split()

stocks = {}

products_to_search = input().split()

for i in range(0, len(stock_string), 2):
    product = stock_string[i]
    quantity = stock_string[i + 1]
    stocks[product] = quantity
for product in products_to_search:
    if product in stocks:
        print(f"We have {stocks[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

