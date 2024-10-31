N = int(input())
blocks = [int(input()) for _ in range(N)]

avg = sum(blocks)//N
n_move = 0

for num_block in blocks:
    if avg < num_block:
        n_move += num_block - avg

print(n_move)