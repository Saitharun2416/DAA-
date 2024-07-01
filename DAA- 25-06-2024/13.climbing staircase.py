def merge_sort(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)
                 
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

arr = [12, 11, 13, 5, 6, 7]
print("Given array is", arr)
sorted_arr = merge_sort(arr)
print("Sorted array is", sorted_arr)
