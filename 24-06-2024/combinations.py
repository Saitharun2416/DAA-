def c(arr, r):
    if r == 0:
        return [[]]

    l = []
    for i in range(len(arr)):
        x = arr[i]
        y = c(arr[i+1:], r-1)
        for i in y:
            l.append([x] + i)
    
    return l
arr= list(input("user input: "))
r = int(input("Combinator: "))
z = c(arr,r)
print(z)
