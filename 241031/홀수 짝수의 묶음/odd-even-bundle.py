N = int(input())
arr = list(map(int,input().split()))
ans = 0
i = 0
flag = 0
while i < N-1:
    # print("start",i)
    s = arr[i] + arr[i+1]
    i+=2
    if i >= N: 
        ans+=1
        break
    while flag%2 == s%2:
        s += arr[i]
        i+=1
    flag+=1 
    ans+=1
print(ans)