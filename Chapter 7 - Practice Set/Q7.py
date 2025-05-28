# Q7. Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3

n = 3
for i in range(1, n+1):
    spaces = n-i
    stars = 2*i-1
    print(" "*spaces+"*"*stars)