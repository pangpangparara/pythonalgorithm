import sys

n =  int(input())
stack = []

for i in range(n):
    s = sys.stdin.readline().split()
    if(s[0]) == 'push':
        stack.append(s[1])
    elif(s[0] == 'pop'):
        if len(stack) == 0:
            print(-1)
        else :
            print(stack.pop(-1))
    elif(s[0] == 'top'):
        if len(stack) == 0:
            print(-1)
        else:
            tmp = stack.pop(-1)
            stack.append(tmp)
            print(tmp)
    elif(s[0] == 'size'):
        print(len(stack))
    elif(s[0] == 'empty'):
        if len(stack) == 0:
            print(1)
        else :
            print(0)