from collections import deque

n, k = map(int,input().split())

p = deque([]) # 입력된 n 명의 사람 
for i in range(n):
    p.append(i+1)           
print(p)

j = deque([]) # 출력값
for a in range(7):
    if a == (k-1): # 0,1,2 => 3번째 값
       if p[k-1]: # 해당 값이 nulㅣ 이 아니면
           j.append(p[k-1])  
    else:
       p.append(p.popleft()) # 3번째 값이 아니면 왼쪽값을 가장 뒤쪽으로 이동

print(j)
