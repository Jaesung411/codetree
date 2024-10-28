N = int(input())
arr = [int(input()) for _ in range(N)]

for _ in range(2):
    start, end = map(int,input().split())
    start-=1
    end-= 1
    for i in range(start,end+1):
        arr[i] = 0

    index = 0
    for i in range(N):
        if arr[i] != 0:
            arr[index] = arr[i]
            index += 1
        else:
            index = i
        
print(arr)