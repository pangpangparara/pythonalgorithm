import sys
from collections import deque

n = int(sys.stdin.readline())

cardList = deque([])

for i in range(n):
    cardList.append(i+1)

for cur in range(n-1):
    cardList.popleft()
    cardList.append(cardList.popleft())
   
print(*cardList,sep=', ',end='')
## 요세푸스에 갇혀서 다른 방법을 도저히 생각 못하겠다.
''' 요세푸스에서 처리한 것 처럼 했더니 시간 초과 뜨네...
n = int(input())

cardList = []

for i in range(n):
    cardList.append(i+1)

pos = 0
r = []
for cur in range(n):
    if pos < len(cardList):
       r.append(cardList.pop(pos)) 
    else:
        pos = 0
        r.append(cardList.pop(pos))
    pos+=1

print(r.pop())

'''