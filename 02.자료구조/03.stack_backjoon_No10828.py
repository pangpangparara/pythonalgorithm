import sys

stack = []

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return -1
    else :
        return stack.pop(-1)

def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1
    else :
        return 0

def top(): 
    if len(stack) == 0:
        return -1
    else:
        tmp = pop()
        push(tmp)
        return tmp
    
n =  int(input())

for i in range(n):
    s = sys.stdin.readline().split()
    if(s[0]) == 'push':
        push(s[1])
    elif(s[0] == 'pop'):
        print(pop())
    elif(s[0] == 'top'):
        print(top())
    elif(s[0] == 'size'):
        print(size())
    elif(s[0] == 'empty'):
        print(empty())
