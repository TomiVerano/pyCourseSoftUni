
def shell_filling(charge, n):
    counter_left = int(0)
    comp_shell = []
    m = 2 * (n ** 2)
    for shell in range(0, m, 1):
        counter_left += 1
    if charge >= counter_left:
        charge -= counter_left
        comp_shell.append(counter_left)
    else:
        comp_shell.append(charge)
        charge = int(0)
        print(comp_shell)
    return charge


charge = int(input())
n = int(1)
is_charged = True
while is_charged:
    charge = shell_filling(charge, n)
    if charge == 0:
        is_charged = False
        break
    n += 1
