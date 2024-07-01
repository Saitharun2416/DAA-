def p(arr, k):
    c= 0
    current = 1
    
    while True:
        if current not in arr:
            c += 1
            if c == k:
                return current
        current += 1
arr1 = [2, 3, 4, 7, 11]
k1 = 5
print(p(arr1, k1))  
arr2 = [1, 2, 3, 4]
k2 = 2
print(p(arr2, k2))
