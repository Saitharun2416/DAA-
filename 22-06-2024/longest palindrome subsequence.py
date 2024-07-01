def lo(s):
    n = len(s)
    table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        table[i][i] = 1

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                table[i][j] = 2
            elif s[i] == s[j]:
                table[i][j] = table[i + 1][j - 1] + 2
            else:
                table[i][j] = max(table[i][j - 1], table[i + 1][j])

    return table


s = "levelc"
table = lo(s)

for row in table:
    print(row)
