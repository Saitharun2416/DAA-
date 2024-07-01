def count_ways(num_sides, num_dice, target):
    dp = [[0] * (target + 1) for _ in range(num_dice + 1)]
    dp[0][0] = 1
    for dice in range(1, num_dice + 1):
        for t in range(1, target + 1):
            dp[dice][t] = 0
            for k in range(1, num_sides + 1):
                if t - k >= 0:
                    dp[dice][t] += dp[dice - 1][t - k]

    return dp[num_dice][target]
num_sides1, num_dice1, target1 = 6, 2, 7
num_sides2, num_dice2, target2 = 4, 3, 10

print(f"Number of ways to reach sum {target1} with {num_dice1} dice of {num_sides1} sides: {count_ways(num_sides1, num_dice1, target1)}")
