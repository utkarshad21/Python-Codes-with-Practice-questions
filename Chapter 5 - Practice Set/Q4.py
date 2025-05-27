# Q4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations?


s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') 

print(s)
print(len(s))

# print(1 == 1.0) This will return true
# Because those are numerically equal
# print(1 == 1.1) This will return False
# Because those are numerically unequal