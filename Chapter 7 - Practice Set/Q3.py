# Q3. Attempt problem 1 using while loop. 
# Problem 1 was: Write a program to print multiplication table of a given number using for loop. 
# So problem 3 is Write a program to print multiplication table of a given number using while loop. 

num = int(input("Enter a number to print a table: "))

i = 1
while i<=10:
    mul = num * i
    print(f"{num} x {i} = {mul}")
    i += 1
