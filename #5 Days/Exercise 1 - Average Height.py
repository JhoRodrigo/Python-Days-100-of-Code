# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
total_height  = 0
number_heigth = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
    total_height  += student_heights[n]
    number_heigth += 1
result = round(total_height/number_heigth)
print(result)

