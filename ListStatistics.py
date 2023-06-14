numbers_input = int(input())
positive = []
negative = []
for number in range(numbers_input):
    current_number = input()
    if int(current_number) < 0:
        negative.append(int(current_number))
    else:
        positive.append(int(current_number))
print(positive)
print(negative)
print('Count of positives: {0:.0f}'.format(len(positive)))
print('Sum of negatives: {0:.0f}'.format(sum(negative)))