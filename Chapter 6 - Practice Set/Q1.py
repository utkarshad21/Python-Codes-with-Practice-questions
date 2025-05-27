# Q1. Write a program to find the greatest of four numbers entered by the user. 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
    greatest = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    greatest = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    greatest = num3
else:
    greatest = num4

print("The greatest number is:", greatest)














# n = []
# for i in range (1, 5):
#     num = input(f"Enter number {i}: ")
#     n.insert(num)
    
# num1 = input(f"Enter number 1: ")
# num2 = input(f"Enter number 2: ")
# num3 = input(f"Enter number 3: ")
# num4 = input(f"Enter number 4: ")

# if(num1>=num2 and num1>=num3 and num1>=num4):
#     print(f"num1 {num1} is greatest number")
# elif(num2>=num1 and num2>=num3 and num2>=num4):
#     print(f"num2 {num2} is greatest number")
# elif(num3>=num1 and num3>=num2 and num3>=num4):
#     print(f"num3 {num3} is greatest number")
# else:
#     print(f"num4 {num4} is greatest number")