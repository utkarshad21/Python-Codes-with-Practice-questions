# Q2. Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []
for i in range(6):
    mark = float(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)
print(f"Marks of 6 students are: {marks}")
marks.sort()
# sorted_marks = sorted(marks)
print(f"Sorted marks of 6 students are: {marks}")


# or
student_marks = []
student_marks.append(int(input("Enter 1st student marks: ")))
student_marks.append(int(input("Enter 2nd student marks: ")))
student_marks.append(int(input("Enter 3rd student marks: ")))
student_marks.append(int(input("Enter 4th student marks: ")))
student_marks.append(int(input("Enter 5th student marks: ")))
student_marks.append(int(input("Enter 6th student marks: ")))
print("The list of setudents marks is:", student_marks)
student_marks.sort()
print("The sorted list of students marks is:", student_marks)
