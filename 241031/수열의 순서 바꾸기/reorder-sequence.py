N = int(input())
arr = list(map(int,input().split()))

arr_sorted = list(sorted(arr))

ans = -1
for i in range(N):
    if arr[i] != arr_sorted[i]:
        ans = i+1
        break

if ans == -1:
    print(0)
else:
    print(ans)