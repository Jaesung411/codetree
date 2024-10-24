N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
mx_dp = [[e for e in row] for row in graph]
mn_dp = [[e for e in row] for row in graph]
dx = [-1,0]
dy = [0,-1]

for i in range(N):
    for j in range(N):
        candidate = []
        for dxz, dyz in zip(dx,dy):
            px = j + dxz
            py = i + dyz
            if 0<=px<N and 0<=py<N:
                candidate.append(mx_dp[py][px])
        if len(candidate) != 0:
            mn_path = min(candidate)
        else:
            mn_path = 0
        mx_dp[i][j] = max(mn_path,mx_dp[i][j])

mx_value = mx_dp[N-1][N-1]
mn_value =float('inf')
for i in range(N):
    for j in range(N):
        if mx_dp[i][j] <= mx_value:
            mn_value = min(mn_value, graph[i][j])
print(mx_value-mn_value)