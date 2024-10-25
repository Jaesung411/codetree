import sys

MIN_INT = -sys.maxsize

def rect_sum(x1,y1,x2,y2):
    ret = 0
    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            ret += graph[i][j]
    return ret

def clear_board():
    for i in range(n):
        for j in range(m):
            check_board[i][j] = 0

def mark_board(x1,y1,x2,y2):
    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            check_board[i][j] += 1

def overlapped(x1,y1,x2,y2,x3,y3,x4,y4):
    mark_board(x1,y1,x2,y2)
    mark_board(x3,y3,x4,y4)
    for i in range(n):
        for j in range(m):
            if check_board[i][j] >= 2:
                clear_board()
                return True
    clear_board()
    return False

def find_max_sum_with_rect(sx,sy,ex,ey):
    max_sum = MIN_INT

    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    #두개의 직사각형이 겹치면 TRUE
                    if not overlapped(sx,sy,ex,ey,i,j,k,l):
                        max_sum = max(max_sum, rect_sum(sx,sy,ex,ey) + rect_sum(i,j,k,l))
    return max_sum

def find_max_sum():
    max_sum = MIN_INT

    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    max_sum = max(max_sum, find_max_sum_with_rect(i,j,k,l))
    
    return max_sum

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
check_board = [[0]*m for _ in range(n)]
ans = MIN_INT

ans = max(ans,find_max_sum())
print(ans)