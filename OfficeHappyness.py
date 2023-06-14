def calculating_office_happiness():
    employees_list = input().split()
    happiness_factor = int(input())
    employees_list = list(map(lambda emp: int(emp) * happiness_factor, employees_list))
    filtered = list(filter(lambda emp: emp >= (sum(employees_list) / len(employees_list)), employees_list))
    if len(filtered) >= len(employees_list) / 2:
        print('Score: {0:.0f}/{1:.0f}. Employees are happy!'.format(len(filtered), len(employees_list)))
    else:
        print('Score: {0:.0f}/{1:.0f}. Employees are not happy!'.format(len(filtered), len(employees_list)))


calculating_office_happiness()