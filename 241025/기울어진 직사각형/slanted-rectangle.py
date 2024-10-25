def possible_square(x,y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0<= nx < N and 0 <= ny < N):
            return False
    return True

#(x,y)에서 최댓값 출력
def solve(x,y):
    s = 0
    ss = [0,0]
    #(x,y)에서 가능한지
    if possible_square(x,y):
        for i in range(4):
            ss[0] += graph[y+dy[i]][x+dx[i]]
            ss[1] += graph[y+dy[i]][x+dx[i]]
        
        for sn, dxn, dyn in [(0,1,-1),(1,-1,-1)]:
            nx, ny = x + dxn, y + dyn
            #연장 가능하다면
            while possible_square(nx,ny):
                ss[sn] += graph[ny-2][nx]
                ss[sn] += graph[ny+dxn][nx+dyn]
                nx, ny = nx + dxn, ny + dyn
                
        s = max(ss)

    return s

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
ans = 0
dx = [1,0,-1,0]
dy = [-1,-2,-1,0]

for col in range(N):
    for row in range(N):
        ans = max(ans,solve(row,col))
print(ans)