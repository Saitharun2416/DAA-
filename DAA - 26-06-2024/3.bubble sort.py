def l(a):
    n=len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a
    
a=[2,6,8,7,9,4]
print("sorted array: ", l(a))
