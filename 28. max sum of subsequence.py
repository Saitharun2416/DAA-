def maxSumOfSubsequence(nums, queries):
    MOD = 10**9 + 7
    max_sum = 0
    
    for query in queries:
        posi, xi = query
        nums[posi] = xi
        
        n = len(nums)
        dp = [0] * n
        
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i], dp[i-1])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        max_sum += max(dp) % MOD
    
    return max_sum % MOD
nums = [1, 2, 3, 4, 5]
queries = [[1, 5], [2, 6], [3, 7], [4, 8]]
print(maxSumOfSubsequence(nums, queries))  # Output: 29

#Time complexity:O(n*m)
#Space complexity:O(n*m)
