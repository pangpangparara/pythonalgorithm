import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([])
for i in range(n):
    c = sys.stdin.readline().split()
    if c[0] == 'push':
        q.append(int(c[1]))
    elif c[0] == 'pop':
        if q:
            print(q.popleft()) # pop[0]는 시간복잡도 Q(n)
                               # deque 사용한다는데 deque가 뭐지?
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        if q :
            print(0)
        else :   
            print(1)
    elif c[0] == 'front':
        if q :
            print(q[0])
        else :   
            print(-1)
    elif c[0] == 'back':
        if q :
            print(q[-1])
        else :   
            print(-1)