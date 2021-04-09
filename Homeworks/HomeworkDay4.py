import numpy as np

data = {}

print("Welcome to the grade calculator!")

students = []
for num in range(5):
  x = input("Enter name of students:\n")
  students.append(x)

midterm_grade = []

for num in range(5):
  a = float(input("Enter a midterm grade:\n"))
  midterm_grade.append(a)

project_grade = []

for num in range(5):
  b = float(input("Enter a project grade:\n"))
  project_grade.append(b)

final_grade = []

for num in range(5):
  c = float(input("Enter a final grade:\n"))
  final_grade.append(c)

grades = [midterm_grade, project_grade, final_grade]

for i in range(5):
  passingGrade = np.asarray(midterm_grade)*0.3 + np.asarray(project_grade)*0.3 + np.asarray(final_grade)* 0.4
print(f"Average grade is: {passingGrade}")

List = [students[0],passingGrade[0],students[1], passingGrade[1], students[2], passingGrade[2], students[3], passingGrade[3], students[4], passingGrade[4]]

print(List)

while i in range(5):
  print(students[0], ":" ,passingGrade[0])
  break
while i in range(5):
  print(students[1], ":" ,passingGrade[1])
  break
while i in range(5):
  print(students[2], ":" ,passingGrade[2])
  break
while i in range(5):
  print(students[3], ":" ,passingGrade[3])
  break
while i in range(5):
  print(students[4], ":" ,passingGrade[4])
  break


students_grades = print(students,":",grades)

min_grade, max_grade = passingGrade[1],passingGrade[0]
for i in range(1,len(passingGrade)):
  if passingGrade[i]<min_grade:
    min_grade = passingGrade[i]
  if passingGrade[i]>max_grade:
    max_grade = passingGrade[i]

passingGrade[0] = max_grade
passingGrade[4] = min_grade

print(passingGrade)



