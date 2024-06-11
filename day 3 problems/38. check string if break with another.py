def checkIfCanBreak(s1, s2):
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    can_s1_break_s2 = all(c1 >= c2 for c1, c2 in zip(sorted_s1, sorted_s2))
    
    can_s2_break_s1 = all(c2 >= c1 for c2, c1 in zip(sorted_s2, sorted_s1))
    return can_s1_break_s2 or can_s2_break_s1

s1 = "abc"
s2 = "xya"
print(checkIfCanBreak(s1, s2))

s1 = "abe"
s2 = "acd"
print(checkIfCanBreak(s1, s2)) 
s1 = "leetcodee"
s2 = "interview"
print(checkIfCanBreak(s1, s2))  
