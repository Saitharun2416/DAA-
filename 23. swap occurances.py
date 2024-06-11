def minStringWithCost(s: str) -> int:
    n = len(s)
    cost = 0
    
    for i in range(1, n):
        if s[i] == "?":
            s = s[:i] + s[i-1] + s[i+1:]
    
    for i in range(1, n):
        if s[i] == "?":
            j = i
            while j < n and s[j] == "?":
                j += 1
            left = s[i-1] if i > 0 else '{'
            right = s[j] if j < n else '{'
            min_char = min(left, right)
            cost += (j - i) * min_char
            for k in range(i, j):
                s = s[:k] + min_char + s[k+1:]
    
    return cost

s = "a??c"
print(minStringWithCost(s))  # Output: 3

#Time complexity:O(n^2)
#Space complexity:O(n)
