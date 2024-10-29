N = int(input())
arr = [int(input()) for _ in range(N)]

for _ in range(2):
    start, end = map(int,input().split())
    start-=1
    end-= 1
    for i in range(start,end+1):
        arr[i] = 0

    temp = []
    for i in range(len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])
    arr = temp
print(len(arr))
for a in arr:
    print(a)