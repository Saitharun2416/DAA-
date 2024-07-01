def findWays(m, n, N, i, j):
    dp = [[[0] * n for _ in range(m)] for _ in range(N+1)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for step in range(1, N + 1):
        for x in range(m):
            for y in range(n):
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        dp[step][x][y] += 1
                    else:
                        dp[step][x][y] += dp[step - 1][nx][ny]
    
    return dp[N][i][j]
print(findWays(2, 2, 2, 0, 0))
print(findWays(1, 3, 3, 0, 1))
