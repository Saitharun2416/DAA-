def m(a):
    n=len(a)
    for i in range(n):
        key = a[i]
        j = i-1
        while (j>=0 and key < a[j]):
            a[j+1] = a[j]
            j=j-1
        a[j+1] = key

a=[3,5,4,1,8]
m(a)
print(a)
