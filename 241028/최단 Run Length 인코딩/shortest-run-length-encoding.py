from collections import deque

def shift(s):
    s.appendleft(s.pop())

def run_length_encoding(s):
    encode = s[0]
    ps = s[0]
    n = 1
    for i in range(1,len(s)):
        if s[i] == ps:
            n+=1
        else:
            encode+=str(n)
            encode+=s[i]
            ps = s[i]
            n = 1
    encode+=str(n)
    return len(encode)

s = deque(map(str,input()))
ans = float('inf')
for i in range(len(s)):
    shift(s)
    ans = min(ans, run_length_encoding(s))
print(ans)