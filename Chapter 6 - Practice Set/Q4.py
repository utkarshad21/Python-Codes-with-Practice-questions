# Q4. Write a program to find whether a given username contains less than 10 characters or not. 

username = input("Enter the username: ")

if len(username) < 10:
    print("Username should contain at least 10 characters.")
else:
    print("Username has 10 or more characters.")
