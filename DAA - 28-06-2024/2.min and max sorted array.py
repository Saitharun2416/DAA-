def f(arr):
    if len(arr) == 0:
        return None, None
    if len(arr) == 1:
        return arr[0], arr[0]
    a= float('inf')
    b= float('-inf')
    def find(arr, low, high):
        nonlocal a, b
        if low == high:
            if arr[low] < a:
                a= arr[low]
            if arr[high] > b:
                b= arr[high]
            return
        mid = (low + high) // 2
        find(arr, low, mid)
        find(arr, mid + 1, high)
        a= min(a, arr[low])
        b = max(b, arr[high])
    find(arr, 0, len(arr) - 1)

    return a,b
arr = [1,2,3,4,5,6]
a,b= f(arr)
print(arr)
print("minimum:",a)
print("maximum:",b)
