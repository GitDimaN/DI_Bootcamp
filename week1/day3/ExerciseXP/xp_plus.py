student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = {}
student_averages = {key: sum(value)/len(value) for key,value in student_grades.items()}
print(student_averages)

student_letter_grades = {}
for (k,v) in student_averages.items():
    if v >= 90:
        grade = 'A'
    elif v >= 80:
        grade = 'B'
    elif v >= 70:
        grade = 'C'        
    elif v >= 60:
        grade = 'D'
    else:
        grade = 'F'
    student_letter_grades[k] = grade
print(student_letter_grades)