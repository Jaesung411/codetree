def get_endpoint(start,number):
    for end in range(start+1,len(numbers)):
        if number != numbers[end]:
            return end-1
    return len(numbers) - 1

N, M = map(int,input().split())
numbers = [int(input()) for _ in range(N)]

while True:
    did_explore = False
    for start, number in enumerate(numbers):
        #벌써 터진 포탄인 경우
        if number == 0:
            continue
        
        #같은 number를 가지는 마지막 지점
        end = get_endpoint(start, number)
        #M번이상 일 경우 0 
        if end - start +1 >= M:
            did_explore = True
            for i in range(start,end+1):
                numbers[i] = 0
        
    temp = []
    for i in range(len(numbers)):
        if numbers[i] != 0:
            temp.append(numbers[i])

    numbers = temp.copy() 
    # print(numbers)
    if not did_explore:
        break
print(len(numbers))
for e in numbers:
    print(e)