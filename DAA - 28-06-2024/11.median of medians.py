def partition(arr, low, high, pivot_index):
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def select(arr, low, high, k):
    if low == high:
        return arr[low]
    while True:
        if low == high:
            return arr[low]
        pivot_index = median_of_medians(arr, low, high)
        pivot_index = partition(arr, low, high, pivot_index)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            high = pivot_index - 1
        else:
            low = pivot_index + 1

def median_of_medians(arr, low, high):
    n = high - low + 1
    if n <= 5:
        sorted_list = sorted(arr[low:high + 1])
        return arr.index(sorted_list[n // 2])
    medians = []
    for i in range(low, high + 1, 5):
        group = arr[i:min(i + 5, high + 1)]
        sorted_group = sorted(group)
        medians.append(sorted_group[len(sorted_group) // 2])
    return median_of_medians(medians, 0, len(medians) - 1)

def kth_smallest(arr, k):
    return select(arr, 0, len(arr) - 1, k - 1)

arr1 = [12, 3, 5, 7, 19]
k1 = 2
print(kth_smallest(arr1, k1))


