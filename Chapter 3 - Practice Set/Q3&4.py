# Q3. Write a program to detect double space in a string.
# Q4. Replace the double space from problem 3 with single spaces.

str = "Hii this  string  have  double  spaces in it"
double_space = str.count("  ")
# double_space = str.find("  ")

if double_space != 0:
    print(f"Double space detected at index: {double_space}")
else:
    print("No double space detected.")

# Strings are immutable which means you cannot change them by running functions on them

replaced_space = str.replace("  ", " ")
print(f"After replacement: {replaced_space}")