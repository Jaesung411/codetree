n, t = map(int,input().split())
container = [list(map(int,input().split())) for _ in range(2)]

for _ in range(t):
    temp_0 = container[0][n-1]
    for i in range(n-1,0,-1):
        container[0][i] = container[0][i-1]
    temp_1 = container[1][n-1]
    for i in range(n-1,0,-1):
        container[1][i] = container[1][i-1]
    container[1][0] = temp_0
    container[0][0] = temp_1
    
for i in range(2):
    print(" ".join(map(str,container[i])))