# Q10. Write a program to print multiplication table of n using for loops in reversed order. 

num = int(input("Enter to print multiplication table of n in reversed order: "))

for i in range (10, 0, -1):
    mul = num * i
    print(f"{num} x {i} = {mul}")