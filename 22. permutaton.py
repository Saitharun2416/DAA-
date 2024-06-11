def canPermuteBreaks(s1: str, s2: str) -> bool:
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    can_break_s2 = all(c1 >= c2 for c1, c2 in zip(s1_sorted, s2_sorted))
    can_break_s1 = all(c2 >= c1 for c1, c2 in zip(s1_sorted, s2_sorted))
    return can_break_s1 or can_break_s2
s1 = "abc"
s2 = "xya"
print(canPermuteBreaks(s1, s2))  # Output: True

s1 = "abe"
s2 = "acd"
print(canPermuteBreaks(s1, s2))  # Output: False

#Time complexity:O(nlogn)
#Spacee complexity:O(n)
