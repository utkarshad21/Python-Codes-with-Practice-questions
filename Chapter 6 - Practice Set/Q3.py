# Q3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
# Write a program to detect these spams.

k1 = "make a lot of money"
k2 = "buy now"
k3 = "subscribe this"
k4 = "click this"
message = input("Enter your comment: ").lower()

if((k1 in message) or (k2 in message) or (k3 in message) or (k4 in message)):
    print("Comment is spam")
else:
    print("Comment is not spam")
    

# Another method using for loop:
# comment = input("Enter the comment: ").lower()

# spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

# is_spam = False
# for keyword in spam_keywords:
#     if keyword in comment:
#         is_spam = True
#         break

# if is_spam:
#     print("This is a spam comment.")
# else:
#     print("This is not a spam comment.")