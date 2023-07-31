a = int(input())
stack = []
for i in range(a):
    t = int(input())
    if t == 0: 
        stack.pop(-1)
    else:
        stack.append(t)
        
if not stack:
    print(0)
else:
    sum = 0
    for j in stack:
        sum = sum +j
    print(sum)     