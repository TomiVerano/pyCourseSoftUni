count = int(input())
students = {}

for _ in range(count):
    line = tuple(input().split())
    student, grade = line
    if student not in students:
        students[student] = []
    students[student].append(float(grade))
#, {2:.0f}sum(value)/len(value)
#[print("{0} -> {1:.0f} (avg: {2:.0f})".format(key, value, sum(value)/len(value))) for key, value in students.items()]
    #print("{0} -> {1} (avg: {2:.0f})".format(key, " ".join(value), sum(value)/len(value)))
for key, value in students.items():
    print("{0} -> {1:.0f} (avg: )".format(key, value))