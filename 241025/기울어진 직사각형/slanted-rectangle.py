def solve(x,y,up,down):
    dx = [1,-1,-1,1]
    dy = [-1,-1,1,1]
    nums_dir = [up,down,up,down]
    s = 0
    nx = x
    ny = y
    for i, n in enumerate(nums_dir):
        for j in range(n):
            nx += dx[i]
            ny += dy[i]
            if 0<=nx<N and 0<=ny<N:
                s+=graph[ny][nx]
            else:
                return 0
   
    return s

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
ans = 0

for col in range(N):
    for row in range(N):
        for up in range(1,N):
            for down in range(1,N):
                ans = max(ans,solve(row,col,up,down))
print(ans)