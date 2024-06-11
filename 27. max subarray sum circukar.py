def maxSubarraySumCircular(nums):
    # Kadane's algorithm to find maximum sum subarray within linear array
    def kadane(nums):
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

    n = len(nums)
    max_sum_linear = kadane(nums)
    
  
    total_sum = sum(nums)
    for i in range(n):
        nums[i] = -nums[i] 
    max_sum_wraparound = total_sum + kadane(nums)
    
    return max(max_sum_linear, max_sum_wraparound if max_sum_wraparound != 0 else max_sum_linear)
nums = [1, -2, 3, -2]
print(maxSubarraySumCircular(nums))  # Output: 3

#
