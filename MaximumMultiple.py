divisor_number = int(input())
boundary_number = int(input())
solution_number = int(0)

for j in range(boundary_number, 0,-1):
    if j % divisor_number == 0:
        solution_number = j
        print(solution_number)
        exit()

