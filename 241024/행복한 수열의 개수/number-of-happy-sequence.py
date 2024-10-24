n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def check(l):
    pn = l[0]
    cnt = 1
    if len(l) == 1 and m == 1:
        return True
    for i in range(1,n):
        if pn == l[i]:
            cnt += 1
        else:
            pn = l[i]
            cnt= 1

        if cnt == m:
            return True
    return False
ans = 0
for row in graph:
        ans+=1
for col in [[row[i] for row in graph] for i in range(n)]:
    if check(col):
        ans+=1
print(ans)