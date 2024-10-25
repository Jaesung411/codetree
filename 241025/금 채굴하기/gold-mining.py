def in_range(x,y):
    return 0<=x<n and 0<=y<n

#손해 보지 않는 채굴의 금의 개수
def solve(x,y):
    ret = 1
    #채굴의 크기 k
    for k in range(1,n):
        #범위 안에 채굴되는 위치들
        shapes =[]
        for i in range(-k,k+1):
            for j in range(-k,k+1):
                if abs(i) + abs(j) <= k:
                    if in_range(x+j,y+i):
                        shapes.append((x+j,y+i))

        #위치 안에 골드 수
        n_gold = 0
        for px,py in shapes:
            if graph[py][px] == 1:
                n_gold += 1

        # 비용 계산
        cost = m * n_gold - (k*k+(k+1)*(k+1))
        if cost < 0:
            continue
        # if n_gold == 4: 
        #     print(shapes,len(shapes))
        #     print(x,y,k,cost)
        ret = max(ret,n_gold)
    return ret
        

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
mx_gold = 0

for i in range(n):
    for j in range(n):
        mx_gold = max(mx_gold,solve(j,i))
if mx_gold == 0:
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                mx_gold = 1
print(mx_gold)