N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = [[False for _ in range(M+1)] for __ in range(N+1)]
dp[0][S] = True

for i in range(1, N+1):
    for j in range(M+1):
        if not dp[i-1][j]:
            continue
        if j - V[i-1] >= 0:
            dp[i][j-V[i-1]] = True
        if j + V[i-1] <= M:
            dp[i][j+V[i-1]] = True

res = -1
for idx, val in enumerate(dp[-1]):
    if val:
        res = idx
print(res)