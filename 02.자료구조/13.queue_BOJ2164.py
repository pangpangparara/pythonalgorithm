n = int(input())

cardList = []

for i in range(n):
    cardList.append(i+1)

pos = 0
for cur in cardList:
    print(pos)
    print(len(cardList))
    if pos < len(cardList):
        cardList.remove(cur) ## index 값을 이용해서 데이터 지우기 
    # elif pos == len(cardList):    
    #     print('test')
    # else:
    #     print('ttt')
    pos+=1

'''
for cur in cardList:
    print(pos)
    print(cardList)
    if pos < len(cardList):
        cardList.remove(cur)
    else:    
        print('test')
        pos = 0
    pos+=1
'''

# if ~ else if문 다음에 왜 else 안타지?