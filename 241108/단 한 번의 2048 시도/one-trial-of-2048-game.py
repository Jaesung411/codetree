def move_left(row):
    temp = []
    pnum = row[0] # 현재 저장된 숫자
    for i in range(1,4):
        if row[i] == 0 : 
            continue
        if pnum == row[i]:
            temp.append(pnum*2)
            pnum = 0
        elif pnum != 0:
            temp.append(pnum)
            pnum = row[i]
        else:
            pnum = row[i]

    if pnum != 0:
        temp.append(pnum)

    while len(temp) != 4:
        temp.append(0)

    return temp

grid = [list(map(int,input().split())) for _ in range(4)]
direction = input()
ret = []

if direction == 'L':
    for i in range(4):
        ret.append(move_left(grid[i]))
elif direction == 'R':
    for i in range(4):
        ret.append(list(reversed(move_left(list(reversed(grid[i]))))))
temp2=[[],[],[],[]]
if direction == 'U':
    for i in range(4):
        rotate_l = [grid[j][i] for j in range(4)]
        temp2 = move_left(rotate_l)
        for k in range(4):
            ret[k].append(temp2[k])
elif direction == 'D':
    for i in range(4):
        rotate_l = [grid[3-j][i] for j in range(4)]
        temp = move_left(rotate_l)
        for k in range(4):
            temp2[k].append(temp[k])
    for i in range(4):
        ret.append(temp2[3-i])

for i in range(4):
    print(" ".join(map(str,ret[i])))