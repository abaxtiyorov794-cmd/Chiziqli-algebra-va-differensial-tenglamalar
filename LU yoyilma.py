def lu_yoyilmasi(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        L[i][i] = 1.0

    for i in range(n):
        for k in range(i, n):
            s = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - s

        for k in range(i + 1, n):
            s = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (A[k][i] - s) / U[i][i]

    return L, U

# Sinov uchun matritsa
A = [
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, 14]
]

L, U = lu_yoyilmasi(A)
print("=== L MATRITSA ===")
for row in L:
    print([round(x, 2) for x in row])

print("\n=== U MATRITSA ===")
for row in U:
    print([round(x, 2) for x in row])