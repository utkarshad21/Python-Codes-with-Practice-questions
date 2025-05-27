
# Time complexcity of dictionary is O(1)
# Time complexcity of list is O[n]

# Dictionary
marks = {
   # Key: Value,
    "Sid": 100,
    "Tina": 67,
    "Roy": 57,
    69: "Sunny"
}

print(marks, type(marks))
print(marks["Tina"])
print(marks[69])
print(marks.get("Shiv"))
print(marks.get("Sid"))

# Interview asked question: Difference between marks[key] and marks.get(key) is 
# marks[key] = Output will be "Error" if key does not exist in the dictionary
# marks.get(key) = Output will be "None" if key does not exist in the dictionary

# example: 
# print(marks["Sid2"]) # This will return an error 
print(marks.get("Sid2")) # This will give output as : None

print(marks.items()) # This gives list of key:value pairs and key:value pairs in form of tupples 
print(marks.keys())
print(marks.values())
marks.update({"Roy":59, "Ren":73})
print(marks)
print(len(marks))

# Set 
e = {1, 4, 32, 54, 4, 4, 4}
print(e) # output: {32, 1, 4, 54} elements in sets can't be repeated
# Output is unordered but if you want in order then use list

# Interview asked question: Create an empty set and dictionary
# Empty Dictionary
d = {}
print(type(d))
# Don't use s = {} as it will create an empty dictionary
# Empty Dictionary
s = set()
print(type(s))

s1 = {1, 4, 32, 5, 5, 4, "Hii"}
s1.add(43)
print(s1, type(s1))

s1.remove(1)
print(s1, type(s1))

# Union and Intersection
s2 = {1, 4, 32, 67, 5, 5, 4}
s3 = {1, 4, 35, 85, 5, 6}
s4 = {1, 4, 43}
print(s2.union(s3))
print(s2.intersection(s3))
print(s4-s3)
print(s3-s4)
print({1,5}.issubset(s2))
print(s3.issuperset({1, 5}))