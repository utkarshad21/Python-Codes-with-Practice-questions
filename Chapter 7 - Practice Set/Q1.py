# Q1. Write a program to print multiplication table of a given number using for loop. 

num = int(input("Enter a number to print a table: "))

for i in range(1, 11):
    mul = num * i
    print(f"{num} x {i} = {mul}")
