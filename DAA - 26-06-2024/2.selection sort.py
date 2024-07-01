def l(a):
    n=len(a)
    for i in range(n):
        m=i
        for j in range(i+1, n):
            if a[j] < a[m]:
                m=j
        a[i], a[m] = a[m], a[i]

a=[2,8,7,9,2,3]
l(a)
print("sorted array: ",a)
