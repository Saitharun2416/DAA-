def m(a,k):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a[k-1]
a=[1,2,4,3,5]
k=3
print(k," th smallest element is ",m(a,k))
