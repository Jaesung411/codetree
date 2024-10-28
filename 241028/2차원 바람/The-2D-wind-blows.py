import copy

def in_range(x,y):
    return 0<=x<M and 0<=y<N

def calculate():
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    temp = copy.deepcopy(grid)
    n = 0
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            n = 1
            sum_n = grid[i][j]
            for k in range(4):
                nx, ny = j + dx[k], i + dy[k]
                if in_range(nx,ny):
                    n+=1
                    sum_n += grid[ny][nx]
            temp[i][j] = sum_n//n

    return temp

def rotate(r1,c1,r2,c2):
    temp = grid[r1][c1]
    for i in range(r1,r2):
        grid[i][c1] = grid[i+1][c1]
    for i in range(c1,c2):
        grid[r2][i] = grid[r2][i+1]
    for i in range(r2,r1,-1):
        grid[i][c2] = grid[i-1][c2]
    for i in range(c2,c1,-1):
        grid[r1][i] = grid[r1][i-1]
    grid[r1][c1+1] = temp 

def simulate(r1,c1,r2,c2):
    global grid
    # step 1 rotate
    rotate(r1,c1,r2,c2)
    # step 2 avg
    grid = calculate()


N,M,Q = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

for _ in range(Q):
    r1, c1, r2, c2 = map(int,input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    simulate(r1,c1,r2,c2)

for i in range(N):
    print(" ".join(map(str,grid[i])))