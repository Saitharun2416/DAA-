def s(arr):
    n = len(arr)
    num = 2**n 
    l= [] 
    for i in range(num):
        x = []
        for j in range(n):
            if i & 2**j:
                x.append(arr[j])
        l.append(x)
`               
    return  l

arr =list(input("user input:"))
l = s(arr)
print("subsets are:")
print(l)
