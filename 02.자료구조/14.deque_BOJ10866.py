import sys
from collections import deque

n = int(sys.stdin.readline())

d = deque([])
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_front':
        d.appendleft(cmd[1])
    if cmd[0] == 'push_back':
        d.append(cmd[1])
    if cmd[0] == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    if cmd[0] == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    if cmd[0] == 'size':
        print(len(d))
    if cmd[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    if cmd[0] == 'front':
        if d:
            t = d.popleft()
            d.appendleft(t)
            print(t)
        else:
            print(-1)
    if cmd[0] == 'back':
        if d:
            t = d.pop()
            d.append(t)
            print(t)
        else:
            print(-1)