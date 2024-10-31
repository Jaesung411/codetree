N = int(input())
arr = list(map(int,input().split()))

mx = 0
mn = float('inf')
ans = 0
for i in range(N):
    ans += 1
    if arr[i] < mn:
        mn = arr[i]
    elif arr[i] > mx:
        mx = arr[i]
    else:
        ans -= 1
        break
print(ans)