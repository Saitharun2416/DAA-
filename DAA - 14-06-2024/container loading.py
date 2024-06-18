a=[10,20,30,20,10,60]
new=[]
a.sort()
c=70
s=0
for i in a:
    s+=i
    if s <= c:
        new.append(i)
print(new)
