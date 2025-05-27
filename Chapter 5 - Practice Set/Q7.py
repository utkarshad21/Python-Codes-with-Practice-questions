# Q7. If the names of 2 friends are same; what will happen to the program in problem 6?

# It will return updated key-value pair
# If two friends have the same name, the later entry will overwrite the earlier one in the dictionary, keeping only the last key-value pair for that name.

friends = {}

for i in range(1, 5):
    name = input(f"Enter the name of friend {i}: ")
    language = input(f"Enter the favorite language of friend {i}: ")
    friends.update({name:language})
    
print(friends)