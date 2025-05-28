# Q4. Write a program to find whether a given number is prime or not. 

num = int(input("Enter the number to check whether it is prime or not: "))

if num<= 1:
    print(f"{num} is not a prime number")
else:
    # is_prime = True
# Another logic: for i in range(2, int(num ** 0.5) + 1):

    for i in range(2, num): 
        if num % i == 0:
            print(f"{num} is not prime") 
            break
    else:
        print(f"{num} is prime")