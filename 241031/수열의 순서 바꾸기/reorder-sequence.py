N = int(input())
arr = list(map(int,input().split()))
ans = -1
for i in range(N-1,0,-1):
    if arr[i] < arr[i-1]:
        ans = i - 1

if ans == -1:
    print(0)
else:
    print(ans)