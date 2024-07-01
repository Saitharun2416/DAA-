from itertools import combinations

def get_subset_sums(arr):
    subset_sums = []
    n = len(arr)
    for r in range(n + 1):
        for comb in combinations(arr, r):
            subset_sums.append(sum(comb))
    return subset_sums

def meet_in_the_middle(arr, target):
    n = len(arr)
    left_half = arr[:n//2]
    right_half = arr[n//2:]

    left_sums = get_subset_sums(left_half)
    right_sums = get_subset_sums(right_half)

    right_sums.sort()

    closest_sum = float('inf')
    closest_diff = float('inf')

    for sum_left in left_sums:
        low, high = 0, len(right_sums) - 1
        while low <= high:
            mid = (low + high) // 2
            current_sum = sum_left + right_sums[mid]
            current_diff = abs(target - current_sum)
            if current_diff < closest_diff:
                closest_diff = current_diff
                closest_sum = current_sum
            if current_sum < target:
                low = mid + 1
            else:
                high = mid - 1

    return closest_sum

set1 = [45, 34, 4, 12, 5, 2]
target1 = 42
print(f"Closest sum to {target1} in set {set1}: {meet_in_the_middle(set1, target1)}")

