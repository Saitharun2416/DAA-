from itertools import combinations

def get_subset_sums(arr):
    subset_sums = set()
    n = len(arr)
    for r in range(n + 1):
        for comb in combinations(arr, r):
            subset_sums.add(sum(comb))
    return subset_sums

def meet_in_the_middle(arr, target):
    n = len(arr)
    left_half = arr[:n//2]
    right_half = arr[n//2:]

    left_sums = get_subset_sums(left_half)
    right_sums = get_subset_sums(right_half)

    for sum_left in left_sums:
        if target - sum_left in right_sums:
            return True

    return False

set1 = [1, 3, 9, 2, 7, 12]
target1 = 15
print(f"Subset with exact sum {target1} in set {set1}: {meet_in_the_middle(set1, target1)}")

