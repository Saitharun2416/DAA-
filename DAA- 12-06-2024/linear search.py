def l(arr, target):
    n=len(arr)
    for i in range(n):
        if arr[i] == target:
            return i+1
    return -1

arr = [3,5,6,2,9]
target = 10
result = l(arr, target)
if (result != -1):
    print(f"element {target} found in index {result}")
else:
    print(f"target not found in this index")
