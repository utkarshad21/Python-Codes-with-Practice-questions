# Q1. Write a program to store seven fruits in a list entered by the user.


fruit_list = [None]*7
fruit_list[0] = input("Enter 1st fruit: ")
fruit_list[1] = input("Enter 2nd fruit: ")
fruit_list[2] = input("Enter 3rd fruit: ")
fruit_list[3] = input("Enter 4th fruit: ")
fruit_list[4] = input("Enter 5th fruit: ")
fruit_list[5] = input("Enter 6th fruit: ")
fruit_list[6] = input("Enter 7th fruit: ")
print(f"The list of fruits is: {fruit_list}")

# or
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)
print("The list of fruits is:", fruits)

# or
# fruit_list = []
# fruit_list.append(input("Enter 1st fruit: "))
# fruit_list.append(input("Enter 2nd fruit: "))
# fruit_list.append(input("Enter 3rd fruit: "))
# fruit_list.append(input("Enter 4th fruit: "))
# fruit_list.append(input("Enter 5th fruit: "))
# fruit_list.append(input("Enter 6th fruit: "))
# fruit_list.append(input("Enter 7th fruit: "))
# print("The list of fruits is:", fruit_list)

