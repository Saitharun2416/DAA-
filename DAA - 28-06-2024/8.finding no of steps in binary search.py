def b(arr, key):
    left, right = 0, len(arr) - 1
    steps = []
    
    while left <= right:
        mid = (left + right) // 2
        steps.append(f"left: {left}, mid: {mid}, right: {right}, arr[mid]: {arr[mid]}")
        
        if arr[mid] == key:
            return mid + 1, steps
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, steps
arr1 = [3, 9, 14, 19, 25, 31, 42, 47, 53]
key1 = 31
position, steps1 = b(arr1, key1)
print(f"Position of {key1} in array: {position}")
print("Steps taken:")
for step in steps1:
    print(step)
