import re

numbers = input()

pattern = r'\b\+359-2-\d{3}-d{4}\b|\+359 2 \d{3} d{4}\b'

matches = re.findall(pattern, numbers)

for number in matches:
    print(number, end=" ")
    