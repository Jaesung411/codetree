n, t = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(3)]

for _ in range(t):
    temp = graph[2][n-1]
    for i in range(n-1,0,-1):
        graph[2][i] = graph[2][i-1]
    graph[2][0] = graph[1][n-1]
    for i in range(n-1,0,-1):
        graph[1][i] = graph[1][i-1]
    graph[1][0] = graph[0][n-1]
    for i in range(n-1,0,-1):
        graph[0][i] = graph[0][i-1]
    graph[0][0] = temp

for i in range(3):
    print(" ".join(map(str,graph[i])))