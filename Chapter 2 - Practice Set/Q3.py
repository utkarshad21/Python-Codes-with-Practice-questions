# Q3. Check the type of variable assigned using input () function.

# Anything in only input is a string type. (for another try int(input("")), floatinput("")), etc)

a = input("Enter something: ")

var_type = type(a)

print(var_type)