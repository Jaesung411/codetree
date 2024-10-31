N = int(input())
arr = list(map(int,input().split()))
ans = 0
even = 0
odd = 0
for i in range(N):
    if arr[i] % 2 == 1:
        odd += 1
    else:
        even += 1

while not ( odd == 0 and even == 0):
    if even != 0:
        even -= 1
    elif odd >= 2:
        odd -= 2
    else:
        ans -= 1
        break
    ans += 1

    if odd != 0:
        odd -= 1
    else:
        break
    ans += 1
print(ans)