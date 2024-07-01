def s(arr):
    n = len(arr)
    t= 0
    num = 2**n 
    l= [] 
    for i in range(num):
        x = []
        for j in range(n):
            if i & 2**j:
                x.append(arr[j])
        l.append(x)

    return  l                                                                        

arr =list(input("user input:"))
l = s(arr)
x=[]
for i in l:
    n=0
    if len(i)>1 and i[0]==i[1]:
        continue
    else:
        j=set(i)
        n=len(j)
        x.append(n**2)
print(sum(x))
