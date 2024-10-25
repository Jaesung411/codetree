def possible_square(x,y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0<= nx < N and 0 <= ny < N):
            return False
    return True

#(x,y)에서 최댓값 출력
def solve(x,y):
    s = 0
    s_1 = 0
    s_2 = 0
    #(x,y)에서 가능한지
    if possible_square(x,y):
        for i in range(4):
            s_1 += graph[y+dy[i]][x+dx[i]]
            s_2 += graph[y+dy[i]][x+dx[i]]
        
        nx, ny = x + dx[0], y + dy[0]
        #연장 가능하다면
        while possible_square(nx,ny):
            s_1 += graph[ny-2][nx]
            s_1 += graph[ny-1][nx+1]
            nx, ny = nx + dx[0], ny + dy[0]

        nx, ny = x - 1, y - 1
        #연장 가능하다면
        while possible_square(nx,ny):
            s_2 += graph[ny-2][nx]
            s_2 += graph[ny-1][nx-1]
            nx, ny = nx - 1, ny - 1
        s = max(s_1,s_2)
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