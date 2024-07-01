a=[1,2,4,3,5]
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)

            
