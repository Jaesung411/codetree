def is_range(x,y,height, length):
    return 0 <= x+length-1 < m and 0 <= y+height-1 < n

def is_positive(x,y,height, length):
    for i in range(y,y+height):
        for j in range(x,x+length):
            if graph[i][j] <= 0:
                return False
    return True

def find_max_size(x,y,height,length):
    if is_range(x,y,height,length):
        if is_positive(x,y,height,length):
            return height * length
    return 0

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        for h in range(1,n+1):
            for l in range(1,m+1):
                ans = max(ans,find_max_size(j,i,h,l))
if ans == 0:
    print(-1)
else:
    print(ans)