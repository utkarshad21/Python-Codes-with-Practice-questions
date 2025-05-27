# Q6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90  => A 
# 70 – 80  => B 
# 60 – 70  =>C 
# 50 – 60  => D 
# <50      => F 

marks = int(input("Enter marks of student to calculate grade: "))

if(marks>=90 and marks<=100):
    print(f"Marks: {marks}, Grade:Ex")
elif(marks>=80):
    print(f"Marks: {marks}, Grade: A")
elif(marks>=70):
    print(f"Marks: {marks}, Grade: B")
elif(marks>=60):
    print(f"Marks: {marks}, Grade: C")
elif(marks>=50):
    print(f"Marks: {marks}, Grade: D")
elif(marks>=0):
    print(f"Marks: {marks}, Grade: F")
else:
    print("Enter Valid marks between 0 to 100")
    
    

# Another code:

# marks = int(input("Enter marks of student to calculate grade: "))

# if(marks>90 and marks<=100):
#     print(f"Marks: {marks}, Grade:Ex")
# elif(marks>80 and marks<=90):
#     print(f"Marks: {marks}, Grade: A")
# elif(marks>70 and marks<=80):
#     print(f"Marks: {marks}, Grade: B")
# elif(marks>60 and marks<=70):
#     print(f"Marks: {marks}, Grade: C")
# elif(marks>50 and marks<=60):
#     print(f"Marks: {marks}, Grade: D")
# elif(marks<50):
#     print(f"Marks: {marks}, Grade: F")
# else:
#     print("Enter Valid marks between 0 to 100")