name_not_done = True
while name_not_done:
    current_name = input()
    if current_name == 'Voldemort':
        print('You must not speak of that name!')
        name_not_done = False
        break
    else:
        if current_name == 'Welcome!':
            print('Welcome to Hogwarts.')
            name_not_done = False
            exit()
        if len(current_name) < 5:
            print('{0} goes to Gryffindor.'.format(current_name))
        if len(current_name) == 5:
            print('{0} goes to Slytherin.'.format(current_name))
        if len(current_name) == 6:
            print('{0} goes to Ravenclaw.'.format(current_name))
        if len(current_name) > 6:
            print('{0} goes to Hufflepuff.'.format(current_name))

