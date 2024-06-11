def numberWays(hats):
    MOD = 10**9 + 7
    n = len(hats)
   
    hat_to_people = [[] for _ in range(41)]
    for i in range(n):
        for hat in hats[i]:
            hat_to_people[hat].append(i)
    dp = [[0] * 41 for _ in range(1 << n)]
    dp[0][0] = 1  
  
    for hat in range(1, 41):
        for mask in range(1 << n):
            dp[mask][hat] = dp[mask][hat - 1]
            for person in hat_to_people[hat]:
                if mask & (1 << person):
                    dp[mask][hat] = (dp[mask][hat] + dp[mask ^ (1 << person)][hat - 1]) % MOD
    
    return dp[(1 << n) - 1][40]

hats = [[3, 4], [4, 5], [5]]
print(numberWays(hats)) 

hats = [[3, 5, 1], [3, 5]]
print(numberWays(hats))  
hats = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
print(numberWays(hats))
