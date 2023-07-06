class_book = {}

num_students = int(input())

for student in range(num_students):
    student_name = input()
    grade = float(input())
    #count = int(1)
    if student_name not in class_book.keys():
        class_book[student_name] = []
        class_book[student_name].append(grade)
    else:
        class_book[student_name].append(grade)
    #print(class_book[student_name])


for name, grade in class_book.items():
    #print(grade)
    calc_grade = (sum(grade)) / (len(grade))
    if not calc_grade <= 4.49:
        print(f"{name} -> {calc_grade:.2f}")
