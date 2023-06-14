out_of_money = True
collored_egg_count = int(0)
budget_value = float(input())
flour_price = float(input())
bread_count= int(0)
egg_price = flour_price * 0.75
milk_price = flour_price + (flour_price * 0.25)
my_4e_bread = (4 * flour_price) + (4 * egg_price) + (milk_price)
my_one = my_4e_bread / 4
while out_of_money:
    if budget_value < my_one:
        out_of_money = False
        break
    budget_value = budget_value - my_one
    bread_count += 1
    collored_egg_count += 3
    if bread_count % 3 == 0:
        collored_egg_count -= (bread_count - 2)
print('You made {0:.0f} loaves of Easter bread! Now you have {1:.0f} eggs and {2:.2f}BGN left.'.format(bread_count, collored_egg_count, budget_value))
