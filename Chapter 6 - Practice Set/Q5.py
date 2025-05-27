# Q5. Write a program which finds out whether a given name is present in a list or not. 

# The strip() method is used to remove any leading and trailing whitespace characters from a string.
# example of strip():
# name = "  Alice  "
# print(name)          # Output: '  Alice  '
# print(name.strip())  # Output: 'Alice'
# lstrip() removes only leading (left) spaces.
# rstrip() removes only trailing (right) spaces.

find = input("Enter name to check whether a given name is present in a list or not: ").strip().lower()

name = ["Sid", "Tony", "Lily", "Jesi", "Dav"]
name_lower = [n.lower() for n in name]

if (find in name_lower):
    print(f"Name {find} is present in the list")
else:
    print(f"Name {find} is not present in the list")