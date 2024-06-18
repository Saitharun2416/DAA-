def c(amount, coins):
    coins.sort(reverse=True)
    
    result = []
    for i in coins:
        while amount >= i:
            amount -= i
            result.append(i)
    
    return result

amount = 87
coins = [25, 10, 5, 1]
change = c(amount, coins)
print("coins used to get rs ",amount," are:",change)
