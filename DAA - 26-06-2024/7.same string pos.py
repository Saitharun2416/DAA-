s="leetcode"
l="leet"
p=0
for i in range(len(s)):
    flag=0
    for j in range(i+1,len(l)):
        if s[i]==l[j]:
            flag=1
        else:
            flag=0
        if flag==1:
            p=i
if flag==0:
    print("-1")
else:
    print(p)
