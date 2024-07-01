a=["ada","car","racecar"]
x=[]
for i in a:
    if i==i[::-1]:
        x.append(i)
        break
for i in x:
    print(i)
