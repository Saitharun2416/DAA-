def p(a):
    if len(a)==1:
        return [a]
    l=[]
    for i in range(len(a)):
        x=a[i]
        y=a[:i]+a[i+1:]
        for j in p(y):
            l.append([x]+j)
    return l
a=list(input("user input:"))
r=p(a)
print(r)
