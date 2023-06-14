grade_data = float(input())
def solve_print_grade(grade):
    if grade <= 2.00 or grade <= 2.99:
        return 'Fail'
    elif grade <= 3.00 or grade <= 3.49:
        return 'Poor'
    elif grade <= 3.50 or grade <= 4.49:
        return 'Good'
    elif grade <= 4.50 or grade <= 5.49:
        return 'Very Good'
    elif grade <= 5.50 or grade <= 6.00:
        return 'Excellent'
print(solve_print_grade(grade_data))
