a=[1,2]
b=[-2,-1]
c=[-1,2]
d=[0,2]
count=0
for w in a:
    for x in b:
        for y in c:
            for z in d:
                if w+x+y+z==0:
                    count+=1
print("output:",count)
