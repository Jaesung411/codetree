n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0 <= x < m and 0 <= y < n

def check(x,y):
    s = 0
    shapes = [
        ((x+1,y),(x+2,y)),
        ((x,y+1),(x,y+2)),
        ((x,y+1),(x+1,y+1)),
        ((x,y+1),(x-1,y+1)),
        ((x+1,y),(x+1,y+1)),
        ((x+1,y),(x+1,y-1)),
        ((x,y-1),(x-1,y-1)),
        ((x,y-1),(x+1,y-1)),
        ((x-1,y),(x-1,y-1)),
        ((x-1,y),(x-1,y+1))
    ]
    for shape in shapes:
        n_stick = graph[y][x]
        for nx, ny in shape:
            if in_range(nx,ny):
                n_stick += graph[ny][nx]
            else:
                break
        s = max(s,n_stick)
    return s

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans,check(j,i))
print(ans)