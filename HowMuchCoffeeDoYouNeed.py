event_gone = True
coffee_count = int(0)
while event_gone:
    current_event = input()
    if current_event == 'END':
        event_gone = False
        break
    if (current_event == 'coding') or (current_event == 'cat') or (current_event == 'dog') or (current_event == 'movie'):
        coffee_count += 1
    if (current_event == 'CODING') or (current_event == 'CAT') or (current_event == 'DOG') or (current_event == 'MOVIE'):
        coffee_count += 2
if coffee_count > 5:
    print('You need extra sleep')
else:
    print('{0:.0f}'.format(coffee_count))
