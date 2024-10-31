N = int(input())
arr = list(map(int,input().split()))

arr.sort()
ans = float('inf')
for i in range(N):
    ans = min(ans, arr[N+i]-arr[i])

print(ans)