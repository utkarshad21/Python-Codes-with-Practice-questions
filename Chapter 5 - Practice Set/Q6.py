# Q6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 

# Unique Names and Favorite language
friends = {}

for i in range(1, 5):
    name = input(f"Enter the name of friend {i}: ")
    language = input(f"Enter the favorite language of friend {i}: ")
    friends.update({name:language})
    
print(friends)