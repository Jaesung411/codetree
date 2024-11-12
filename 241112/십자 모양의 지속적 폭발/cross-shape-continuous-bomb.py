import copy

def drop(x,temp):
    temp_col = [0 for row in range(N)]
    cpoint = 0
    for i in range(N-1,-1,-1):
        if temp[i][x] != 0:
            temp_col[cpoint] = temp[i][x]
            cpoint += 1

    for i in range(N):
        temp[i][x] = temp_col[N-1-i]

def bomb(x,y):
    temp = [[0]*N for _ in range(N)]
    temp = copy.deepcopy(grid)

    bound = grid[y][x] 
    temp[y][x] = 0
    for i in range(4):
        for j in range(bound):
            nx = x + j * dx[i]
            ny = y + j * dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                temp[ny][nx] = 0

    for i in range(N):
        drop(i,temp)

    return temp

N, M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(M):
    c = int(input())
    c-= 1
    for i in range(N):
        if grid[i][c] != 0:
            grid = bomb(c,i)

for i in range(N):
    print(" ".join(map(str,grid[i])))