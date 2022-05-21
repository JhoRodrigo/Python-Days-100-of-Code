student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
for i in student_scores:
    if student_scores[i] < 70:
        student_grades[i] = "Fail"
    elif student_scores[i] < 80:
        student_grades[i] = "Acceptable"
    elif student_scores[i] < 90:
        student_grades[i] = "Exceeds Expectations"
    else:
        student_grades[i] = "Outstanding"     

'''
-->Fonte execultado de exemplo
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = 'Outstanding'
    elif score > 80:
        student_grades[student] = 'Exceeds Expectations'
    elif score > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
''' 

# 🚨 Don't change the code below 👇
print(student_grades)