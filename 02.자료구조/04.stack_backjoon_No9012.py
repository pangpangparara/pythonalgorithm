import sys

n = int(input())

for i in range(n):
    stack = []
    a = input()
    for j in a:
        if j == '(':   
            stack.append(j)
        elif j == ')':
            if len(stack) == 0 :
                print("NO")
                break
            else :  
                stack.pop(-1) 
    else:  ## for - else 문 for 문에서 break 만나지 않았을 경우 실행         
        if len(stack) != 0:
            print("NO")
        elif len(stack) == 0:
            print("YES")
