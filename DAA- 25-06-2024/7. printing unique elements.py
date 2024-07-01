def l(a,b):
    m=0
    n=0
    for i in a:
        if i in b:
            m+=1
    for i in b:
        if i in a:
            n+=1
    
    return m,n
a=[2,3,2]
b=[1,2]
x=list(l(a,b))
print(x)

