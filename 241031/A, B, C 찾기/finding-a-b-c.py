arr = list(map(int,input().split()))

arr.sort()
# print(arr)
print(arr[0],arr[1],arr[-1]-arr[0]-arr[1])