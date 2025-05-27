# Q8. If languages of two friends are same; what will happen to the program in problem 6?

# If two friends have the same favorite language, the program will still store all entries correctly since dictionary keys (names) are unique, and values (languages) can be duplicates.

friends = {}

for i in range(1, 5):
    name = input(f"Enter the name of friend {i}: ")
    language = input(f"Enter the favorite language of friend {i}: ")
    friends.update({name:language})
    
print(friends) 