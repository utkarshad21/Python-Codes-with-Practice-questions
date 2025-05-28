# Q6. Write a program to calculate the factorial of a given number using for loop. 

num = int(input("Enter a number to calculate its factorial: "))

factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f"Factorial of {num} is 1")
else:
    for i in range(2, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")