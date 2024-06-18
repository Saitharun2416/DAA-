def add(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def sub(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def mul(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]

    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]

    M1 = mul(add(A11, A22), add(B11, B22))
    M2 = mul(add(A21, A22), B11)
    M3 = mul(A11, sub(B12, B22))
    M4 = mul(A22, sub(B21, B11))
    M5 = mul(add(A11, A12), B22)
    M6 = mul(sub(A21, A11), add(B11, B12))
    M7 = mul(sub(A12, A22), add(B21, B22))

    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)

    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]

    return C

A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 1, 2],
    [3, 4, 5, 6]
]
B = [
    [1, 2, 3, 4],
    [7, 5, 3, 6],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
]

print("Matrix 1:")
for i in A:
    print(i)

print("\nMatrix 2:")
for i in B:
    print(i)

C = mul(A, B)

print("\nResult:")
for i in C:
    print(i)
