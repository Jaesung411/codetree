def in_range(x,y):
    return 0 <= x < N and 0<= y < N

def drop(x):
    temp = [0] * N
    cpoint = 0
    for i in range(N-1,-1,-1):
        if grid[i][x] != 0:
            temp[cpoint] = grid[i][x]
            cpoint += 1

    for i in range(N):
        grid[i][x] = temp[N-i-1]

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
r, c = map(int,input().split())
r -= 1
c -= 1

scope = grid[r][c]
scope -= 1
dx = [1,0,-1,0]
dy = [0,1,0,-1]

#bomb
grid[r][c] = 0
for i in range(4):
    for j in range(1,scope+1):
        if in_range(c + j * dx[i], r + j * dy[i]):
            grid[r + j * dy[i]][c + j * dx[i]] = 0

for i in range(c - scope, c + scope + 1):
    if in_range(i,r):
        drop(i)

for i in range(N):
    print(" ".join(map(str,grid[i])))