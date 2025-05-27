# Q9. Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 

# No, you cannot change the values inside a list contained in a set because lists are mutable and unhashable, so a set cannot contain a list at all—the line s = {8, 7, 12, "Harry", [1,2]} will raise a TypeError.
# There is no index in set
# List can't be included in a set
"""
1. Lists are mutable: Sets only allow immutable (unchangeable) elements because mutable objects like lists can change, which would break the internal hashing mechanism used by sets.

2. Lists are unhashable: Sets require all elements to be hashable (i.e., have a fixed hash value), but lists are unhashable due to their mutability, so Python throws a TypeError.

Correct alternative: Use a tuple instead of a list if you need to store a sequence inside a set:
s = {8, 7, 12, "Harry", (1, 2)}  # This works!
"""
    
s = {8, 7, 12, "Harry", [1,2]}
