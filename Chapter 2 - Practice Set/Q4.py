# Q4. Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80

a = 34
b = 80

if (a>b):
    print ("a is greater than be")
elif (a<b): 
    print ("a is smaller than be")
else:
    print (" a is equal to b")

# or check with true or false taking input from user

c = int(input("Enter first number: "))
d = int(input("Enter second number: "))
print("First number is greater than second number: ", c>d)