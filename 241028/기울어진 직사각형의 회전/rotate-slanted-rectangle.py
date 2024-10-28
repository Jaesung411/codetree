def in_range(x,y):
    return 0<= x < N and 0 <= y < N

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
# r행, c열에서 시작하여 1번, 2번, 3번, 4번 방향으로 
# 각각 m1, m2, m3, m4만큼 순서대로 이동했을 때 그려지는 직사각형
# dir이 0인 경우에는 반시계 방향으로 1칸씩 회전해야 함을, dir이 1인 경우에는 시계 방향으로 1칸씩 회전해야 함을 의미
r, c, m1, m2, m3, m4, d = map(int,input().split())
r-=1
c-=1

temp = grid[r][c]
cx = c 
cy = r
#반시계
if d == 0:
    dx = [-1,1,1,-1]
    dy = [-1,-1,1,1]

    for i, m in enumerate([m4,m3,m2,m1]):
        for j in range(m):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if in_range(nx,ny):
                grid[cy][cx] = grid[ny][nx]
                cx, cy = nx, ny
    grid[r-1][c+1] = temp
else:
    dx = [1,-1,-1,1]
    dy = [-1,-1,1,1]

    for i, m in enumerate([m1,m2,m3,m4]):
        for j in range(m):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if in_range(nx,ny):
                grid[cy][cx] = grid[ny][nx]
                cx, cy = nx, ny
    grid[r-1][c-1] = temp


for i in range(N):
    print(" ".join(map(str,grid[i])))