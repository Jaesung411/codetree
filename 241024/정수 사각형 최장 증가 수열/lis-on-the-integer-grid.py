N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

dp = [[1]*N for _ in range(N)]

cells = []
for i in range(N):
    for j in range(N):
        cells.append((graph[i][j],j,i))

for value,x,y in cells:
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<N and 0 <= ny < N:
            if graph[y][x] < graph[ny][nx]:
                dp[ny][nx] = max(dp[ny][nx], dp[y][x]+1)
                  
print(max(map(max,dp)))