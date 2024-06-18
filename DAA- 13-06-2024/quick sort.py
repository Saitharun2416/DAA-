def quicksort(nums):
    def partition(low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def x(low, high):
        if low < high:
            pi = partition(low, high)
            x(low, pi - 1)
            x(pi + 1, high)

    x(0, len(nums) - 1)
    return nums

nums = [3, 6, 8, 10, 1, 2, 1]
result= quicksort(nums)
print(result)  

