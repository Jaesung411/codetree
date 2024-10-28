def move(r,d):
    #오른쪽 왼쪽
    if d == -1:
        temp = grid[r][M-1]
        for i in range(M-1,0,-1):
            grid[r][i] = grid[r][i-1]
        grid[r][0] = temp
    else:
        temp = grid[r][0]
        for i in range(M-1):
            grid[r][i] = grid[r][i+1]
        grid[r][M-1] = temp

def in_range(r):
    return 0<=r<N

def check(org_r, a_r):
    for i in range(M):
        if grid[org_r][i] == grid[a_r][i]:
            return True
    return False

def up_blow(r,d):
    if r < 0: return
    move(r,d)
    if in_range(r-1) and check(r,r-1):
        up_blow(r-1,-1 * d)

def down_blow(r,d):
    if r == N: return
    move(r,d)
    if in_range(r+1) and check(r,r+1):
        down_blow(r+1,-1 * d)

def solve(r,d):
    #이동 
    move(r,d)

    #영향을 주는 위 아래 row
    if in_range(r-1) and check(r,r-1):
        up_blow(r-1,-1 * d)
    if in_range(r+1) and check(r,r+1):
        down_blow(r+1,-1 * d)

N, M, Q = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

for _ in range(Q):
    r, d = map(str,input().split())
    r = int(r)
    r-=1
    if d == 'L':
        d = -1
    else:
        d = 1
    
    solve(r,d)
for i in range(N):
    print(" ".join(map(str,grid[i])))