N,M = map(int,input().split())
people = list(map(int,input().split()))

ans = 0
i = 0
while i != N:
    if people[i]:
        i+= 2*M+1
        ans+=1
# for i in range(N):
#     if people[i] and not poss_internet[i]:
#         for j in range(i,i+2*M+1):
#             poss_internet[j] = True
        # ans+=1
print(ans)