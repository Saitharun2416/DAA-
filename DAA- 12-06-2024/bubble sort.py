a=[2,4,3,1,5]
temp=0
n=len(a)
for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)
