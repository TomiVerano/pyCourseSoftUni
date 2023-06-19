first_emp_efficiency_per_hour = int(input())
sec_emp_efficiency_per_hour = int(input())
thirth_emp_efficiency_per_hour = int(input())
students = int(input())
counter = int(0)
total_time = int(0)

party_emp = first_emp_efficiency_per_hour +\
            sec_emp_efficiency_per_hour +\
            thirth_emp_efficiency_per_hour

while students > 0:
    counter += 1
    total_time += 1
    if counter % 4 == 0:
        continue
    total_time += 1
    students -= party_emp
print('Time needed: {0}'.format(total_time))

