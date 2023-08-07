from collections import deque

n, k = map(int,input().split())

p = deque([]) # 입력된 n 명의 사람 
for i in range(n):
    p.append(i+1)           

j = [] # 출력값
for a in range((n-1)*k):
    if (a+1)%k == 0: # 0,1,2 => 3번째 값
       if p: # 해당 값이 nulㅣ 이 아니면
           j.append(p.popleft())   
    else:
        p.append(p.popleft()) # 3번째 값이 아니면 왼쪽값을 가장 뒤쪽으로 이동
j.append(p.popleft())

print('<',end='')
print(*j,sep=', ',end='') # * 배열명 해야 [] 없어짐
print('>')
