def s(a):
    n = len(a)
    t= 0
    num= 2 ** n
    subset = []
    for i in range(num):
        subsets=[]
        s = 0   
        for j in range(n):
            if i & (2 ** j):
                subsets.append(a[j])
                s += a[j]
        t.append(subsets)
        t += s

    return t


a = [1, 2, 3]

print("sum of subset:",s(a))
