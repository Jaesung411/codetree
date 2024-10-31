N = int(input())
blocks = [int(input()) for _ in range(N)]

avg = sum(blocks)//N
n_move = 0

for i in range(N):
    # 블럭이 작다면 패스
    if blocks[i] <= N:
        continue

    possible_move = blocks[i] - avg
    # 다른 블럭에 이동
    temp = [] 
    for j in range(N):
        # 같은 블럭이라면 패스
        if i == j: 
            temp.append(blocks[i])
            continue
        # 평균보다 크거나 같다면 패스
        if blocks[j] >= avg:
            temp.append(blocks[j])
        else: # 작다면 이동
            mx_move = avg - blocks[j] # 이동해야할 최대 갯수
            if possible_move >= mx_move:
                temp.append(avg)
                possible_move -= mx_move
                n_move += mx_move
            else:
                temp.append(blocks[j]+possible_move)
                n_move += mx_move-possible_move
                possible_move = 0
    temp[i] = avg + possible_move
    blocks = temp
    # print(temp,n_move)
print(n_move)