beggars_collected = []
collected = []
cash_input = input().split(', ')
beggars = int(input())
for element in cash_input:
    collected.append(int(element))
start_index = int(0)
while start_index < beggars:
    sum_curr = int(0)
    for curr_index in range(start_index, len(collected), beggars):
        sum_curr += collected[curr_index]
    beggars_collected.append(sum_curr)
    start_index += 1
print(beggars_collected)