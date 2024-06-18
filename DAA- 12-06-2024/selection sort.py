def se(arr):
    n=len(arr)
    for i in range(n):
        m = i
        for j in range(i+1,n):
            if arr[j] < arr[m]:
                m = j
        arr[i],arr[m] = arr[m], arr[i]

arr=[5,8,2,4,3,1]
se(arr)
print("after sorting", arr)
