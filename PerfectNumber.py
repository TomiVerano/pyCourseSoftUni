def calc_sum_dividors(number):
    sum_divisors = int(0)
    counter = int(1)
    found = True
    while found:
        if number % counter == 0:
            sum_divisors += counter
        counter += 1
        if sum_divisors > number:
            found = False
            print('It\'s not so perfect.')
            break
        elif sum_divisors == number:
            print('We have a perfect number!')
            found = False
            break



number = int(input())
calc_sum_dividors(number)