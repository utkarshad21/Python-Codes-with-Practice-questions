# Q2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.


sub1 = int(input("Enter marks (Out of 100) of English Subject: "))
sub2 = int(input("Enter marks (Out of 100) of Maths Subject: "))
sub3 = int(input("Enter marks (Out of 100) of Science Subject: "))


total = sub1 + sub2 + sub3
tot_per = (total / 300) * 100  
if tot_per >= 40:
    if sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
        print(f"Total Percentage is: {tot_per:.2f}%")
        print(f"Marks: English = {sub1}, Maths = {sub2}, Science = {sub3}")
        print("Student is Passed")
    else:
        print(f"Marks: English = {sub1}, Maths = {sub2}, Science = {sub3}")
        print("Student is Failed — Needs at least 33 marks in each subject to pass")
else:
    print(f"Total Percentage is: {tot_per:.2f}%")
    print("Student is Failed — Requires at least 40% total to pass")







# sub1 = int(input("Enter marks (Out of 100) of English Subject: "))
# sub2 = int(input("Enter marks (Out of 100) of Maths Subject: "))
# sub3 = int(input("Enter marks (Out of 100) of Science Subject: "))

# tot_per = ((sub1 + sub2 + sub3)/100) * 100

# sub1_per = ((sub1)/100) * 100
# sub2_per = ((sub2)/100) * 100
# sub3_per = ((sub3)/100) * 100

# if tot_per >= 40:
#     if sub1_per >= 33 and sub2_per >= 33 and sub3_per >= 33:
#         print(f"Total Percentage is: {tot_per}")
#         print(f"Subject Percentage is: English: {sub1_per}, Maths: {sub2_per}, Science: {sub3_per}")
#         print("Student is Passed")
#     else:
#         print(f"Subject Percentage is: English: {sub1_per}, Maths: {sub2_per}, Science: {sub3_per}")
#         print("Student is Failed, student should have at least 33% in each subject to pass ")
# else:
#     print(f"Total Percentage is: {tot_per}")
#     print("Student is Failed, student requires total 40% to pass")

