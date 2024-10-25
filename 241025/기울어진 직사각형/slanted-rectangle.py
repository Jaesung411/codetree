def possible_square(x,y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0<= nx < N and 0 <= ny < N):
            return False
    return True

#(x,y)에서 최댓값 출력
def solve(x,y):
    s = 0
    #(x,y)에서 가능한지
    if possible_square(x,y):
        for i in range(4):
            s += graph[y+dy[i]][x+dx[i]]
        nx, ny = x + dx[0], y + dy[0]
        #연장 가능하다면
        while possible_square(nx,ny):
            s += graph[ny-2][nx]
            s += graph[ny-1][nx+1]
            nx, ny = nx + dx[0], ny + dy[0]
    if s == 19:
        print(x,y)
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