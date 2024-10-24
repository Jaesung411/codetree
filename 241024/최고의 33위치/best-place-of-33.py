N=int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
ans = 0
def in_range(x,y):
    return 0<=x+2<N and 0<=y+2<N

def count(x,y):
    ret = 0
    for i in range(y,y+3):
        for j in range(x,x+3):
            if graph[j][i] == 1:
                ret += 1
    return ret

for i in range(N-2):
    for j in range(N-2):
        if in_range(j,i):
            ans = max(ans,count(j,i))
print(ans)